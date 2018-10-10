from django import forms
from .models import *


class proveedorForm(forms.ModelForm):
	class Meta:
		model=Proveedor
		fields=[
		'nombre',
		'telefono',
		'direccion',
		'email',
		]
		labels={
		'nombre':'Nombre del proveedor',
		'telefono':'Número teléfonico',
		'direccion':'Dirección',
		'email':'Correo electrónico',
		}
		widgets={
			'nombre': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'nombre', 'type':'text',}),
			'telefono': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'telefono', 'type':'text', 'pattern':'-?[0-9]*(\[0-9]+)?'}),
			'direccion':forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'direccion', 'type':'text',}),
			'email': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'email', 'type':'email',}),
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
		widgets={
			'nombre': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'nombre', 'type':'text',}),
			'telefono': forms.TextInput(attrs={'class': 'mdl-textfield__input', 'id': 'telefono', 'type':'text', 'pattern':'-?[0-9]*(\[0-9]+)?'}),
		}