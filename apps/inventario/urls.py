from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

app_name = 'inventario'

urlpatterns =[

	#ADMINISTRAR PRODUCTOS
	url(r'^administrarProductos', adminProductos ,name="adm_pro"),
	url(r'^registroInventario$', regInventario ,name="reg_inv"),
]
