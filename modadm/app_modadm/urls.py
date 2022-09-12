from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
# from django.conf.urls import url
#from rest_framework.routers import DefaultRouter
from modadm.app_modadm.views import * 
from .models import *


urlpatterns = [
# direcciones del modulo admin
    path('',portada_adm().vst_raiz),
    path('inicio',portada_adm().vst_inicio, name = 'inicio_adm'),
    path('r_mod', portada_adm().vst_instal_mods, name='reg01_mod'),
    
# crud módulos
    path('reg_mod/', vts_reg_mod.as_view(), name ='reg_mod'),
    path('cons_mod/', vts_ls_mod.as_view(), name ='cons_mod'),
    path('cons_esp_mod/<int:pk>', vts_ver_mod.as_view(), name ='cons_esp_mod'),
    path('edt_mod/<int:pk>', vts_edt_mod.as_view(), name ='edt_mod'),
    path('eli_mod/<int:pk>', vts_elim_mod.as_view(), name ='eli_mod'),
# crud Aplicaciones
    path('reg_app/', vts_reg_app.as_view(), name ='reg_app'),
    path('cons_app/', vts_ls_app.as_view(), name ='cons_apps'),
     path('cons_esp_app/<int:pk>', vts_ver_app.as_view(), name ='cons_esp_app'),
    path('edt_app/<int:pk>', vts_edt_app.as_view(), name ='edt_app'),
    path('eli_app/<int:pk>', vts_elim_app.as_view(), name ='eli_app'),

# crud Roles
    path('reg_rol/', vts_reg_rol.as_view(), name ='reg_rol'),
    path('cons_rol/', vts_ls_rol.as_view(), name ='consulta_rol'),
    path('edt_rol/<int:pk>', vts_edt_rol.as_view(), name ='edt_rol'),
    path('eli_rol/<int:pk>', vts_elim_rol.as_view(), name ='eli_rol'),

# crud funciones
    path('reg_func/', vts_reg_rol.as_view(), name ='reg_func'),
    path('cons_func/', vts_ls_rol.as_view(), name ='cons_func'),
    path('edt_func/<int:pk>', vts_edt_rol.as_view(), name ='edt_func'),
    path('eli_func/<int:pk>', vts_elim_rol.as_view(), name ='eli_func'),

]
