from tokenize import group
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import *


#Clase que automatiza la creación de formularios para el modelo de usuarios(as) individuales usu.
class frm_usu(forms.ModelForm):
    
    class Meta:
        model = usu
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de usuarios(as) grupales usugr.
class frm_usugr(forms.ModelForm):
    
    class Meta:
        model = usugr
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de usuarios(as) institucionales usui.
class frm_usui(forms.ModelForm):
    
    class Meta:
        model = usui
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de módulos adm_mod.
class frm_mod(forms.ModelForm):
    
    class Meta:
        model =  adm_mod
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de aplicaciones adm_app.
class frm_app(forms.ModelForm):
    #Clase que automatiza la creación de formularios de consulta de Usuario en Django.
    class Meta:
        model =  adm_app
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de funciones adm_func.
class frm_rol(forms.ModelForm):
    class Meta:
        model =  adm_rol
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de funciones adm_func.
class frm_func(forms.ModelForm):
    class Meta:
        model =  adm_func
        fields = '__all__'

#Clase que automatiza la creación de formularios para el modelo de relación funciones y roles rl_func_rol.
class frm_rl_func_rol(forms.ModelForm):
    class Meta:
        model =  rl_func_rol
        fields = '__all__'

