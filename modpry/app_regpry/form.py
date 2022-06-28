from django import forms
from django.forms import ModelForm
from django import forms
from modpry.app_modpry.models import *
from .models import *

class frm_reg_pry(ModelForm):
    class Meta:
        model = pry_base
        fields = (
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'id_usu',
            'est_pry',
        )
        labels = {
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'id_usu' : 'Propietario del proyecto',
            'est_pry' : 'Estado del proyecto',
        }

class frm_con_pry(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = pry_base
        fields = (
            'nombre_pry',
            'desc_pry',
            'tipo_pry',
            'id_usu',
        )
        labels = {
            'nombre_pry' : 'Nombre del proyecto',
            'desc_pry': 'Descripción del proyecto',
            'tipo_pry' : 'Tipo de proyecto',
            'id_usu' : 'Propietario del proyecto',
        }

class frm_info_pry(forms.ModelForm):
    #Clase que permite diligenciar la información adicional del proyecto
    class Meta:
        model = inf_pry
        fields = (
            'nombre_archivo',
            'url_archivo',
            'dat_dep',
            'url_ap',
            'url_ao',
            'obj_gen',
            'obj_esp',
        )
        labels = {
            'nombre_archivo' : 'Nombre del archivo',
            'url_archivo' : 'URL del archivo',
            'url_ap' : 'URL del árbol de problemas',
            'url_ao' : 'URL del árbol de objetivos',
            'obj_gen' : 'Objetivo general',
            'obj_esp' : 'Objetivos específico',
        }

