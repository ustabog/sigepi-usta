# Lista de urls para las vistas del registro de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 25 -08 -2022

from django.urls import path
from .models import * 
from modprd.app_regprd.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    #Url's Para el registro de producto

    path('iniprd', login_required(ini_regprd().view_prd), name='ini_prd'), # url al inicio de la interfaz de productos
    path('crearprd/', login_required(vst_regprd.as_view()), name='crear_prd'), # url para la interfaz de creacion de productos
    path('regprd/', login_required(vst_regprd), name='reg_prd'), # url para la creacion de productos
    path('listprd/', login_required(vst_listprd.as_view()), name='listar_prd'), # url para la interfaz de listado de productos
    path('consprd/<int:pk>', login_required(vst_cons_prd.as_view()), name='consultar_prd'), # url para la interfaz de consulta de productos
    path('updprd/<int:pk>', login_required(vst_updprd.as_view()), name='editar_prd'), # url para la interfaz de actualizacion de productos
    path('eliprd/<int:pk>', login_required(vst_delprd.as_view()), name='eliminar_prd'), # url para la interfaz de eliminacion de productos
    path('archiprd/<id>', login_required(vst_archiprd.as_view()), name='archivar_prd'), # url para la interfaz de archivacion de productos
    path('buscarprd', login_required(vst_searchprd), name='buscar_prd'), # url para la interfaz de busqueda de productos
    path('buscarpry', login_required(vst_searchpry), name='buscar_pry'), # url para la interfaz de busqueda de proyectos pare productos

    #Url's Para el registro de requerimientos de existencia
    
    path('creareqexs/', login_required(vst_regreqexist.as_view()), name='crear_reqexs'),# urls para la interfaz de creacion de requerimientos de existencia
    path('listreqexs/', login_required(vst_list_reqexist.as_view()), name='listar_reqexs'),# urls para la interfaz para listar los requerimientos de existencia
    path('consreqexs/<int:pk>/', login_required(vst_cons_reqexist.as_view()), name='consultar_reqexs'),# urls para la interfaz para la consulta de los requerimientos de existencia
    path('updreqexs/<int:pk>/', login_required(vst_upd_reqexist.as_view()), name='editar_reqexs'),# urls para la interfaz para editar los requerimientos de existencia
    path('delreqexs/<int:pk>/', login_required(vst_del_reqexist.as_view()), name='eliminar_reqexs'),# urls para la interfaz para eliminar requerimientos de existencia
    path('archireqexs/<id>', login_required(vst_archi_reqexist.as_view()), name='archivar_reqexs'), # url para la interfaz de archivacion de requerimientos de existencia
    path('buscareqexs', login_required(vst_search_reqexist), name='buscar_reqexist'), # url para la interfaz de busqueda de requerimientos de existencia

    #Url's Para el registro de requerimientos de calidad

    path('creareqcal/', login_required(vst_regreqcal.as_view()), name='crear_reqcal'),# urls para la interfaz de creacion de requerimientos de calidad
    path('listreqcal/', login_required(vst_list_reqcal.as_view()), name='listar_reqcal'),# urls para la interfaz de listado de requerimientos de calidad
    path('consreqcal/<int:pk>', login_required(vst_cons_reqcal.as_view()), name='consultar_reqcal'),# urls para la interfaz de consulta de requerimientos de calidad
    path('updreqcal/<int:pk>/', login_required(vst_upd_reqcal.as_view()), name='editar_reqcal'),# urls para la interfaz de edicion de requerimientos de calidad
    path('delreqcal/<int:pk>/', login_required(vst_del_reqcal.as_view()), name='eliminar_reqcal'),# urls para la interfaz de eliminacion de requerimientos de calidad
    path('archireqcal/<id>', login_required(vst_archi_reqcal.as_view()), name='archivar_reqcal'), # url para la interfaz de archivacion de requerimientos de calidad
    path('buscareqcal', login_required(vst_search_reqcal), name='buscar_reqcal'), # url para la interfaz de busqueda de requerimientos de calidad

    #Url's Para el registro de categorias

    path('crearcateg/', login_required(vst_regcateg.as_view()), name='crear_categ'),# urls para la interfaz de creacion de categoria
    path('listcateg/', login_required(vst_list_categ.as_view()), name='listar_categ'),# urls para la interfaz de listado una categoria
    path('conscateg/<int:pk>', login_required(vst_cons_categ.as_view()), name='consultar_categ'),# urls para la interfaz de consultar una categoria
    path('updcateg/<int:pk>/', login_required(vst_upd_categ.as_view()), name='editar_categ'),# urls para la interfaz de consultar una categoria
    path('delcateg/<int:pk>', login_required(vst_del_categ.as_view()), name='eliminar_categ'),# urls para la interfaz de consultar una categoria
    path('archicateg/<id>', login_required(vst_archi_categ.as_view()), name='archivar_categ'), # url para la interfaz de archivacion de categorias
    path('buscarcateg', login_required(vst_search_categ), name='buscar_categ'), # url para la interfaz de busqueda de categorias de productos

    #Url's Para el registro de tipos de producto

    path('creartipoprd/', login_required(vst_regtipo.as_view()), name='regtipo'),# urls para la interfaz de creacion de tipo de producto
    path('listipoprd/', login_required(vst_list_tipo.as_view()), name='listar_tipo'),# urls para la interfaz de listado de tipos de producto
    path('constipoprd/<int:pk>', login_required(vst_cons_tipo.as_view()), name='consultar_tipo'),# urls para la interfaz de consulta de tipos de producto
    path('updtipoprd/<int:pk>/', login_required(vst_upd_tipo.as_view()), name='editar_tipo'),# urls para la interfaz de edicion de tipos de producto
    path('deltipoprd/<int:pk>/', login_required(vst_del_tipo.as_view()), name='eliminar_tipo'),# urls para la interfaz de edicion de tipos de producto
    path('archiripoprd/<id>', login_required(vst_archi_tipo.as_view()), name='archivar_tipo'), # url para la interfaz de archivacion de tipos de productos
    path('buscartipo', login_required(vst_search_tipo), name='buscar_tipo'), # url para la interfaz de busqueda de tipo de producto

    #Url's Para el registro de campos de un producto

    path('crearcampo/', login_required(vst_regcampo.as_view()), name='regcampo'),# urls para la interfaz de creacion de campo 
    path('listcampo/', login_required(vst_list_camp.as_view()), name='listar_campo'),# urls para la interfaz de listado de campos 
    path('conscampo/<int:pk>', login_required(vst_cons_campo.as_view()), name='consultar_campo'),# urls para la interfaz de consulta de campos 
    path('updcampo/<int:pk>', login_required(vst_upd_camp.as_view()), name='editar_campo'),# urls para la interfaz de edicion de campos 
    path('delcampo/<int:pk>', login_required(vst_del_camp.as_view()), name='eliminar_campo'),# urls para la interfaz de edicion de campos 
    path('archireqexs/<id>', login_required(vst_archi_campo.as_view()), name='archivar_campo'), # url para la interfaz de archivacion de campos de plantillas
    path('buscarcampo', login_required(vst_search_campo), name='buscar_campo'), # url para la interfaz de busqueda de campos de plantillas

    #Url's Para el registro de plantillas de un producto

    path('crearplt/', login_required(vst_regplt.as_view()), name='registrar_plantilla'),# urls para la interfaz de creacion de plantillas de un producto
    path('listplt/', login_required(vst_list_plt.as_view()), name='listar_plantilla'),# urls para la interfaz de listado de plantillas de un producto
    path('consplt/<int:pk>', login_required(vst_cons_plt.as_view()), name='consultar_plantilla'),# urls para la interfaz de consulta de plantillas de un producto
    path('updplt/<int:pk>', login_required( vst_upd_plt.as_view()), name='editar_plantilla'),# urls para la interfaz de edicion de plantillas de un producto
    path('delplt/<int:pk>', login_required(vst_del_plt.as_view()), name='eliminar_plantilla'),# urls para la interfaz de eliminacion de plantillas de un producto
    path('archiplt/<id>', login_required(vst_archi_plt.as_view()), name='archivar_plantilla'), # url para la interfaz de archivacion de plantillas
    path('buscarplt', login_required(vst_search_plt), name='buscar_plantilla'), # url para la interfaz de busqueda de plantillas

]