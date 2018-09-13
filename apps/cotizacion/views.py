from django.shortcuts import render
from .models import *
from django.contrib.auth.models import User

# Create your views here.

# def gestionProducto(request):
# 	administrador=User.objects.get(id=request.user.id)
# 	if administrador.is_superuser:
# 		if request.method=='POST':
# 			