from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *
from . import views

app_name = 'pedido'

urlpatterns =[
    url(r'^gestionPedido$', GestionPedido, name="ges_pedi")
]