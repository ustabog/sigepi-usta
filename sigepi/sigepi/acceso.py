#funciones principales de sigepi
#creado por maria Zambrano
#fecha 24/04/2021
from django.contrib.auth.models import User
from .form import *
from modadm.App_regusu.models import usu_inf_apps


class ls_rolusu():
# clase para retornar roles de usuario
    def sel_rol_usu(id_usu):
        #seleccion de roles por id de usuario inico sesion
        ls_rol_usu = usu_inf_apps.objects.get(id = id_usu)
        return ls_rol_usu




"""
    def __init__(self):
        #recuperar los datos de usurio
        self.usuario = User.objects.all()
        return self.usuario

    def mostrar_datos(self):
        pass
"""
