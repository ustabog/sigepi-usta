from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
# from django.conf.urls import url
#from rest_framework.routers import DefaultRouter
from modadm.App_modadm.views import *
from .models import *

urlpatterns = [
# direcciones del modulo admin
# registrar modulos
    path('reg_mod/', vts_reg_mod.as_view(), name ='reg_mod'),
    path('cons_mod/', vts_ls_mod.as_view(), name ='consulta_modulos'),
    path('edt_mod/<int:pk>', vts_edt_mod.as_view(), name ='edt_mod'),
    path('eli_mod/<int:pk>', vts_del_mod.as_view(), name ='eli_mod'),
# Aplicaciones de módulo
    path('reg_app_mod/', vts_reg_app_mod.as_view(), name ='reg_app_mod'),
    path('cons_app_mod/', vts_ls_app_mod.as_view(), name ='consulta_aplicaciones_modulos'),
    path('edt_app_mod/<int:pk>', vts_edt_app_mod.as_view(), name ='edt_app_mod'),
    path('eli_app_mod/<int:pk>', vts_del_app_mod.as_view(), name ='eli_app_mod'),
# Grupos - Permisos
    # path('reg_grp/', vts_reg_group.as_view(), name ='reg_grp'),
    # path('cons_grp/', vts_ls_group.as_view(), name ='consulta_grupos'),
    # path('edt_grp/<int:pk>', vts_edt_group.as_view(), name ='edt_grp'),
    # path('eli_grp/<int:pk>', vts_del_group.as_view(), name ='eli_grp'),

# Roles
    path('reg_rol/', vts_reg_rol.as_view(), name ='reg_rol'),
    path('cons_rol/', vts_ls_rol.as_view(), name ='consulta_rol'),
    path('edt_rol/<int:pk>', vts_edt_rol.as_view(), name ='edt_rol'),
    path('eli_rol/<int:pk>', vts_del_rol.as_view(), name ='eli_rol'),
#funciones
    path('funciones/',funcionList.as_view(), name = 'funciones'),
    path('crearfun/',funcionCreate.as_view(), name = 'crearfun'),
    path('editarfun/<int:pk>/',funcionUpdate.as_view(), name='editarfun'),
    path('eliminarfun/<int:pk>/',funcionDelete.as_view(), name='eliminarfun')

]
