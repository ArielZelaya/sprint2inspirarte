from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/usuario/login')
def crearProveedor(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		valor=""
		if request.method=='POST':
			form=proveedorForm(request.POST)
			if form.is_valid():
				form.save()
				objeto=Proveedor.objects.latest('id')
				tipo=request.POST['t_proveedor']
				if tipo=='Servicios':
					objeto.tipo='S'
				else:
					objeto.tipo='M'
				# objeto.tipo=t_proveedor
				objeto.save()
				return redirect('proveedor:gestion_proveedor')
				#return redirect('usuario:index')
				# return render(request, 'usuario/index.html')
			else:
				valor="Error al guardar"
		empresa=proveedorForm()
		context={'form':empresa}
		return render(request, 'proveedor/crear.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')

@login_required(login_url='/usuario/login')
def gestionProveedor(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		proveedores=Proveedor.objects.all()
		contactos=ContactoProveedor.objects.all()
		tipo='M'
		context={
		'proveedores':proveedores,
		'contactos':contactos,
		't':tipo,
		}
		return render(request,'proveedor/gestion.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')


@login_required(login_url='/usuario/login')
def crearContacto(request,id_proveedor):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		valor=""
		if request.method=='POST':
			form=contactoForm(request.POST)
			if form.is_valid():
				nom=request.POST['nombre']
				tel=request.POST['telefono']
				p=Proveedor.objects.get(id=id_proveedor)
				ContactoProveedor.objects.create(nombre=nom,telefono=tel, proveedor=p)
				return redirect('proveedor:gestion_proveedor')
			else:
				valor="Error al guardar"
		form=contactoForm()
		context={
		'form':form, 
		'valor':valor,
		}
		return render(request, 'proveedor/contacto.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')


@login_required(login_url='/usuario/login')
def eliminarProveedor(request, id_proveedor):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		p=Proveedor.objects.get(id=id_proveedor)
		if request.method=='POST':
			p.delete()
			return redirect('proveedor:gestion_proveedor')
		context={
		'p':p,
		}
		return render(request, 'proveedor/eliminarProveedor.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')

@login_required(login_url='/usuario/login')
def eliminarContacto(request, id_contacto):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		c=ContactoProveedor.objects.get(id=id_contacto)
		if request.method=='POST':
			c.delete()
			return redirect('proveedor:gestion_proveedor')
		context={
		'c':c,
		}
		return render(request, 'proveedor/eliminarContacto.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')

@login_required(login_url='/usuario/login')
def editarProveedor(request,id_proveedor):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		valor=""
		p=Proveedor.objects.get(id=id_proveedor)
		if request.method=='POST':
			form=proveedorForm(request.POST)
			if form.is_valid():
				p.nombre=request.POST['nombre']
				p.telefono=request.POST['telefono']
				p.direccion=request.POST['direccion']
				p.email=request.POST['email']
				tipo=request.POST['t_proveedor']
				if tipo=='Servicios':
					p.tipo='S'
				else:
					p.tipo='M'
				p.save()
				return redirect('proveedor:gestion_proveedor')
			else:
				valor="Error al actualizar"
		else:
			form=proveedorForm(instance=p)
			context={"form":form,'valor':valor}
			return render(request,'proveedor/crear.html',context)
	else:
		return render(request,'usuario/bienvenido/index.html')

@login_required(login_url='/usuario/login')
def editarContacto(request,id_contacto):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		valor=""
		c=ContactoProveedor.objects.get(id=id_contacto)
		if request.method=='POST':
			form=contactoForm(request.POST)
			if form.is_valid():
				nom=request.POST['nombre']
				tel=request.POST['telefono']
				c.nombre=nom
				c.telefono=tel
				c.save()
				return redirect('proveedor:gestion_proveedor')
			else:
				valor="Error al actualizar"
		else:
			form=contactoForm(instance=c)
			context={"form":form,'valor':valor}
			return render(request,'proveedor/contacto.html',context)
	else:
		return render(request,'usuario/bienvenido/index.html')


#Mostrar los contactos de los poveedores en Detalles del Proveedor
@login_required(login_url='/usuario/login')
def detallesProveedor(request,id_proveedor):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser :
		proveedor = Proveedor.objects.get(id=id_proveedor)
		contactos = ContactoProveedor.objects.filter(proveedor=proveedor)
		return render(request, 'proveedor/detalles.html',{'proveedor':proveedor,'contactos': contactos})
	else:
		return render(request,'usuario/bienvenido/index.html')