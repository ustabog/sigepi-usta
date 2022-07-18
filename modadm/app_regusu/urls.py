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
    path('cons_usus/', vts_ls_usu.as_view(), name='consulta_usuarios'),
    #Seleccionar usuario de consulta
    path('sel_usu_cons/', vst_selc_usu_cons.as_view(), name='seleccion_usuario_consulta'),
#   #editar usuario de consulta
    path('edi_usu/<int:pk>/',vst_edit_usu.as_view(), name = 'editar_usu'),
    #from urls modAdm
    path('eli_usu/<id>',vst_eli_usu, name = 'eliminar_usu'),
    
    #Crear información adicional de usuarios
    path('crearinf/',infopersCreate.as_view(), name = 'crearinf'),
    #Lista de información de usuarios
    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    #Modificar la información de usuarios
    path('editarinf/<int:pk>/',infopersUpdate.as_view(), name='editarinf'),
    #Eliminar información de usuarios
    path('eliminarinf/<int:pk>/',infopersDelete.as_view(), name='eliminarinf'),

    # CRUD DISCAPACIDAD
    path('reg_disc/', vts_reg_discap.as_view(), name = 'reg_disc'),
    path('cons_disc/', vts_ls_discap.as_view(), name = 'cons_discapacidad'),
    path('edt_disc/<int:pk>/', vts_edt_discap.as_view(), name='edt_disc'),
    path('eli_disc/<int:pk>/', vts_del_discap.as_view(), name='eli_disc'),

    # CRUD INFORMACION PERSONAL
    path('reg_infopers/', vts_reg_usu_inf_pers.as_view(), name = 'reg_infopers'),
    path('cons_infopers/', vts_ls_usu_inf_pers.as_view(), name = 'cons_infopers'),
    path('edt_infopers/<int:pk>/', vts_edt_usu_inf_pers.as_view(), name='edt_infopers'),
    path('eli_infopers/<int:pk>/', vts_del_usu_inf_pers.as_view(), name='eli_infopers'),

]
    

