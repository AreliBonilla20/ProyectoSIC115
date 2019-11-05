from django.conf.urls import url,include
from django.contrib import admin
from apps.asientos_contables.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='asientos_contables'

urlpatterns = [
    url(r'^asientoCrear/$',asientoContableCrear.as_view(),name='nuevo_asientoContable'),
    url(r'^libroDiario/$',listarLibroDiario.as_view(),name='libroDiario'),
    url(r'^cuentaCrear/$', cuentaCreate.as_view(), name='nueva_cuenta'),
    url(r'^catalogo/$',catalogoCuentas,name='catalogo_cuentas'),
    url(r'^catalogoActivos/$',listaActivos,name='catalogo_activos'),
    url(r'^catalogoPasivos/$',listaPasivos,name='catalogo_pasivos'),
    url(r'^catalogoPatrimonio/$',listaPatrimonio,name='catalogo_patrimonio'), 
    url(r'^libroMayor/$',listarElementosMayor.as_view(),name='listarLibroMayor'),
    url(r'^cerrarPeriodo/$',cerrarPeriodoContable,name='cierre'),
]
