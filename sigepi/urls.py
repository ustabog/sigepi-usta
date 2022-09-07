"""SIGEPI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#Librerías de sistema
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.staticfiles import views
from django.contrib import admin
from django.urls import path, include, re_path
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter

#Librerías de aplicaciones
from modadm.app_modadm.views import *
from modadm.app_modadm.urls import *
from modcons.app_cons.views import *
from modadm.app_regusu.urls import *
from modadm.app_regusugr.urls import *
from modprd.app_regprd.urls import *
from modprd.app_modprd.urls import *

from .views import *

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
    urlpatterns += staticfiles_urlpatterns()


urlpatterns = [
    path('admdjg/', admin.site.urls),
    #Direcciones de la Aplicación app_regusu
    path('modadm/',include("modadm.app_regusu.urls")),
    #Direcciones de la Aplicación app_regusui
    path('modadm/',include("modadm.app_regusui.urls")),
    #Direcciones de la Aplicación app_reguusgr
    path('modadm/',include("modadm.app_regusugr.urls")),
    #Direcciones de la aplicación app_modadm
    path('modadm/',include("modadm.app_modadm.urls")),

    #direcciones del front (finales en producción)
    path('',front().vst_raiz),
    path('inicio',front().vst_inicio, name = 'inicio'),
    path('vue',front().vst_vue, name = 'vue'),
    path('ingreso',front().vst_ingreso, name = 'ingreso'),
    path('cerrar', front().vst_cerrar, name = 'cerrar'),
    path('doc', front().vst_doc, name ='doc'),
    path('registro', front().vst_registro, name ='registro'),

    #Direcciones módulo de proyectos
    path('pry/', include('modpry.app_modpry.urls')),
    path('pry/', include('modpry.app_regpry.urls')),

    #consultas globales
    #path('conusus', vts_ls_usu.as_view(), name='consulta_usuarios'),
    path('modcons/', include('modcons.app_cons.urls')),

    # Resetear contrasena
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name = 'password_reset_form.html'), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name = 'password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'password_reset_complete.html'), name="password_reset_complete"),

    # consultas módulo de productos
    path('prd/', include('modprd.app_modprd.urls')),
    path('prd/', include('modprd.app_regprd.urls')),
    path('creareqexs/', vst_regreqexist.as_view(), name='crear_reqexs'),
    path('creareqcal/', vst_regreqcal.as_view(), name='reqcal'),
]

urlpatterns += staticfiles_urlpatterns()
