from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter
from modadm.App_regusu.views import *
from .models import *


urlpatterns = [ 
    #crear usuario del modulo adm
    path('creausu/',vts_reg_usu().vst_registro, name = 'crea_nvo_usu'),
    #Consulta de usuarios
    path('cons_usus/', vts_ls_usu.as_view(), name='consulta_usuarios'),
    #Seleccionar usuario de consulta
    path('sel_usu_cons/', vst_selc_usu_cons.as_view(), name='seleccion_usuario_consulta'),
#   #editar usuario de consulta
    path('edi_usu/<int:pk>/',vst_mod_usu.as_view(), name = 'editar_usu'),
    #from urls modAdm
    path('eli_usu/<id>',eli_usu, name = 'eliminar_usu'),
    
    #Crear información adicional de usuarios
    path('crearinf/',infopersCreate.as_view(), name = 'crearinf'),
    #Lista de información de usuarios
    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    #Modificar la información de usuarios
    path('editarinf/<int:pk>/',infopersUpdate.as_view(), name='editarinf'),
    #Eliminar información de usuarios
    path('eliminarinf/<int:pk>/',infopersDelete.as_view(), name='eliminarinf')
# #funciones

]
