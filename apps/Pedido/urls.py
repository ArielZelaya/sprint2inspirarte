from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'pedido'
#Se crean las url que estan relacionadas con las vistas las cuales son funciones
urlpatterns =[
    url(r'^gestionPedido$', GestionPedido, name="ges_pedi"),
    url(r'^registrarPedido/(?P<id_cotizacion>\d+)/$', RegistrarPedido, name="reg_pedi"),
url(r'^rastreo$', Rastreo , name="ras_pedi"),
    url(r'^eliminarPedido/(?P<id_pedido>\d+)/$', eliminarPedido,name="del_pedi"),
    url(r'^CambiarEstado/(?P<id_pedido>\d+)/$', CambiarEstado,name="esta_pedi"),
    url(r'^detallePedido/(?P<id_pedido>\d+)/$', DetallePedidos,name="deta_pedi"),
]