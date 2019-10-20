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
    success_url=reverse_lazy('asiento:lista_asientos')

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

class listarRegistrosT(ListView):
    model=registroTMayor
    template_name='Cuentas/libroMayor.html'

class registroTMayor(CreateView):
    model=registroTMayor
    form_class=registroTMayorForm
    template_name='Cuentas/registroTMayor.html'
    success_url=reverse_lazy('asiento:registrost')

class listarMovimientos(ListView):
    model=movimiento
    template_name='Cuentas/listarMovimientos.html'

    def get_initial(self):
      initial=super().get_initial()
      initial['registro']=self.kwargs['id_registro']
      return initial

class movimiento(CreateView):
    model=movimiento
    form_class=movimientoForm
    template_name='Cuentas/movimiento.html'
    success_url=reverse_lazy('asiento:lista_asientos')

    def get_initial(self):
      initial=super().get_initial()
      initial['registro']=self.kwargs['id_registro']
      return initial

#FUNCION PARA PODER VER LAS CUENTAS QUE HAN CARGADO Y ABONADO
def cuentaT(request,idCuenta):
  total_debe=0
  total_haber=0
  cuentas=cuenta.objects.filter(id=idCuenta)
  cargos=asientoContable.objects.filter(cuenta_debe_id=idCuenta)
  abonos=asientoContable.objects.filter(cuenta_haber_id=idCuenta)
  if cargos:
    for cargo in cargos:
      total_debe=total_debe+cargo.debe
  
  if abonos:
    for abono in abonos:
      total_haber=total_haber+abono.haber
      
  return render(request,'Cuentas/cuentasT.html',{'cuentas':cuentas,'cargos':cargos,'abonos':abonos,'total_debe':total_debe,'total_haber':total_haber})
 