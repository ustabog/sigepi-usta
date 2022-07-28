# App de diseño un proyecto de investigación - Formulario para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 28 -07-2022

from django import forms
from modpry.app_disinv.models import *
from .models import *

class frm_reg_dispry(forms.ModelForm):
    #Clase que contiene el formulario para el registro de un diseño de investigación
    class Meta:
        model = dis_pry
        fields = (
            'id_usu',
            'nomb_dis',
            'tipo_inv',
            'delim_tem',
            'fch_ini_dis',
            'fch_fin_dis',
            'arb_pro',
            'arb_obj',
        )
        labels = {
            'id_usu':'Encargado del diseño de un proyecto de investigación',
            'nomb_dis':'Nombre del diseño del proyecto de investigación',
            'delim_tem':'Delimitación temática',
            'fch_ini_dis':'Fecha de inicio del diseño',
            'fch_fin_dis':'Fecha de finalización del diseño',
        }

class frm_reg_tema(forms.ModelForm):
    #Clase que contiene el formulario para el registro de un tema de investigación
    class Meta:
        model = tema
        fields = (
            'tema',
            'desc_categ',
            'categ',
        )
        labels = {
            'tema':'Tema',
            'desc_categ':'Descripción del tema',
            'categ':'Palabras claves',
        }

class frm_reg_defi(forms.ModelForm):
    #Clase que contiene el formulario para el registro de una definción de investigación
    class Meta:
        model = defin
        fields = (
            'ver',
            'tipo',
            'fch_reg',
            'vers1',
            'vers2',
            'vers3',
            'vers4',
            'vers5',
            'fch_mod',

        )
        labels = {
            'ver':'Versión',
            'tipo':'Tipo',
            'fch_reg':'Fecha de registro',
            'vers1':'Versión 1',
            'vers2':'Versión 2',
            'vers3':'Versión 3',
            'vers4':'Versión 4',
            'vers5':'Versión 5',
            'fch_mod':'Fecha de modificación',
        }

class frm_reg_ap(forms.ModelForm):
    #Clase que contiene el formulario para el registro de un árbol de problemas de investigación
    class Meta:
        model = arb_pro
        fields = (
            'tit_ap',
            'nomb_arc',
            'url_arc',
        )
        labels = {
            'tit_ap':'Título del árbol de problemas',
            'nomb_arc':'Nombre del archivo del árbol de problemas ',
            'url_arc':'URL del archivo',
        }

class frm_reg_ao(forms.ModelForm):
    #Clase que contiene el formulario para el registro de un árbol de objetivos de investigación
    class Meta:
        model = arb_obj
        fields = (
            'tit_ao',
            'nomb_arc',
            'url_arc',
        )
        labels = {
            'tit_ap':'Título del árbol de objetivos',
            'nomb_arc':'Nombre del archivo del árbol de objetivos',
            'url_arc':'URL del archivo',
        }

class frm_reg_causa(forms.ModelForm):
    #Clase que contiene el formulario para el registro de causas
    class Meta:
        model = causa
        fields = (
            'nomb_cau',
            'desc_cau',
            'nivel_cau',
            'defs',
        )
        labels = {
            'nomb_cau':'Nombre de la causa',
            'desc_cau':'Descripción de la causa',
            'nivel_cau':'Nivel de la causa',
        }

class frm_reg_efecto(forms.ModelForm):
    #Clase que contiene el formulario para el registro de efectos 
    class Meta:
        model = efecto
        fields = (
            'nomb_efe',
            'desc_efe',
            'nivel_efe',
            'defs',
        )
        labels = {
            'nomb_cau':'Nombre del efecto',
            'desc_cau':'Descripción del efecto',
            'nivel_cau':'Nivel del efecto',
        }

class frm_reg_medio(forms.ModelForm):
    #Clase que contiene el formulario para el registro de medios
    class Meta:
        model = medio
        fields = (
            'nomb_med',
            'desc_med',
            'nivel_med',
            'defs',
        )
        labels = {
            'nomb_cau':'Nombre del medio',
            'desc_cau':'Descripción del medio',
            'nivel_cau':'Nivel del medio',
        }

class frm_reg_fin(forms.ModelForm):
    #Clase que contiene el formulario para el registro de fines
    class Meta:
        model = fin
        fields = (
            'nomb_fin',
            'desc_fin',
            'nivel_fin',
            'defs',
        )
        labels = {
            'nomb_cau':'Nombre del fin',
            'desc_cau':'Descripción del fin',
            'nivel_cau':'Nivel del fin',
        }