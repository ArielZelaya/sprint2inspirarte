# dsi2018\apps\inventario\urls.py
# MODULO: inventario
# OJETIVO: almacenar las urls correpondientes a las views (controladores) del modulo inventario
# ANALISTA PROGRAMADOR: Edwin Molina,	FECHA CREACION: 18/08/2018
# MODIFICADO POR: Edwin Molina,			FECHA MODIFICACION: 16/09/2018

from __future__ import unicode_literals
from __future__ import absolute_import

from django.conf.urls import url, include
from .views import *

app_name = 'inventario'

urlpatterns =[

	#ADMINISTRAR PRODUCTOS
	url(r'^administrarProductos', adminProductos ,name="adm_pro"),

	url(r'^editarProducto/(?P<id_producto>\d+)$', editarProducto, name='edt_pro'),
	url(r'^proveedoresProducto/(?P<id_producto>\d+)$', consultarProveedores, name='cop_prv'),
	url(r'^desvincularProveedor/(?P<id_producto>\d+)//(?P<id_proveedor>\d+)/$', desvincularProveedor, name="des_prv"),
	#REGISTRO DE INVENTARIO
	url(r'^sacarMateriaPrima/(?P<producto_id>\d+)/$', sacarMateriaPrima ,name="sac_pro"),
	url(r'^registroInventario$', regInventario ,name="reg_inv"),
]
