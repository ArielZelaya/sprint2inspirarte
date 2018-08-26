from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import time, date
import datetime
from apps.inventario.models import *
from apps.proveedor.models import *

promedio_precio = []
total_egreso = 0
seleccion_producto = False
seleccion_registro = False

# Create your views here.
def filtro(producto_list, producto, productos, request):
	if producto == 1:
		for p in reversed(producto_list):
			if p.tipo == 'P':
				productos.append(p)
	elif producto == 2:
		for p in producto_list:
			if p.tipo == 'S':
				productos.append(p)
	paginator = Paginator(productos, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)

def adminProductos(request):
	producto_list = Producto.objects.all()
	productos = []
	if request.method == 'POST':
		if 'tipo' in request.POST:
			producto = int(request.POST.get('producto'))
			productos = filtro(producto_list, producto, productos, request)
			return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto})
		if 'guardar' in request.POST:
			p = Producto()
			p.tipo = request.POST.get('tipoP')
			p.nombre = request.POST.get('nombre')
			p.descripcion = request.POST.get('descripcion')
			p.unidades = request.POST.get('unidades')
			p.save()
			if p.tipo == 'S':
				producto = 2
				productos = filtro(producto_list, producto, productos, request)
			if p.tipo == 'P':
				producto = 1
				productos = filtro(producto_list, producto, productos, request)
			return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto})
	else:
		producto = 1
		productos = filtro(producto_list, producto, productos, request)
		return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto})

def sacarMateriaPrima(producto_id, salida):
	global promedio_precio, total_egreso
	del promedio_precio [:]
	total_egreso = 0
	existencias = CatalogoExistencias.objects.all().order_by('id')
	for e in existencias:
		if e.producto_id == producto_id:
			if e.cantidad >= salida:
				e.cantidad = e.cantidad - salida

				promedio_precio.append(e.precio)
				total_egreso = total_egreso + salida*e.precio

				e.save()
				return redirect('inventario:reg_inv')
			elif e.cantidad>0:
				salida = salida - e.cantidad

				promedio_precio.append(e.precio)
				total_egreso = total_egreso + e.cantidad*e.precio

				e.cantidad = 0
				e.save()

def filtroPorMateria(request, registros_list_reversed, producto):
	registros_ppl = []

	for r in registros_list_reversed:
		if r.producto_id == int(producto):
			registros_ppl.append(r)

	paginator = Paginator(registros_ppl, 8)
	page = request.GET.get('page')

	return paginator.get_page(page)

def regInventario(request):
	global promedio_precio, total_egreso
	registros_list = RegistroDeInventario.objects.all()
	productos_list = Producto.objects.all()
	proveedores_list = Proveedor.objects.all()
	catalogoProducto = CatalogoProductos.objects.all()
	registros_list_reversed = []
	productos = []
	proveedores = []

	for pd in reversed(productos_list):
		if pd.tipo == 'P':
			productos.append(pd)

	for pv in reversed(proveedores_list):
		if pv.tipo == 'P':
			proveedores.append(pv)

	for r in reversed(registros_list):
		registros_list_reversed.append(r)

	paginator = Paginator(registros_list_reversed, 8)
	page = request.GET.get('page')
	registros = paginator.get_page(page)

	if request.method == 'POST':
		if 'meter' in request.POST:
			e = CatalogoExistencias()
			e.producto_id = request.POST.get('producto')
			e.precio = float(request.POST.get('precio'))
			e.cantidad = int(request.POST.get('cantidad'))
			e.save()
																		#AFECTAR EL CATALOGO DE PRODUCTOS (actualizar el precio  del proveedor)
			r = RegistroDeInventario()
			r.producto_id =  e.producto_id
			r.proveedor_id = request.POST.get('proveedor')
			r.empleado_id = 2 											#SUJETO A CAMBIOS (cuando se loguee el empleado y autorice el registro: request.user.id)
			r.tipo = 'E'
			r.fecha = date.today()
			r.descripcion = request.POST.get('descripcion')
			r.precio = float(request.POST.get('precio'))
			r.cantidad = int(request.POST.get('cantidad'))
			r.total = r.precio*r.cantidad
			r.save()
			return redirect('inventario:reg_inv')
		if 'sacar' in request.POST:
			existencias = CatalogoExistencias.objects.all()
			totalDisponible = 0

			producto_id = int(request.POST.get('productoSacar'))
			salida = int(request.POST.get('cantidadSacar'))
			descripcion = request.POST.get('descripcionSacar')

			#SE COMPRUEBA SI EXISTE LA CANTIDAD DESEADA DE MATERIA PRIMA
			for e in existencias:
				if e.producto_id == producto_id:
					totalDisponible = totalDisponible + e.cantidad

			#SI NO ESTA DISPONIBLE MANDA UN MENSAJE
			if totalDisponible < salida:
				return redirect('inventario:adm_pro')

			#SI EXISTE LA CANTIDAD COMIENZA EL EGRESO DE MATERIA PRIMA
			else:
				sacarMateriaPrima(producto_id, salida)
				r = RegistroDeInventario()
				r.producto_id =  producto_id
				r.proveedor_id = None											# (RESULETO) CAMBIO EN EL MODELO REALIZADO
				r.empleado_id = 2 										#SUJETO A CAMBIOS
				r.tipo = 'S'
				r.fecha = date.today()
				r.descripcion = descripcion

				total_prom = 0
				for precio in promedio_precio:
					total_prom = total_prom + precio
				r.precio = total_prom/len(promedio_precio)						# (RESULETO) SUJETO A CAMBIOS ERROR! (usar var global y acumular el total)
				
				r.cantidad = salida
				r.total = total_egreso											# (RESULETO) SUJETO A CAMBIOS
				r.save()
				return redirect('inventario:reg_inv')
		if 'tipo' in request.POST:
			producto = request.POST.get('productoFiltro')
			if producto == 'all':
				return redirect('inventario:reg_inv')
			else:
				registros = filtroPorMateria(request, registros_list_reversed, producto)
				return render(request, 'inventario/registroInventario.html', {'productos':productos, 'proveedores':proveedores, 'registros':registros})
	return render(request, 'inventario/registroInventario.html', {'productos':productos, 'proveedores':proveedores, 'registros':registros})


# INDICACIONES
# No es un inventario contable, solo sirve para ingresar y sacar materia prima, por tanto no se maneja por kardex separdos, 
# toda la materia prima esta en el mismo inventario siguiendo el metodo PEPS de forma individual

# Para ingresar materia prima:
# 	1. Se debe crear un proveedor y producto y relacionar los dos desde el admin django, en la clase Catalogo de productos
# 	2. Crear un empleado y asignar el numero de la id a r.empleado_id en la linea 157

# Esto se resolveran posteriormente en accesos mas rapidos en las interfaces correspondientes, 
# pero con el objetivo de no atrasar la parte de cotizacion actualamente cuenta con las funciones necesarias para manejar el invetario