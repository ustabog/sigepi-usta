from django.urls import path
from modpry.app_convo.views import *
from .models import *

urlpatterns = [ 
    #URL's para la aplicación de convocatoria
    path('inicio',vst_convo().vst_inicio, name = 'ini_convo'), #inicio de la app de convocatoria
]