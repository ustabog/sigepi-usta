from django.urls import path
from modpry.app_disinv.views import *
from modpry.app_disinv.func import *
from .models import *

urlpatterns = [ 
    #URL para la aplicación de diseño de proyecto de investigación
    path('inicio',vst_disinv().vst_inicio, name = 'ini_disinv'), #inicio de la app de diseño de proyecto de investigación
    
    #URL para el registro de un diseño de investigación
    path('creadis/',vts_reg_dispry.as_view(), name = 'crea_dis'), #Crea el diseño de un proyecto 
    path('cndis/', vst_ls_dispry.as_view(), name='cn_dispry'), #Lista de diseños de proyectos
    path('cndetdis/', vts_ls_detdis.as_view(), name='cn_det_dis'), #Añadir información del diseño de un proyecto
    path('editdis/<int:pk>/',vts_edit_dispry.as_view(), name = 'edit_dis'), #Actualizar diseño de un proyecto
    path('archidis/<id>',fn_archi_dis, name = 'archi_dis'), #Archivar un diseño de un proyecto
    path('elidis/<id>',fn_eli_dis, name = 'eli_dis'),#Eliminar un diseño de un proyecto

    #URL para el registro de un tema
    path('createma/',vts_reg_tema.as_view(), name = 'crea_tema'), #Crea el tema
    path('cntema/', vst_ls_tema.as_view(), name='cn_tema'), #Lista de los tema
    path('editema/<int:pk>/',vts_edit_tema.as_view(), name = 'edit_tema'), #Actualiza el tema
    path('architema/<id>',fn_archi_tema, name = 'archi_tema'), #Archivar un tema
    path('elitema/<id>',fn_eli_tema, name = 'eli_tema'),#Eliminar un tema

    #URL para el registro de una definición
    path('creadefin/',vts_reg_defi.as_view(), name = 'crea_defin_dis'), #Crea la definición
    path('cndefin/', vst_ls_defi.as_view(), name='cn_defin_dis'), #Lista de laa definiciones
    path('edirdefin/<int:pk>/',vts_edit_defi.as_view(), name = 'edit_defin_dis'), #Actualiza una definición
    path('archidefin/<id>',fn_archi_defi, name = 'archi_defin_dis'), #Archivar una definición
    path('elidefin/<id>',fn_eli_defi, name = 'eli_defin_dis'),#Eliminar una definición

    #URL para el registro de un árbol de problemas
    path('creaap/',vts_reg_ap.as_view(), name = 'crea_arb_pro'), #Crea un árbol de problemas
    path('cnap/', vst_ls_ap.as_view(), name='cn_arb_pro'), #Lista los árboles de problemas
    path('edirap/<int:pk>/',vts_edit_ap.as_view(), name = 'edit_arb_pro'), #Actualiza un árbol de problemas
    path('archiap/<id>',fn_archi_ap, name = 'archi_arb_pro'), #Archivar un árbol de problemas
    path('eliap/<id>',fn_eli_ap, name = 'eli_arb_pro'),#Eliminar un árbol de problemas

    #URL para el registro de un árbol de objetivos
    path('creaao/',vts_reg_ao.as_view(), name = 'crea_arb_obj'), #Crea un árbol de objetivos
    path('cnao/', vst_ls_ao.as_view(), name='cn_arb_obj'), #Lista los árboles de objetivos
    path('edirao/<int:pk>/',vts_edit_ao.as_view(), name = 'edit_arb_obj'), #Actualiza un árbol de objetivos
    path('archiao/<id>',fn_archi_ao, name = 'archi_arb_obj'), #Archivar un árbol de objetivos
    path('eliao/<id>',fn_eli_ao, name = 'eli_arb_obj'),#Eliminar un árbol de objetivos

    #URL para el registro de causas
    path('creacau/',vts_reg_cau.as_view(), name = 'crea_causa'), #Crea una causa
    path('cncau/', vst_ls_cau.as_view(), name='cn_causa'), #Lista las causas
    path('edircau/<int:pk>/',vts_edit_cau.as_view(), name = 'edit_causa'), #Actualiza una causa
    path('archicau/<id>',fn_archi_cau, name = 'archi_causa'), #Archivar una causa
    path('elicau/<id>',fn_eli_cau, name = 'eli_causa'),#Eliminar una causa

    #URL para el registro de un efecto
    path('creaefe/',vts_reg_efe.as_view(), name = 'crea_efecto'), #Crea un efecto
    path('cnefe/', vst_ls_efe.as_view(), name='cn_efecto'), #Lista las efecto
    path('editefe/<int:pk>/',vts_edit_efe.as_view(), name = 'edit_efecto'), #Actualiza un efecto
    path('archiefe/<id>',fn_archi_efe, name = 'archi_efecto'), #Archivar un efecto
    path('eliefe/<id>',fn_eli_efe, name = 'eli_efecto'),#Eliminar un efecto

    #URL para el registro de un medio
    path('creamed/',vts_reg_med.as_view(), name = 'crea_medio'), #Crea un medio
    path('cnmed/', vst_ls_med.as_view(), name='cn_medio'), #Lista las medio
    path('editmed/<int:pk>/',vts_edit_med.as_view(), name = 'edit_medio'), #Actualiza un medio
    path('archimed/<id>',fn_archi_med, name = 'archi_medio'), #Archivar un medio
    path('elimed/<id>',fn_eli_med, name = 'eli_medio'),#Eliminar un medio

    #URL para el registro de un fin
    path('creafin/',vts_reg_fin.as_view(), name = 'crea_fin'), #Crea un fin
    path('cnfin/', vst_ls_fin.as_view(), name='cn_fin'), #Lista las fin
    path('editfin/<int:pk>/',vts_edit_fin.as_view(), name = 'edit_fin'), #Actualiza un fin
    path('archifin/<id>',fn_archi_fin, name = 'archi_fin'), #Archivar un fin
    path('elifin/<id>',fn_eli_fin, name = 'eli_fin'),#Eliminar un fin
]