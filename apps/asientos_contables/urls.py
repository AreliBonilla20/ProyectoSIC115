from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.auth.views import login_required
from apps.asientos_contables.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='asientos_contables'

urlpatterns = [
    #url(r'^$', index, name='index'),
    url(r'^asientoCrear/$',asientoContableCreate.as_view(),name='nuevo_asientoContable'),
    url(r'^libroDiario/$',listaAsiento.as_view(),name='lista_asientos'),
    url(r'^cuentaCrear/$', cuentaCreate.as_view(), name='nueva_cuenta'), 
    url(r'^catalogo/$',listaCuentas.as_view(),name='catalogo'),
    #url(r'^cargar/$',cargarCuenta,name='cargar'),  
      # url(r'^nueva_reservacion$', ReservacionNueva.as_view(), name='nueva_reservacion'),
]
