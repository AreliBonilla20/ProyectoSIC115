from django import forms
from django.forms.models import modelformset_factory,inlineformset_factory
from apps.asientos_contables.models import *

class asientoContableForm(forms.ModelForm):
	class Meta:
		model = asientoContable

		fields=[
		'numero_asiento',
		'fecha',
		'cuenta_debe',
		'detalle_debe',
		'debe',
		'cuenta_haber',
		'detalle_haber',
		'haber',

		
		]

		labels={
		'numero_asiento':'N° asiento',
		'fecha':'Fecha',
		'cuenta_debe':'Cuenta a cargar',
		'detalle_debe':'Detalle',
		'debe':'Debe',
		'cuenta_haber':'Cuenta a abonar',
		'detalle_haber':'Detalle',
		'haber':'haber',
		}

		widgets={
		'numero_asiento':forms.NumberInput(attrs={'class':'form-control'}),
		'fecha':forms.TextInput(attrs={'class':'form-control','type':'Date'}),
		'cuenta_debe':forms.Select(attrs={'class':'form-control'}),
		'detalle_debe':forms.TextInput(attrs={'class':'form-control'}),
		'debe':forms.NumberInput(attrs={'class':'form-control'}),
		'cuenta_haber':forms.Select(attrs={'class':'form-control'}),
		'detalle_haber':forms.TextInput(attrs={'class':'form-control'}),
		'haber':forms.NumberInput(attrs={'class':'form-control'}),
		}
class cuentaForm(forms.ModelForm):
	class Meta:
		model = cuenta

		fields=[
		'codigo',
		'nombre',
		'tipo_cuenta',

		
		]

		labels={
		'codigo': 'Codigo',
		'nombre':'Nombre',
		'tipo_cuenta':'Seleccione el tipo de cuenta',
		}

		widgets={
		'codigo':forms.NumberInput(attrs={'class':'form-control'}),
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		'tipo_cuenta':forms.Select(attrs={'class':'form-control'}),
		}

class tipoCuentaForm(forms.ModelForm):
	class Meta:
		model = tipoCuenta

		fields=[
		'tipo',
		
		]

		labels={
		'tipo':'tipo',
		}

		widgets={
		'tipo':forms.TextInput(attrs={'class':'form-control'}),
		}

class registroTMayorForm(forms.ModelForm):
	class Meta:
		model = registroTMayor

		fields=[
		'cuenta',
		
		]

		labels={
		'cuenta':'cuenta',
		}

		widgets={
		'cuenta':forms.Select(attrs={'class':'form-control'}),
		}

class movimientoForm(forms.ModelForm):
	class Meta:
		model = movimiento

		fields=[
		'registro',
		'concepto',
		'debe',
		'haber',
		
		]

		labels={
		'registro':'Registro',
		'concepto':'Cuenta que ha cargado o abonado',
		'debe':'Debe',
		'haber':'Haber',
		}

		widgets={
		'registro':forms.HiddenInput(attrs={'class':'form-control'}),
		'concepto':forms.Select(attrs={'class':'form-control'}),
		'debe':forms.NumberInput(attrs={'class':'form-control'}),
		'haber':forms.NumberInput(attrs={'class':'form-control'}),
		}