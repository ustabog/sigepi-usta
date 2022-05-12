from django import forms
from django.forms import ModelForm
from django import forms
from modpry.App_modpry.models import *
from .models import *

class frm_reg_pry(ModelForm):
    class Meta:
        model = pry_base
        fields = '__all__'

class frm_con_pry(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = pry_base
        fields = (
            'cod_pry',
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'prop_pry',
            'est_pry',
        )
        labels = {
            'cod_pry' : 'Código del proyecto',
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'prop_pry' : 'Propietario del proyecto',
            'est_pry' : 'Estado del proyecto',
        }

