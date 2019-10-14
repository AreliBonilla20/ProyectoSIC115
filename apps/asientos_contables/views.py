from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from apps.asientos_contables.forms import *
from apps.asientos_contables.models import *


def index(request):
  return render(request,'Cuentas/login.html')

def indexAdmin(request):
  return render(request,'Cuentas/index.html')

class asientoContableCreate(CreateView):
	model=asientoContable
	form_class=asientoContableForm
	template_name='Cuentas/asientoContableCrear.html'
	success_url=reverse_lazy('asiento:nuevo_asientoContable')

class listaAsiento(ListView):
	model=asientoContable
	template_name='Cuentas/listaAsientos.html'

class cuentaCreate(CreateView):
	model=cuenta
	form_class=cuentaForm
	template_name='Cuentas/cuentaCrear.html'
	success_url=reverse_lazy('asiento:lista_asientos')

class listaCuentas(ListView):
	model=cuenta
	template_name='Cuentas/listaCuentas.html'
