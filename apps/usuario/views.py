from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
from .models import *
# Create your views here.

def usuario(request):
     return render(request,'usuario/index.html')


#Consulta los empleados (con contrato vigente) y se define el entorno para la gestion de estos
def gestionEmpleado(request):
	empleados = Empleado.objects.all()
	contratos = Contrato.objects.all()
	return render(request, 'empleado/gestionar.html', {'empleados':empleados, 'contratos':contratos})


#Habilita al emepleado para que acceda al sistema
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


#Funcion para ordenar los dias (y horarios atipicos si asi se requiere) en una cadena de caracteres
def addDiasLaborales(dias, horaEntrada, horaSalida):
	cadenaDias = ""
	k=0
	for i in range(len(dias)):
		for j in range(len(horaEntrada)):
			if i == j and dias[i] is not None and horaEntrada[j] != "":
				dias[i] = dias[i] + "(" + str(horaEntrada[j])
		
	for i in range(len(dias)):
		for j in range(len(horaSalida)):
			if i == j and dias[i] is not None and horaSalida[j] != "":
				dias[i] = dias[i] + "-" + str(horaSalida[j])  + ")"
	for i in range(len(dias)):
		if dias[i] is not None:
			if k == 0:
				cadenaDias = cadenaDias + str(dias[i])
				k = 1
			else:
				cadenaDias = cadenaDias + ", " + str(dias[i])
	return cadenaDias


#REGISTRO DE EMPLEADOS
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
		#Si se selecciono el checkbox habilitar, active = True
		#Creacion de objeto Empleado
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
		contrato.fechaInicio = request.POST.get('fechaInicio')
		contrato.fechaFinal = request.POST.get('fechaFinal')
		contrato.duracion = 10
		contrato.horaEntrada = request.POST.get('horaEntrada')
		contrato.horaSalida = request.POST.get('horaSalida')
		#Identificacion de dias labores
		dias = []
		horaSalida = []
		horaEntrada = []
		contrato.diasLaborales = ""
		dias.append(request.POST.get('lunes'))			#lunes
		horaEntrada.append(request.POST.get('helu'))
		horaSalida.append(request.POST.get('hslu'))
		dias.append(request.POST.get('martes'))			#martes
		horaEntrada.append(request.POST.get('hema'))
		horaSalida.append(request.POST.get('hsma'))	
		dias.append(request.POST.get('miercoles'))		#miercoles
		horaEntrada.append(request.POST.get('hemi'))
		horaSalida.append(request.POST.get('hsmi'))
		dias.append(request.POST.get('jueves'))			#jueves
		horaEntrada.append(request.POST.get('heju'))
		horaSalida.append(request.POST.get('hsju'))
		dias.append(request.POST.get('viernes'))		#viernes
		horaEntrada.append(request.POST.get('hevi'))
		horaSalida.append(request.POST.get('hsvi'))
		dias.append(request.POST.get('sabado'))			#sabado
		horaEntrada.append(request.POST.get('hesa'))
		horaSalida.append(request.POST.get('hssa'))
		dias.append(request.POST.get('domingo'))		#domingo
		horaEntrada.append(request.POST.get('hedo'))
		horaSalida.append(request.POST.get('hsdo'))
		contrato.diasLaborales = addDiasLaborales(dias, horaEntrada, horaSalida) #Retorno de cadena
		contrato.salario = request.POST.get('salario')
		contrato.vigente = True
		contrato.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/registrar_editar.html', {'editar':editar, 'puestos':puestos})


#EDITAR EMPLEADO
def editarEmpleado(request, id_user):
	editar = True
	puestos = Puesto.objects.all()
	empleado = Empleado.objects.get(id=id_user)
	contrato = Contrato.objects.get(empleado_id=id_user, vigente=True)
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
		#No se podra editar un de objeto Contrato
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/registrar_editar.html', {'editar':editar, 'puestos':puestos, 'empleado':empleado, 'contrato':contrato})


#CREACION CONTRATO
def crearContrato(request, id_user):
	empleado = Empleado.objects.get(id=id_user)
	#Se busca el contrato actualmente vigente del empleado al que se le creara uno nuevo
	contratoAnterior = Contrato.objects.get(empleado_id=id_user, vigente=True)
	if request.method == 'POST':
		#Cancelacion de contrato anterior
		contratoAnterior.vigente = False
		contratoAnterior.save()
		#Creacion de nuevo contrato
		contrato = Contrato()
		contrato.empleado_id = id_user
		contrato.tipo = request.POST.get('tipo')
		contrato.fechaCelebracion = date.today()
		contrato.duracion = 10
		contrato.fechaInicio = request.POST.get('fechaInicio')
		contrato.fechaFinal = request.POST.get('fechaFinal')
		contrato.horaEntrada = request.POST.get('horaEntrada')
		contrato.horaSalida = request.POST.get('horaSalida')
		#Identificacion de dias labores
		dias = []
		horaSalida = []
		horaEntrada = []
		contrato.diasLaborales = ""
		dias.append(request.POST.get('lunes'))			#lunes
		horaEntrada.append(request.POST.get('helu'))
		horaSalida.append(request.POST.get('hslu'))
		dias.append(request.POST.get('martes'))			#martes
		horaEntrada.append(request.POST.get('hema'))
		horaSalida.append(request.POST.get('hsma'))	
		dias.append(request.POST.get('miercoles'))		#miercoles
		horaEntrada.append(request.POST.get('hemi'))
		horaSalida.append(request.POST.get('hsmi'))
		dias.append(request.POST.get('jueves'))			#jueves
		horaEntrada.append(request.POST.get('heju'))
		horaSalida.append(request.POST.get('hsju'))
		dias.append(request.POST.get('viernes'))		#viernes
		horaEntrada.append(request.POST.get('hevi'))
		horaSalida.append(request.POST.get('hsvi'))
		dias.append(request.POST.get('sabado'))			#sabado
		horaEntrada.append(request.POST.get('hesa'))
		horaSalida.append(request.POST.get('hssa'))
		dias.append(request.POST.get('domingo'))		#domingo
		horaEntrada.append(request.POST.get('hedo'))
		horaSalida.append(request.POST.get('hsdo'))
		contrato.diasLaborales = addDiasLaborales(dias, horaEntrada, horaSalida) #Retorno de dias laborales
		contrato.salario = request.POST.get('salario')
		contrato.vigente = True
		contrato.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/crearContrato.html', {'empleado':empleado})


#CANCELACION DE CONTRATO
def cancelarContrato(request, id_user):
	contrato = Contrato.objects.get(empleado_id=id_user, vigente=True)
	empleado = Empleado.objects.get(id=id_user)
	if request.method == 'POST':
		contrato.fechaFinal = date.today()
		contrato.vigente = False
		contrato.save()
		return redirect('usuario:ges_emp')
	return render(request, 'empleado/cancelarContrato.html', {'empleado':empleado})


#Consulta de contratos no vigentes
def noVigentes(request):
	empleados = Empleado.objects.all()
	contratos = Contrato.objects.all()
	return render(request, 'empleado/contratosNoVigentes.html', {'empleados':empleados, 'contratos':contratos})
