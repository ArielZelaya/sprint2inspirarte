from django.shortcuts import render, redirect
from .models import *
from django.views.generic.list import ListView
from apps.Pedido.models import Pedido, LineaPedido
from datetime import date

# Create your views here.

class ListadoVenta(ListView):
    model = Venta
    template_name = 'venta/listarventas.html'
    context_object_name = 'ventas'


def crearVenta(request, pk):
	pedido=Pedido.objects.get(id=pk)
	linea=LineaPedido.objects.get(Pedido=pedido)
	venta=Venta.objects.create(pedido=linea, fecha=date.today())
	return redirect('venta:listado_venta')