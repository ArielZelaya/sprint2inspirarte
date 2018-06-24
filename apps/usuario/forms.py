from django import forms
from .models import *


class clienteForm(forms.ModelForm):
	class Meta:
		model=Cliente
		fields={
		'username',
		'first_name',
		'last_name',
		'email',
		'password',
		'dui',
		'telefono',
		'direccion',
		}
		labels={
		'username':'Ingrese su nombre de usuario',
		'first_name':'Ingrese su nombre',
		'last_name':'Ingrese su apellido',
		'email':'Correo electronico',
		'password':'Contraseña',
		'dui':'Ingrese su dui',
		'telefono':'Numero telefonico',
		'direccion':'Ingrese su direccion',
		}