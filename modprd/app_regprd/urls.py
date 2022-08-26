# Lista de urls para las vistas del registro de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 25 -08 -2022

from django.urls import path
from .models import *
from modprd.app_regprd.views import *

urlpatterns = [
    path('iniprd', ini_regprd().view_prd, name='ini_prd'), 
    path('crearprd/', vst_regprd.as_view(), name='crear_prd'), 
    path('creareqexs/', vst_regreqexist.as_view(), name='reqexs')
]