from django.urls import path
from django.contrib.auth.views import *
#from rest_framework.routers import DefaultRouter
from modpry.app_regpry.views import *
from modpry.app_regpry.func import *
from modpry.app_regpry.urls import *
from modpry.app_modpry.views import *
from modpry.app_crono.views import *
from modpry.app_crono.func import *
from modpry.app_crono.urls import *
from modpry.app_evapry.views import *
from modpry.app_evapry.func import *
from modpry.app_modpry.urls import *
from .models import *

urlpatterns = [ 
    #URL's para registro de proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cnpry/', vst_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    path('archipry/<id>',fn_archi_pry, name = 'archi_pry'), #Archivar un proyecto
    path('elipry/<id>',fn_eli_pry, name = 'eli_pry'),#Eliminar un proyecto
    path('addpry/',vts_add_pry.as_view(), name = 'add_pry'),#Añadir información del proyecto

    #URL para las funciones de un cronograma
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    #URL para cronogramas
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crear cronograma 
    path('cncrono/',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('editcrono/<int:pk>/',vst_edit_crono.as_view(), name = 'edit_crono'),#Editar cronograma
    path('archicrono/<id>/',fn_archi_crono, name = 'archi_crono'), #Archivar cronograma
    path('elicrono/<id>/',fn_eli_crono, name = 'eli_crono'), #Eliminar cronograma
    #URL para etapas
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaeta'), #Crear etapa de un cronograma
    path('cneta/',vst_ls_etapa.as_view(), name = 'veretapa'),#Lista de etapas
    path('editeta/<int:pk>/',vst_edit_etapa.as_view(), name = 'edit_crono'),#Editar etapa
    path('archieta/<id>/',fn_archi_etapa, name = 'archi_etapa'), #Archivar etapa
    path('elieta/<id>/',fn_eli_etapa, name = 'eli_etapa'), #Eliminar etapa
    #URL para fases
    path('creafase/',vst_crea_fase.as_view(), name = 'creafase'), #Crear fase de una etapa
    path('cnfase/',vst_ls_fase.as_view(), name = 'verfase'),#Lista de fases
    path('editfase/<int:pk>/',vst_edit_fase.as_view(), name = 'edit_fase'),#Editar fase
    path('archifase/<id>/',fn_archi_fase, name = 'archi_fase'), #Archivar fase
    path('elifase/<id>/',fn_eli_fase, name = 'eli_fase'), #Eliminar fase
    #URL para procesos
    path('creaproc/',vst_crea_proc.as_view(), name = 'creaproc'), #Crea el proceso de una fase
    path('cnproc/',vst_ls_proc.as_view(), name = 'verproc'),#Lista de procesos
    path('editproc/<int:pk>/',vst_edit_proc.as_view(), name = 'edit_proc'),#Editar procesos
    path('archiproc/<id>/',fn_archi_proceso, name = 'archi_proc'), #Archivar proceso
    path('eliproc/<id>/',fn_eli_proceso, name = 'eli_proc'), #Eliminar proceso
    #URL para tareas
    path('creatar/',vst_crea_tarea.as_view(), name = 'creatar'), #Crea la tarea de un proceso
    path('cntarea/',vst_ls_tarea.as_view(), name = 'vertarea'),#Lista de tareas
    path('editar/<int:pk>/',vst_edit_tarea.as_view(), name = 'edit_tarea'),#Editar tarea
    path('architar/<id>/',fn_archi_tarea, name = 'archi_tar'), #Archivar tarea
    path('elitar/<id>/',fn_eli_tarea, name = 'eli_tar'), #Eliminar tarea
    #URL para actividades
    path('creacti/',vst_crea_acti.as_view(), name = 'creacti'), #Crea la actividad de una tarea
    path('cnacti/',vst_ls_acti.as_view(), name = 'veracti'),#Lista de actividades
    path('editacti/<int:pk>/',vst_edit_acti.as_view(), name = 'edit_acti'),#Editar actividad
    path('archiacti/<id>/',fn_archi_acti, name = 'archi_acti'), #Archivar actividad
    path('eliacti/<id>/',fn_eli_acti, name = 'eli_acti'), #Eliminar actividad

    #URL para las funciones de la evaluación de un proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    #URL para la evaluación de un proyecto
    path('creaeva/', vst_reg_evapry.as_view(), name = 'crear_eva'), #Crear evaluación de un proyecto
    path('cneva/', vst_ls_evapry.as_view(), name = 'cn_evapry'), #Consultar evaluación de un proyecto
    path('editeva/<int:pk>/',vst_edit_evapry.as_view(), name = 'edit_eva'), #Editar la evaluación de un proyecto
    path('archieva/<id>',fn_archi_eva, name = 'archi_eva'), #Archivar la evaluación de un proyecto
    path('elieva/<id>',fn_eli_eva, name = 'eli_eva'),#Eliminar la evaluación de un proyecto
    #URL para rúbrica de evaluación
    path('crearub/', vst_crear_rub.as_view(), name = 'crear_rub'), #Crear rúbrica
    path('cnrub/', vst_ls_rub.as_view(), name = 'cn_rub'), #Consultar rúbrica
    path('editrub/<int:pk>/',vst_edit_rub.as_view(), name = 'edit_rub'), #Editar la rúbrica de evaluación de un proyecto
    path('archirub/<id>',fn_archi_rub, name = 'archi_rub'), #Archivar la rúbrica de evaluación de un proyecto
    path('elirub/<id>',fn_eli_rub, name = 'eli_rub'),#Eliminar la rúbrica de evaluación de un proyecto
    #URL para criterio de evaluación
    path('creacrit/', vst_crear_crit.as_view(), name = 'crear_crit'), #Crear criterios de la rúbrica
    path('cncrit/', vst_ls_crit.as_view(), name = 'cn_crit'), #Consultar criterios evaluación de un proyecto
    path('editcrti/<int:pk>/',vst_edit_crit.as_view(), name = 'edit_crit'), #Editar el criterio de evaluación de un proyecto
    path('archicrit/<id>',fn_archi_crit, name = 'archi_crit'), #Archivar el criterio de evaluación de un proyecto
    path('elicrti/<id>',fn_eli_crit, name = 'eli_crit'),#Eliminar el criterio de evaluación de un proyecto
    #URL para rango de evaluación
    path('crearango/', vst_crear_rango.as_view(), name = 'crear_rango'), #Crear un rango de evaluación 
    path('cnrango/', vst_ls_rango.as_view(), name = 'cn_rango'), #Consultar rango de evaluación de un proyecto
    path('editrng/<int:pk>/',vst_edit_rng.as_view(), name = 'edit_rng'), #Editar el rango de evaluación de un proyecto
    path('archirng/<id>',fn_archi_rng, name = 'archi_rng'), #Archivar el rango de evaluación de un proyecto
    path('elirng/<id>',fn_eli_rng, name = 'eli_rng'),#Eliminar el rango de evaluación de un proyecto
    #URL para resultado de evaluación
    path('crearesul/', vst_crear_resul.as_view(), name = 'crear_resul'), #Crear un resultado de evaluación
    path('cnres/', vst_ls_resultado.as_view(), name = 'cn_res'), #Consultar resultado de una evaluación de un proyecto
    path('editres/<int:pk>/',vst_edit_res.as_view(), name = 'edit_res'), #Editar el rsultado de una evaluación de un proyecto
    path('archires/<id>',fn_archi_res, name = 'archi_res'), #Archivar el resultado de evaluación de un proyecto, solo para el rol de evaluadores
    path('elires/<id>',fn_eli_res, name = 'eli_res'),#Eliminar el resultado de evaluación de un proyecto
    #URL para tipo de evaluación
    path('creatipo/', vst_crear_tipoeva.as_view(), name = 'crear_tipo'), #Crear tipo de evaluación
    path('cntipoeva/', vst_ls_tipoeva.as_view(), name = 'cn_tipoeva'), #Consultar tipo de evaluación de un proyecto
    path('editipo/<int:pk>/',vst_edit_tipo.as_view(), name = 'edit_tipo'), #Editar el tipo de evaluación de un proyecto
    path('elitipo/<id>',fn_eli_tipo, name = 'eli_tipo'),#Eliminar el tipo de evaluación de un proyecto
    #URL para definciónes, comentarios, ect, de evaluación
    path('creardefi/', vst_crear_defi.as_view(), name = 'crear_defi'), #Crear definición, comentario, recomendación
    path('cndefi/', vst_ls_defi.as_view(), name = 'cn_defi'), #Consultar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('editdefi/<int:pk>/',vst_edit_defi.as_view(), name = 'edit_defi'), #Editar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('archidefi/<id>',fn_archi_defi, name = 'archi_defi'), #Archivar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('elidefi/<id>',fn_eli_defi, name = 'eli_defi'),#Eliminar definciónes, comentarios, ect, de la evaluación de un proyecto
]


