# Este codigo se trae de el modulo de consulta
from django import forms
from modadm.app_modadm.models import usu
from modadm.app_regusu.models import *
from modadm.app_regusugr.models import usugr
from modadm.app_regusui.models import usui
from modadm.app_modadm.models import mod

class frm_con_usu(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
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

class frm_con_usugr(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = usugr
        fields = ['id_gr',
                  'passgr',
                  'id_usu_admin',
                  #'id_rol_app',
                  'activo',
                 ]
        labels = {
                'id_gr' : 'id',
                'passgr' : 'password',
                'id_usu_admin' : 'id usuario',
                #'id_rol_app' : 'id rol',
                'activo' : 'activo',
                }




class frm_con_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model = usui
        fields = ['id_usuinst',
                  'passinst',
                  'id_usu_admin',
                  'id_rol_app',
                  'fch_regi',
                  'activo'
                 ]
        labels = {
                'id_usuinst' : 'id',
                'passinst' : 'password',
                'id_usu_admin' : 'id usuario',
                'id_rol_app' : 'id rol',
                'fch_regi' : 'fch_regi',
                'activo' : 'activo',
                }

class frm_con_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de modulos en Django.
    class Meta:
        model = mod
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
        model = usu_inf_apps
        fields = '__all__'
