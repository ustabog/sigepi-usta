from django.urls import path
from modpry.app_mlog.views import *
from .models import *

urlpatterns = [ 
    #URL's para la aplicación de marco lógico
    path('inicio',vst_mlog().vst_inicio, name = 'ini_mlog'), #inicio de la app de marco lógico
]