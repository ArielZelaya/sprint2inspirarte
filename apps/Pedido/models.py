from django.db import models
from apps.usuario.models import Cliente
from apps.cotizacion.models import Cotizacion
# Create your models here.


#Creacion de los modelos

#Este modelo es el pedido el cual representa a un pedido en general
class Pedido(models.Model):
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE) #Se asigna un cliente
    Valor_total= models.FloatField()
    Cant_productos= models.IntegerField()
    Deposito=models.FloatField()
    Fecha= models.DateField()
    Num_seguimiento=models.CharField(max_length=50)
    Estado=models.CharField(max_length=10)
    class Meta:
        verbose_name='pedido'
        verbose_name_plural='pedidos'
    def __str__(self):
        return '%s' %(self.id)
#Este modelo es una linea de pedido puesto que un pedido puede tener varias cotizaciones
#Se ha agregado este modelo representando 1.n

class LineaPedido(models.Model):
    Pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE) #se le asigna un pedido
    Cotizacion=models.ForeignKey(Cotizacion, on_delete=models.CASCADE) # se asigna a una cotizacion

    class Meta:
        verbose_name='LineaPedido'
        verbose_name_plural='LineaPedidos'
    def __str__(self):
        return '%s' %(self.id)