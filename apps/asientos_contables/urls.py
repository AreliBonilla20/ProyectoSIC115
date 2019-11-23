from django.conf.urls import url,include
from django.contrib import admin
from apps.asientos_contables.views  import *
from django.contrib.auth.views import login_required
#reservacion_view,cliente_view,RegistroReservacion
app_name='asientos_contables'

urlpatterns = [
    url(r'^asientoCrear/$',login_required(asientoContableCrear.as_view()),name='nuevo_asientoContable'),
    url(r'^libroDiario/$',login_required(listarLibroDiario),name='libroDiario'),
    url(r'^transacciones/$',login_required(listaTransacciones),name='lista_transacciones'),
    url(r'^cuentaCrear/$', login_required(cuentaCreate.as_view()), name='nueva_cuenta'),
    url(r'^catalogoActivos/$',login_required(listaActivos),name='catalogo_activos'),
    url(r'^catalogoPasivos/$',login_required(listaPasivos),name='catalogo_pasivos'),
    url(r'^catalogoPatrimonio/$',login_required(listaPatrimonio),name='catalogo_patrimonio'), 
    url(r'^catalogoIngresos/$',login_required(listaIngresos),name='catalogo_ingresos'), 
    url(r'^catalogoGastos/$',login_required(listaGastos),name='catalogo_gastos'), 
    url(r'^libroMayor/$',login_required(listarElementosMayor.as_view()),name='listarLibroMayor'),
    url(r'^cerrarPeriodo/$',login_required(cerrarPeriodoContable),name='cierre'),
    url(r'^estadoResultados/(?P<id_periodoContable>\d+)/$',login_required(resultados),name='estado_Resultados'),
    url(r'^estadoFlujoCapital/(?P<id_periodoContable>\d+)/$',login_required(flujocapital),name='estado_flujo_capital'),
    url(r'^balanceGeneral/(?P<id_periodoContable>\d+)/$',login_required(balanceGeneral),name='balance_general'),
    url(r'^balanceComprobacion/(?P<id_periodoContable>\d+)/$',login_required(balanceComprobacion),name='balance_comprobacion'),
    url(r'^crearPeriodoContable/$',login_required(crearPeriodoContable),name='crear_periodo_contable'),
    url(r'^listarPeriodoContable/$',login_required(listarPeriodoContable.as_view()),name='lista_periodo_contable'),
    url(r'^transaccionesPeriodoContable/(?P<id_periodoContable>\d+)/$',login_required(transaccionesPeriodo),name='transacciones_periodo'),
    url(r'^libroMayorPeriodoContable/(?P<id_periodoContable>\d+)/$',login_required(libroMayorPeriodo),name='libro_mayor_periodo'),
    
    
]

