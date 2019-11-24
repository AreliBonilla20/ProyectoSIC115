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

def mensajeGuardadoCuenta(request):
    return render(request,'Cuentas/mensajeGuardadoCuenta.html')

def mensajeGuardadoAsiento(request):
    return render(request,'Cuentas/mensajeGuardadoAsiento.html')

def mensajeGuardadoPeriodo(request):
    return render(request,'Cuentas/mensajeGuardadoPeriodo.html')

def confirmarCerrarPeriodo(request):
    periodos = periodoContable.objects.filter(estado="Abierto")
    return render(request,'Cuentas/confirmacionCerrarPeriodo.html', {'periodos':periodos})

def crearPeriodoContable(request):
    periodos = periodoContable.objects.filter(estado="Abierto")
    mensaje = ""
    
    if periodos:
        mensaje = "No se puede abrir un período, ya que hay un ciclo contable en curso"
        return render(request,'Cuentas/periodoContable.html',{'mensaje':mensaje})

    else:
        if request.method == 'POST':
            form = periodoContableForm(request.POST)
            if form.is_valid():
                form.save()
            return redirect('asiento:periodo_registrado')
        else:
            form = periodoContableForm()

        return render(request,'Cuentas/periodoContable.html',{'form':form})
    

class listarPeriodoContable(ListView):
    model=periodoContable
    template_name='Cuentas/listaPeriodoContable.html'

def listaTransacciones(request):
    lista = asientoContable.objects.filter(periodo__isnull=True)
    return render(request, 'Cuentas/listaAsientos.html',{'lista':lista})

class cuentaCreate(CreateView):
    model = cuenta
    template_name = 'Cuentas/cuentaCrear.html' 
    form_class = cuentaForm
    success_url = reverse_lazy('asiento:cuenta_registrada')


def listarLibroDiario(request):
    libroDiario = asientoContable.objects.filter(periodo__isnull=True)
    return render(request, 'Cuentas/libroDiario.html',{'libroDiario':libroDiario})


class asientoContableCrear(CreateView):
    model = asientoContable
    template_name = 'Cuentas/asientoContableCrear.html' 
    form_class = asientoContableForm
    second_form_class = libroDiarioForm
    success_url = reverse_lazy('asiento:asiento_registrado')
    

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
  periodoCont = periodoContable.objects.get(estado='Abierto')
  transacciones = asientoContable.objects.filter(periodo__isnull=True)
  
  for i in transacciones:
      i.periodo = periodoCont
      i.save()

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
        elemento.periodoCont = periodoCont
        elemento.save()
    
    periodoCont.estado = 'Cerrado'
    periodoCont.save()

    return redirect('asiento:listarLibroMayor')

def transaccionesPeriodo(request,id_periodoContable):
    asientos = asientoContable.objects.filter(periodo=id_periodoContable)
    
    return render(request,'Cuentas/transaccionesPeriodoContable.html',{'asientos':asientos})

def libroMayorPeriodo(request,id_periodoContable):
    elemento = elementoMayor.objects.filter(periodoCont=id_periodoContable)
    return render(request,'Cuentas/libroMayorPeriodoContable.html',{'elemento':elemento})


def balanceComprobacion(request,id_periodoContable):
    cuentasComprobacion = elementoMayor.objects.filter(periodoCont=id_periodoContable)
    periodo = periodoContable.objects.filter(id=id_periodoContable)
    monto_debe = 0
    monto_haber = 0
    for i in cuentasComprobacion:
        if i.monto > 0:
            monto_debe+=i.monto
        else:
            monto_haber+=i.monto
    return render(request,'Cuentas/balanceComprobacion.html',{'cuentasComprobacion':cuentasComprobacion, 'monto_haber':monto_haber, 'monto_debe':monto_debe, 'id_periodoContable':id_periodoContable,'periodo':periodo})

def resultados(request,id_periodoContable):
    ingresos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=4, periodoCont=id_periodoContable)
    gastos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=5, periodoCont=id_periodoContable)
    periodo = periodoContable.objects.filter(id=id_periodoContable)
    monto_ingresos=0
    monto_gastos=0
    utilidad=0
    for i in ingresos:
        monto_ingresos += i.saldo
    for i in gastos:
        monto_gastos += i.saldo
    utilidad=monto_ingresos-monto_gastos
    return render(request,'Cuentas/estadoResultados.html',{'ingresos':ingresos,'gastos':gastos, 'monto_ingresos':monto_ingresos,'monto_gastos':monto_gastos,'utilidad':utilidad,'id_periodoContable':id_periodoContable,'periodo':periodo})

def flujocapital(request,id_periodoContable):
    listaFlujoCapital = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=3, periodoCont=id_periodoContable)
    periodo = periodoContable.objects.filter(id=id_periodoContable)
    montoFlujoCapital = 0
    for l in listaFlujoCapital:
        montoFlujoCapital+=l.saldo
    
    return render(request,'Cuentas/estadoFlujoCapital.html',{'listaFlujoCapital':listaFlujoCapital,'montoFlujoCapital':montoFlujoCapital,'id_periodoContable':id_periodoContable,'periodo':periodo})


def balanceGeneral(request,id_periodoContable):
    listaActivos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=1, periodoCont=id_periodoContable)
    listaPasivos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=2, periodoCont=id_periodoContable)
    listaPatrimonio = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=3, periodoCont=id_periodoContable)
    listaIngresos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=4, periodoCont=id_periodoContable)
    listaGastos = elementoMayor.objects.filter(mayor__nombre_cuenta__tipo_cuenta=5, periodoCont=id_periodoContable)
    periodo = periodoContable.objects.filter(id=id_periodoContable)
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

    return render(request,'Cuentas/balanceGeneral.html',{'listaActivos':listaActivos,'listaPasivos':listaPasivos,'listaPatrimonio':listaPatrimonio,'montoActivos':montoActivos,'montoPasivos':montoPasivos,'montoPatrimonio':montoPatrimonio,'montoUtilidad':montoUtilidad, 'montoPasivosPatrimonioUtilidad':montoPasivosPatrimonioUtilidad,'id_periodoContable':id_periodoContable,'periodo':periodo})



    