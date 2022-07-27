from django import forms
from modpry.app_regprgi.models import *

class frm_reg_prgi(forms.ModelForm):
    #Clase del formulario para registrar un programa de investigación
    class Meta:
        model = prgi_base
        fields = (
            'id_usu',
            'titulo_prg',
            'desc_prg',
            'nomb_archi',
            'url_archi',
            'num_inv',
            'prom_frm',
            'conv',
            'fch_ini_prg',
            'fch_fin_prg',
            'geo',
            'resu',
            'url_ap',
            'url_ao',
            'pobl_bnd',
            'pobl_bni',
            'obj_gen',
            'obj_esp',
        )
        labels = {
            'id_usu':'Propietario del programa de investigación',
            'titulo_prg':'Título del Programa de Investigación',
            'desc_prg':'Descripción del Programa de Investigación',
            'nomb_archi':'Nombre del archivo del del Programa de Investigación',
            'url_archi':'URL del archivo del Programa de Investigación',
            'num_inv':'Número de investigadores',
            'conv':'Convenio propuesto',
            'fch_ini_prg':'Fecha de inicio del programa de investigación',
            'fch_fin_prg':'Fecha de finalización del programa de investigación',
            'resu':'Resumen del programa de investigación',
            'url_ap':'URL del árbol de problemas',
            'url_ao':'URL del árbol de objetivos',
            'pobl_bnd':'Tamaño de la población beneficiaria directa del proyecto',
            'pobl_bni':'Tamaño de la población beneficiaria indirecta',
            'obj_gen':'Objetivo General',
            'obj_esp':'Objetivo Específico',
        }

