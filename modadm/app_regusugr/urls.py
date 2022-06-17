from django.urls import path, include
from modadm.app_regusugr.views import *

urlpatterns = [
    #url para crear registro de igrupo

    path('crearusugr/', vts_reg_usugr.as_view(), name = 'crear_usugr'),
    path('conusugrmod/', vts_selc_usugr_mod.as_view(), name = 'cons_usugr'),
    path('edit_usugr/<int:pk>/', vts_modf_usugr.as_view(), name = 'editar_usugr'),


]
