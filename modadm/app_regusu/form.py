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
from modadm.app_modadm.models import *
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
        fields = '__all__'

class frm_con_usu_inf_pers(forms.ModelForm):
    #clase para la creación de un formulario de registro de información personal de usuario SIGEPI.
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = '__all__'

class frm_con_discapacidad(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = discapacidad
        fields = '__all__'

class frm_con_info_contact(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = usu_inf_contac
        fields = '__all__'

class frm_con_red_social(forms.ModelForm):
    #Red Social
    class Meta:
        model = red_soc
        fields = '__all__'

class frm_form_academica(forms.ModelForm):
    #Formación académica
    class Meta:
        model = form_acad
        fields = '__all__'

class frm_curs_dict(forms.ModelForm):
    #Formación académica
    class Meta:
        model = form_acad
        fields = '__all__'