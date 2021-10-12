from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class frm_reg_usu_su(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Super Usuario en Django.
    class Meta:
        model = User
        fields = '__all__'

class frm_reg_usu_adm(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email',
                  'is_staff',
                  'is_active'
                 ]
class frm_reg_usu(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model = User
        fields = ['username',
                  'password',
                  'first_name',
                  'last_name',
                  'email'
                 ]
