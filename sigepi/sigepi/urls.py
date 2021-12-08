"""SIGEPI_PRO URL Configuration

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
from django.urls import re_path
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter

#Librerías de aplicaciones
from modadm.App_modadm.views import *
from modadm.App_modadm.urls import *
from modcons.App_cons.views import *
from modadm.App_regusu.urls import *
from modadm.App_regusugr.urls import *

from .views import *

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^static/(?P<path>.*)$', views.serve),
    ]
    urlpatterns += staticfiles_urlpatterns()


urlpatterns = [
    path('admin/', admin.site.urls),
    #Direcciones de la Aplicación App_regusu
    path('modadm/',include("modadm.App_regusu.urls")),
    #Direcciones de la Aplicación App_regusui
    path('modadm/',include("modadm.App_regusui.urls")),
    #Direcciones de la Aplicación App_reguusgr
    path('modadm/',include("modadm.App_regusugr.urls")),
    #Direcciones de la aplicación App_modadm
    path('modadm/',include("modadm.App_modadm.urls")),
    
    #direcciones del front (finales en producción)
    path('',front().vst_raiz),
    path('inicio',front().vst_inicio, name = 'inicio'),
    path('ingreso',front().vst_ingreso, name = 'ingreso'),
    path('cerrar', front().vst_cerrar, name = 'cerrar'),
    path('doc', front().vst_doc, name ='doc'),
    path('registro', front().vst_registro, name ='registro'),


    #consultas globales
    #path('conusus', vts_ls_usu.as_view(), name='consulta_usuarios'),
    path('accounts', include('django.contrib.auth.urls')),
]

urlpatterns += staticfiles_urlpatterns()


