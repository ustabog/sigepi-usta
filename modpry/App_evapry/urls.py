from django.urls import path
from modpry.app_modpry.views import *
from modpry.app_evapry.views import *
from .models import *


urlpatterns = [ 
    path('inicio',vst_pry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    path('creaeva', vst_reg_evapry.as_view(), name = 'crear_eva'), #Crear evaluación de un proyecto
    path('cneva', vst_ls_evapry.as_view(), name = 'cn_evapry'), #Consultar evaluación de un proyecto
    path('crearub', vst_crear_rub.as_view(), name = 'crear_rub'), #Crear rúbrica
    path('cnrub', vst_ls_rub.as_view(), name = 'cn_rub'), #Consultar rúbrica
    path('creacrit', vst_crear_crit.as_view(), name = 'crear_crit'), #Crear criterios de la rúbrica
    path('crearango', vst_crear_rango.as_view(), name = 'crear_rango'), #Crear un rango de evaluación
    path('creaciclo', vst_crear_cicloeva.as_view(), name = 'crear_ciclo'), #Crear un ciclo de evaluación  
    path('crearesul', vst_crear_resul.as_view(), name = 'crear_resul'), #Crear un resultado de evaluación
    path('creatipo', vst_crear_tipoeva.as_view(), name = 'crear_tipo'), #Crear tipo de evaluación 
    path('creardefi', vst_crear_defi.as_view(), name = 'crear_defi'), #Crear definición, comentario, recomendación
]