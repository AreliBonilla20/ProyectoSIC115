from django.contrib import admin

# Register your models here.
from apps.asientos_contables.models import *

admin.site.register(asientoContable)
admin.site.register(cuenta)
admin.site.register(tipoCuenta)
admin.site.register(libroDiario)
admin.site.register(elementoMayor)
admin.site.register(libroMayor)
admin.site.register(libroMayores)
admin.site.register(elementoBalanceComprobacion)
admin.site.register(balanceComprobacion)
