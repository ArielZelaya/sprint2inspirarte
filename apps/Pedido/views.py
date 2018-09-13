from django.shortcuts import render

# Create your views here.
def GestionPedido(request):
     return render(request,'pedido/gestionpedido.html')