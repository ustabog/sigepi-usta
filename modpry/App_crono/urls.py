from django.urls import path
from modpry.App_regpry.views import *
from modpry.App_modpry.views import *
from modpry.App_crono.views import *
from .models import *


urlpatterns = [ 
    
    #URL para registro de proyecto individual
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crear cronograma 
    path('cncrono',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaetapa'), #Crear etapa de un cronograma
    path('funcrono',vst_ls_crono.as_view(), name = 'verfuncrono'),#Lista de las funciones del cronograma (etapa, fase, proceso, tarea y actividades)
    #path('creafase/',vts_crea_fase.as_view(), name = 'creafase'), #Crear fase de una etapa
    #path('creaproc/',vts_crea_proc.as_view(), name = 'creaproc'), #Crea el proceso de una fase
    #path('creatarea/',vts_crea_tarea.as_view(), name = 'creatarea'), #Crea la tarea de un proceso
    #path('creaacti/',vts_crea_acti.as_view(), name = 'creaacti'), #Crea la actividad de una tarea
]