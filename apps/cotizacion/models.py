from django.db import models
from apps.usuario.models import Cliente, Empleado
from apps.inventario.models import Producto

# Create your models here.

class TipoProducto(models.Model):
	nombre = models.CharField(max_length=30)
	activo = models.BooleanField()
	def __str__(self):
		return '%s' %(self.nombre)

class TamanioProducto(models.Model):
	tamaño = models.CharField(max_length=20)
	descripcion = models.CharField(max_length=30)
	def __str__(self):
		return '%s' %(self.descripcion)

class PrecioProducto(models.Model):
	producto = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
	tamanio = models.ForeignKey(TamanioProducto, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	precio = models.DecimalField(max_digits = 5,decimal_places = 2)
	tipoCliente = models.CharField(max_length=1)
	def __str__(self):
		return '%s' %(self.producto)


class Cotizacion(models.Model):
	cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
	fecha = models.DateField(null=True)
	descripcion = models.CharField(max_length=200)
	# detalle = models.ManyToOne(DetalleCotizacion, on_delete=models.CASCADE)
	total = models.FloatField(null=True)
	class Meta:
		verbose_name='Cotizacion'
		verbose_name_plural='Cotizaciones'
	def __str__(self):
		return '%s' %(self.detalle)

class DetalleCotizacion(models.Model):
	Cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	tamaño = models.CharField(max_length=25)
	tipo = models.ForeignKey(TipoProducto, on_delete=models.CASCADE)
	material = models.ForeignKey(Producto, on_delete=models.CASCADE)
	subtotal = models.FloatField(null=True)
	disenio = models.BooleanField()
	archivo = models.FileField(upload_to='uploads/{0}'.format("%Y-%m-%d/%H_%M_%S"), null=True)
	def __str__(self):
		return '%s' %(self.id)



