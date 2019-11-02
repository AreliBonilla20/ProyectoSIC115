from django.conf.urls import url,include
from django.contrib import admin
from apps.asientos_contables.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='asientos_contables'

urlpatterns = [
    url(r'^asientoCrear/$',asientoContableCrear.as_view(),name='nuevo_asientoContable'),
    url(r'^libroDiario/$',listarLibroDiario.as_view(),name='libroDiario'),
    url(r'^cuentaCrear/$', cuentaCreate.as_view(), name='nueva_cuenta'), 
    url(r'^catalogo/$',catalogoCuentas.as_view(),name='catalogo'),
    url(r'^elementoMayor/$', elementoMayorCreate.as_view(), name='nuevo_elementoMayor'), 
    url(r'^elementoComprobacion/(?P<id_balance>\d+)/$',elementoBalanceComprobacionCreate.as_view(),name='elemento_nuevo'),
    url(r'^libroMayor/$',listarElementosMayor.as_view(),name='listarLibroMayor'),
]
