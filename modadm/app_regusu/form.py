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

from sqlite3 import Date
from django import forms
from django.contrib.auth.forms import UserCreationForm
from modadm.app_modadm.models import *
from .models import *

#clase para la creación de un formulario de registro de información personal de usuario SIGEPI.

class DateInput(forms.DateInput):
    input_type= 'date'

class TimeInput(forms.TimeInput):
    input_type= 'time'

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
        widgets = {
            'fch_naci':DateInput(),
            'id_usu':forms.HiddenInput()
        }
       
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

#Formulario para el modelo de Información de los cursos dictados por el usuario individual
class frm_curs_dict(forms.ModelForm):
    #Formación académica
    class Meta:
        model = usu_curs_dict
        fields = '__all__'

#Formulario para el modelo de Información de Habilidades del usuario individual
class frm_usu_habil(forms.ModelForm):
    #Formación académica
    class Meta:
        model = habil
        fields = '__all__'

#Formulario para el modelo de Información de Habilidades del usuario individual
class frm_usu_form_empl(forms.ModelForm):
    #Formación académica
    class Meta:
        model = usu_empleo
        fields = '__all__'

#Formulario para el modelo de Disponibilidad del usuario individual
class frm_usu_calendario(forms.ModelForm):
    #Formación académica
    class Meta:
        model = usu_inf_calen
        fields = '__all__'
        widgets = {
            'de':TimeInput(),
            'a':TimeInput(),
            'id_usu':forms.HiddenInput()
        }
