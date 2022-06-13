from django.urls import path
from modpry.app_regpry.views import *
from modpry.app_modpry.views import *
from modpry.app_crono.views import *
from .models import *


urlpatterns = [ 
    
    #URL para registro de proyecto individual
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crear cronograma 
    path('cncrono',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaetapa'), #Crear etapa de un cronograma
    path('funcrono/',vst_ls_crono.as_view(), name = 'verfuncrono'),#Lista de las funciones del cronograma (etapa, fase, proceso, tarea y actividades)
    path('creafase/',vst_crea_fase.as_view(), name = 'creafase'), #Crear fase de una etapa
    path('creaproc/',vst_crea_proc.as_view(), name = 'creaproc'), #Crea el proceso de una fase
    path('creatar/',vst_crea_tarea.as_view(), name = 'creatarea'), #Crea la tarea de un proceso
    path('creacti/',vst_crea_acti.as_view(), name = 'creaacti'), #Crea la actividad de una tarea
]