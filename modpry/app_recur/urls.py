from .models import *
from django.urls import path
from modpry.app_recur.views import *
from modpry.app_recur.models import *
from modpry.app_recur.func import *

urlpatterns = [ 
    #URL para la aplicación de recursos
    path('inicio',vst_recur().vst_inicio, name = 'ini_recur'), #inicio de la app de recursos
    path('crearecu/',vts_reg_recu.as_view(), name = 'crea_recu'), #Crea el recurso 
    path('cnrecu/', vst_ls_recu.as_view(), name='cn_recu'), #Lista de recursos
    path('cndetrecu/',vst_ls_detrecu.as_view(), name = 'cn_det_recu'), #Información en detalle de un recurso
    path('editrecu/<int:pk>/',vts_edit_recu.as_view(), name = 'edit_recu'), #Actualizar recurso
    path('archirecu/<id>',fn_archi_recu, name = 'archi_recu'), #Archivar un recurso
    path('elirecu/<id>',fn_eli_recu, name = 'eli_recu'),#Eliminar un recurso
]