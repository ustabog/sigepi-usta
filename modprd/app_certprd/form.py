# App de certificacion de productos - Formularios para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_certprd.models import *

#Formulario para la medicion de productos

class form_med(forms.ModelForm):
    class Meta:
        model = prd_med
        fields = (
            'nom_med',
            'num_conv',
            'fch_ini',
            'fch_fin',
            'url_doc',
            'url_resul',
            'est_med',
            #'desc_med'
        )
        labels ={
            'nom_med': 'Nombre de la medicion',
            'num_conv': 'Numero de la convocatoria',
            'fch_ini': 'Fecha de inicio',
            'fch_fin': 'Fecha de finalizacion',
            'url_doc': 'Enlaces de documentacion',
            'url_resul': 'Resultados de la convocatoria',
            'est_med' : 'Estado de la Medicion',
            #'desc_med' : 'Descripcion de la medicion'
        }