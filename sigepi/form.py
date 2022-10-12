from django import forms
from django.contrib.auth.forms import UserCreationForm, User
from django.forms import fields


class frm_reg_usu_su(forms.ModelForm):
    #Clase que automatiza la creación de formularios de Registro de Super Usuario en Django.
    class Meta:
        model = User
        fields = '__all__'

class frm_reg_usu_adm(forms.ModelForm):
    #Clase que automatiza la creación de formularios de Registro de Usuario en Django.
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
class frm_reg_usu(UserCreationForm):
    #Clase que automatiza la creación de formularios de Registro de Usuario en Django.
    first_name = forms.CharField(max_length=140, required=True)
    last_name = forms.CharField(max_length=140, required=False)
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',

        )

