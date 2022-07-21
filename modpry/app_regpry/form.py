from django import forms
from django.forms import ModelForm
from django import forms
from modpry.app_modpry.models import *
from .models import *

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

class frm_inf_pry(forms.ModelForm):
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

class frm_inf_geo(forms.ModelForm):
#Clase que permite diligenciar la información geográfica del proyecto
    class Meta:
        model = inf_geo_pry
        fields = (
            'dat_dep',
            'municipio',
            'ciudad',
        )
        labels = {
            'municipio' : 'Municipio',
            'ciudad' : 'Ciudad',
        }

class frm_even_pry(forms.ModelForm):
#Clase que permite diligenciar la información de los eventos del proyecto
    class Meta:
        model = even_pry
        fields = (
            'nomb_eve',
            'desc_eve',
            'fch_eve',
            'hora_eve',
            'lugar_eve',
            'dir_eve',
            'mod_eve',
            'inf_adi',
        )
        labels = {
            'nomb_eve' : 'Nombre del evento:',
            'desc_eve' : 'Descripción del evento',
            'fch_eve' : 'Fecha del evento',
            'hora_eve' : 'Hora del evento',
            'lugar_eve' : 'Lugar del evento',
            'dir_eve' : 'Dirección del evento',
            'inf_adi' : 'Información adicional',
        }

class frm_lin_inv(forms.ModelForm):
#Clase que permite diligenciar la información de la línea de investigación de un proyecto
    class Meta:
        model = lin_inv
        fields = (
            'nomb_ln_inv',
            'desc_ln_inv',
            'fch_ini_ln',
            'fch_fin_ln',
            'fch_mod_ln',
            #'res_ln_inv',
            #'invs_ln_inv',
            'cmp_dis_ocde',
            'cmp_dis_minc',
            'est_ln_inv',
        )
        labels = {
            'nomb_ln_inv' : 'Nombre de la línea de investigación',
            'desc_ln_inv' : 'Descripción de la línea de investigación',
            'fch_ini_ln' : 'Fecha de inicio de la línea de investigación',
            'fch_fin_ln' : 'Fecha de finalización de la línea de investigación',
            'fch_mod_ln' : 'Fecha de modificiación de la línea de investigación',
            #'res_ln_inv' : 'Responsable de la línea de investigación',
            #'invs_ln_inv' : 'Investigadores de la línea de investigación',
        }
