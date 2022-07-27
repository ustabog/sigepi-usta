from django.urls import path
from modpry.app_regprgi.views import *
from modpry.app_regprgi.func import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de registro de programa de investigación
    path('inicio',vst_regprgi().vst_inicio, name = 'ini_regprgi'), #inicio de la app de registro de programas de investigación
    path('creaprgi/',vts_reg_prgi.as_view(), name = 'crea_prgi'), #Crea el programa de investigación                                                                                                                                               
    path('cnprgi/', vst_ls_prgi.as_view(), name='cn_prgi'), #Lista de programas de investigación
    path('cndetprgi/',vst_ls_detprgi.as_view(), name = 'cn_det_prgi'), #Información en detalle de un programa de investigación
    path('editprgi/<int:pk>/',vts_edit_prgi.as_view(), name = 'edit_prgi'), #Actualizar un programa de investigación
    path('archiprgi/<id>',fn_archi_prgi, name = 'archi_prgi'), #Archivar un programa de investigación
    path('eliprgi/<id>',fn_eli_prgi, name = 'eli_prgi'),#Eliminar un programa de investigación
]