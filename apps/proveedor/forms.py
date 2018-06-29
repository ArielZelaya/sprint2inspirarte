from django import forms
from .models import *


class proveedorForm(forms.ModelForm):
	class Meta:
		model=Proveedor
		fields={
		'nombre',
		'telefono',
		'direccion',
		'email',
		}
		labels={
		'nombre':'Nombre del proveedor',
		'telefono':'Numero telefonico',
		'direccion':'Direccion',
		'email':'Correo electronico',
		}


class contactoForm(forms.ModelForm):
	class Meta:
		model=ContactoProveedor
		fields={
		'nombre',
		'telefono',
		}
		labels={
		'nombre':'Nombre del contacto',
		'telefono':'Telefono del contacto',
		}