# App de desarrollo de productos - Formularios para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 30 -10 -2022

from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_desprd.models import *
from modprd.app_regprd.form import DateInput
from modprd.app_certprd.form import RangeInput

#Formulario para la etapa de desarrollo de productos de productos

class form_etp(forms.ModelForm):
    class Meta:
        model = prd_etp
        fields = (
            'nom_etp',
            'desc_etp',
            'esc_trl',
            'fch_ini',
            'fch_fin'
        )
        label = {
            'nom_etp': 'Nombre de la etapa de desarrollo',
            'desc_etp': 'Descripción de la etapa de desarrollo',
            'esc_trl': 'Estado de maduracion',
            'fch_ini': 'Fecha de inicio de la etapa',
            'fch_fin' : 'Fecha de finalizacion de la etapa'
        }
        widgets = {
            'esc_trl': forms.RadioSelect(attrs={'class': 'myfieldclass'}),
            'fch_ini': DateInput() ,      
            'fch_fin' : DateInput()
        }