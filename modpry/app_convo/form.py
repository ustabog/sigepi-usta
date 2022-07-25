# App de convocatorias para un proyecto - Formulario para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 25-07-2022

from django import forms
from modpry.app_convo.models import *

class frm_reg_convo(forms.ModelForm):
    #Clase del formulario para registrar una convocatoria
    class Meta:
        model = convo_pry
        fields = (
            'nombre_convo',
            'desc_convo',
            'fch_ini_convo',
            'fch_fin_convo',

        )
        labels = {
            'nombre_convo':'Nombre de la convocatoria',
            'desc_convo':'Descripción de la convocatoria',
            'fch_ini_convo':'Fecha de inicio de la convocatoria',
            'fch_fin_convo':'Fecha de fin de la convocatoria',

        }

