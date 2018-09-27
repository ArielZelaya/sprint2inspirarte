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
<<<<<<< HEAD
		return '%s' %(self.descripcion)
=======
		return '%s' %(self.id)
>>>>>>> origin/Ariel2

class DetalleCotizacion(models.Model):
	Cotizacion = models.ForeignKey(Cotizacion, on_delete=models.CASCADE)
	cantidad = models.IntegerField()
	producto = models.ForeignKey(PrecioProducto, on_delete=models.CASCADE)
	subtotal = models.FloatField(null=True)
	disenio = models.BooleanField()
	def __str__(self):
		return '%s' %(self.id)


