from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'proveedor'

urlpatterns =[

	#USUARIO
	url(r'^crearProveedor$', crearProveedor, name="crear_proveedor"),
	url(r'^gestion$', gestionProveedor, name="gestion_proveedor"),
	url(r'^contacto/(?P<id_proveedor>\d+)/$', crearContacto,name="crear_contacto"),
	url(r'^eliminarProveedor/(?P<id_proveedor>\d+)/$', eliminarProveedor, name="elim_proveedor"),
	url(r'^eliminarContacto/(?P<id_contacto>\d+)/$', eliminarContacto, name="elim_contacto"),
	url(r'^editarProveedor/(?P<id_proveedor>\d+)/$', editarProveedor, name="edit_proveedor"),
	url(r'^editarContacto/(?P<id_contacto>\d+)/$', editarContacto, name="edit_contacto"),
]