# Lista de urls para las vistas del registro de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 25 -08 -2022

from django.urls import path
from .models import *
from modprd.app_regprd.views import *

urlpatterns = [
    path('iniprd', ini_regprd().view_prd, name='ini_prd'), # url al inicio de la interfaz de productos
    path('crearprd/', vst_regprd.as_view(), name='crear_prd'), # url para la interfaz de creacion de productos
    path('selecprd/', vst_selecprd.as_view(), name='selec_prd'), # url para la interfaz de seleccion de productos
    path('updprd/', vst_updprd.as_view(), name='editar_prd'), # url para la interfaz de seleccion de productos
    path('eliprd/', vst_delprd.as_view(), name='eliminar_prd'), # url para la interfaz de eliminacion de productos

    path('creareqexs/', vst_regreqexist.as_view(), name='reqexs'),# urls para la interfaz de creacion de requerimientos de existencia
    path('creareqcal/', vst_regreqcal.as_view(), name='reqcal'),# urls para la interfaz de creacion de requerimientos de calidad
    path('crearcateg/', vst_regcateg.as_view(), name='regcateg'),# urls para la interfaz de creacion de categoria
    path('creartipoprd/', vst_regtipo.as_view(), name='regtipo'),# urls para la interfaz de creacion de tipo de producto
    path('crearcampo/', vst_regcampo.as_view(), name='regcampo'),# urls para la interfaz de creacion de campo 
]