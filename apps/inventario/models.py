# dsi2018\apps\inventario\models.py
# MODULO: inventario
# OBJETIVO: alamcena las clases necesarias para formar la estructura del modulo inventario 
# ANALISTA PROGRAMADOR: Edwin Molina,	FECHA CREACION: 15/08/2018
# MODIFICADO POR: Edwin Molina,			FECHA MODIFICACION: 16/09/2018

from django.db import models
from apps.proveedor.models import *
from apps.usuario.models import *

#INICIO DE CLASE (Producto): hace referencia a los productos que se adquieren periodicamente, como los son bienes y servicios
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
#FINAL DE CLASE (Producto)

#INICIO DE CLASE (CatalogoExistencias): hace referencia a los productos en existente segun las entradas realizadas (es el inventario mismo)
class CatalogoExistencias(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	precio = models.FloatField()
	cantidad = models.IntegerField()
	class Meta:
		verbose_name='Catalogo de Existencia'
		verbose_name_plural='Catalogo de Existencias'
	def __str__(self):
		return '%s' %(self.producto)
#FINAL DE CLASE (CatalogoExistencias):

#INICIO DE CLASE (CatalogoProductos): hace referencia al registro de proveedores y prodcutos vinculados
class CatalogoProductos(models.Model):
	producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	class Meta:
		verbose_name='Catalogo de Producto'
		verbose_name_plural='Catalogo de Productos'
	def __str__(self):
		return '%s' %(self.producto)
#FINAL DE CLASE (CatalogoProductos): 

#INICIO DE CLASE (RegistroDeInventario): hace referencia al registro de entradas y salidas de materia prima
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
#FINAL DE CLASE (RegistroDeInventario): 