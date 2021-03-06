"""Inspirarte URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^usuario/', include('apps.usuario.urls')),
	url(r'^proveedor/', include('apps.proveedor.urls')),

    url(r'^inventario/', include('apps.inventario.urls')),
    url(r'^pedido/', include('apps.Pedido.urls')),

    url(r'^admin/', admin.site.urls),    
    #Index temporal
    url(r'^index', views.index, name="index"),

    #Sprint 2
    url(r'^cotizacion/', include('apps.cotizacion.urls')),
    url(r'^inventario/', include('apps.inventario.urls')),
    url(r'^venta/', include('apps.venta.urls')),
    
]
