from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'usuario'

urlpatterns =[
	#EMPLEADO
    url(r'^$',views.index,name='usuario'),
    url(r'^gestionEmpleado', gestionEmpleado, name="ges_emp"),
	url(r'^confirmarHabilitacion/(?P<id_user>\d+)/$', habilitarUsuario, name='act_emp'),
	url(r'^registrarEmpleado$', registrarEmpleado, name="reg_emp"),
	url(r'^editarEmpleado/(?P<id_user>\d+)/$', editarEmpleado, name='edt_emp'),
	url(r'^cancelarContrato/(?P<id_user>\d+)/$', cancelarContrato, name='can_cto'),
	url(r'^crearContrato/(?P<id_user>\d+)/$', crearContrato, name='cre_cto'),
	url(r'^contratosNoVigentes$', noVigentes, name='nvi_cto'),

	#USUARIO
	url(r'^index$', index, name="index"),
	url(r'^login$', iniciarSesion, name="login"),
	url(r'^logout$', cerrarSesion, name="logout"),
	url(r'^crearCliente$', crearCliente,name="crear_cliente"),
	url(r'^editarCliente/(?P<id_user>\d+)/$', editarCliente,name="editar_cliente"),
	url(r'^gestionCliente$', gestionCliente, name="gestion_cliente"),
	url(r'^tipoCliente/(?P<id_user>\d+)/$', tipoCliente,name="tipo_cliente"),
	url(r'^wc$', wc, name='wlc'),	
]
