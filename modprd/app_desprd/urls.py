# Lista de urls para las vistas del desarrollo de producto - URL's para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 30 -10 -2022


from django.urls import path
from .models import *
from modprd.app_desprd.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [

    #Url's Para el registro de producto

    path('mis_productos/', login_required(vst_list_des.as_view()), name='listar_etp'), # urlpara la consulta de productos
    path('crear_etapa/<int:id>', login_required(vst_reg_etp), name='registrar_etp'), # url para el registro de etapa de productos
    path('desarrollo/<int:pk>', login_required(vst_cons_etp.as_view()), name='consultar_etp'), # url para el la consulta de etapa de productos
    path('Modificar_etapa/<int:pk>', login_required(vst_upd_etp.as_view()), name='editar_etp'), # url para la actualizacion de etapa de productos

]