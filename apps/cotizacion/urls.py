from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

app_name = 'cotizacion'

urlpatterns =[

	#Gestion tamaño
	url(r'^gestionTamanio$', ListadoTamanio.as_view(), name="listado_tamanio"),
	url(r'^crearTamanio/$', crearTamanio.as_view(), name="crear_tamanio"),
	url(r'^modificarTamanio/(?P<pk>.+)/$',modificarTamanio.as_view(), name="modificar_tamanio"),
	url(r'^eliminarTamanio/(?P<pk>.+)/$', eliminarTamanio.as_view(), name="eliminar_tamanio"),
	url(r'^menu', menu, name='menu'),


	#Gestion precio
	url(r'^gestionPrecio$', gestionPrecio, name="gestion_precio"),
	url(r'^crearPrecio/$', crearPrecio.as_view(), name="crear_precio"),
	url(r'^modificarPrecio/(?P<pk>.+)/$',modificarPrecio.as_view(), name="modificar_precio"),
	url(r'^eliminarPrecio/(?P<pk>.+)/$', eliminarPrecio.as_view(), name="eliminar_precio"),

	
	# Gestion producto
	url(r'^gestionProductos/$', ListadoProducto.as_view(), name="listado_productos"),
	url(r'^crearProducto/$', crearProducto.as_view(), name="crear_producto"),
	url(r'^modificarProducto/(?P<pk>.+)/$',modificarProducto.as_view(), name="modificar_producto"),
	url(r'^eliminarProducto/(?P<pk>.+)/$', eliminarProducto.as_view(), name="eliminar_producto"),


	#Gestion cotizacion
	url(r'^gestionCotizacion/$', ListadoCotizacion.as_view(), name="listado_cotizacion"),
	url(r'^gestionCotizacion2/$', ListadoCotizacion2.as_view(), name="listado_cotizacion2"),
	url(r'^detalle/(?P<id>\d+)/$', detallesCotizacion, name="detalle_cotizacion"),
	url(r'^eliminarCotizacion/(?P<pk>.+)/$', eliminarCotizacion.as_view(), name="eliminar_cotizacion"),

	# Parte de ricardo
	url(r'^formulario$', cotizacion_cliente, name='formulario'),
    url(r'^subconjunto/(?P<produ>\w{0,50})/$', obtener_subconjunto, name='mia'),



]
