from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Cliente(User):
	#idCliente= model.IntegerField(primary_key=True)
	diuCliente= models.IntegerField()
	direccionCliente= models.IntegerField()
	tipoCliente = models.CharField(max_length=100)
	tipoCliente = models.CharField(max_length=1)
	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
	def __str__(self):
		return '%s' %(self.first_name)

class Empleado(User):
	#idEmpleado = model.IntegerField() 
	duiEmpleado =models.IntegerField()
	nitEmpleado = models.IntegerField()
	isssEmpleado = models.IntegerField()
	afpEmpleado = models.IntegerField()
	codigoEmpleado = models.CharField(max_length=6)
	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'
	def __str__(self):
		return '%s' %(self.first_name)

class Departamento(models.Model):
	"""docstring for Departamento"""
	nombreDepartamento=models.CharField(max_length=20)
	def __init__(self, arg):
		super(Departamento, self).__init__()
		self.arg = arg
		
class Puesto(models.Model):
	puesto=models.CharField(max_length=30)
	funcion= models.CharField(max_length=500)
	departamento = models.ForeignKey(Departamento)
	class Meta:
		verbose_name='Puesto'
		verbose_name_plural='Puestos'
	def __str__(self):
		return '%s' %(self.puesto)

class Contrato(models.Model):
	#idContrato = model.IntegerField()
	tipoContrato = models.CharField(max_length=30)
	fechaContrato = models.DateField()
	duracionContrato = models.CharField(max_length=15)
	fechaInicio = models.DateField()
	fechaFinal = models.DateField()
	horaEntrada = models.DateTimeField()
	horaSalida = models.DateTimeField()
	salario = models.FloatField()
	vigente = models.BooleanField()
	empleado =models.ForeignKey(Empleado)
	class Meta:
		verbose_name='Contrato'
		verbose_name_plural='Contratos'
	def __str__(self):
		return '%s' %(self.empleado)