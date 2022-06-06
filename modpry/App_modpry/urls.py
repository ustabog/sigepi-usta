from django.urls import path
from django.contrib.auth.views import *
#from rest_framework.routers import DefaultRouter
from modpry.App_regpry.views import *
from modpry.App_regpry import *
from modpry.App_regpry.urls import *
from modpry.App_modpry.views import *
from modpry.App_crono.views import *
from modpry.App_crono.urls import *
from .models import *

urlpatterns = [ 
    
    #URL para registro de proyecto
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cons_pry/', vts_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    #path('elipry/<int_pk>',vts_reg_pry.as_view(), name = 'elim_pry'), #Borrar proyecto
    path('elipry/<id>',eli_pry, name = 'eliminar_usu'),

    #URL para cronograma
    path('creacrono/',vts_crea_crono.as_view(), name = 'crea_crono'), #Crea el proyecto
    #path('creaeta/',vts_crea_etapa.as_view(), name = 'crea_etapa'), #Crear etapa de un cronograma
    #path('creafase/',vts_crea_fase.as_view(), name = 'crea_fase'), #Crear fase de una etapa
    #path('creaproc/',vts_crea_proc.as_view(), name = 'crea_proc'), #Crea el proceso de una fase
    #path('creatarea/',vts_crea_tarea.as_view(), name = 'crea_tarea'), #Crea la tarea de un proceso
    #path('creaacti/',vts_crea_acti.as_view(), name = 'crea_acti'), #Crea la actividad de una tarea 

]


