from django import forms
#from django.contrib.auth.models import User
from modadm.app_regusu.models import *
from modadm.app_modadm.models import *

#Clase que automatiza la creación de formularios de consulta de Usuario en Django.
class frm_cons_usu(forms.ModelForm):
    
    class Meta:
        model = usu
        fields = '__all__'
#Clase que automatiza la creación de formularios de consulta de Usuarios de grupo en Django.
class frm_cons_usugr(forms.ModelForm):

    class Meta:
        model = usugr
        fields = '__all__'

class frm_cons_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuarios institucionales en Django.
    class Meta:
        model = usui
        fields = '__all__'

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
        fields = '__all__'

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
