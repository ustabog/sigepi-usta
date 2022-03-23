from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import *

class funcionForm(forms.ModelForm):
    class Meta:
        model =  func_app
        fields = '__all__'

class frm_reg_mod(forms.ModelForm):
    #Calse que automatiza la creación de formularios de Registro de Usuario en Django.
    class Meta:
        model =  mod
        fields = '__all__'

class frm_con_mod(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model =  mod
        fields = '__all__'