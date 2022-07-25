from django import forms
from modpry.app_recur.models import *

class frm_reg_recur(forms.ModelForm):
    #Clase del formulario para registrar un recurso
    class Meta:
        model = recu_pry
        fields = (
            'nombre_rec',
            'desc_rec',
            'uti_rec',
            'tip_rec',
            'cont_rec',
            'num_cont',
        )
        labels = {
            'nombre_rec':'Nombre del recurso',
            'desc_rec': 'Descripción del recurso',
            'uti_rec':'Utilidad que se le dará al recurso',
            'cont_rec':'Contacto del recurso',
            'num_cont':'Número de contacto',
        }