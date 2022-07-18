from django.urls import path
from modpry.app_regprgi.views import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de registro de programa de investigación
    path('inicio',vst_regprgi().vst_inicio, name = 'ini_regprgi'), #inicio de la app de registro de programas de investigación
]