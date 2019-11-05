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

def catalogoCuentas(request):
    listaAct = cuenta.objects.filter(tipo_cuenta=1)
    listaPas = cuenta.objects.filter(tipo_cuenta=2)
    listaPatr = cuenta.objects.filter(tipo_cuenta=3)
    return render(request,'Cuentas/catalogoCuentas.html',{'listaAct':listaAct,'listaPas':listaPas,'listaPatr':listaPatr})

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