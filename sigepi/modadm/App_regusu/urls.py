from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
#from rest_framework.routers import DefaultRouter
from modadm.App_regusu.views import *
from modadm.App_regusu.class_view import *
from .models import *


urlpatterns = [
    #Prueba para el registo de urls
    path('prueba/', prueba ),
    #crear usuario del modulo adm
    path('creausu/',vts_reg_usu_su.as_view(), name = 'crea_usu'),
    path('cons_usus/', vts_ls_usu.as_view(), name='consulta_usuarios'),

    #Lista de usuarios
    path('ls_mod_usu/',vst_selc_usu_cons.as_view(), name='ls_mod_usu'),
 
#   #editar usuario de consulta
    path('edi_usu/<int:pk>/',vst_mod_reg_usu.as_view(), name = 'editar_usu'),
    #from urls modAdm
    #path('editar_usu/<int:pk>/',UsuUpdate.as_view(), name='editarusu'),
    
    #path('sel_usu_cons/', vst_selc_usu_cons.as_view(), name='seleccion_usuario_consulta'),
    
    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    path('crearinf/',infopersCreate.as_view(), name = 'crearinf'),
    path('editarinf/<int:pk>/',infopersUpdate.as_view(), name='editarinf'),
#     path('eliminarinf/<int:pk>/',infopersDelete.as_view(), name='eliminarinf')
# #funciones

]
