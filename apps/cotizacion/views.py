from django.shortcuts import render
from .models import *
from .forms import *
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
# Create your views here.

def gestionProducto(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser:
		productos =TipoProducto.objects.all()
		context={'productos':productos}
		return render(request,'cotizacion/gestionProducto.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')

class ListadoProducto(ListView):
    model = TipoProducto
    template_name = 'cotizacion/gestionProducto.html'
    context_object_name = 'productos'

class crearProducto(CreateView):
    template_name = 'cotizacion/crearProducto.html'
    form_class = TipoProductoForm
    success_url = reverse_lazy('cotizacion:listado_productos')

class modificarProducto(UpdateView):
    model = TipoProducto
    template_name = 'cotizacion/crearProducto.html'
    form_class = TipoProductoForm
    success_url = reverse_lazy('cotizacion:listado_productos')

class eliminarProducto ( DeleteView ):
	model = TipoProducto
	template_name='cotizacion/eliminarProducto.html'
	success_url = reverse_lazy('cotizacion:listado_productos')



#Gestion Tamanio

def gestionTamanio(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser:
		tamanio =TamanioProducto.objects.all()
		context={'tamanio':tamanio}
		return render(request,'cotizacion/gestionTamanio.html', context)
	else:
		return render(request,'usuario/bienvenido/index.html')


class ListadoTamanio(ListView):
    model = TamanioProducto
    template_name = 'cotizacion/gestionTamanio.html'
    context_object_name = 'tamanio'

class crearTamanio(CreateView):
    template_name = 'cotizacion/crearTamanio.html'
    form_class = TamanioProductoForm
    success_url = reverse_lazy('cotizacion:listado_tamanio')

class modificarTamanio(UpdateView):
    model = TamanioProducto
    template_name = 'cotizacion/crearProducto.html'
    form_class = TamanioProductoForm
    success_url = reverse_lazy('cotizacion:listado_tamanio')

class eliminarTamanio ( DeleteView ):
	model = TamanioProducto
	template_name='cotizacion/eliminarTamanio.html'
	success_url = reverse_lazy('cotizacion:listado_tamanio')



#Gestion Precio

def gestionPrecio(request):
	administrador=User.objects.get(id=request.user.id)
	if administrador.is_superuser:
		lista=[]
		productos=TipoProducto.objects.all()
		for p in productos:
			if p.activo:
				precios=PrecioProducto.objects.filter(producto=p)
				obj={
				'producto':p,
				'precios':precios
				}
				lista.append(obj)
		context={
		'lis':lista
		}
		return render(request, 'cotizacion/gestionPrecio.html',context)
	else:
		return render(request,'usuario/bienvenido/index.html')

class crearPrecio(CreateView):
    template_name = 'cotizacion/crearPrecio.html'
    form_class = PrecioProductoForm
    success_url = reverse_lazy('cotizacion:gestion_Precio')

class modificarPrecio(UpdateView):
    model = PrecioProducto
    template_name = 'cotizacion/crearPrecio.html'
    form_class = PrecioProductoForm
    success_url = reverse_lazy('cotizacion:gestion_Precio')

class eliminarPrecio( DeleteView ):
	model = PrecioProducto
	template_name='cotizacion/eliminarPrecio.html'
	success_url = reverse_lazy('cotizacion:gestion_Precio')


#Gestion Cotizacion
class ListadoCotizacion(ListView):
    model = Cotizacion
    template_name = 'cotizacion/gestioCotizacion.html'
    context_object_name = 'cotizacion'

def detallesCotizacion(request,id):
	detalles=DetalleCotizacion.objects.filter(Cotizacion=id)
	return render(request, 'cotizacion/detalles.html', {'detalles':detalles})

class eliminarCotizacion(DeleteView):
	model = Cotizacion
	template_name='cotizacion/eliminarCotizacion.html'
	success_url = reverse_lazy('cotizacion:listado_cotizacion')