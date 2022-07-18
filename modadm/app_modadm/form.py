from tokenize import group
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.views.generic.edit import CreateView, DeleteView, UpdateView, FormView

#Clase formulario de Registro nuevo de Usuario base en Django.
class frm_user_base(UserCreationForm):
    fields = ('username', 'password1', 'password2', 'email', 'first_name', 'last_name')
    class Meta:
        fields = [
                    'username',
                    'password1',
                    'password2',
                    'email',
                    'first_name',
                    'last_name',
                 ]
        labels = {
                    'username' : 'Usuario',
                    'password1': 'Contraseña',
                    'password2': 'Repetir Contraseña',
                    'email': 'Correo',
                    'first_name' : 'Nombre',
                    'last_name' : 'Apellido',
                }


#clase que genera un formulario de consulta de los usuarios individuales
class frm_usu(forms.ModelForm):
    class Meta:
        model = usu
        fields = [
            'id_user',
            'fch_reg',
            'activo',
            'archi',
            ]
        labels = {
            'id_user': 'Identificador de Usuario Individual',
            'fch_reg': 'Fecha de registro',
            'activo': 'Usuario Activo',
            'archi': 'Usuario archivado',
            }

#Clase que automatiza la creación de formularios para el modelo de usuarios(as) grupales usugr.
class frm_usugr(forms.ModelForm):
    class Meta:
        model = usugr
        fields = [
            'id_user',
            'sigla',
            'nom_grup',
            'emailgr',
            'id_usu_adm',
            'id_usu_asig',
            'fch_reg',
            'activo',
            'archi',
            ]
        labels = {
            'id_user': 'Identificador de Usuario Grupo',
            'sigla': 'Sigla del Grupo',
            'nom_grup': 'Nombre del Grupo',
            'emailgr': 'Correo electrónico del Grupo',
            'id_usu_adm': 'Usuario del director(a) del Grupo',
            'id_usu_asig': 'Usuario asignado para Administración del Grupo',
            'fch_reg': 'Fecha de registro del Grupo',
            'activo': '¿Usuario Grupo activo?',
            'archi': '¿Usuario Grupo archivado?',
            }

#Clase que automatiza la creación de formularios para el modelo de usuarios(as) institucionales usui.
class frm_usui(forms.ModelForm):
    class Meta:
        model = usui
        fields = [
            'id_user',
            'sigla',
            'nom_inst',
            'email_inst',
            'id_usu_adm',
            'id_usu_asig',
            'fch_reg',
            'activo',
            'archi',
            ]
        labels = {
            'id_user': 'Identificador de Usuario Institucional',
            'sigla': 'Sigla de la Institución',
            'nom_inst': 'Nombre de la Institución',
            'email_inst': 'Correo electrónico de la Institución',
            'id_usu_adm': 'Usuario(a) del Administrador(a) del Usuario Institución',
            'id_usu_asig': 'Usuario(a) asignado(a) para Administración del Grupo',
            'fch_reg': 'Fecha de registro de la Institución',
            'activo': '¿Usuario Institucional activo?',
            'archi': '¿Usuario Institucional archivado?',
            }

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

#Clase formulario de Registro nuevo de Usuario Individual en SIGEPI.
class frm_crear_usu(CreateView):
    model = usu
    fields = ('fch_reg','activo', 'archi')

#Clase formulario para editar un Usuario Individual en SIGEPI.
class frm_edit_usu(UpdateView):
    model = usu
    fields = ('fch_reg','activo', 'archi')

#Clase formulario de eliminar o borrar Usuario Individual en SIGEPI.
class frm_elim_usu(DeleteView):
    model = usu
    fields = ('fch_reg','activo', 'archi')


#Clase formulario de Registro nuevo de Usuario de grupo en SIGEPI.
class frm_crear_usugr(CreateView):
    model = usugr
    fields = ('sigla', 'nom_grup', 'emailgr', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')

#Clase formulario para editar un Usuario Individual en SIGEPI.
class frm_edit_usugr(UpdateView):
    model = usugr
    fields = ('sigla', 'nom_grup', 'emailgr', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')

#Clase formulario de eliminar o borrar Usuario Individual en SIGEPI.
class frm_elim_usu(DeleteView):
    model = usugr
    fields = ('sigla', 'nom_grup', 'emailgr', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')


#Clase formulario de Registro nuevo de Usuario institucional en Django.
class frm_crear_usui(CreateView):
    model = usui
    fields = ('sigla', 'nom_inst', 'email_inst', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')

#Clase formulario para editar un Usuario Individual en SIGEPI.
class frm_edit_usui(UpdateView):
    model = usugr
    fields = ('sigla', 'nom_inst', 'email_inst', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')

#Clase formulario de eliminar o borrar Usuario Individual en SIGEPI.
class frm_elim_usu(DeleteView):
    model = usui
    fields = ('sigla', 'nom_inst', 'email_inst', 'id_usu_adm', 'id_usu_asig', 'fch_reg', 'activo', 'archi')
