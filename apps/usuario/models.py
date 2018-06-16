from django.db import models
from django.contrib.auth.models import User

class Cliente(User):
	#idCliente = model.IntegerField(primary_key=True)
	dui = models.IntegerField()
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=100)
	tipo = models.CharField(max_length=1)
	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
	def __str__(self):
		return '%s' %(self.first_name)

class Departamento(models.Model):
	"""docstring for Departamento"""
	nombre = models.CharField(max_length=20)
	def __init__(self, arg):
		super(Departamento, self).__init__()
		self.arg = arg
		
class Puesto(models.Model):
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=30)
	funcion = models.CharField(max_length=500)
	class Meta:
		verbose_name='Puesto'
		verbose_name_plural='Puestos'
	def __str__(self):
		return '%s' %(self.nombre)

class Empleado(User):
	#idEmpleado = model.IntegerField()
	puesto = models.ForeignKey(Puesto, on_delete=models.CASCADE) 
	dui = models.IntegerField()
	nit = models.IntegerField()
	isss = models.IntegerField()
	nup = models.IntegerField()
	codigo = models.CharField(max_length=6)
	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'
	def __str__(self):
		return '%s' %(self.first_name)

class Contrato(models.Model):
	#idContrato = model.IntegerField()
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=30)
	fechaCelebracion = models.DateField()
	duracion = models.CharField(max_length=15)
	fechaInicio = models.DateField()
	fechaFinal = models.DateField()
	horaEntrada = models.DateTimeField()
	horaSalida = models.DateTimeField()
	salario = models.FloatField()
	vigente = models.BooleanField()
	class Meta:
		verbose_name='Contrato'
		verbose_name_plural='Contratos'
	def __str__(self):
		return '%s' %(self.empleado)