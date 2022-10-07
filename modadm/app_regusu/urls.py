from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter
from modadm.app_regusu.views import *
from .models import *


urlpatterns = [ 
    #crear usuario del modulo adm
    path('creausu/',vts_reg_usu().vst_registro, name = 'crea_nvo_usu'),
    #Consulta de usuarios
    path('cons_usus/', vts_ls_usu.as_view(), name='cons_usu'),
    #Seleccionar usuario de consulta
    path('sel_usu_cons/<int:pk>', vst_selc_usu_cons.vis_esp, name='sel_cons_usu'),
#   #editar usuario de consulta
    path('edi_usu/<int:pk>/',vst_edit_usu.as_view(), name = 'editar_usu'),
    #from urls modAdm
    path('eli_usu/<id>',vst_eli_usu, name = 'eliminar_usu'),
    
    #Crear información adicional de usuarios
    path('crearinf/',portada_adm().vst_raiz, name = 'crearinf'),
    #Lista de información de usuarios
    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    #Modificar la información de usuarios
    path('editarinf/<int:pk>/',infopersUpdate.as_view(), name='editarinf'),
    #Eliminar información de usuarios
    path('eliminarinf/<int:pk>/',infopersDelete.as_view(), name='eliminarinf'),

    # CRUD DISCAPACIDAD
    path('reg_disc/', vts_reg_discap.as_view(), name = 'reg_usu_disc'),
    path('cons_disc/', vts_ls_discap.as_view(), name = 'cons_discapacidad'),
    path('edt_disc/<int:pk>/', vts_edt_discap.as_view(), name='edt_disc'),
    path('eli_disc/<int:pk>/', vts_del_discap.as_view(), name='eli_disc'),

    # CRUD INFORMACION PERSONAL
    path('reg_infopers/', vts_reg_usu_inf_pers.crear, name = 'reg_infopers'),
    path('cons_infopers/', vts_ls_usu_inf_pers.as_view(), name = 'cons_infopers'),
    path('edt_infopers/<int:pk>/', vts_edt_usu_inf_pers.as_view(), name='edt_infopers'),
    path('eli_infopers/<int:pk>/', vts_del_usu_inf_pers.as_view(), name='eli_infopers'),

    # CRUD HABILIDAD
    path('reg_habpers/', vts_reg_usu_hab.as_view(), name='reg_habpers'),

    # CRUD EMPLEO
    path('reg_empleo/', vts_reg_usu_emp.as_view(), name='reg_empleo'),
    path('cons_empleo/', vst_ls_usu_emp.consultar_todos, name='cons_empleo'),

    # CRUD CURSO
    path('reg_usu_cur/', App_regusu_frm_cursos.as_view(), name='reg_usu_cur'),
   
    # CRUD FORMACION
    path('reg_acad_inf/', App_regusu_frm_form_acad.as_view(), name='reg_acad_inf'),

    # CRUD INF.CONTACTO
    path('mi_contacto/', App_regusu_frm_contac.as_view(), name='mi_contacto'),


    
]
    

