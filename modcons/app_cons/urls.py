#URLs para la configuración de la Interfaz de Usuario (IU) para SIGEPI
#creado por: Milton O. Castro Ch.
#fecha: 16-04-2022
#Versión: 0.1.04.22

from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
#from rest_framework.routers import DefaultRouter
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView

from modcons.app_cons.views import *

urlpatterns = [
    path('cons',consulta().vst_cons_inv, name = 'cons_gen'),
]
