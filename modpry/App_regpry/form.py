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
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'prop_pry',
        )
        labels = {
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'prop_pry' : 'Propietario del proyecto',
        }

'''
class frm_reg_pry(forms.ModelForm):
    #Clase para el formulario del registro de proyecto
    class Meta:
        model = pry_base
        fields = (
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'prop_pry',
        )
        labels = {
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'prop_pry' : 'Propietario del proyecto',
        }
'''