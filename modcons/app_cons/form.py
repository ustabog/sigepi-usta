from django import forms
#from django.contrib.auth.models import User
from modadm.app_regusu.models import *
from modadm.app_modadm.models import *

#Clase que automatiza la creación de formularios de consulta de Usuario en Django.
class frm_con_usu(forms.ModelForm):
    
    class Meta:
        model = usu
        fields = ['username',
                  'first_name',
                  'last_name',
                  'email',
                 ]
        labels ={
                'username' : 'username',
                'first_name' : 'nombre',
                'last_name' : 'apellido',
                'email' : 'correo',
                }
#Clase que automatiza la creación de formularios de consulta de Usuarios de grupo en Django.
class frm_con_usugr(forms.ModelForm):
    
    class Meta:
        model = usugr
        fields = ['id',
                  'username',
                  'first_name',
                  'email',
                  'fch_reg',
                  'activo',
                  'id_usu_adm',
                  'id_usu_asig',
                 ]
        labels = {
                'id': 'id',
                'username': 'Sigla',
                'first_name': 'Nombre del Grupo',
                'email': 'Correo-e del grupo',
                'fch_reg': 'Fecha de Registro',
                'activo': 'Activo',
                'id_usu_adm': 'Identificador de usuario Adm. del grupo',
                'id_usu_asig': 'Identificador de usuario asignado para Adm. del grupo',
                }

class frm_con_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuarios institucionales en Django.
    class Meta:
        model = usui
        fields = ['id',
                  'username',
                  'first_name',
                  'email',
                  'fch_reg',
                  'activo',
                  'id_usu_adm',
                  'id_usu_asig',
                 ]
        labels = {
                'id': 'id',
                'username': 'Sigla',
                'first_name': 'Nombre del Grupo',
                'email': 'Correo-e del grupo',
                'fch_reg': 'Fecha de Registro',
                'activo': 'Activo',
                'id_usu_adm': 'Identificador de usuario Adm. del grupo',
                'id_usu_asig': 'Identificador de usuario asignado para Adm. del grupo',
                }
class frm_con_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = adm_mod
        fields = [
                'id_mod',
                'titulo',
                'desc',
                'url_doc',
                'version',
                'activo',
                'instalado',
                'visible',
                'ls_param_cnf'
                ]
        labels = {
                'id_mod' : 'id',
                'titulo' : 'titulo',
                'desc' : 'descripcion',
                'url_doc' : 'url del documento',
                'version' : 'versión',
                'activo' : 'activo',
                'instalado' : 'instalado',
                'visible' : 'visible',
                'ls_param_cnf' : 'parametros',
                }


class frm_rol_usu(forms.ModelForm):
    #Calse que busca los campos de roles de usaurio
    class Meta:
        model = rl_usu_rol
        fields = '__all__'
