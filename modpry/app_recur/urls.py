from django.urls import path
from modpry.app_recur.views import *
from modpry.app_regpry.models import *
from modpry.app_crono.models import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de recursos
    path('inicio',vst_recur().vst_inicio, name = 'ini_recur'), #inicio de la app de recursos
]