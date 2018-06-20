from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
from .models import *
# Create your views here.

def usuario(request):
     return render(request,'usuario/index.html')

def gestionEmpleado(request):
	empleados = Empleado.objects.all()
	contratos = Contrato.objects.all()
	return render(request, 'empleado/gestionar.html', {'empleados':empleados, 'contratos':contratos})

def habilitarUsuario(request, id_user):
	empleado = User.objects.get(id=id_user)
	#estado: booleano para seleccionar mensaje hailitar/deshabilitar
	if empleado.is_active:
		estado = False
	else:
		estado = True
	if request.method == "POST":
		if empleado.is_active:
			empleado.is_active = False
		else:
			empleado.is_active = True
		empleado.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/confirmarHabilitacion.html', {'empleado':empleado, 'estado':estado})

def registrarEmpleado(request):
	editar = False
	puestos = Puesto.objects.all()

	if request.method == 'POST':

		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		username = request.POST.get('codigo')
		puesto_id = request.POST.get('puesto')
		dui = request.POST.get('dui')
		nit = request.POST.get('nit')
		isss = request.POST.get('isss')
		nup = request.POST.get('nup')
		codigo = request.POST.get('codigo')
		domicilio = request.POST.get('domicilio')
		telefono = request.POST.get('telefono')
		active = request.POST.get('active')
		#REGISTRAR
		if active:
			empleado = Empleado.objects.create_user(
							username=username, 
							email=email, 
							first_name=first_name, 
							last_name=last_name, 
							password=password, 
							is_active=True,
							puesto_id=puesto_id,
							dui=dui,
							nit=nit,
							isss=isss,
							nup=nup,
							codigo=codigo,
							domicilio=domicilio,
							telefono=telefono)
		else:
			empleado = Empleado.objects.create_user(
							username=username, 
							email=email, 
							first_name=first_name, 
							last_name=last_name, 
							password=codigo, 
							is_active=False,
							puesto_id=puesto_id,
							dui=dui,
							nit=nit,
							isss=isss,
							nup=nup,
							codigo=codigo,
							domicilio=domicilio,
							telefono=telefono)
		empleado.save()
		#Creacion de objeto Contrato
		contrato = Contrato()
		contrato.empleado_id = empleado.id
		contrato.tipo = request.POST.get('tipo')
		contrato.fechaCelebracion = date.today()
		contrato.duracion = request.POST.get('duracion')
		contrato.fechaInicio = date.today()
		contrato.fechaFinal = date.today()
		contrato.horaEntrada = 'hora'
		contrato.horaSalida = 'hora'
		contrato.salario = request.POST.get('salario')
		contrato.vigente = True
		contrato.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/registrar_editar.html', {'editar':editar, 'puestos':puestos})

def editarEmpleado(request, id_user):
	editar = True
	puestos = Puesto.objects.all()
	empleado = Empleado.objects.get(id=id_user)
	contrato = Contrato.objects.get(empleado_id=id_user)

	if request.method == 'POST':
		first_name = request.POST.get('first_name')
		last_name = request.POST.get('last_name')
		email = request.POST.get('email')
		password = request.POST.get('password')
		username = request.POST.get('codigo')
		puesto_id = request.POST.get('puesto')
		dui = request.POST.get('dui')
		nit = request.POST.get('nit')
		isss = request.POST.get('isss')
		nup = request.POST.get('nup')
		codigo = request.POST.get('codigo')
		domicilio = request.POST.get('domicilio')
		telefono = request.POST.get('telefono')
		active = request.POST.get('active')
		#Edicion del objeto a empleado
		empleado.username=username
		empleado.email=email
		empleado.first_name=first_name
		empleado.last_name=last_name
		empleado.puesto_id=puesto_id
		empleado.dui=dui
		empleado.nit=nit
		empleado.isss=isss
		empleado.nup=nup
		empleado.codigo=codigo
		empleado.domicilio=domicilio
		empleado.telefono=telefono
		#ACTIVO: Si se ha activado el usuario
		if active:	
			empleado.password=password
			empleado.is_active=True
		#NO ACTIVO: Si no se ha dado activado el usuario
		else:
			empleado.password=codigo
			empleado.is_active=False
		empleado.save()
		#Edicion de objeto Contrato
		contrato.empleado_id = empleado.id
		contrato.tipo = request.POST.get('tipo')
		contrato.fechaCelebracion = date.today()
		contrato.duracion = request.POST.get('duracion')
		contrato.fechaInicio = date.today()
		contrato.fechaFinal = date.today()
		contrato.horaEntrada = 'hora'
		contrato.horaSalida = 'hora'
		contrato.salario = float(request.POST.get('salario').replace(',', '.'))
		contrato.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/registrar_editar.html', {'editar':editar, 'puestos':puestos, 'empleado':empleado, 'contrato':contrato})

# def cancelarRegistro(request, id_user):
# 	usuario= User.objects.get(id=id_user)
# 	if request.method == 'POST':
# 		usuario.delete()
# 		return redirect('usuario:ges_emp')
# 	return render(request, 'empleado/registrar_editar.html', {'editar':editar})