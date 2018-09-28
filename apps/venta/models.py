from django.db import models
from apps.Pedido.models import LineaPedido

# Create your models here.

class Venta(models.Model):
	pedido = models.ForeignKey(LineaPedido, on_delete=models.CASCADE)
	fecha= models.DateField()

	def __str__(self):
		return '%s' %(self.id)
