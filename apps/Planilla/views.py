from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic import View
from .models import Salario,Empleado,Cargo,Contrato
import datetime
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
        return render(request,'planilla/registro_empleado.html',context={})


class TablaPlanillaView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        lista = list(Contrato.objects.all().order_by('empleado__apellidos'))
        total_salario = sum
        context.update({'lista':lista})
        return render(request,'planilla/tabla_sueldos.html',context)

    def post(self, request, *args, **kwargs):
        context={}
        anyo,mes = request.POST['mes'].split('-')
        lista = Contrato.objects.filter(fechaContratacion__lte=datetime.date(int(anyo),int(mes),1)).order_by('empleado__apellidos')
        print(lista)
        context.update({'lista':list(lista)})
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