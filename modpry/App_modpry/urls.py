from django.urls import path
from django.contrib.auth.views import *
#from rest_framework.routers import DefaultRouter
from modpry.App_regpry.views import *
from modpry.App_regpry.urls import *
from modpry.App_modpry.views import *
from .models import *

urlpatterns = [ 
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cons_pry/', vts_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    #path('elipry/<int_pk>',vts_reg_pry.as_view(), name = 'elim_pry'), #Borrar proyecto
    #path('elimpry/<pk>/',vst_pry.vts_eli_pry, name = 'elim_pry'),
    path(include('modcons.App_regpry.urls')),
]

