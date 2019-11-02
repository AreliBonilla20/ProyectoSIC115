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
    
class catalogoCuentas(ListView):
    model=cuenta
    template_name='Cuentas/catalogoCuentas.html'

class cuentaCreate(CreateView):
    model = cuenta
    template_name = 'Cuentas/cuentaCrear.html' 
    form_class = cuentaForm
    success_url = reverse_lazy('asiento:libroDiario')


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

class elementoMayorCreate(CreateView):
    model=elementoMayor
    second_model=libroMayor
    form_class=elementoMayorForm
    second_form_class=libroMayorForm
    template_name='Cuentas/elementoMayorCrear.html'
    success_url=reverse_lazy('asiento:listarLibroMayor')

    def get_context_data(self,**kwargs):
        context = super(elementoMayorCreate,self).get_context_data(**kwargs)
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
            elemento = form.save(commit=False)
            elemento.mayor = form2.save()
            elemento.save()
            return HttpResponseRedirect(self.get_success_url())

        else:
            return self.render_to_response(self.get_context_data(form=form,form2=form2))

class elementoBalanceComprobacionCreate(CreateView):
    model=elementoBalanceComprobacion
    form_class=elementoBalanceComprobacionForm
    template_name='Cuentas/elementoComprobacionCrear.html'
    success_url=reverse_lazy('asiento:elemento_nuevo')

    def get_initial(self):
      initial=super().get_initial()
      initial['balance']=self.kwargs['id_balance']
      return initial