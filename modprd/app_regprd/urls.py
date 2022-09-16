# Lista de urls para las vistas del registro de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 25 -08 -2022

from django.urls import path
from .models import *
from modprd.app_regprd.views import *

urlpatterns = [
    #Url's Para el registro de producto
    path('iniprd', ini_regprd().view_prd, name='ini_prd'), # url al inicio de la interfaz de productos
    path('crearprd/', vst_regprd.as_view(), name='crear_prd'), # url para la interfaz de creacion de productos
    path('listprd/', vst_selecprd.as_view(), name='listar_prd'), # url para la interfaz de seleccion de productos
    path('updprd/', vst_updprd.as_view(), name='editar_prd'), # url para la interfaz de seleccion de productos
    path('eliprd/', vst_delprd.as_view(), name='eliminar_prd'), # url para la interfaz de eliminacion de productos

    #Url's Para el registro de requerimientos de existencia
    path('creareqexs/', vst_regreqexist.as_view(), name='crear_reqexs'),# urls para la interfaz de creacion de requerimientos de existencia
    path('listreqexs/', vst_list_reqexist.as_view(), name='listar_reqexs'),# urls para la interfaz para listar los requerimientos de existencia
    path('updreqexs/', vst_upd_reqexist.as_view(), name='editar_reqexs'),# urls para la interfaz para editar los requerimientos de existencia
    path('delreqexs/', vst_del_reqexist.as_view(), name='eliminar_reqexs'),# urls para la interfaz para eliminar requerimientos de existencia

    #Url's Para el registro de requerimientos de calidad
    path('creareqcal/', vst_regreqcal.as_view(), name='crear_reqcal'),# urls para la interfaz de creacion de requerimientos de calidad
    path('consreqcal/', vst_cons_reqcal.as_view(), name='consultar_reqcal'),# urls para la interfaz de consulta de requerimientos de calidad
    path('updreqcal/', vst_upd_reqcal.as_view(), name='editar_reqcal'),# urls para la interfaz de edicion de requerimientos de calidad
    path('delreqcal/', vst_del_reqcal.as_view(), name='eliminar_reqcal'),# urls para la interfaz de eliminacion de requerimientos de calidad

    #Url's Para el registro de categorias
    path('crearcateg/', vst_regcateg.as_view(), name='crear_categ'),# urls para la interfaz de creacion de categoria
    path('conscateg/', vst_cons_categ.as_view(), name='consultar_categ'),# urls para la interfaz de consultar una categoria
    path('updcateg/', vst_upd_categ.as_view(), name='editar_categ'),# urls para la interfaz de consultar una categoria
    path('delcateg/<int:pk>', vst_del_categ.as_view(), name='eliminar_categ'),# urls para la interfaz de consultar una categoria

    #Url's Para el registro de tipos de producto
    path('creartipoprd/', vst_regtipo.as_view(), name='regtipo'),# urls para la interfaz de creacion de tipo de producto
    path('constipoprd/', vst_cons_tipo.as_view(), name='consultar_tipo'),# urls para la interfaz de consulta de tipos de producto
    path('updtipoprd/<int:pk>', vst_upd_tipo.as_view(), name='editar_tipo'),# urls para la interfaz de edicion de tipos de producto
    path('deltipoprd/', vst_del_tipo.as_view(), name='eliminar_tipo'),# urls para la interfaz de edicion de tipos de producto

    #Url's Para el registro de campos de un producto
    path('crearcampo/', vst_regcampo.as_view(), name='regcampo'),# urls para la interfaz de creacion de campo 
    path('conscampo/', vst_cons_camp.as_view(), name='consultar_campo'),# urls para la interfaz de consulta de campos 
    path('updcampo/', vst_upd_camp.as_view(), name='editar_campo'),# urls para la interfaz de edicion de campos 
    path('delcampo/', vst_del_camp.as_view(), name='eliminar_campo'),# urls para la interfaz de edicion de campos 

    #Url's Para el registro de plantillas de un producto
    path('crearplt/', vst_regplt.as_view(), name='registrar_plantilla'),# urls para la interfaz de creacion de plantillas de un producto
    path('listplt/', vst_cons_plt.as_view(), name='consultar_plantilla'),# urls para la interfaz de consulta de plantillas de un producto
    path('updplt/', vst_upd_plt.as_view(), name='editar_plantilla'),# urls para la interfaz de edicion de plantillas de un producto
    path('delplt/<int:pk>', vst_del_plt.as_view(), name='eliminar_plantilla'),# urls para la interfaz de eliminacion de plantillas de un producto

]