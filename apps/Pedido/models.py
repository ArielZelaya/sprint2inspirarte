from django.db import models
from apps.usuario.models import Cliente
from apps.cotizacion.models import Cotizacion
# Create your models here.

class Pedido(models.Model):
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
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

class LineaPedido(models.Model):
    Pedido=models.ForeignKey(Pedido, on_delete=models.CASCADE)
    Cotizacion=models.ForeignKey(Cotizacion, on_delete=models.CASCADE)

    class Meta:
        verbose_name='LineaPedido'
        verbose_name_plural='LineaPedidos'
    def __str__(self):
        return '%s' %(self.id)