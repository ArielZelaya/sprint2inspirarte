from django.db import models
from django.contrib.auth.models import User

class Cliente(User):
	#idCliente = model.IntegerField(primary_key=True)
	dui = models.IntegerField()
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=500)
	tipo = models.CharField(max_length=1)
	class Meta:
		verbose_name='Cliente'
		verbose_name_plural='Clientes'
	def __str__(self):
		return '%s' %(self.first_name)

class Departamento(models.Model):
	nombre = models.CharField(max_length=50)
	descripcion = models.CharField(max_length=500)
	class Meta:
		verbose_name='Departamento'
		verbose_name_plural='Departamentos'
	def __str__(self):
		return '%s' %(self.nombre)
		
class Puesto(models.Model):
	departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50)
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
	domicilio = models.CharField(max_length=500)
	telefono = telefono = models.IntegerField()
	class Meta:
		verbose_name='Empleado'
		verbose_name_plural='Empleados'
	def __str__(self):
		return '%s' %(self.first_name)

class Contrato(models.Model):
	#idContrato = model.IntegerField()
	empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
	tipo = models.CharField(max_length=50)
	fechaCelebracion = models.DateField()
	duracion = models.CharField(max_length=50)
	fechaInicio = models.DateField()
	fechaFinal = models.DateField()
	horaEntrada = models.CharField(max_length=10)
	horaSalida = models.CharField(max_length=10)
	diasLaborales = models.CharField(max_length=135)
	salario = models.FloatField()
	vigente = models.BooleanField()
	class Meta:
		verbose_name='Contrato'
		verbose_name_plural='Contratos'
	def __str__(self):
		return '%s' %(self.empleado)