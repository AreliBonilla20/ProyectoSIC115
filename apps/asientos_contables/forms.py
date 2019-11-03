from django import forms
from django.forms.models import modelformset_factory,inlineformset_factory
from apps.asientos_contables.models import *

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
		'numero_asiento':'N° asiento',
		'cuenta_debe':'Cuenta a cargar',
		'importeDebe':'Debe (Monto en $)',
		'cuenta_haber':'Cuenta a abonar',
		'importeHaber':'Haber (Monto en $)',
		}

		widgets={
		'numero_asiento':forms.NumberInput(attrs={'class':'form-control'}),
		'cuenta_debe':forms.Select(attrs={'class':'form-control'}),
		'importeDebe':forms.NumberInput(attrs={'class':'form-control'}),
		'cuenta_haber':forms.Select(attrs={'class':'form-control'}),
		'importeHaber':forms.NumberInput(attrs={'class':'form-control'}),
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
		'codigo': 'Código',
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
		'fecha':forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'concepto':forms.TextInput(attrs={'class':'form-control', 'type':'textarea'}),
		}

class elementoMayorForm(forms.ModelForm):
	class Meta:
		model = elementoMayor

		fields=[
		'fecha',
		'debe',
		'haber',
		#'saldo',
		
		
		]

		labels={
		'fecha':'Fecha',
		'debe':'Debe',
		'haber':'Haber',
		#'saldo':'Saldo',
		
		}

		widgets={
		'fecha':forms.TextInput(attrs={'class':'form-control','type':'date'}),
		'debe':forms.NumberInput(attrs={'class':'form-control'}),
		'haber':forms.NumberInput(attrs={'class':'form-control'}),
		#'saldo':forms.NumberInput(attrs={'class':'form-control'}),
		}

class libroMayorForm(forms.ModelForm):
	class Meta:
		model = libroMayor

		fields=[
		'nombre_cuenta',
		
		]

		labels={
		'nombre_cuenta':'Cuenta',
		}

		widgets={
		'nombre_cuenta':forms.Select(attrs={'class':'form-control'}),
		}

class elementoBalanceComprobacionForm(forms.ModelForm):
	class Meta:
		model = elementoBalanceComprobacion

		fields=[
		'cuentas',
		'balance',
		'sumaDebe',
		'sumaHaber',
		#'saldoDebe',
		#'saldoHaber',
		
		
		]

		labels={
		'cuentas':'Cuenta',
		'balance':'Balance',
		'sumaDebe':'Debe',
		'sumaHaber':'Haber',
		#'saldoDebe':'Saldo Acreedor',
		#'saldoHaber':'Saldo Deudor',
		
		}

		widgets={
		'cuentas':forms.Select(attrs={'class':'form-control'}),
		'balance':forms.HiddenInput(attrs={'class':'form-control'}),
		'sumaDebe':forms.NumberInput(attrs={'class':'form-control'}),
		'sumaHaber':forms.NumberInput(attrs={'class':'form-control'}),
		#'saldoDebe':forms.NumberInput(attrs={'class':'form-control'}),
		#'saldoHaber':forms.NumberInput(attrs={'class':'form-control'}),
		}

