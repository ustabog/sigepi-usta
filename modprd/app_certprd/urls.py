# App de certificacion de productos - URL'S para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022
#Edicion 30/10/2022

from django.urls import path
from .models import *
from modprd.app_certprd.views import *
from django.contrib.auth.decorators import login_required

#urls para la app de mediciones y certificaciones de productos

urlpatterns = [
    #Urls del CRUD de mediciones de productos
    path('crearmed/<int:pk>', login_required(vst_reg_med.as_view()), name='crear_med'),# url para la interfaz de creacion de mediciones
    path('listmed/', login_required(vst_list_med.as_view()), name='listar_med'),# url para la interfaz de listado de mediciones
    path('consmed/<int:pk>', login_required(vst_cons_med.as_view()), name='consultar_med'),# url para la interfaz de consulta de mediciones
    path('updmed/<int:pk>', login_required(vst_upd_med.as_view()), name='editar_med'),# url para la interfaz de actualizacion de mediciones
    path('delmed/<int:pk>', login_required(vst_del_med.as_view()), name='eliminar_med'),# url para la interfaz de eliminacion de mediciones
    path('archimed/<int:pk>', login_required(vst_archi_med.as_view()), name='archivar_med'),# url para la interfaz de eliminacion de mediciones
    path('searchmed/<int:pk>', login_required(vst_search_med), name='buscar_med'),# url para la interfaz de eliminacion de mediciones


    #Urls del CRUD de cerficacion de productos
    path('crearcert/<int:pk>', login_required(vst_reg_cert.as_view()), name='crear_cert'),# url para la interfaz de creacion de certificaciones
    path('conscert/<int:pk>', login_required(vst_cons_cert.as_view()), name='consultar_cert'),# url para la interfaz de consulta de certificaciones
    path('updcert/<int:pk>', login_required(vst_upd_cert.as_view()), name='editar_cert'),# url para la interfaz de actualizacion de certificaciones
    path('delcert/<int:pk>', login_required(vst_del_cert.as_view()), name='eliminar_cert'),# url para la interfaz de eliminacion de certificaciones
    path('crearsupp/<int:id>', login_required(vst_reg_supp), name='crear_soporte'),# url para la interfaz de adicion de soportes
]
