# dsi2018\apps\inventario\views.py
# MODULO: inventario
# OJETIVO: almacenar las views (el equivalente a controladores) necesarias para gestionar todo lo relacionado con el inventario, materia prima, servicios y demás
# ANALISTA PROGRAMADOR: Edwin Molina,	FECHA CREACION: 18/08/2018
# MODIFICADO POR: Edwin Molina,			FECHA MODIFICACION: 16/09/2018

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from datetime import time, date
import datetime
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.usuario.models import *
from apps.inventario.models import *
from apps.proveedor.models import *

#INICIO DE DECLARACION DE VARIABLES GLOBALES
promedio_precio = []
total_egreso = 0
producto = False
reg_producto = False
#FIN DE DECLARACION DE VARIABLES GLOBALES

#INICIO DE FUNCION DE SEGURIDAD 1
def seguridad(request):
	admin = None
	empdo = None
	try:
		administrador = User.objects.get(id=request.user.id)
		if administrador.is_superuser:
			admin = True
		else:
			admin = False
	except User.DoesNotExist:
		administrador = None
		admin = False
	try:
		empleado = Empleado.objects.get(id=request.user.id)
		empdo = True
	except Empleado.DoesNotExist:
		empleado = None
		empdo = False
	if admin == True or empdo == True:
		return True
	else:
		return False
#INICIO DE FUNCION DE SEGURIDAD 1

#INICIO DE FUNCION DE SEGURIDAD 2
def seguridad_reg_inv(request):
	empdo = None
	try:
		empleado = Empleado.objects.get(id=request.user.id)
		empdo = True
	except Empleado.DoesNotExist:
		empleado = None
		empdo = False
	if empdo == True:
		return True
	else:
		return False
#INICIO DE FUNCION DE SEGURIDAD 2

#INICIO DE FUNCION (filtro): sirve para filtrar los productos por materia prima y servicios
def filtro(producto_list, producto, productos, request):
	if producto == 1:
		for p in reversed(producto_list):
			if p.tipo == 'P':
				productos.append(p)
	elif producto == 2:
		for p in reversed(producto_list):
			if p.tipo == 'S':
				productos.append(p)
	paginator = Paginator(productos, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)
#FIN DE FUNCION (filtro)

#INICIO DE FUNCION (numProductos): calcula en numero de productos
def numProductos(producto_list):
	class CE:
		idP = 0
		num = 0
	catalogo = CatalogoExistencias.objects.all()
	numProducto = []
	acumulador = 0
	for p in reversed(producto_list):
		for c in catalogo:
			if p.id == c.producto_id:
				acumulador = acumulador + c.cantidad
		ce = CE()
		ce.idP = int(p.id)
		ce.num = int(acumulador)
		numProducto.append(ce)
		acumulador = 0
	return numProducto
#FIN DE FUNCION (numProductos)

#INICIO DE FUNCION (adminProductos): controlador para administrar los prodcutos que la empresa aquiere (materia prima y servicios)
@login_required(login_url='/usuario/login')
def adminProductos(request):
	#INICIO DE BLOQUE 1 DE SEGURIDAD
	if seguridad(request):
	#FIN DE BLOQUE 1 DE SEGURIDAD
		global producto;
		producto_list = Producto.objects.all()
		#json_list = json.dumps(producto_list)
		productos = []
		cantidad = []
		if request.method == 'POST':
			if 'tipo' in request.POST:
				producto = int(request.POST.get('producto'))
				productos = filtro(producto_list, producto, productos, request)
				cantidad = numProductos(producto_list)
				return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto, 'producto_list':producto_list, 'cantidad':cantidad})
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
					cantidad = numProductos(producto_list)
				return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto, 'producto_list':producto_list, 'cantidad':cantidad})
		else:
			if producto is False:
				producto = 1
			elif producto is not False:
				producto = producto
			productos = filtro(producto_list, producto, productos, request)
			cantidad = numProductos(producto_list)
			return render(request, 'inventario/adminProductos.html', {'productos':productos, 'producto':producto, 'producto_list':producto_list, 'cantidad':cantidad})
	#INICIO DE BLOQUE 2 DE SEGURIDAD
	else:
		return render(request,'usuario/bienvenido/index.html')
	#FIN DE BLOQUE 2 DE SEGURIDAD	
#FIN DE FUNCION (adminProductos) 

#INICIO DE FUNCION (sacarMateriaPrima): aloritmo para sacar materia prima segun el metodo PEPS
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
#FIN DE FUNCION (sacarMateriaPrima)

#INICIO DE FUNCION (filtroPorMateria): permite filtrar la materia prima segun el producto seleccionado
def filtroPorMateria(request, registros_list_reversed, producto):
	registros_ppl = []

	if producto == 'all':
		for r in registros_list_reversed:
			registros_ppl.append(r)
	else:
		for r in registros_list_reversed:
			if r.producto_id == int(producto):
				registros_ppl.append(r)

	paginator = Paginator(registros_ppl, 8)
	page = request.GET.get('page')

	return paginator.get_page(page)
#FIN DE FUNCION (filtroPorMateria)

