from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter
from modadm.App_regusu.views import *
from .models import *


urlpatterns = [ 
    #crear usuario del modulo adm
    path('creausu/',vts_reg_usu().vst_registro, name = 'crea_nvo_usu'),
    path('cons_usus/', vts_ls_usu.as_view(), name='consulta_usuarios'),
    path('sel_usu_cons/', vst_selc_usu_cons.as_view(), name='seleccion_usuario_consulta'),
    path('edi_usu/<int:pk>/',vst_mod_usu.as_view(), name = 'editar_usu'),
    path('eli_usu/<id>',eli_usu, name = 'eliminar_usu'),

    # CRUD DISCAPACIDAD  # General
    path('reg_disc/', vts_reg_discapacidad.as_view(), name = 'reg_disc'),
    path('cons_disc/', vts_ls_discapacidad.as_view(), name = 'cons_discapacidad'),
    path('edt_disc/<int:pk>/', vts_edt_discapacidad.as_view(), name='edt_disc'),
    path('eli_disc/<int:pk>/', vts_del_discapacidad.as_view(), name='eli_disc'),

    # CRUD INFORMACION PERSONAL # PROPIO DEL USUARIO
    path('reg_infopers/', vts_reg_usu_inf_pers.as_view(), name = 'reg_infopers'),
    path('cons_infopers/', vts_ls_usu_inf_pers.as_view(), name = 'cons_infopers'),
    path('edt_infopers/<int:pk>/', vts_edt_usu_inf_pers.as_view(), name='edt_infopers'),
    
    # CRUD INFORMACION PERSONAL # PROPIO DEL USUARIO
    path('reg_infocontc/', vts_reg_contc.as_view(), name = 'reg_infocontc'),
    path('cons_infocontc/', vts_ls_contc.as_view(), name = 'cons_infocontc'),
    path('edt_infocontc/<int:pk>/', vts_edt_contc.as_view(), name='edt_infocontc'),

    # CRUD RED SOCIAL # PROPIO DEL USUARIO
    path('reg_red_soc/', vts_reg_red_soc.as_view(), name = 'reg_red_soc'),
    path('cons_red_soc/', vts_reg_red_soc.as_view(), name = 'cons_red_soc'),
    path('edt_red_soc/<int:pk>/', vts_reg_red_soc.as_view(), name='edt_red_soc'),


]
    

