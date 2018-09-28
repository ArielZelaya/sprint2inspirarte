from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

app_name = 'venta'

urlpatterns =[

	#Gestion tamaño
	url(r'^listarVentas$', ListadoVenta.as_view(), name="listado_venta"),
	url(r'^crearVenta/(?P<pk>.+)/$', crearVenta, name="crear_venta"),
	]