#INICIO DE FUNCION (regInventario): controlador para ingresar y sacar materia del inventario
@login_required(login_url='/usuario/login')
def regInventario(request):
	#INICIO DE BLOQUE 1 DE SEGURIDAD
	if seguridad_reg_inv(request):
	#FIN DE BLOQUE 1 DE SEGURIDAD
		global promedio_precio, total_egreso, reg_producto
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
																			
				r = RegistroDeInventario()
				r.producto_id =  e.producto_id
				r.proveedor_id = request.POST.get('proveedor')
				r.empleado_id = request.user.id 									# (RESULETO) SUJETO A CAMBIOS (cuando se loguee el empleado y autorice el registro: request.user.id)
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
					r.empleado_id = request.user.id									# (RESULETO) SUJETO A CAMBIOS
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
				reg_producto = request.POST.get('productoFiltro')
				if reg_producto == 'all':
					return redirect('inventario:reg_inv')
				else:
					registros = filtroPorMateria(request, registros_list_reversed, reg_producto)
					return render(request, 'inventario/registroInventario.html', {'productos':productos, 'proveedores':proveedores, 'registros':registros})
		else:
			if reg_producto is False:
				reg_producto = 'all'
			elif reg_producto is not False:
				reg_producto = reg_producto
			registros = filtroPorMateria(request, registros_list_reversed, reg_producto)
		return render(request, 'inventario/registroInventario.html', {'productos':productos, 'proveedores':proveedores, 'registros':registros})
	#INICIO DE BLOQUE 2 DE SEGURIDAD
	else:
		return render(request,'usuario/bienvenido/index.html')
	#FIN DE BLOQUE 2 DE SEGURIDAD
#FIN DE FUNCION (regInventario)

# INDICACIONES
# No es un inventario contable, solo sirve para ingresar y sacar materia prima, por tanto no se maneja por kardex separdos, 
# toda la materia prima esta en el mismo inventario siguiendo el metodo PEPS de forma individual

# Para ingresar materia prima:
# 	1. Se debe crear un proveedor y producto y relacionar los dos desde el admin django, en la clase Catalogo de productos
# 	2. Crear un empleado y asignar el numero de la id a r.empleado_id en la linea 157

# Esto se resolveran posteriormente en accesos mas rapidos en las interfaces correspondientes, 
# pero con el objetivo de no atrasar la parte de cotizacion actualamente cuenta con las funciones necesarias para manejar el invetario

#INICIO DE FUNCION (editarProducto): sirve para editar el producto seleccionado en el template respectivo
@login_required(login_url='/usuario/login')
def editarProducto(request, id_producto):
	#INICIO DE BLOQUE 1 DE SEGURIDAD
	if seguridad(request):
	#FIN DE BLOQUE 1 DE SEGURIDAD
		producto = Producto.objects.get(id=id_producto)
		proveedores = Proveedor.objects.all()
		if request.method == 'POST':
			if 'guardarCambios' in request.POST:
				producto.nombre = request.POST.get('nombre')
				producto.descripcion = request.POST.get('descripcion')
				producto.unidades = request.POST.get('unidades')
				producto.save()
				return redirect('inventario:adm_pro')
			if 'eliminar' in request.POST:
				producto.delete()
				return redirect('inventario:adm_pro')
		return render(request, 'inventario/editarProducto.html', {'producto':producto, 'proveedores':proveedores})
	#INICIO DE BLOQUE 2 DE SEGURIDAD
	else:
		return render(request,'usuario/bienvenido/index.html')
	#FIN DE BLOQUE 2 DE SEGURIDAD
#FIN DE FUNCION (editarProducto)

#INICIO DE FUNCION (paginadoContactos): proporciona la paginacion de tabla
def paginadoContactos(request, proveedores):
	proveedores_page = []
	for p in proveedores:
		proveedores_page.append(p)
	paginator = Paginator(proveedores_page, 5)
	page = request.GET.get('page')
	return paginator.get_page(page)
#FIN DE FUNCION (paginadoContactos)

#INICIO DE FUNCION (consultarProveedores): permite consultar y gestionar los proveedores
@login_required(login_url='/usuario/login')
def consultarProveedores(request, id_producto):
	#INICIO DE BLOQUE 1 DE SEGURIDAD
	if seguridad(request):
	#FIN DE BLOQUE 1 DE SEGURIDAD
		producto = Producto.objects.get(id=id_producto)
		catalogo = CatalogoProductos.objects.all().order_by('id')
		proveedores_list = Proveedor.objects.all().order_by('nombre')
		catalogo_producto = []
		proveedores = []
		proveedores_producto = []
		s = 0
		for p in proveedores_list:
			for c in catalogo:
				if int(id_producto) == c.producto_id and c.proveedor_id == p.id:
					proveedores.append(p)
		for p1 in proveedores_list:
			for p2 in proveedores:
				if p1.id == p2.id:
					s = 1
			if s == 0:
				proveedores_producto.append(p1)
			else:
				s = 0
		proveedores_contacts = paginadoContactos(request, proveedores)
		if request.method == 'POST':
			id_proveedor = request.POST.get('proveedor')
			c = CatalogoProductos()
			c.proveedor_id = id_proveedor
			c.producto_id = id_producto
			#c.precioUnitario = 10					# (RESUELTO) ELIMINAR PRECIO UNITARIO
			c.save()
			return redirect(reverse('inventario:cop_prv', kwargs={"id_producto": id_producto}))
		return render(request, 'inventario/proveedoresProducto.html', {'producto':producto, 'proveedores_contacts':proveedores_contacts, 'proveedores_producto':proveedores_producto, 'catalogo':catalogo})
	#INICIO DE BLOQUE 2 DE SEGURIDAD
	else:
		return render(request,'usuario/bienvenido/index.html')
	#FIN DE BLOQUE 2 DE SEGURIDAD
#FIN DE FUNCION (consultarProveedores)

#INICIO DE FUNCION (desvincularProveedor): sirve para desvincular el proveedor del producto
def desvincularProveedor(request, id_producto, id_proveedor):
	catalogo = CatalogoProductos.objects.get(producto_id=id_producto, proveedor_id=id_proveedor)
	catalogo.delete()
	return redirect(reverse('inventario:cop_prv', kwargs={"id_producto": id_producto}))
#FIN DE FUNCION (desvincularProveedor)