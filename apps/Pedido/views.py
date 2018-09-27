from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
import datetime
from .models import *
from apps.cotizacion.models import DetalleCotizacion
from apps.inventario.views import sacarMateriaPrima

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
# Create your views here.
def GestionPedido(request):
    usuario=User.objects.get(id=request.user.id)
    if usuario.is_superuser:
        pedido_list=Pedido.objects.all()
        #paginator = Paginator(pedido_list,5)
		#page = request.GET.get('page')
		#pedidos = paginator.get_page(page)
        return render(request,'pedido/gestionpedido.html',{'pedidos':pedido_list})
    else:
        
        return render(request,'pedido/gestionpedido.html',{'usuario':usuario.id})#Solo buscara los pedidos con ese id de usuario
@login_required(login_url='/usuario/login')
def RegistrarPedido(request):
    usuario=User.objects.get(id=request.user.id)
    clientes=Cliente.objects.all()
    if usuario.is_superuser:
        id=True
    else:
        id=False
    if request.method == 'POST':
        pedido=Pedido()

        pedido.Cliente = Cliente.objects.get(id=4)#Se debe ingresar un objeto del tipo Cliente
        pedido.Valor_total=request.POST.get('Valor_total')
        pedido.Cant_productos=request.POST.get('Cant_productos')
        pedido.Deposito=request.POST.get('Deposito')
        pedido.Fecha=request.POST.get('Fecha')
        pedido.Num_seguimiento=request.POST.get('Num_seguimiento')
        pedido.Estado=request.POST.get('Estado')
        pedido.save()
        linea= LineaPedido()
        linea.Pedido=pedido
        linea.Cotizacion=Cotizacion.objects.get(id=4)#Se debe ingresar un objeto del tipo Cotizacion
        linea.save()
        #sacarMateriaPrima(3, 50)
        return redirect('pedido:ges_pedi')
    return render(request,'pedido/registrarpedido.html', {'clientes':clientes  ,'id': id, 'usuario': usuario})

def DetallePedidos(request,id_pedido):
    usuario = User.objects.get(id=request.user.id)
    pedido =Pedido.objects.get(id=id_pedido)
    cliente=Cliente.objects.get(id=pedido.Cliente.id)
    linea=LineaPedido.objects.all()

    detalleCoti=DetalleCotizacion.objects.all()
    return render(request,'pedido/DetallePedido.html', {'pedido': pedido, 'cliente': cliente, 'linea': linea, 'detalleCoti':detalleCoti, 'usuario':usuario})
@login_required(login_url='/usuario/login')
def eliminarPedido(request,id_pedido):
    if request.method=='POST':
        pedido=Pedido.objects.get(id=id_pedido)
        pedido.delete()
        return redirect('pedido:ges_pedi')
    return render(request,'pedido/eliminarPedido.html')

def CambiarEstado(request,id_pedido):
    if request.method=="POST":
        if request.method == 'POST':
            pedido = Pedido.objects.get(id=id_pedido)
            pedido.Estado = request.POST.get('Estado')
            pedido.save()
            return redirect('pedido:ges_pedi')
    return render(request, 'pedido/EstadoPedido.html')

