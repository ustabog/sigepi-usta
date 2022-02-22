# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 25-04-2021
Última Modificación: 25-04-2021 08:02
Autor: Milton castro
colaboración: María Fernanza Zambrano
Hora:04:24

Formularios de Registro de usuarios (form.py)
Aplicación registro de usuarios
Módulo administrativo SIGEPI

"""

from django import forms
from modadm.App_modadm.models import *
from .models import *

#clase ubicado inicialmente en el modulo de consulta y App_cons
class frm_con_usu(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = usu
        fields = [
                    'username',
                    'first_name',
                    'last_name',
                    'email',
                    'password',
                 ]
        labels = {
                    'username' : 'Username',
                    'first_name' : 'Nombre',
                    'last_name' : 'Apellido',
                    'email' : 'Correo',
                    'password' : 'Contraseña',
                }

class frm_reg_usu_pers(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = [
            'id_usu',
            'tipo_nuip',
            'nuip',
            # 'nombres',
            # 'apelllidos',
            'mail',
            'telefono',
            'nal',
            'fch_naci',
            'gene',
            'ocup',
            'dir',
            # 'discap',
            # 'tipo_discap',
            # 'url_imag',
            # 'zona_hor'
        ]

        labels = {
            'id_usu' : 'Id',
            'tipo_nuip': 'Tipo de identificación',
            'nuip' : 'Número de identificación',
            # 'nombres': 'Nombres',
            # 'apelllidos':'Apellidos',
            'mail' : 'Email',
            'telefono' : 'Telefono',
            'nal' : 'Nacionalidad',
            'fch_naci' : 'Fecha de nacimiento',
            'gene' : 'Género',
            'ocup':'Ocupación',
            'dir' : 'Dirección',
            # 'discap' : 'Discapacidad',
            # 'tipo_discap':'Tipo de Disc.',
            # 'url_imag' : 'URL Imagen',
            # 'zona_hor' : 'Zona Horaria',
        }
        verbose_name = "DatosPersonales"
        verbose_name_plural = 'DatosPersonales'
