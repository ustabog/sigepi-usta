from django.urls import path
from modpry.app_disinv.views import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de diseño de proyecto de investigación
    path('inicio',vst_disinv().vst_inicio, name = 'ini_disinv'), #inicio de la app de diseño de proyecto de investigación
]