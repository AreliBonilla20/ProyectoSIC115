from django.conf.urls import url,include
from django.contrib import admin
from apps.asientos_contables.views  import *
#reservacion_view,cliente_view,RegistroReservacion
app_name='asientos_contables'

urlpatterns = [
    url(r'^asientoCrear/$',asientoContableCrear.as_view(),name='nuevo_asientoContable'),
    url(r'^libroDiario/$',listarLibroDiario.as_view(),name='libroDiario'),
    url(r'^transacciones/$',listaTransacciones,name='lista_transacciones'),
    url(r'^cuentaCrear/$', cuentaCreate.as_view(), name='nueva_cuenta'),
    url(r'^catalogo/$',catalogoCuentas,name='catalogo_cuentas'),
    url(r'^catalogoActivos/$',listaActivos,name='catalogo_activos'),
    url(r'^catalogoPasivos/$',listaPasivos,name='catalogo_pasivos'),
    url(r'^catalogoPatrimonio/$',listaPatrimonio,name='catalogo_patrimonio'), 
    url(r'^catalogoIngresos/$',listaIngresos,name='catalogo_ingresos'), 
    url(r'^catalogoGastos/$',listaGastos,name='catalogo_gastos'), 
    url(r'^libroMayor/$',listarElementosMayor.as_view(),name='listarLibroMayor'),
    url(r'^cerrarPeriodo/$',cerrarPeriodoContable,name='cierre'),
    url(r'^estadoResultados/$',resultados,name='estado_Resultados'),
    url(r'^estadoFlujoCapital/$',flujocapital,name='estado_flujo_capital'),
    url(r'^balanceGeneral/$',balanceGeneral,name='balance_general'),
    url(r'^balanceComprobacion/$',balanceComprobacion,name='balance_comprobacion'),
    url(r'^crearPeriodoContable/$',periodoContableCreate.as_view(),name='crear_periodo_contable'),
    url(r'^listarPeriodoContable/$',listarPeriodoContable.as_view(),name='lista_periodo_contable'),
]
