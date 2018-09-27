from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'pedido'

urlpatterns =[
    url(r'^gestionPedido$', GestionPedido, name="ges_pedi"),
    url(r'^registrarPedido$', RegistrarPedido, name="reg_pedi"),
    url(r'^eliminarPedido/(?P<id_pedido>\d+)/$', eliminarPedido,name="del_pedi"),
    url(r'^CambiarEstado/(?P<id_pedido>\d+)/$', CambiarEstado,name="esta_pedi"),
    url(r'^detallePedido/(?P<id_pedido>\d+)/$', DetallePedidos,name="deta_pedi"),
]