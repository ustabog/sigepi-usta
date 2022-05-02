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

# Roles
    path('reg_rol/', vts_reg_rol.as_view(), name ='reg_rol'),
    path('cons_rol/', vts_ls_rol.as_view(), name ='consulta_rol'),
    path('edt_rol/<int:pk>', vts_edt_rol.as_view(), name ='edt_rol'),
    path('eli_rol/<int:pk>', vts_del_rol.as_view(), name ='eli_rol'),

# Listado Aplicativo
    path('reg_lsapp/', vts_reg_list_app.as_view(), name ='reg_lsapp'),
    path('cons_lsapp/', vts_ls_list_app.as_view(), name ='consulta_lsapp'),
    path('edt_lsapp/<int:pk>', vts_edt_list_app.as_view(), name ='edt_lsapp'),
    path('eli_lsapp/<int:pk>', vts_del_list_app.as_view(), name ='eli_lsapp'),

# Extensiones de modulo
    path('reg_extmod/', vts_reg_ext_mod.as_view(), name ='reg_ext_mod'),
    path('cons_extmod/', vts_ls_ext_mod.as_view(), name ='consulta_ext_mod'),
    path('edt_extmod/<int:pk>', vts_edt_ext_mod.as_view(), name ='edt_ext_mod'),
    path('eli_extmod/<int:pk>', vts_del_ext_mod.as_view(), name ='eli_ext_mod'),

# Aplicaciones externas
    path('reg_extapp/', vts_reg_ext_app.as_view(), name ='reg_ext_app'),
    path('cons_extapp/', vts_ls_ext_app.as_view(), name ='consulta_ext_app'),
    path('edt_extapp/<int:pk>', vts_edt_ext_app.as_view(), name ='edt_ext_app'),
    path('eli_extapp/<int:pk>', vts_del_ext_app.as_view(), name ='eli_ext_app'),

]
