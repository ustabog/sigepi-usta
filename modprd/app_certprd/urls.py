# App de certificacion de productos - URL'S para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.urls import path
from .models import *
from modprd.app_certprd.views import *

#urls para la app de mediciones y certificaciones de productos

urlpatterns = [
    path('crearmed/', vst_regprd.as_view(), name='crear_med')# url para la interfaz de creacion de mediciones
]
