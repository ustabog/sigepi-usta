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
from django.contrib.auth.forms import UserCreationForm
from modadm.App_modadm.models import *
from .models import *

class frm_reg_usu(UserCreationForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = usu
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
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

class frm_con_info_contact(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = usu_inf_contac
        fields = [
                    'id_usu',
                    'ind_nal',
                    'cel',
                    'wa',
                    'email',
                    'cod_post',
                    'ls_ha',
                    'web',
                    'dir_offi',
                 ]
        labels = {
                    'id_usu' : 'ID',
                    'ind_nal' : 'Indicador Nacional',
                    'cel' : 'Celular',
                    'wa' : 'WhatsApp',
                    'email' : 'Correo',
                    'cod_post' : 'Código Postal',
                    'ls_ha' : 'Horario Atención',
                    'web' : 'Página Web',
                    'dir_offi' : 'Dirección Oficina',
                }

class frm_con_red_social(forms.ModelForm):
    #Red Social
    class Meta:
        model = red_soc
        fields = [
                    'id_red',
                    'nombre_red',
                    'usuario',
                    'url',
                    'uso',
                    'pub',
                 ]
        labels = {
                    'id_red' : 'ID',
                    'nombre_red' : 'Nombre Red',
                    'usuario' : 'Usuario',
                    'url' : 'URL',
                    'uso' : 'Uso',
                    'pub' : 'Acceso público',
                }

class frm_form_academica(forms.ModelForm):
    #Formación académica
    class Meta:
        model = form_acad
        fields = [
                    'id_fa',
                    'id_usu',
                    'instit',
                    'tipo_form',
                    'fch_ini',
                    'fch_fin',
                    'certif',
                    'nal',
                    'ciudad',
                    'mod',
                    'tit',
                    'menc',
                    'token',
                 ]
        labels = {
                    'id_fa' : 'Id',
                    'id_usu' : 'Id usuario',
                    'instit' : 'Institución',
                    'tipo_form' : 'Tipo de formación',
                    'fch_ini' : 'Fecha inicio',
                    'fch_fin' : 'Fecha finalización',
                    'certif' : 'Certificado',
                    'nal' : 'Pais',
                    'ciudad' : 'Ciudad',
                    'mod' : 'Modalidad',
                    'tit' : 'Título',
                    'menc' : 'Mención',
                    'token' : 'Validación',
                }

# class frm_curs_dict(forms.ModelForm):
#     #Formación académica
#     class Meta:
#         model = form_acad
#         fields = [
#                     'id_cd',
#                     'id_usu',
#                     'instit',
#                     'tipo_form',
#                     'fch_ini',
#                     'fch_fin',
#                     'certif',
#                     'nal',
#                     'ciudad',
#                     'mod',
#                     'num_est',
#                     'dur',
#                     'nom_curs',
#                     'mun_ciclos',
#                     'url_prog',
#                  ]
#         labels = {
#                     'id_cd' : 'ID',
#                     'id_usu' : 'ID usu',
#                     'instit' : 'Nombre Institución',
#                     'tipo_form' : 'Tipo de formación',
#                     'fch_ini' : 'Fecha inicio',
#                     'fch_fin' : 'Fecha finalización',
#                     'certif' : 'Certificado',
#                     'nal' : 'Pais',
#                     'ciudad' : 'Ciudad',
#                     'mod' : 'Modalidad',
#                     'num_est' : 'Número de estudiantes',
#                     'dur' : 'Duración',
#                     'nom_curs' : 'Nombre curso',
#                     'mun_ciclos' : 'Número de ciclos',
#                     'url_prog' : 'URL Programa',
#                 }