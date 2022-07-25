# App de convocatorias para un proyecto - URL's para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.urls import path
from modpry.app_convo.views import *
from modpry.app_convo.func import *
from .models import *

urlpatterns = [ 
    #URL's para la aplicación de convocatoria
    path('inicio',vst_convo().vst_inicio, name = 'ini_convo'), #inicio de la app de convocatoria
    path('crearconvo/',vts_reg_convo.as_view(), name = 'crea_convo'), #Crea la convocatoria 
    path('cnconvo/', vst_ls_convo.as_view(), name='cn_convo'), #Lista de convocatorias
    path('verconvo/', vst_ls_detconvo.as_view(), name = 'cn_det_convo'), # Información de una convocatoria
    path('editconvo/<int:pk>/',vts_edit_convo.as_view(), name = 'edit_convo'), #Actualizar convocatoria
    path('archiconvo/<id>',fn_archi_convo, name = 'archi_convo'), #Archivar una convocatoria
    path('eliconvo/<id>',fn_eli_convo, name = 'eli_convo'),#Eliminar una convocatoria
]