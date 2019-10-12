from django import forms
from django.forms.models import modelformset_factory,inlineformset_factory
from apps.asientos_contables.models import *

class asientoContableForm(forms.ModelForm):
	class Meta:
		model = asientoContable

		fields=[
		'fecha',
		'detalle',
		'importeDebe',
		'importeHaber',
		'cuentas',
		
		]

		labels={
		'fecha':'Fecha',
		'detalle':'Detalle',
		'importeDebe':'Debe',
		'importeHaber':'Haber',
		'cuentas':'Cuentas',
		}

		widgets={
		'fecha':forms.TextInput(attrs={'class':'form-control','type':'Date'}),
		'detalle':forms.TextInput(attrs={'class':'form-control'}),
		'importeDebe':forms.NumberInput(attrs={'class':'form-control'}),
		'importeHaber':forms.NumberInput(attrs={'class':'form-control'}),
		'cuentas':forms.Select(attrs={'class':'form-control'}),
		}

class cuentaForm(forms.ModelForm):
	class Meta:
		model = cuenta

		fields=[
		'codigo',
		'nombre',
		
		]

		labels={
		'codigo': 'Codigo',
		'nombre':'Nombre',
		}

		widgets={
		'codigo':forms.NumberInput(attrs={'class':'form-control'}),
		'nombre':forms.TextInput(attrs={'class':'form-control'}),
		}