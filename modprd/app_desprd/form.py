# App de desarrollo de productos - Formularios para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 30 -10 -2022

from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_desprd.models import *
from modprd.app_regprd.form import DateInput

#Formulario para la etapa de desarrollo de productos de productos

class form_etp(forms.ModelForm):
    class Meta:
        model = prd_etp
        fields = (
            'nom_etp',
            'desc_etp',
            'esc_trl'
        )
        label = {
            'nom_etp': 'Nombre de la etapa de desarrollo',
            'desc_etp': 'Descripción de la etapa de desarrollo',
            'esc_trl': 'Estado de maduracion'
        }