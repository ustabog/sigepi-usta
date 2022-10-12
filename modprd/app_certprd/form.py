# App de certificacion de productos - Formularios para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_certprd.models import *
from modprd.app_regprd.form import DateInput

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
            'desc_med'
        )
        labels ={
            'nom_med': 'Nombre de la medicion',
            'num_conv': 'Numero de la convocatoria',
            'fch_ini': 'Fecha de inicio',
            'fch_fin': 'Fecha de finalizacion',
            'url_doc': 'Enlaces de documentacion',
            'url_resul': 'Resultados de la convocatoria',
            'est_med' : 'Estado de la Medicion',
            'desc_med' : 'Descripcion de la medicion'
        }
        widgets = {
            'fch_ini' : DateInput(),
            'fch_fin' : DateInput(),
        }

#Formulario para la certificacion de productos

class form_cert(forms.ModelForm):
    class Meta:
        model = prd_cert
        fields = (
            'id_prd',
            'est_cert',
            'id_soporte',
        )
        labels ={
            'id_prd': 'Producto a certificar',
            'est_cert': 'Estado de la certificacion',
            'id_soporte': 'Archivos de certificacion',

        }

class form_etp(forms.ModelForm):
    class Meta:
        model = prd_etp
        fields = (
            'nom_etp',
            'desc_etp',
            'id_prd',
            'esc_trl',

        )
        labels ={
            'nom_etp': 'Nombre de la etapa',
            'desc_etp': 'Descripción de la etapa',
            'id_prd': 'Producto relacionado',
            'esc_trl': 'Escala de maduracion tecnologica',
        }
        widgets = {

        }
    