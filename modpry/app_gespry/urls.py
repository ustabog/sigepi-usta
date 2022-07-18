from django.urls import path
from modpry.app_gespry.views import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de gestión de proyectos
    path('inicio',vst_gespry().vst_inicio, name = 'ini_gespry'), #inicio de la app de gestión de proyectos de investigación
]