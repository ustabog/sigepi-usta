#URLs para la configuración de la Interfaz de Usuario (IU) para SIGEPI
#creado por: Milton O. Castro Ch.
#fecha: 15-04-2022
#Versión: 0.1.04.22

from django.urls import path
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
#from rest_framework.routers import DefaultRouter
from modadm.app_conf.views import *
from .models import *

urlpatterns = [
# direcciones de la aplicación de configuración de IU SIGEPI
# agregar tema
# modificar tema
]
