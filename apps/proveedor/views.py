from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def crearProveedor(request):
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
			return redirect('usuario:index')
			# return render(request, 'usuario/index.html')
		else:
			valor="Error al guardar"
	empresa=proveedorForm()
	context={'form':empresa}
	return render(request, 'proveedor/crear.html', context)


def gestionProveedor(request):
	proveedores=Proveedor.objects.all()
	contactos=ContactoProveedor.objects.all()
	tipo='M'
	context={
	'proveedores':proveedores,
	'contactos':contactos,
	't':tipo,
	}
	return render(request,'proveedor/gestion.html', context)

def crearContacto(request,id_proveedor):
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


def eliminarProveedor(request, id_proveedor):
	p=Proveedor.objects.get(id=id_proveedor)
	if request.method=='POST':
		p.delete()
		return redirect('proveedor:gestion_proveedor')
	context={
	'p':p,
	}
	return render(request, 'proveedor/eliminarProveedor.html', context)

def eliminarContacto(request, id_contacto):
	c=ContactoProveedor.objects.get(id=id_contacto)
	if request.method=='POST':
		c.delete()
		return redirect('proveedor:gestion_proveedor')
	context={
	'c':c,
	}
	return render(request, 'proveedor/eliminarContacto.html', context)

def editarProveedor(request,id_proveedor):
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

def editarContacto(request,id_contacto):
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