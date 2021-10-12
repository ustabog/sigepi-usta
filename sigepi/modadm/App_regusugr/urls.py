from django.urls import path, include
from modadm.App_regusugr.views import *

urlpatterns = [
    #url para crear registro de igrupo

    path('crearusugrprb/', vts_reg_usugr.as_view(), name = 'crear_usugr'),
    path('conusugrmod/', vts_selc_usugr_mod.as_view(), name = 'ls_mod_usugr'),
    path('edit_usugr/<int:pk>/', vts_modf_usugr.as_view(), name = 'editar_usugr'),


]
