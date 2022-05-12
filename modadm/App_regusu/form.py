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
                 ]
        labels = {
                    'username' : 'Username',
                    'first_name' : 'Nombre',
                    'last_name' : 'Apellido',
                    'email' : 'Correo',
                }

class frm_reg_usu_pers(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = '__all__'

class frm_con_usu_inf_pers(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = [
                    'nuip',
                    'tipo_nuip',
                    'nal',
                    'fch_naci',
                    'mail',
                    'telefono',
                    'gene',
                    'ocup',
                    'dir',
                    'discap',
                    'tipo_discap',
                    'url_imag',
                    'zona_hor',
                 ]
        labels = {
                    'nuip' : 'Número de Identificación',
                    'tipo_nuip' : 'Tipo de Identificación',
                    'nal' : 'Nacionalidad',
                    'fch_naci' : 'Fecha de nacimiento' ,
                    'mail' : 'Correo',
                    'telefono' : 'Número telefónico',
                    'gene' : 'Género',
                    'ocup' : 'Ocupación',
                    'dir' : 'Dirección',
                    'discap' : 'Discapacidad',
                    'tipo_discap' : 'Tipo de discapacidad',
                    'url_imag' : 'URL Imágen',
                    'zona_hor' : 'Zona Horaria',
                }

class frm_con_discapacidad(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = discapacidad
        fields = '__all__'

class frm_con_info_contact(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = usu_inf_contac
        fields = [
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
                    'ind_nal' : 'Indicativo nacional',
                    'cel' : 'Celular',
                    'wa' : 'Whatsapp',
                    'email' : 'Correo',
                    'cod_post' : 'Código postal',
                    'ls_ha' : 'Horario de atención',
                    'web' : 'Página Web',
                    'dir_offi' : 'Dirección de Oficina',
                }

class frm_con_red_social(forms.ModelForm):
    #Red Social
    class Meta:
        model = red_soc
        fields = [
                    'nombre_red',
                    'usuario',
                    'url',
                    'uso',
                    'pub',
                 ]
        labels = {
                    'nombre_red' : 'Dirección de Oficina',
                    'usuario' : 'Direcció n de Oficina',
                    'url' : 'URL de página',
                    'uso' : 'Uso de la red',
                    'pub' : 'Acceso público de información',
                }

class frm_form_academica(forms.ModelForm):
    #Formación académica
    class Meta:
        model = form_acad
        fields = '__all__'

class frm_curs_dict(forms.ModelForm):
    #Formación académica
    class Meta:
        model = curs_dict
        fields = [
                    'id_cd',
                    'id_usu',
                    'instit',
                    'tipo_form',
                    'fch_ini',
                    'fch_fin',
                    'certif',
                    'nal',
                    'ciudad',
                    'mod',
                    'num_est',
                    'dur',
                    'nom_curs',
                    'mun_ciclos',
                    'url_prog',
                 ]
        labels = {
                    'id_cd' : 'Cursos Dictados',
                    'id_usu' : 'Usuario',
                    'instit' : 'Institución',
                    'tipo_form' : 'Tipo de Formación',
                    'fch_ini' : 'Fecha de Inicio',
                    'fch_fin' : 'Fecha de Finalización',
                    'certif' : 'Certificado',
                    'nal' : 'Nacionalidad',
                    'ciudad' : 'Ciudad',
                    'mod' : 'Modalidad',
                    'num_est' : 'Número de Estudiantes',
                    'dur' : 'Duración',
                    'nom_curs' : 'Nombre del Curso',
                    'mun_ciclos' : 'Número de Ciclos',
                    'url_prog' : 'URL del Sitio Web',
                }

class frm_empleos(forms.ModelForm):
    #Formación académica
    class Meta:
        model = empleos
        fields = [
                    'id_empl',
                    'id_usu',
                    'instit',
                    'nom_cargo',
                    'fch_ini',
                    'fch_fin',
                    'certif',
                    'nal',
                    'ciudad',
                    'tipo_contr',
                    'tit',
                    'menc',
                    'token',
                    'ret',
                 ]
        labels = {
                    'id_empl' : 'Empleado',
                    'id_usu' : 'Usuario',
                    'instit' : 'Institución',
                    'nom_cargo' : 'Nombre del Cargo',
                    'fch_ini' : 'Fecha de Inicio',
                    'fch_fin' : 'Fecha de Finalización',
                    'certif' : 'Certificado',
                    'nal' : 'Nacionalidad',
                    'ciudad' : 'Ciudad',
                    'tipo_contr' : 'Tipo de Contrato',
                    'tit' : 'Título Obtenido',
                    'menc' : 'Mención',
                    'token' : 'Token de Validación',
                    'ret' : 'Motivo del Retiro',
                }

class frm_habilidades(forms.ModelForm):
    #Formación académica
    class Meta:
        model = habilidades
        fields = fields = '__all__'

class frm_valid_hab(forms.ModelForm):
    #Formación académica
    class Meta:
        model = valid_hab
        fields = [
            'id_hab',
            'id_usu_val',
            'id_esc',
            'val',
        ]
        labels = {
            'id_hab' : 'Habilidades',
            'id_usu_val' : 'Usuario',
            'id_esc' : 'Escala de Validación',
            'val' : 'Valor en al Escala de Validación',
        }
