"""SIC115 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from apps.asientos_contables.views import index,indexAdmin
from django.contrib.auth.views import login, logout_then_login, password_reset, password_reset_done, password_reset_confirm, password_reset_complete
from apps.Planilla.views import RegistroView,TablaPlanillaView
urlpatterns = [
	url(r'^admin/',admin.site.urls),
	url(r'^indexAdmin/',indexAdmin,name="indexAdmin"),  
    url(r'^asiento/', include('apps.asientos_contables.urls',namespace="asiento")), 
    url(r'^accounts/login/', login, {'template_name':'Cuentas/login.html'}, name='login'),
    url(r'^$', login, {'template_name':'Cuentas/login.html'}, name='login'),
    url(r'^registro/$', RegistroView.as_view(), name='registro'),
    url(r'^tabla/$', TablaPlanillaView.as_view(), name='tabla'),
    url(r'^logout/', logout_then_login, name='logout'),
] + static (settings.STATIC_URL , document_root = settings.STATIC_ROOT)
