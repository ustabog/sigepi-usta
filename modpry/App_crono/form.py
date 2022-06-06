from django.forms import ModelForm
from django import forms
from modpry.App_modpry.models import *
from modpry.App_crono.models import *

#---------------------------Formulario para crear un nuevo cronograma para un proyecto--------------------------
class frm_crea_crono(ModelForm):
    class Meta:
        model = crono_pry
        fields = (
            'resp_pry',
            #'id_pry',
            'nomb_crono',
            'desc_crono',
            'fch_ini_pry',
            'fch_fin_pry',
        )
        labels = {
            'resp_pry' : 'Responsable del cronograma', 
            #'id_pry' : 'Identificador del proyecto',
            'nomb_crono' : 'Nombre del cronograma',
            'desc_crono' : 'Descripción del cronograma',
            'fch_ini_pry' : 'Fecha de inicio del proyecto',
            'fch_fin_pry' : 'Fecha de finalización del proyecto',
        }

#---------------------------Formulario para crear una nueva etapa dentro de un cronograma --------------------------
class frm_crea_etapa(ModelForm):
    class Meta:
        model = etapa
        fields = (
            'nombre_eta',
            'desc_eta',
            'fch_ini_eta',
            'fch_fin_eta',
        )
        labels = {
            'nombre_eta' : 'Nombre de la etapa',
            'desc_eta' : 'Descripción de la etapa',
            'fch_ini_eta' : 'Fecha de inicio de la etapa',
            'fch_fin_eta' : 'Fecha de finalización de la etapa',
        }

#---------------------------Formulario para crear una nueva fase dentro de una etapa --------------------------
class frm_crea_fase(ModelForm):
    class Meta:
        model = fase
        fields = (
            'nombre_fase',
            'desc_fase',
            'fch_ini_fase',
            'fch_fin_fase',
        )
        labels = {
            'nombre_fase' : 'Nombre de la fase',
            'desc_fase' : 'Descripción de la fase',
            'fch_ini_fase' : 'Fecha de inicio de la fase',
            'fch_fin_fase' : 'Fecha de finalización de la fase',
        }

#---------------------------Formulario para crear un nuevo proceso dentro de una fase --------------------------
class frm_crea_proc(ModelForm):
    class Meta:
        model = proceso
        fields = (
            'nombre_proc',
            'desc_proc',
            'fch_ini_proc',
            'fch_fin_proc',
        )
        labels = {
            'nombre_proc' : 'Nombre del proceso',
            'desc_proc' : 'Descripción del proceso',
            'fch_ini_proc' : 'Fecha de inicio del proceso',
            'fch_fin_proc' : 'Fecha de finalización del proceso',
        }

#---------------------------Formulario para crear una nueva tarea dentro de un proceso --------------------------
class frm_crea_tarea(ModelForm):
    class Meta:
        model = tarea
        fields = (
            'id_usu',
            'nombre_tarea',
            'desc_tarea',
            'fch_ini_tarea',
            'fch_fin_tarea',
            'url_tar',
            #'ima_tar',
            #'docu_tar',
        )
        labels = {
            'id_usu': 'Responsable de la tarea',
            'nombre_tarea' : 'Nombre de la tarea',
            'desc_tarea' : 'Descripción de la tarea',
            'fch_ini_tarea' : 'Fecha de inicio de la tarea',
            'fch_fin_tarea' : 'Fecha de finalización de la tarea',
            'url_tar' : 'URL de la evidencia de la tarea',
            #'ima_tar':'Imagen de la evidencia de la tarea',
            #'docu_tar' : 'Documento de la evidencia de la tarea',        
        }

#---------------------------Formulario para crear una nueva actividad dentro de una tarea --------------------------
class frm_crea_acti(ModelForm):
    class Meta:
        model = acti
        fields = (
            'id_usu',
            'nombre_acti',
            'desc_acti',
            'fch_ini_acti',
            'fch_fin_acti',
            'url_acti',
            #'ima_acti',
            #'docu_acti',
        )
        labels = {
            'id_usu' : 'Responsable de la actividad',
            'nombre_acti' : 'Nombre de la actividad',
            'desc_acti' : 'Descripción de la actividad',
            'fch_ini_acti' : 'Fecha de inicio de la actividad',
            'fch_fin_acti' : 'Fecha de finalización de la actividad',
            'url_acti' : 'URL de la evidencia de la actividad',
            #'ima_acti':'Imagen de la evidencia de la actividad',
            #'docu_acti' : 'Documento de la evidencia de la actividad',        
        }