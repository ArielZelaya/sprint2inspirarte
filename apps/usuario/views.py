from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
import datetime
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.

def index(request):
     return render(request,'usuario/index.html')


def wc(request):
     return render(request,'usuario/bienvenido/index.html')

#Consulta los empleados (con contrato vigente) y se define el entorno para la gestion de estos
@login_required(login_url='/usuario/login')
def gestionEmpleado(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		empleado_list = Empleado.objects.all()
		contratos = Contrato.objects.all()
		paginator = Paginator(empleado_list,5)
		page = request.GET.get('page')
		empleados = paginator.get_page(page)
		return render(request, 'empleado/gestionar.html', {'empleados':empleados, 'contratos':contratos})
	else:
		return render(request,'usuario/bienvenido/index.html')


#Habilita al emepleado para que acceda al sistema
@login_required(login_url='/usuario/login')
def habilitarUsuario(request, id_user):
	empleado = User.objects.get(id=id_user)
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
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
	else:
		return render(request,'usuario/bienvenido/index.html')


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


#3 - ARREGLO inicio
#Funciones para generar el codigo de empleado segun el patron establecido
def generadorCombinacion(first_name, last_name):
		codigo = ""
		for i in range(len(last_name)):
			if i == 0:
				codigo = last_name[i]
		for i in range(len(first_name)):
			if i == 0:
				codigo = codigo + first_name[i]
		return codigo
def generarCodigo(first_name, last_name):
	empleados = Empleado.objects.all()
	codigo=""
	if not empleados:
		codigo = generadorCombinacion(first_name, last_name)
		codigo = codigo + '1000'
		return codigo
	else:
		n = len(empleados)
		empleado = empleados[n-1]
		codigo = generadorCombinacion(first_name, last_name)
		codigo2 = ""
		m = len(empleado.codigo)
		print("PRUEBA:"+str(m))
		for i in range(m):
			if i == m-4:
				codigo2 = codigo2 + empleado.codigo[i]
				print(codigo2)
			if i == m-3:
				codigo2 = codigo2 + empleado.codigo[i]
				print(codigo2)
			if i == m-2:
				codigo2 = codigo2 + empleado.codigo[i]
				print(codigo2)
			if i == m-1:
				codigo2 = codigo2 + empleado.codigo[i]
				print(codigo2)
		codigo3 = int(codigo2) + 1
		print(codigo3)
		codigo = codigo + str(codigo3)
		print(codigo)
		return codigo


#Funcion para calcular la duracion del contrato
def calcularDuracion(a, b):
	fi = datetime.datetime.strptime(a, '%Y-%m-%d').date()
	ff = datetime.datetime.strptime(b, '%Y-%m-%d').date()
	opDias = ff - fi
	lsDias = str(opDias)
	dias = ""
	meses = ""
	anios = ""
	k = 0
	j = 0
	for i in range(len(lsDias)):
		if lsDias[i] == " ":
			break
		else:
			dias = dias + lsDias[i]
	lsMeses = str(float(int(dias)/30))
	for i in range(len(lsMeses)):
		if j == 1:
			break
		if i == 4:
			j = 1
		else:
			meses = meses + lsMeses[i]
	lsAnios = str(float(int(dias)/365))
	for i in range(len(lsAnios)):
		if k == 1:
			break
		if i == 4:
			k = 1
		else:
			anios = anios + lsAnios[i]
	print("PRUEBA"+dias+" "+meses+" "+anios)
	return dias+" dias, "+meses+" meses, "+anios+" anios"


#REGISTRO DE EMPLEADOS
@login_required(login_url='/usuario/login')
def registrarEmpleado(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		editar = False
		puestos = Puesto.objects.all()
		if request.method == 'POST':
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			puesto_id = request.POST.get('puesto')
			dui = request.POST.get('dui')
			nit = request.POST.get('nit')
			isss = request.POST.get('isss')
			nup = request.POST.get('nup')
			codigo = generarCodigo(first_name, last_name) #1 - ARREGLO
			username = codigo #2 - ARREGLO
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
			contrato.duracion = calcularDuracion(contrato.fechaInicio, contrato.fechaFinal)
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
	else:
		return render(request,'usuario/bienvenido/index.html')


#EDITAR EMPLEADO
@login_required(login_url='/usuario/login')
def editarEmpleado(request, id_user):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		editar = True
		puestos = Puesto.objects.all()
		empleado = Empleado.objects.get(id=id_user)
		contrato = Contrato.objects.get(empleado_id=id_user, vigente=True)
		if request.method == 'POST':
			first_name = request.POST.get('first_name')
			last_name = request.POST.get('last_name')
			email = request.POST.get('email')
			password = request.POST.get('password')
			puesto_id = request.POST.get('puesto')
			dui = request.POST.get('dui')
			nit = request.POST.get('nit')
			isss = request.POST.get('isss')
			nup = request.POST.get('nup')
			domicilio = request.POST.get('domicilio')
			telefono = request.POST.get('telefono')
			active = request.POST.get('active')
			#Edicion del objeto a empleado
			empleado.email=email
			empleado.first_name=first_name
			empleado.last_name=last_name
			empleado.puesto_id=puesto_id
			empleado.dui=dui
			empleado.nit=nit
			empleado.isss=isss
			empleado.nup=nup
			empleado.domicilio=domicilio
			empleado.telefono=telefono
			#ACTIVO: Si se ha activado el usuario
			if active:	
				empleado.password=password
				empleado.is_active=True
			#NO ACTIVO: Si no se ha dado activado el usuario
			else:
				empleado.password=empleado.codigo
				empleado.is_active=False
			empleado.save()
			#No se podra editar un de objeto Contrato
			return redirect('usuario:ges_emp')
		return render(request, 'empleado/registrar_editar.html', {'editar':editar, 'puestos':puestos, 'empleado':empleado, 'contrato':contrato})
	else:
		return render(request,'usuario/bienvenido/index.html')


#CREACION CONTRATO
@login_required(login_url='/usuario/login')
def crearContrato(request, id_user):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
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
			contrato.fechaInicio = request.POST.get('fechaInicio')
			contrato.fechaFinal = request.POST.get('fechaFinal')
			contrato.duracion = calcularDuracion(contrato.fechaInicio, contrato.fechaFinal)
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
	else:
		return render(request,'usuario/bienvenido/index.html')


#CANCELACION DE CONTRATO
@login_required(login_url='/usuario/login')
def cancelarContrato(request, id_user):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		contrato = Contrato.objects.get(empleado_id=id_user, vigente=True)
		empleado = Empleado.objects.get(id=id_user)
		if request.method == 'POST':
			contrato.fechaFinal = date.today()
			contrato.vigente = False
			contrato.save()
			return redirect('usuario:ges_emp')
		return render(request, 'empleado/cancelarContrato.html', {'empleado':empleado})
	else:
		return render(request,'usuario/bienvenido/index.html')


#Consulta de contratos no vigentes
@login_required(login_url='/usuario/login')
def noVigentes(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		empleados = Empleado.objects.all()
		contratos = Contrato.objects.all()
		return render(request, 'empleado/contratosNoVigentes.html', {'empleados':empleados, 'contratos':contratos})
	else:
		return render(request,'usuario/bienvenido/index.html')


#Parte de los usuarios
def iniciarSesion(request):
	form=AuthenticationForm(request.POST)
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user=User.objects.get(username=username)
		user.check_password(password)
		# user = authenticate(username=username, password=password)
		if user is not None:
			login(request,user)
			return redirect('usuario/')
		else :
			valor = "Ingrese usuario valido o contrasena correcta"
			print(user)
			context= { "form":form,'valor':valor }
			return render(request,'usuario/login.html',context)
	if request.user.is_active:
		return redirect('/')
	valor = ""
	context= { "form":form,'valor':valor }
	return render(request,'usuario/login.html',context)
	
def cerrarSesion(request):
    logout(request)
    return redirect('usuario:idex')

def crearCliente(request):
	valor=""
	if request.method=='POST':
		form=clienteForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request, 'usuario/index.html')
		else:
			valor="Error al guardadr"
	form=clienteForm()
	context={"form":form,'valor':valor}
	return render(request,'usuario/crearCliente.html',context)
	# if request.method=='POST':
		#guardara
	# else :

@login_required(login_url='/usuario/login')
def editarCliente(request,id_user):
	valor=""
	cliente=Cliente.objects.get(id=id_user)		
	if request.method=='POST':
		form=clienteForm(request.POST,instance=cliente)
		if form.is_valid():
			form.save()
			return redirect('usuario:index')
			# return HttpResponse(request, 'usuario/index.html')
	else:
		form=clienteForm(instance=cliente)
		context={"form":form,'valor':valor}
		return render(request,'usuario/crearCliente.html',context)

@login_required(login_url='/usuario/login')
def gestionCliente(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		usuarios=Cliente.objects.all()
		context={'usuarios':usuarios}
		return render(request,'usuario/gestionar.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')

@login_required(login_url='/usuario/login')
def tipoCliente(request,id_user):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		cliente=Cliente.objects.get(id=id_user)
		if request.method=='POST':
			tipoC=request.POST['t_cliente']
			cliente.tipo=tipoC
			cliente.save()
			return redirect('usuario:gestion_cliente')
		else:
			return render(request, 'usuario/tipoCliente.html')
	else:
		return render(request,'usuario/bienvenido/index.html')