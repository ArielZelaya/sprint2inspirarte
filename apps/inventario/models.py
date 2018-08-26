from django.db import models
from apps.proveedor.models import *
from apps.usuario.models import *
# Create your models here.

#Producto: hace referencia a los productos que se adquieren periodicamente, como los son bienes y servicios
class Producto(models.Model):
	tipo = models.CharField(max_length=1)
	nombre = models.CharField(max_length=60)
	descripcion = models.CharField(max_length=100)
	unidades = models.CharField(max_length=20)
	class Meta:
		verbose_name='Producto'
		verbose_name_plural='Productos'
	def __str__(self):
		return '%s' %(self.nombre)

#CatalogoExistencias: contiene 
class CatalogoExistencias(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	class Meta:
		verbose_name='Catalogo de Existencia'
		verbose_name_plural='Catalogo de Existencias'
	def __str__(self):
		return '%s' %(self.producto)

class CatalogoProductos(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	precioUnitario = models.FloatField()
	class Meta:
		verbose_name='Catalogo de Producto'
		verbose_name_plural='Catalogo de Productos'
	def __str__(self):
		return '%s' %(self.producto)

class RegistroDeInventario(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, null=True, on_delete=models.CASCADE)
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=1)
	fecha = models.DateField()
	descripcion = models.CharField(max_length=200)
	precio = models.FloatField(null=True)
	cantidad = models.IntegerField()
	total = models.FloatField()
	class Meta:
		verbose_name='Registro de Inventario'
		verbose_name_plural='Registros de Inventario'
	def __str__(self):
		return '%s' %(self.proveedor)