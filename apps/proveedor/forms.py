<<<<<<< HEAD
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
=======
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
# agrega el estilo a los inputs
	def __init__(self, *args, **kwargs):
		super(proveedorForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class': 'mdl-textfield__input'})
		self.fields['telefono'].widget.attrs.update({'class': 'mdl-textfield__input', 'size': 10})
		self.fields['direccion'].widget.attrs.update({'class': 'mdl-textfield__input'})
		self.fields['email'].widget.attrs.update({'class': 'mdl-textfield__input'})

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
		errors={
		'nombre':'',
		'telefono':'Numero de telefono invalido'
		}
# agrega el estilo a los inputs		
	def __init__(self, *args, **kwargs):
		super(contactoForm, self).__init__(*args, **kwargs)
		self.fields['nombre'].widget.attrs.update({'class': 'mdl-textfield__input'})
		self.fields['telefono'].widget.attrs.update({'class': 'mdl-textfield__input'})

		
>>>>>>> origin/virginia
