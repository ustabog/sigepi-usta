import imp
from django.forms import ModelForm
from .models import *
from modpry.app_modpry.models import *
from modpry.app_evapry.models import *

class frm_evapry(ModelForm):
#Formulario para crear la evaluación de proyectos base
    class Meta:
        model = eva_pry
        fields = (
            'nomb_eva',
            'eval',
            'desc_eva',
            
        )
        labels = {
            'nomb_eva': 'Nombre de la evaluación del proyecto',
            'eval': 'Nombre del evaluador',
            'desc_eva': 'Descripción de la evaluación del proyecto',          
        }

class frm_criterio(ModelForm):
#Formulario para crear un criterio 
    class Meta:
        model = criterio
        fields = (
            'nomb_crit', 
            'desc_crit',
            'nombre_rango',
            'url_doc',
        )
        labels = {
            'nomb_crit':'Nombre del criterio', 
            'desc_crit' : 'Descripción del criterio',
            'nombre_rango' : 'Rango de evaluación',
            'url_doc' : 'URL del documento',    
        }

class frm_rubrica(ModelForm):
#Formulario para crear una rúbrica de evaluación
    class Meta:
        model = rubrica
        fields = (
            'nomb_rub', 
            'desc_rub',
            'arb_crit',
        )
        labels = {
            'nomb_rub' : 'Nombre de la rúbica de evaluación', 
            'desc_rub' : 'Descripción de la rúbrica de evaluación',
            'arb_crit' : 'Árbol de criterios',
        }

class frm_rangoeva(ModelForm):
#Formulario para crear un rango de evaluación
    class Meta:
        model = rango_eva
        fields = (
            'nombre_rango',
            'c_eva_pry',
            'valor_ini',
            'valor_fin',
        )
        labels = {
            'nombre_rango': 'Nombre del rango de evaluación',
            'valor_ini' : 'Valor inicial de la evaluación',
            'valor_fin' : 'Valor final de la evaluación',
        }

class frm_cicloeva(ModelForm):
#Formulario para crear un ciclo de evaluación
    class Meta:
        model = ciclo_eva
        fields = (
            'fch_ini',
            'fch_fin',
            'estado_eva',
        )
        labels = {
            'fch_ini' : 'Fecha de inicio de la evaluación del proyecto',
            'fch_fin' : 'Fecha de finalización de la evaluación del proyecto',
            'estado_eva' : 'Estado de la evaluación',
        }

class frm_resultado(ModelForm):
#Formulario para crear un resultado
    class Meta:
        model = resultado
        fields = (
            'valor_total',  
            'ls_comen', 
            'estado_eva',
        )
        labels ={
            'valor_total' : 'Resultado total', 
        }

class frm_tipoeva(ModelForm):
#Formulario para crear un tipo de evaluación de proyectos
    class Meta:
        model = tipo_eva
        fields = (
            'tipo_eva', 
            'desc_eva',
        )
        labels = {
            'tipo_eva' : 'Tipo de evaluación', 
            'desc_eva' : 'Descripción del tipo de evaluación',
        }

class frm_defi(ModelForm):
#Formulario para crear definiciones, comentarios, recomendaciones, etc.
    class Meta:
        model = defi
        fields = (
            'id_usu',
            'tipo_def',
            'vers',
            'fch_reg',
            'vers1',
            'vers2',
            'vers3',
            'vers4',
            'vers5',
            'fch_mod',
        )
        labels = {
            'id_usu' : 'Responsable',
            'tipo_def' : 'Tipo', 
            'vers' : 'Versión',
            'fch_reg' : 'Fecha de registro',
            'vers1' : 'Versión 1',
            'vers2' : 'Versión 2',
            'vers3' : 'Versión 3',
            'vers4' : 'Versión 4',
            'vers5' : 'Versión 5',
            'fch_mod' : 'Fecha de modificación',
        }
