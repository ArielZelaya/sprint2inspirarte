from django.db import models
from apps.usuario.models import Cliente, Empleado
from apps.inventario.models import Producto

# Create your models here.

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=30)
	activo = models.BooleanField()
	precio = models.FloatField(null=True)
	def __str__(self):
		return '%s' %(self.nombre)

class DetalleCotizacion(models.Model):
	cantidad = models.IntegerField()
	tamaño = models.CharField(max_length=25)
	tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
	material = models.ForeignKey(Producto, on_delete=models.CASCADE)
	subtotal = models.FloatField(null=True)
	disenio = models.BooleanField()
	archivo = models.FileField(upload_to='uploads/{0}'.format("%Y-%m-%d/%H_%M_%S"), null=True)


class Cotizacion(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	fecha = models.DateField(null=True)
	detalle = models.ForeignKey(DetalleCotizacion, on_delete=models.CASCADE)
	total = models.FloatField(null=True)
	class Meta:
		verbose_name='Cotizacion'
		verbose_name_plural='Cotizaciones'
	def __str__(self):
		return '%s' %(self.detalle)
