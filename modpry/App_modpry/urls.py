from django.urls import path
from django.contrib.auth.views import *
#from rest_framework.routers import DefaultRouter
from modpry.app_regpry.views import *
from modpry.app_regpry.urls import *
from modpry.app_modpry.views import *
from modpry.app_crono.views import *
from modpry.app_crono.urls import *
from modpry.app_evapry.views import *
from modpry.app_modpry.urls import *
from .models import *

urlpatterns = [ 
    #URL's para registro de proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cnpry/', vts_ls_pry.as_view(), name = 'cn_pry'), #Lista de proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    #path('elipry/<int_pk>',vts_reg_pry.as_view(), name = 'elim_pry'), #Borrar proyecto
    path('elipry/<id>',eli_pry, name = 'eliminar_usu'),

    #URL's para cronograma
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crea el proyecto
    path('cncrono',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaetapa'), #Crear etapa de un cronograma
    path('funcrono/',vst_ls_crono.as_view(), name = 'veretapa'),#Lista de etapas de un cronograma
    path('creafase/',vst_crea_fase.as_view(), name = 'crea_fase'), #Crear fase de una etapa
    path('funcrono/',vst_ls_crono.as_view(), name = 'verfase'),#Lista de fases de un cronograma
    path('creaproc/',vst_crea_proc.as_view(), name = 'crea_proc'), #Crea el proceso de una fase
    path('funcrono/',vst_ls_crono.as_view(), name = 'verproc'),#Lista de procesos de un cronograma
    path('creatar/',vst_crea_tarea.as_view(), name = 'crea_tarea'), #Crea la tarea de un proceso
    path('funcrono/',vst_ls_crono.as_view(), name = 'vertarea'),#Lista de tareas de un cronograma
    path('creacti/',vst_crea_acti.as_view(), name = 'crea_acti'), #Crea la actividad de una tarea 
    path('funcrono/',vst_ls_crono.as_view(), name = 'veracti'),#Lista de actividades de un cronograma

    #URL's para la evaluación de proyectos
    path('creaeva', vst_reg_evapry.as_view(), name = 'crear_eva'), #Crear evaluación de un proyecto
    path('cneva', vst_ls_evapry.as_view(), name = 'cn_evapry'), #Consultar evaluación de un proyecto
    path('crearub', vst_crear_rub.as_view(), name = 'crear_rub'), #Crear rúbrica
    path('cnrub', vst_ls_rub.as_view(), name = 'cn_rub'), #Consultar rúbrica
    path('creacrit', vst_crear_crit.as_view(), name = 'crear_crit'), #Crear criterios de la rúbrica
    path('crearango', vst_crear_rango.as_view(), name = 'crear_rango'), #Crear un rango de evaluación
    path('creaciclo', vst_crear_cicloeva.as_view(), name = 'crear_ciclo'), #Crear un ciclo de evaluación  
    path('crearesul', vst_crear_resul.as_view(), name = 'crear_resul'), #Crear un resultado de evaluación
    path('creatipo', vst_crear_tipoeva.as_view(), name = 'crear_tipo'), #Crear tipo de evaluación 
    path('creardefi', vst_crear_defi.as_view(), name = 'crear_defi'), #Crear definición, comentario, recomendación
]


