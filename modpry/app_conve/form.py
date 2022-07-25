# App de convenios de un proyecto de investigación - Formulario para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 25-07-2022

from django import forms
from modpry.app_conve.models import *

class frm_reg_conve(forms.ModelForm):
    #Clase del formulario para registrar un convenio
    class Meta:
        model = conve_pry
        fields = (
            'nombre_conv',
            'desc_conv',
            'fch_ini_conv',
            'fch_fin_conv',
            'tipo_recur_conv',
            'url_archv_conv',
            'dep_resp',
            'cont_conv',
        )
        labels = {
            'nombre_conv':'Nombre del convenio',
            'desc_conv':'Descripción del convenio',
            'fch_ini_conv':'Fecha de inicio del convenio',
            'fch_fin_conv':'Fecha de fin del convenio',
            'tipo_recur_conv':'Tipo de recurso del convenio',
            'url_archv_conv':'Url del archivo del convenio',
            'dep_resp':'Departamento responsable',
            'cont_conv':'Contacto del convenio',
        }
