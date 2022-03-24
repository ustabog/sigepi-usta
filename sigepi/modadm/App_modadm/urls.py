from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
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

#funciones
    path('funciones/',funcionList.as_view(), name = 'funciones'),
    path('crearfun/',funcionCreate.as_view(), name = 'crearfun'),
    path('editarfun/<int:pk>/',funcionUpdate.as_view(), name='editarfun'),
    path('eliminarfun/<int:pk>/',funcionDelete.as_view(), name='eliminarfun')

]
