from django.shortcuts import render,redirect
from django.views.generic import CreateView,ListView,TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from apps.asientos_contables.forms import *
from apps.asientos_contables.models import *

def index(request):
    return render(request,'Cuentas/login.html')

def indexAdmin(request):
    return render(request,'Cuentas/index.html')

def listaActivos(request):
    listaAct = cuenta.objects.filter(tipo_cuenta=1)
    return render(request,'Cuentas/listaActivos.html',{'listaAct':listaAct})

def listaPasivos(request):
    listaPas = cuenta.objects.filter(tipo_cuenta=2)
    return render(request,'Cuentas/listaPasivos.html',{'listaPas':listaPas})

def listaPatrimonio(request):
    listaPatr = cuenta.objects.filter(tipo_cuenta=3)
    return render(request,'Cuentas/listaPatrimonio.html',{'listaPatr':listaPatr})

def listaIngresos(request):
    listaIng = cuenta.objects.filter(tipo_cuenta=4)
    return render(request,'Cuentas/listaIngresos.html',{'listaIng':listaIng})

def listaGastos(request):
    listaGast = cuenta.objects.filter(tipo_cuenta=5)
    return render(request,'Cuentas/listaGastos.html',{'listaGast':listaGast})

def catalogoCuentas(request):
    listaAct = cuenta.objects.filter(tipo_cuenta=1)
    listaPas = cuenta.objects.filter(tipo_cuenta=2)
    listaPatr = cuenta.objects.filter(tipo_cuenta=3)
    listaIng = cuenta.objects.filter(tipo_cuenta=4)
    listaGast = cuenta.objects.filter(tipo_cuenta=5)
    return render(request,'Cuentas/catalogoCuentas.html',{'listaAct':listaAct,'listaPas':listaPas,'listaPatr':listaPatr,'listaIng':listaIng,'listaGast':listaGast})

def listaTransacciones(request):
    lista = asientoContable.objects.all()
    return render(request, 'Cuentas/listaAsientos.html',{'lista':lista})

class cuentaCreate(CreateView):
    model = cuenta
    template_name = 'Cuentas/cuentaCrear.html' 
    form_class = cuentaForm
    success_url = reverse_lazy('asiento:catalogo_cuentas')


class listarLibroDiario(ListView):
    model=asientoContable
    template_name='Cuentas/libroDiario.html'


class asientoContableCrear(CreateView):
    model = asientoContable
    template_name = 'Cuentas/asientoContableCrear.html' 
    form_class = asientoContableForm
    second_form_class = libroDiarioForm
    success_url = reverse_lazy('asiento:libroDiario')

    def get_context_data(self,**kwargs):
        context = super(asientoContableCrear,self).get_context_data(**kwargs)
        if 'form' not in  context:
            context['form'] = self.form_class(self.request.GET)

        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
            return context

    def post(self,request,*args,**kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        #form3 = self.third_form_class(request.POST)

        if form.is_valid() and form2.is_valid():
            asiento = form.save(commit=False)
            asiento.libroD = form2.save()
            asiento.save()
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))

class listarElementosMayor(ListView):
    model=elementoMayor
    template_name='Cuentas/libroMayor.html'

def cerrarPeriodoContable(request):
  cuentas=cuenta.objects.all()
  asientos=asientoContable.objects.all()
  if cuentas:
    for c in cuentas:
      cuenta_id=c.id
      totalDebe=0
      totalHaber=0
      if asientos:
        for a in asientos:
          cuenta_debe=a.cuenta_debe.id
          if cuenta_id==cuenta_debe:
            totalDebe+=a.importeDebe
            
        for a in asientos:
          cuenta_haber=a.cuenta_haber.id
          if cuenta_id==cuenta_haber:
            totalHaber+=a.importeHaber
        
        bill=cuenta.objects.get(id=c.id)
        elemento=elementoMayor()
        libro=libroMayor()
        libro.nombre_cuenta=bill
        libro.save()
        elemento.debe=totalDebe
        elemento.haber=totalHaber
        elemento.mayor=libro
        elemento.save()
  return redirect('asiento:listarLibroMayor')

def resultados(request):
    ingresos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=4)
    gastos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=5)
    monto_ingresos=0
    monto_gastos=0
    utilidad=0
    for i in ingresos:
        monto_ingresos += i.saldo
    for i in gastos:
        monto_gastos += i.saldo
    utilidad=monto_ingresos-monto_gastos
    return render(request,'Cuentas/estadoResultados.html',{'ingresos':ingresos,'gastos':gastos, 'monto_ingresos':monto_ingresos,'monto_gastos':monto_gastos,'utilidad':utilidad})

def flujocapital(request):
    listaFlujoCapital = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=3)
    montoFlujoCapital = 0
    for l in listaFlujoCapital:
        montoFlujoCapital+=l.saldo
    
    return render(request,'Cuentas/estadoFlujoCapital.html',{'listaFlujoCapital':listaFlujoCapital,'montoFlujoCapital':montoFlujoCapital})


def balanceGeneral(request):
    listaActivos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=1)
    listaPasivos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=2)
    listaPatrimonio = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=3)
    listaIngresos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=4)
    listaGastos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=5)
    montoActivos = 0
    montoPasivos = 0
    montoPatrimonio = 0
    montoIngresos=0
    montoGastos=0
    montoUtilidad=0
    montoPasivosPatrimonioUtilidad = 0

    for i in listaActivos:
        montoActivos += i.saldo

    for i in listaPasivos:
        montoPasivos += i.saldo

    for i in listaPatrimonio:
        montoPatrimonio += i.saldo

    for i in listaIngresos:
        montoIngresos += i.saldo

    for i in listaGastos:
        montoGastos += i.saldo

    montoUtilidad = montoIngresos-montoGastos
    montoPasivosPatrimonioUtilidad =montoPasivos + montoPatrimonio + montoUtilidad

    return render(request,'Cuentas/balanceGeneral.html',{'listaActivos':listaActivos,'listaPasivos':listaPasivos,'listaPatrimonio':listaPatrimonio,'montoActivos':montoActivos,'montoPasivos':montoPasivos,'montoPatrimonio':montoPatrimonio,'montoUtilidad':montoUtilidad, 'montoPasivosPatrimonioUtilidad':montoPasivosPatrimonioUtilidad})
    