from django.urls import path
from modpry.app_regpry.views import *
from modpry.app_modpry.views import *
from modpry.app_crono.views import *
from modpry.app_crono.func import *
from .models import *

urlpatterns = [   
    #URL's para las funciones de un cronograma
    path('inicio',vst_crono().vst_inicio, name = 'ini_crono'), #inicio de la app de cronograma
    #URL para cronogramas
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crear cronograma 
    path('cncrono/',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('addcrono/',vst_add_crono.as_view(), name = 'addcrono'),#Añadir al cronograma
    path('editcrono/<int:pk>/',vst_edit_crono.as_view(), name = 'edit_crono'),#Editar cronograma
    path('archicrono/<id>/',fn_archi_crono, name = 'archi_crono'), #Archivar cronograma
    path('elicrono/<id>/',fn_eli_crono, name = 'eli_crono'), #Eliminar cronograma
    #URL para etapas
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaeta'), #Crear etapa de un cronograma
    path('cndetcrono/',vst_ls_etapa.as_view(), name = 'veretapa'),#Lista de etapas
    path('editeta/<int:pk>/',vst_edit_etapa.as_view(), name = 'edit_etapa'),#Editar etapa
    path('archieta/<id>/',fn_archi_etapa, name = 'archi_etapa'), #Archivar etapa
    path('elieta/<id>/',fn_eli_etapa, name = 'eli_etapa'), #Eliminar etapa
    #URL para fases
    path('creafase/',vst_crea_fase.as_view(), name = 'creafase'), #Crear fase de una etapa
    path('cndetcrono/',vst_ls_fase.as_view(), name = 'verfase'),#Lista de fases
    path('editfase/<int:pk>/',vst_edit_fase.as_view(), name = 'edit_fase'),#Editar fase
    path('archifase/<id>/',fn_archi_fase, name = 'archi_fase'), #Archivar fase
    path('elifase/<id>/',fn_eli_fase, name = 'eli_fase'), #Eliminar fase
    #URL para procesos
    path('creaproc/',vst_crea_proc.as_view(), name = 'creaproc'), #Crea el proceso de una fase
    path('cndetcrono/',vst_ls_proc.as_view(), name = 'verproc'),#Lista de procesos
    path('editproc/<int:pk>/',vst_edit_proc.as_view(), name = 'edit_proc'),#Editar procesos
    path('archiproc/<id>/',fn_archi_proceso, name = 'archi_proc'), #Archivar proceso
    path('eliproc/<id>/',fn_eli_proceso, name = 'eli_proc'), #Eliminar proceso
    #URL para tareas
    path('creatar/',vst_crea_tarea.as_view(), name = 'creatar'), #Crea la tarea de un proceso
    path('cndetcrono/',vst_ls_tarea.as_view(), name = 'vertarea'),#Lista de tareas
    path('editar/<int:pk>/',vst_edit_tarea.as_view(), name = 'edit_tarea'),#Editar tarea
    path('architar/<id>/',fn_archi_tarea, name = 'archi_tar'), #Archivar tarea
    path('elitar/<id>/',fn_eli_tarea, name = 'eli_tar'), #Eliminar tarea
    #URL para actividades
    path('creacti/',vst_crea_acti.as_view(), name = 'creacti'), #Crea la actividad de una tarea
    path('cndetcrono/',vst_ls_acti.as_view(), name = 'veracti'),#Lista de actividades
    path('editacti/<int:pk>/',vst_edit_acti.as_view(), name = 'edit_acti'),#Editar actividad
    path('archiacti/<id>/',fn_archi_acti, name = 'archi_acti'), #Archivar actividad
    path('eliacti/<id>/',fn_eli_acti, name = 'eli_acti'), #Eliminar actividad
]