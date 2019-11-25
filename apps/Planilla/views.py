from django.shortcuts import render,redirect
#from django.urls import reverse
from django.core.urlresolvers import reverse
from django.views.generic import CreateView
from django.views.generic import View
from .models import Salario,Empleado,Cargo,Contrato
import datetime
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect


# Create your views here.



class RegistroView(View):
    def get(self, request, *args, **kwargs):
        
        return render(request,'planilla/registro_empleado.html',context={})

    def post(self, request, *args, **kwargs):
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        dui = request.POST['dui']
        nit = request.POST['nit']
        nup = request.POST['nup']
        fechaNacimiento = request.POST['fechaNacimiento']
        isss = request.POST['isss']

        cargo = request.POST['cargo']
        gerencia = request.POST['gerencia']

        haberBase = int(request.POST['haberBase'])

        empleado = Empleado.objects.create(nombres=nombres,apellidos=apellidos,
                                            dui=dui,nit=nit,nup=nup,fechaNacimiento=fechaNacimiento,
                                            isss=isss)

        cargo = Cargo.objects.create(nombreCargo=cargo,gerencia=gerencia)

        monto_afp = calculo_afp(haberBase)
        monto_isss = calculo_isss(haberBase)
        haber_con_descuento = haberBase - monto_afp - monto_isss
        monto_renta = calculo_renta(haber_con_descuento)
        monto_neto = haber_con_descuento - monto_renta
        salario = Salario.objects.create(haberBase=haberBase, porcISSS=monto_isss,
                            porcAFP = monto_afp,renta=monto_renta,sueldoNeto=monto_neto)
        
        empleado.save()
        cargo.save()
        salario.save()
        print('ok')
        contrato = Contrato.objects.create(empleado=empleado,salario=salario,cargo=cargo,fechaContratacion=datetime.date.today())
        contrato.save()
        return HttpResponseRedirect(reverse('tabla'))
        #return render(request,'planilla/tabla_sueldos.html',context={})


class TablaPlanillaView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        lista = list(Contrato.objects.all().order_by('empleado__apellidos'))
        total_salarios = Contrato.objects.all().order_by('empleado__apellidos').aggregate(Sum('salario__sueldoNeto'))
        total_afp = Contrato.objects.all().order_by('empleado__apellidos').aggregate(Sum('salario__porcAFP'))
        total_isss = Contrato.objects.all().order_by('empleado__apellidos').aggregate(Sum('salario__porcISSS'))
        total_renta = Contrato.objects.all().order_by('empleado__apellidos').aggregate(Sum('salario__renta'))
        context.update({'lista':lista})
        context.update(total_salarios)
        context.update(total_afp)
        context.update(total_isss)
        context.update(total_renta)
        return render(request,'planilla/tabla_sueldos.html',context)

    def post(self, request, *args, **kwargs):
        context={}
        anyo,mes = request.POST['mes'].split('-')
        lista = Contrato.objects.filter(fechaContratacion__lte=datetime.date(int(anyo),int(mes),1)).order_by('empleado__apellidos')
        total_salarios = lista.aggregate(Sum('salario__sueldoNeto'))
        context.update({'lista':list(lista)})
        total_afp = lista.aggregate(Sum('salario__porcAFP'))
        total_isss = lista.aggregate(Sum('salario__porcISSS'))
        total_renta = lista.aggregate(Sum('salario__renta'))
        context.update(total_salarios)
        context.update(total_afp)
        context.update(total_isss)
        context.update(total_renta)
        return render(request,'planilla/tabla_sueldos.html',context)


def calculo_renta(monto):
    if monto <= 487.60 and monto > 0:
        renta = 0
    elif monto > 487.60 and monto <= 642.85:
        renta = (monto-487.60) * 0.1 + 17.48
    elif monto > 642.85 and monto <= 915.81:
        renta = (monto-642.85) * 0.1 + 32.70
    elif monto > 915.81 and monto <= 2068.67:
        renta = (monto-915.81) * 0.2 + 60.00
    elif monto > 2068.67 :
        renta = (monto-2068.81) * 0.3 + 288.57
    else :
        renta = 'imposible el calculo'
    return round(renta,2)


def calculo_isss(monto):
    if monto > 1000:
        isss = 1000*0.0725
    else:
        isss = monto * 0.0725
    return round(isss,2)


def calculo_afp(monto):
    afp = monto * 0.0750
    return afp