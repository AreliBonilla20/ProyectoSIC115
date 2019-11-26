from django import forms
from django.forms.models import modelformset_factory,inlineformset_factory
from apps.asientos_contables.models import *

class periodoContableForm(forms.ModelForm):
	class Meta:
		model = periodoContable
	

		fields=[
		'fechaInicio',
		'fechaFinal',
		
		]

		labels={
		'fechaInicio':'Fecha de inicio del período',
		'fechaFinal':'Fecha final del período',
		
		}

		widgets={
		'fechaInicio':forms.TextInput(attrs={'class':'form-control','type':'date','required':'required'}),
		'fechaFinal':forms.TextInput(attrs={'class':'form-control','type':'date','required':'required'}),
		
		
		}

class asientoContableForm(forms.ModelForm):
	class Meta:
		model = asientoContable

		fields=[
		'numero_asiento',
		'cuenta_debe',
		'importeDebe',
		'cuenta_haber',
		'importeHaber',

		
		]

		labels={
		'numero_asiento':'Número de asiento',
		'cuenta_debe':'Cuenta a cargar',
		'importeDebe':'Debe (Monto en $)',
		'cuenta_haber':'Cuenta a abonar',
		'importeHaber':'Haber (Monto en $)',
		}

		widgets={
		'numero_asiento':forms.NumberInput(attrs={'class':'form-control','required':'required'}),
		'cuenta_debe':forms.Select(attrs={'class':'form-control','required':'required'}),
		'importeDebe':forms.NumberInput(attrs={'class':'form-control','required':'required', 'placeholder':'Monto de la cuenta debe'}),
		'cuenta_haber':forms.Select(attrs={'class':'form-control','required':'required'}),
		'importeHaber':forms.NumberInput(attrs={'class':'form-control','required':'required', 'placeholder':'Monto de la cuenta haber'}),
		}
class cuentaForm(forms.ModelForm):
	class Meta:
		model = cuenta

		fields=[
		'codigo',
		'nombre',
		'tipo_cuenta',
		'subcuenta',

		
		]

		labels={
		'codigo': 'Código',
		'nombre':'Nombre',
		'tipo_cuenta':'Seleccione el tipo de cuenta',
		'subcuenta':'Subcuenta',
		}

		widgets={
		'codigo':forms.TextInput(attrs={'class':'form-control','required':'required', 'placeholder':'Código de la cuenta'}),
		'nombre':forms.TextInput(attrs={'class':'form-control', 'pattern':'[A-Za-záéíóúÁÉÍÓÚ\s]{1,50}','required':'required', 'placeholder':'Nombre de la cuenta'}),
		'tipo_cuenta':forms.Select(attrs={'class':'form-control','required':'required'}),
		'subcuenta':forms.TextInput(attrs={'class':'form-control', 'pattern':'[A-Za-záéíóúÁÉÍÓÚ\'\s]{1,50}', 'placeholder':'Nombre de la subcuenta'}),
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

class libroDiarioForm(forms.ModelForm):
	class Meta:
		model = libroDiario

		fields=[
		'fecha',
		'concepto',
		
		]

		labels={
		'fecha':'Fecha',
		'concepto':'Concepto',
		}

		widgets={
		'fecha':forms.TextInput(attrs={'class':'form-control','type':'date','required':'required'}),
		'concepto':forms.TextInput(attrs={'class':'form-control', 'pattern':'[A-Za-záéíóúÁÉÍÓÚ\s]{1,50}','required':'required', 'placeholder':'Nombre de la cuenta', 'type':'textarea'}),
		}
