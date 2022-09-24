# App de certificacion de productos - URL'S para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.urls import path
from .models import *
from modprd.app_certprd.views import *

#urls para la app de mediciones y certificaciones de productos

urlpatterns = [
    path('crearmed/', vst_reg_med.as_view(), name='crear_med'),# url para la interfaz de creacion de mediciones
    path('listmed/', vst_list_med.as_view(), name='listar_med'),# url para la interfaz de creacion de mediciones
    path('consmed/<int:pk>', vst_cons_med.as_view(), name='consultar_med'),# url para la interfaz de creacion de mediciones
    path('updmed/<int:pk>', vst_upd_med.as_view(), name='editar_med'),# url para la interfaz de creacion de mediciones
    path('delmed/<int:pk>', vst_del_med.as_view(), name='eliminar_med'),# url para la interfaz de creacion de mediciones
]
