from django import forms
from .models import *


class TipoProductoForm(forms.ModelForm):
	class Meta:
		model=TipoProducto
		fields={
		'nombre',
		'activo',
		}
		labels={
		'nombre':'Nombre producto',
		'activo':'Producto activo',
		}
class PrecioProductoForm(forms.ModelForm):
	class Meta:
		model=PrecioProducto
		fields={
		'nombre',
		'producto',
		'tamanio',
		'cantidad',
		'precio',
		'tipoCliente',
		}
		labels={
		'nombre':'Nombre referente',
		'producto':'Seleccione Producto',
		'tamanio':'Seleccione Tamaño',
		'cantidad':'Cantidad',
		'precio':'Precio',
		'tipoCliente':'Tipo de cliente:'
		}

class TamanioProductoForm(forms.ModelForm):
	class Meta:
		model=TamanioProducto
		fields={
		'tamaño',
		'descripcion',
		}
		labels={
		'tamaño':'Tamaño',
		'descripcion':'Descripcion',
		}
	# def __init__(self, *args, **kwargs):
	# 	super(ProveedorForm, self).__init__(*args, **kwargs)
	# 	for field in iter(self.fields):
	# 		if field <> 'activo':
	# 			self.fields[field].widget.attrs.update({
	# 				'class': 'form-control'
	# 				})