from django.contrib import admin
from .models import Empleado,Salario,Cargo,Contrato

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('apellidos','nombres','nit','dui','nup','isss','fechaNacimiento')

admin.site.register(Empleado, EmpleadoAdmin)

class SalarioAdmin(admin.ModelAdmin):
    list_display = ('haberBase','bonoAntig','sueldoBruto',
                    'porcISSS','porcAFP','otrosDescuentos',
                    'sueldoNeto')

admin.site.register(Salario, SalarioAdmin)

class CargoAdmin(admin.ModelAdmin):
    list_display = ('nombreCargo','gerencia')

admin.site.register(Cargo, CargoAdmin)


class ContratoAdmin(admin.ModelAdmin):
    list_display = ('pk','empleado','salario','cargo','fechaContratacion')
    list_filter = ('fechaContratacion',)

admin.site.register(Contrato, ContratoAdmin)

