from django import forms
from django.forms import ModelForm
from django import forms
from modpry.App_modpry.models import *
from .models import *

class frm_reg_pry(ModelForm):
    class Meta:
        model = pry_base
        fields = (
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'prop_pry',
            'est_pry',
        )
        labels = {
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'prop_pry' : 'Propietario del proyecto',
            'est_pry' : 'Estado del proyecto',
        }

class frm_reg_pry_grp(ModelForm):
    class Meta:
        model = pry_grp
        fields = (
            'nombre_pry_grp',
            'desc_pry_grp',
            'tipo_pry_grp',
            'prop_pry_grp',
            'est_pry_grp',
        )
        labels = {
            'nombre_pry_grp' : 'Nombre del proyecto',
            'desc_pry_grp': 'Descripción del proyecto',
            'tipo_pry_grp' : 'Tipo de proyecto',
            'prop_pry_grp' : 'Propietario del proyecto',
            'est_pry_grp' : 'Estado del proyecto',
        }

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