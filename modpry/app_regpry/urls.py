from django.urls import path
from modpry.app_regpry.views import *
from modpry.app_modpry.views import *
from modpry.app_regpry.func import *
from .models import *


urlpatterns = [ 
    #URL para registro de un proyecto
    path('inicio',vst_regpry().vst_inicio, name = 'ini_regpry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cnpry/', vst_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('cndetpry/', vst_ls_infopry.as_view(), name='cn_det_pry'), #Lista de la información de los proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    path('archipry/<id>',fn_archi_pry, name = 'archi_pry'), #Archivar un proyecto
    path('elipry/<id>',fn_eli_pry, name = 'eli_pry'),#Eliminar un proyecto

    #URL para la información adicional de un proyecto
    path('addpry/',vts_add_pry.as_view(), name = 'add_pry'),#Añadir información del proyecto
    path('cninf/', vst_ls_infopry.as_view(), name = 'cn_infpry'),#Consultar información adicional de un proyecto
    path('editinf/<int:pk>/', vts_edit_infpry.as_view(), name = 'edit_inf'),#Editar información de un proyecto
    path('archinf/<id>',fn_archi_infpry, name = 'archi_inf_pry'), #Archivar la información adicional de un proyecto
    path('elinf/<id>',fn_eli_infpry, name = 'eli_inf_pry'),#Eliminar la información adicional de un proyecto

    #URL para la información geográfica de un proyecto
    path('addgeo/',vts_reg_geo.as_view(), name = 'add_geo'),#Añadir información geográfica del proyecto
    path('cngeo/', vst_ls_geopry.as_view(), name = 'cn_geo'),#Consultar información geográfica  de un proyecto
    path('editgeo/<int:pk>/', vts_edit_geo.as_view(), name = 'edit_geo'),#Editar información geográfica de un proyecto
    path('archigeo/<id>',fn_archi_geo, name = 'archi_geo'), #Archivar la información geográfica de un proyecto
    path('eligeo/<id>',fn_eli_geo, name = 'eli_geo'),#Eliminar la información geográfica de un proyecto

    #URL para los eventos de un proyecto
    path('addeven/',vts_reg_even.as_view(), name = 'add_even'),#Añadir eventos de un proyecto
    path('cneven/', vst_ls_evenpry.as_view(), name = 'cn_even'),#Consultar eventos de un proyecto
    path('editeven/<int:pk>/', vts_edit_even.as_view(), name = 'edit_even'),#Editar eventos de un proyecto
    path('archieven/<id>',fn_archi_even, name = 'archi_even'), #Archivar eventos de un proyecto
    path('elieven/<id>',fn_eli_even, name = 'eli_even'),#Eliminar eventos de un proyecto

    #URL para la línea de investigación
    path('addlninv/',vts_reg_lninv.as_view(), name = 'add_lninv'),#Añadir línea de investigación
    path('cnlninv/', vst_ls_lninv.as_view(), name = 'cn_lninv'),#Consultar línea de investigación
    path('editlninv/<int:pk>/', vts_edit_lninv.as_view(), name = 'edit_lninv'),#Editar línea de investigación
    path('archilninv/<id>',fn_archi_lninv, name = 'archi_lninv'), #Archivar línea de investigación
    path('elilninv/<id>',fn_eli_lninv, name = 'eli_lninv'),#Eliminar línea de investigación
]