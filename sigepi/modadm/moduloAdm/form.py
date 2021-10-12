from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class RolForm(forms.ModelForm):
    class Meta:
        model = rol
    #    fields = ('nombre', 'descricion',) para llamar a campos especificos
        fields = '__all__'

class ModForm(forms.ModelForm):
    class Meta:
        model = mod
    #    fields = '__all__'
        fields = [
            'titulo',
            'desc',
            'url_doc',
            'version',
            'activo',
            'instalado',
            'visible',
        ]
        labels = {
            'titulo': 'Titulo del modulo:',
            'desc': 'Descripcion del modulo',
            'url_doc': 'url',
            'version': 'version del modulo',
            'activo': 'el modulo esta activo',
            'instalado': 'el modulo esta instalado',
            'visible': 'el modelo desea que sea visible',
        }


class PermisoForm(forms.ModelForm):
    class Meta:
        model =  Permiso
        fields = '__all__'

class AppForm(forms.ModelForm):
    class Meta:
        model = app_mod
        fields = '__all__'

class FuentForm(forms.ModelForm):
    class Meta:
        model =  func_app
        fields = '__all__'

class AplicativoForm(forms.ModelForm):
    class Meta:
        model =  listado_aplicativo
        fields = '__all__'

class UsuForm(forms.ModelForm):
    class Meta:
        model =  usu
        fields = '__all__'

class UsuInfoperForm(forms.ModelForm):
    class Meta:
        model =  usu_inf_pers
        fields = '__all__'

"""
        fields = [
            'nuip',
            'tipo_nuip',
            'nombres',
            'apelllidos',
            'nal',
            'fch_naci',
            'gene',
            'ocup',
            'tipo_discap',
        ]
        labels = {
            'nuip' : 'nuip',
            'tipo_nuip': 'tipo',
            'nombres': 'nombres',
            'apelllidos':'apellidos',
            'nal' : 'nacionalidad',
            'fch_naci' : 'fecha',
            'gene' : 'genero',
            'ocup':'ocupacion',
            'tipo_discap':'discapacidad',
        }
"""
class RlmodrolForm(forms.ModelForm):
    class Meta:
        model = rl_mod_rol
        fields = '__all__'

class formregistro(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]
        labels = {
            'username': 'nombre de usuario',
            'first_name': 'nombre',
            'last_name' : 'apellidos',
            'email' : 'email',
        }

class infocontactoForm(forms.ModelForm):
    class Meta:
        model =  usu_inf_contac
        fields = '__all__'

class infoacadForm(forms.ModelForm):
    class Meta:
        model = form_acad
        fields = '__all__'

class etapa_grForm(forms.ModelForm):
    class Meta:
        model = etapa_gr
        fields = '__all__'

class usugrForm(forms.ModelForm):
    class Meta:
        model = usugr
        fields = '__all__'

class usugr_inf_grForm(forms.ModelForm):
    class Meta:
        model = usugr_inf_gr
        fields = '__all__'

class curs_dictForm(forms.ModelForm):
    class Meta:
        model = curs_dict
        fields = '__all__'

class empleosForm(forms.ModelForm):
    class Meta:
        model = empleos
        fields = '__all__'

class usugr_inf_contacForm(forms.ModelForm):
    class Meta:
        model = usugr_inf_contac
        fields = '__all__'

class rl_usu_inf_apps_rolForm(forms.ModelForm):
    class Meta:
        model = rl_usu_inf_apps_rol
        fields = '__all__'
