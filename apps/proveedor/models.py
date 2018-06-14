from django.db import models

# Create your models here.
class Proveedor(models.Model):
	nombreProveedor=models.CharField(max_length=30)
	telefonoProveedor = models.IntegerField()
	direccionProveedor= models.CharField(max_length=100)
	tipoProveedor = models.CharField(max_length=1)
	emailProveedor = models.EmailField()
	class Meta:
		verbose_name='Proveedor'
		verbose_name_plural='Proveedores'
	def __str__(self):
		return '%s' %(self.nombreProveedor)