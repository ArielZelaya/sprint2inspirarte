from django.db import models
from apps.usuario.models import Cliente
# Create your models here.

class Pedido(models.Model):
    Numero=models.IntegerField()
    Cliente= models.ForeignKey(Cliente, on_delete=models.CASCADE)
    Cotizacion=models.IntegerField() 
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
        return '%s' %(self.Cliente)