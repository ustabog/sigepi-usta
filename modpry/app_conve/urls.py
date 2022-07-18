from django.urls import path
from modpry.app_conve.views import *
from .models import *

urlpatterns = [ 
    #URL's para la aplicación de convenios
    path('inicio',vst_conve().vst_inicio, name = 'ini_conve'), #inicio de la app de convenios
]