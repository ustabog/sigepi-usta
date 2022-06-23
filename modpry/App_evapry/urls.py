from django.urls import path
from modpry.app_modpry.views import *
from modpry.app_evapry.views import *
from modpry.app_evapry.funciones import *
from .models import *


urlpatterns = [ 
    #URL para las funciones de la evaluación de un proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    #URL para la evaluación de un proyecto
    path('creaeva/', vst_reg_evapry.as_view(), name = 'crear_eva'), #Crear evaluación de un proyecto
    path('cneva/', vst_ls_evapry.as_view(), name = 'cn_evapry'), #Consultar evaluación de un proyecto
    path('editeva/<int:pk>/',vst_edit_evapry.as_view(), name = 'edit_eva'), #Editar la evaluación de un proyecto
    path('archieva/<id>',archi_eva, name = 'archi_eva'), #Archivar la evaluación de un proyecto
    path('elieva/<id>',eli_eva, name = 'eli_eva'),#Eliminar la evaluación de un proyecto
    #URL para rúbrica de evaluación
    path('crearub/', vst_crear_rub.as_view(), name = 'crear_rub'), #Crear rúbrica
    path('cnrub/', vst_ls_rub.as_view(), name = 'cn_rub'), #Consultar rúbrica
    path('editrub/<int:pk>/',vst_edit_rub.as_view(), name = 'edit_rub'), #Editar la rúbrica de evaluación de un proyecto
    path('archirub/<id>',archi_rub, name = 'archi_rub'), #Archivar la rúbrica de evaluación de un proyecto
    path('elirub/<id>',eli_rub, name = 'eli_rub'),#Eliminar la rúbrica de evaluación de un proyecto
    #URL para criterio de evaluación
    path('creacrit/', vst_crear_crit.as_view(), name = 'crear_crit'), #Crear criterios de la rúbrica
    path('cncrit/', vst_ls_crit.as_view(), name = 'cn_crit'), #Consultar criterios evaluación de un proyecto
    path('editcrti/<int:pk>/',vst_edit_crit.as_view(), name = 'edit_crit'), #Editar el criterio de evaluación de un proyecto
    path('archicrit/<id>',archi_crit, name = 'archi_crit'), #Archivar el criterio de evaluación de un proyecto
    path('elicrti/<id>',eli_crit, name = 'eli_crit'),#Eliminar el criterio de evaluación de un proyecto
    #URL para rango de evaluación
    path('crearango/', vst_crear_rango.as_view(), name = 'crear_rango'), #Crear un rango de evaluación 
    path('cnrango/', vst_ls_rango.as_view(), name = 'cn_rango'), #Consultar rango de evaluación de un proyecto
    path('editrng/<int:pk>/',vst_edit_rng.as_view(), name = 'edit_rng'), #Editar el rango de evaluación de un proyecto
    path('archirng/<id>',archi_rng, name = 'archi_rng'), #Archivar el rango de evaluación de un proyecto
    path('elirng/<id>',eli_rng, name = 'eli_rng'),#Eliminar el rango de evaluación de un proyecto
    #URL para resultado de evaluación
    path('crearesul/', vst_crear_resul.as_view(), name = 'crear_resul'), #Crear un resultado de evaluación
    path('cnres/', vst_ls_resultado.as_view(), name = 'cn_res'), #Consultar resultado de una evaluación de un proyecto
    path('editres/<int:pk>/',vst_edit_res.as_view(), name = 'edit_res'), #Editar el rsultado de una evaluación de un proyecto
    path('elires/<id>',eli_res, name = 'eli_res'),#Eliminar el resultado de evaluación de un proyecto
    #URL para tipo de evaluación
    path('creatipo/', vst_crear_tipoeva.as_view(), name = 'crear_tipo'), #Crear tipo de evaluación
    path('cntipoeva/', vst_ls_tipoeva.as_view(), name = 'cn_tipoeva'), #Consultar tipo de evaluación de un proyecto
    path('editipo/<int:pk>/',vst_edit_tipo.as_view(), name = 'edit_tipo'), #Editar el tipo de evaluación de un proyecto
    path('elitipo/<id>',eli_tipo, name = 'eli_tipo'),#Eliminar el tipo de evaluación de un proyecto
    #URL para definciónes, comentarios, ect, de evaluación
    path('creardefi/', vst_crear_defi.as_view(), name = 'crear_defi'), #Crear definición, comentario, recomendación
    path('cndefi/', vst_ls_defi.as_view(), name = 'cn_defi'), #Consultar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('editdefi/<int:pk>/',vst_edit_defi.as_view(), name = 'edit_defi'), #Editar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('archidefi/<id>',archi_defi, name = 'archi_defi'), #Archivar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('elidefi/<id>',eli_defi, name = 'eli_defi'),#Eliminar definciónes, comentarios, ect, de la evaluación de un proyecto
]