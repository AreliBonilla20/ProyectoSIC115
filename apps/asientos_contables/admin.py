from django.contrib import admin

# Register your models here.
from apps.asientos_contables.models import *

admin.site.register(asientoContable)
admin.site.register(cuenta)
admin.site.register(tipoCuenta)
admin.site.register(registroTMayor)
admin.site.register(movimiento)
