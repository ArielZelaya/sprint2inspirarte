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

	#Gestion precio
	url(r'^gestionPrecio$', gestionPrecio, name="gestion_Precio"),
	url(r'^crearPrecio/$', crearPrecio.as_view(), name="crear_precio"),
	url(r'^modificarPrecio/(?P<pk>.+)/$',modificarPrecio.as_view(), name="modificar_precio"),
	url(r'^eliminarProducto/(?P<pk>.+)/$', eliminarPrecio.as_view(), name="eliminar_precio"),

	
	# Gestion producto
	url(r'^gestionProductos/$', ListadoProducto.as_view(), name="listado_productos"),
	url(r'^crearProducto/$', crearProducto.as_view(), name="crear_producto"),
	url(r'^modificarProducto/(?P<pk>.+)/$',modificarProducto.as_view(), name="modificar_producto"),
	url(r'^eliminarProducto/(?P<pk>.+)/$', eliminarProducto.as_view(), name="eliminar_producto"),


	#Gestion cotizacion
	url(r'^gestionCotizacion/$', ListadoCotizacion.as_view(), name="listado_cotizacion"),
	url(r'^detalle/(?P<id>\d+)/$', detallesCotizacion, name="detalle_cotizacion"),
	url(r'^eliminarCotizacion/(?P<pk>.+)/$', eliminarCotizacion.as_view(), name="eliminar_cotizacion"),





]
