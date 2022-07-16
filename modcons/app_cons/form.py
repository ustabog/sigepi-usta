from django import forms
#from django.contrib.auth.models import User
from modadm.app_regusu.models import *
from modadm.app_modadm.models import *

#Clase que automatiza la creación de formularios de consulta de Usuario en Django.
class frm_cons_usu(forms.ModelForm):
    
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
class frm_cons_usugr(forms.ModelForm):

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

class frm_cons_usui(forms.ModelForm):
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
class frm_cons_mod(forms.ModelForm):
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

#Calse que automatiza la creación de formularios de consulta de las aplicaciones del sistema.
class frm_cons_app(forms.ModelForm):
    
    class Meta:
        model = adm_app
        fields = [
            'id_app',
            'titulo',
            'desc',
            'url_doc',
            'url_instal',
            'url_pl',
            'nom_url',
            'version',
            'id_mod',
            'ver_mod',
            'activo',
            'instalada',
            'visible',
            'externa',
            'tipo_app',
            'ico',
            'id_usu_reg',
            ]
        labels = {
            'id_app' :'Identificador de Aplicación',
            'titulo' :'Título o Nombre',
            'desc' :'Descripción',
            'url_doc' :'URL de la documentación',
            'url_instal' :'URL relativa de instalación',
            'url_pl' :'URL de Plantilla de aplicación',
            'nom_url' :'Nombre de la URL',
            'version' :'Versión de la Aplicación',
            'id_mod' :'Identificador del Módulo',
            'ver_mod' :'Versión del Módulo',
            'activo' :'¿La aplicación se encuentra activa?',
            'instalada' :'¿La aplicación está instalada?',
            'visible' :'¿La aplicación está visible?',
            'externa' :'¿Es una aplicación externa?',
            'tipo_app' :'Tipo de aplicación',
            'ico' :'nombre del ícono de la aplicación ',
            'id_usu_reg' :'Usuario quien registra la app',
            }

class frm_cons_rol(forms.ModelForm):
    #Clase que consulta los roles registrados en el sistema
    class Meta:
        model = adm_rol
        fields = '__all__'


class frm_cons_rl_rol_usu(forms.ModelForm):
    #Clase que consulta las relaciones entre roles y usuarios
    class Meta:
        model = rl_usu_rol
        fields = '__all__'
