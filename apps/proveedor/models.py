from django.db import models
from django import forms

# Create your models here.
class Proveedor(models.Model):
	nombre = models.CharField(max_length=30)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1)
	email = models.EmailField()
	class Meta:
		verbose_name='Proveedor'
		verbose_name_plural='Proveedores'
	def __str__(self):
		return '%s' %(self.nombre)

class ContactoProveedor(models.Model):
	proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=60)
	telefono = models.IntegerField()
	class Meta:
		verbose_name='Contacto'
		verbose_name_plural='Contactos'
	def __str__(self):
		return '%s' %(self.nombre)