from django import forms
from django.contrib.auth.models import User, Permission
from modadm.app_regusu.models import *
from modadm.app_modadm.models import *


class frm_cons_usui(forms.ModelForm):
    #Calse que automatiza la creación de formularios de consulta de Usuarios institucionales en Django.
    class Meta:
        model = User
        fields ='__all__'
        exclude = ('user_permissions','groups','password',)