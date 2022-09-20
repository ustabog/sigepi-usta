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

#clase para la creación de un formulario de registro de información personal de usuario SIGEPI.

class frm_cons_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuarios institucionales en Django.
    class Meta:
        model = User
        fields ='__all__'
        exclude = ('user_permissions','groups','password',)

class frm_usu_inf_pers(forms.ModelForm):
    
    class Meta:
        #Metadatos de la clase
        model =  usu_inf_pers
        fields = '__all__'

#Formulario para el modelo de Discapacidad
class frm_discap(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = discap
        fields = '__all__'

#Formulario para el modelo de Información de Contacto usuario individual
class frm_usu_inf_contact(forms.ModelForm):
    #Información de contacto
    class Meta:
        model = usu_inf_contac
        fields = '__all__'

#Formulario para el modelo de redes sociales del usuario individual
class frm_usu_red_soc(forms.ModelForm):
    #Red Social
    class Meta:
        model = usu_red_soc
        fields = '__all__'

#Formulario para el modelo de formación académica del usuario individual
class frm_usu_form_acad(forms.ModelForm):
    #Formación académica
    class Meta:
        model = usu_form_acad
        fields = '__all__'

#Formulario para el modelo de Información de Contacto usuario individual
class frm_curs_dict(forms.ModelForm):
    #Formación académica
    class Meta:
        model = usu_form_acad
        fields = '__all__'