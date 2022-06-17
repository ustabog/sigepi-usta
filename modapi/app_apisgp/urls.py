from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from modapi.app_apisgp.views import *

#from administr.views import inicio, inicio2, inicioapp, crearrol, crearmod, editarRol, crearapp, editarMod,editarApp, eliminarMod,eliminarApp
#inicio nombre de la funcion importada e viw de adminityr
router = DefaultRouter()

urlpatterns = [
    #router.register(r'permisosj', permisoViewSet),
    #router.register(r'modelosj', moduloViewSet),
    #router.register(r'rolesj', rolViewSet),
    #router.register(r'appsj', appViewSet),
    #router.register(r'funcionesj', funcionViewSet),
    path('',vst_api().vst_inicio),
]
