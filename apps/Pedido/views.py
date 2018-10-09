from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from datetime import time, date
import datetime
from .models import *
from apps.cotizacion.models import *
from apps.inventario.views import sacarMateriaPrima

from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

#Se crean las vistas las cuales son las funciones en el FRAMEWORK
#GestionPedido nos muestra una tabla con los pedidos y acciones sobre ellos

@login_required(login_url='/usuario/login')
def GestionPedido(request):
    usuario = User.objects.get(id=request.user.id) #Obtenemos el objeto usuario que esta logeado
    x = 1
    if usuario.is_superuser:  # Si el usuario es administrador se muestran todos los pedidos
        pedido_list=Pedido.objects.all() # Obtencion de todos los pedido
        return render(request,'pedido/gestionpedido.html',{'pedidos':pedido_list,'x':x, 'usuario': usuario})
    else: # Si el usuario no tiene derecho de administrador
        x=2
        usuario = User.objects.get(id=request.user.id) # Se muestra solo los pedidos que el mismo ha hecho
        pedido_list = Pedido.objects.all() # Obtencion de los pedidos que solo el ha hecho
    return render(request, 'pedido/gestionpedido.html', {'pedidos': pedido_list, 'x': x, 'usuario': usuario})#Solo buscara los pedidos con ese id de usuario

#RegistrarPedido nos permite crear un pedido apartir de una cotizacion existente

@login_required(login_url='/usuario/login')
def RegistrarPedido(request, id_cotizacion):
    cotizacion =Cotizacion.objects.get(id=id_cotizacion)#obtenemos el id de la cotizacion realizada
    detalles=DetalleCotizacion.objects.get(Cotizacion=cotizacion.id) #Obtenemos los detalles de ella misma
    if request.method == 'POST':
        pedido = Pedido() #Inicializacion del la instancia de pedido
        #Se completan los datos del pedido tomando los del form
        pedido.Cliente = cotizacion.cliente  # Se debe ingresar un objeto del tipo Cliente
        pedido.Valor_total = cotizacion.total
        pedido.Cant_productos = 1
        pedido.Deposito = request.POST.get('Deposito')
        pedido.Fecha = request.POST.get('Fecha')
        pedido.Num_seguimiento = cotizacion.id
        pedido.Estado = "Activo"
        pedido.save()
        #Se inicializa una linea de pedido
        linea = LineaPedido()
        linea.Pedido = pedido
        linea.Cotizacion = cotizacion  # Se debe ingresar un objeto del tipo Cotizacion
        linea.save()
        # sacarMateriaPrima(3, 50) este metodo saca materia prima del inventario
        return redirect('pedido:ges_pedi')
    return render(request, 'pedido/registrarpedido.html', {'cotizacion': cotizacion, 'detalles': detalles })

#DetallePedidos nos muestra la informacion correspondiente al pedido deseado

def DetallePedidos(request,id_pedido):
    usuario = User.objects.get(id=request.user.id)#Obtenemos el id del usuario para verficar si es administrador
    #Si es administrador podra ver todos los pedidos de los clientes sino solo los que el realizo
    pedido =Pedido.objects.get(id=id_pedido)
    cliente=Cliente.objects.get(id=pedido.Cliente.id)
    linea=LineaPedido.objects.all()

    detalleCoti=DetalleCotizacion.objects.all()
    return render(request,'pedido/DetallePedido.html', {'pedido': pedido, 'cliente': cliente, 'linea': linea, 'detalleCoti':detalleCoti, 'usuario':usuario})

#EliminarPedido nos permite eliminar el pedido deseado

@login_required(login_url='/usuario/login')
def eliminarPedido(request,id_pedido):
    if request.method=='POST':
        pedido=Pedido.objects.get(id=id_pedido)#obtenemos el id del pedido a borrar
        pedido.delete()
        return redirect('pedido:ges_pedi')
    return render(request,'pedido/eliminarPedido.html')

#CambiarEstado nos permite mover el estado en la produccion del pedido
@login_required(login_url='/usuario/login')
def CambiarEstado(request,id_pedido):
    if request.method=="POST":
        if request.method == 'POST':
            pedido = Pedido.objects.get(id=id_pedido)
            pedido.Estado = request.POST.get('Estado')
            pedido.save()
            return redirect('pedido:ges_pedi')
    return render(request, 'pedido/EstadoPedido.html')

#Rastreo nos permite poder ver un pedido sin la necesidad de entrar al sistema
@login_required(login_url='/usuario/login')
def Rastreo(request):
    if request.method=="POST":
        id = request.POST.get('id')
        pedido=Pedido.objects.get(id=id)
        return redirect('pedido:deta_pedi',pedido)
    return render(request, 'pedido/menu.html')


