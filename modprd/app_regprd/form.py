# App de registro de un producto - Formulario para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 23 -08-2022

from cProfile import label
from django import forms
from django.forms import ModelForm
from django import forms
from .models import *
from modprd.app_regprd.models import *

#Formulario para el registro de un producto

# class form_prd(forms.ModelForm):
#     class Meta:
#         model = prd_base
#         fields = (
#             'nom_prd',
#             'fech_entrega',
#             'ids_pry',
#             'ids_usu',
#             'id_tipo_prd_minc'
#         )
#         labels ={
#             'nom_prd': 'Nombre del producto',
#             'fech_entrega': 'Fecha de entrega estimada',
#             'ids_pry': 'Proyecto de referencia',
#             'ids_usu': 'Propietario del producto',
#             'id_tipo_prd_minc': 'Tipo de producto'
#         }

#---------------------------FORMULARIOS PARA EL REGISTRO DE PRODUCTOS --------------------------------
#Formulario para el registro de un producto

class DateInput(forms.DateInput):
    input_type = 'date'

class label_pry(forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return "%s" % obj.nombre_pry

class label_tipo_prd (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.nom_tipo
        
class label_req_cal (forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.desc_reqcal

class label_req_exist (forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.nom_reqexs

class label_categ (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.nom_categ

class label_campo (forms.ModelMultipleChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.nom_campo

class label_plt (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.nom_plt

class form_reg_prd(forms.ModelForm):

    class Meta:
        model=prd_base
        fields = (
            'nom_prd',
            'ids_usu',
            'ids_pry',
            'id_tipo_prd_minc',
            'fech_entrega',
        )
        labels ={
            'nom_prd': 'Nombre del producto',
            'fech_entrega': 'Fecha de entrega estimada',
            'ids_usu': 'Propietario del producto',
        }
        widgets = {
            'fech_entrega': DateInput(),
        }
    ids_pry = label_pry(
        queryset=pry_base.objects.all(),
        label='Proyectos de los cuales se basa',
    )
    id_tipo_prd_minc = label_tipo_prd(
        queryset=prd_tipo.objects.all(),
        label='Tipo de producto'
    )

#Formulario para el registro  de los requerimientos de existencia 

class form_req_exist(forms.ModelForm):
    class Meta:
        model = prd_req_Exist
        fields = (
            'nom_reqexs',
            'desc_reqexs',
        )
        labels ={
            'nom_reqexs': 'Nombre del requerimiento',
            'desc_reqexs': 'Descripcion del requerimiento',
        }

#Formulario para el registro  de los requerimientos de calidad

class form_req_cal(forms.ModelForm):
    class Meta:
        model = prd_req_cal
        fields = (
            'desc_reqcal',
        )
        labels ={
            'desc_reqcal': 'Descripcion del requerimiento',
        }

class form_categ(forms.ModelForm):
    class Meta:
        model = prd_categ
        fields = (
            'nom_categ',
            'peso_rel',
            'id_reqcal',
        )
        labels ={
            'nom_categ': 'Nombre de la categoria',
            'peso_rel': 'Peso relativo de la categoria',
        }
    
    id_reqcal = label_req_cal(
        queryset= prd_req_cal.objects.all(),
        label= 'Requsitos de calidad de la categoria '
    )

class form_tipo(forms.ModelForm):
    class Meta:
        model = prd_tipo
        fields = (
            'nom_tipo',
            'id_reqexist',
            'id_categ',
            'vent_obs',
            'id_plt_desc',
            'tipo_cal',
            
        )
        labels ={
            'nom_tipo': 'Nombre del tipo de producto',
            'vent_obs': 'Ventana de observacion en dias',
            'tipo_cal': 'Tipologia a utilizar',
        }

    id_reqexist = label_req_exist(
        queryset=prd_req_Exist.objects.all(),
        label='Requerimientos de existencia'
    )

    id_categ= label_categ(
        queryset=prd_categ.objects.all(),
        label='Categoria'
    )

    id_plt_desc= label_plt(
        queryset=prd_plt_desc.objects.all(),
        label='Plantilla a utilizar'
    )

class form_campo(forms.ModelForm):
    class Meta:
        model = campo
        fields = (
            'nom_campo',
            'rango',
            'Formato',
            'valor_def',
            'desc_campo',
        )
        labels ={
            'nom_campo': 'Nombre del campo',
            'rango': 'Rango del campo',
            'Formato': 'Formato a utilizar',
            'valor_def': "Valor por defecto",
            'desc_campo': "Descripcion",
        }
        
class form_template(forms.ModelForm):
    class Meta:
        model = prd_plt_desc
        fields = (
            'nom_plt',
            'desc_plt',
            'id_campo',
        )
        labels ={
            'nom_plt' : 'Nombre de la plantilla:',
            'desc_plt' : 'Descripcion de la plantilla',
            'id_campo' : 'Campos a usar en la plantilla',
        }
    
    id_campo = label_campo(
        queryset= campo.objects.all(),
        label='Campos de la plantilla'
    )