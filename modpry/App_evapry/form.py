from django import forms
from django.forms import ModelForm
from .models import *

class frm_reg_evapry(ModelForm):
    class Meta:
        model = eva_pry
        fields = (
            'eval',
            'nombre_eva',
            'desc_eva',
            'tipo_eva',
            'criterio',
            'lista_pry',
            'rubrica',
            'resultado',
            
        )
        labels = {
            'eval': 'Nombre del evaluador',
            'nombre_eva': 'Nombre de la evaluación del proyecto',
            'desc_eva': 'Descripción del proyecto',          
        }