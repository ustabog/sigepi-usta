# App de convenios de proyectos de investigación - URL's para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a): Milton O. Castro Ch.
#fecha 25-07-2022

from django.urls import path
from modpry.app_conve.views import *
from modpry.app_conve.func import *
from .models import *

urlpatterns = [ 
    #URL's para la aplicación de convenios
    path('inicio',vst_conve().vst_inicio, name = 'ini_conve'), #inicio de la app de convenios
    path('crearconve/',vts_reg_conve.as_view(), name = 'crea_conve'), #Crea el convenio 
    path('cnconve/', vst_ls_conve.as_view(), name='cn_conve'), #Lista de convenios
    path('cndetconve/', vst_ls_detconve.as_view(), name = 'cn_det_conve'),# Información de un convenio
    path('editconve/<int:pk>/',vts_edit_conve.as_view(), name = 'edit_conve'), #Actualizar convenio
    path('archiconve/<id>',fn_archi_conve, name = 'archi_conve'), #Archivar un convenio
    path('eliconve/<id>',fn_eli_conve, name = 'eli_conve'),#Eliminar un convenio
]