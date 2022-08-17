from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework import viewsets
from .models import *
from .form import *
from modcons.app_cons.form import *
#from .roles import roles

#Clase que presenta la portada del administrador de SIGEPI.
class portada_adm():
    #función para plantilla de inicio
    def vst_inicio(self,solicitud):
        return render(solicitud,"inicio_adm.html")

    #función para plantilla de inicio de al documentación del sistema
    def vst_doc(self, solicitud):
        respuesta='Documentación del sistema'
        return HttpResponse(respuesta)

    #función para plantilla de inicio sin extensión
    def vst_raiz(self, solicitud):
        plt=loader.get_template('inicio_adm.html')
        respuesta=plt.render()
        return HttpResponse(respuesta)
    

##CRUD de módulo ##
#Vista de registro de módulos nuevos en el sistema
class vts_reg_mod(CreateView, PermissionRequiredMixin):
    model = adm_mod
    form_class = frm_mod
    template_name = 'app_ma_frm_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    success_message = 'El modelo fue creado satisfactoriamente'
    permission_required = 'mod.add_mod'   

#Vista de listado de módulos registrados en el sistema
class vts_ls_mod(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = adm_mod
    form_class = frm_mod
    template_name = 'cn_mod.html'
    success_url = reverse_lazy('cn_mod.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'mod.view_mod' 

#Vista de edición o modificación de módulos registrados en el sistema
class vts_edt_mod(UpdateView, PermissionRequiredMixin):
    model = adm_mod
    form_class = frm_mod
    template_name = 'app_ma_frm_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    permission_required = 'mod.change_mod' 
    
#Vista de eliminación o borrado de módulos en el sistema
class vts_elim_mod(DeleteView, PermissionRequiredMixin):
    model = adm_mod
    template_name = 'app_ma_elim_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    permission_required = 'mod.delete_mod'

## CRUD de aplicaciones ##

#Vista de registro de aplicaciones en el sistema
class vts_reg_app(CreateView, PermissionRequiredMixin):
    model = adm_app
    form_class = frm_cons_app
    template_name = 'app_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    success_message = 'La aplicacion de modulos fue creada satisfactoriamente'
    permission_required = 'adm_mod.add_adm_mod'

#Vista del listado de aplicaciones registradas en el sistema
class vts_ls_app(ListView, PermissionRequiredMixin): #hereda de listwview
    model = adm_mod
    form_class = frm_cons_app
    template_name = 'cn_app.html'
    success_url = reverse_lazy('cn_app.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'adm_mod.view_adm_mod'

#Vista de edición o modificación de aplicaciones registradas en el sistema
class vts_edt_app(UpdateView, PermissionRequiredMixin):
    model = adm_mod
    form_class = frm_cons_app
    template_name = 'app_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    permission_required = 'adm_mod.change_adm_mod'

#Vista de eliminación o borrado de aplicaciones en el sistema
class vts_elim_app(DeleteView, PermissionRequiredMixin):
    model = adm_mod
    form_class = frm_cons_app
    template_name = 'app_ma_elim_app.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    permission_required = 'adm_mod.delete_adm_mod'

## CRUD de roles ##
#Vista de registro de roles en el sistema
class vts_reg_rol(CreateView, PermissionRequiredMixin):
    model = adm_rol
    form_class = frm_cons_rol
    template_name = 'app_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    success_message = 'El rol fue creado satisfactoriamente'
    #crear_rol = roles.crear_roles(self=None)
    permission_required = 'adm_rol.add_adm_rol'

#Vista del listado de registro de roles en el sistema
class vts_ls_rol(ListView, PermissionRequiredMixin): 
    model = adm_rol
    form_class = frm_cons_rol
    template_name = 'cn_rol.html'
    success_url = reverse_lazy('cn_rol.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'adm_rol.view_adm_rol'

#Vista de edición o modificación de registro de roles en el sistema
class vts_edt_rol(UpdateView, PermissionRequiredMixin):
    model = adm_rol
    form_class = frm_cons_rol
    template_name = 'app_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    permission_required = 'adm_rol.change_adm_rol'
    
#Vista de eliminación de registro de roles en el sistema
class vts_elim_rol(DeleteView, PermissionRequiredMixin):
    model = adm_rol
    form_class = frm_cons_rol
    template_name = 'app_ma_elim_rol.html'
    success_url = reverse_lazy('consulta_rol')
    permission_required = 'adm_rol.delete_adm_rol'


## CRUD de funciones ##
#Vista de listado de funciones registradas en el sistema
class vst_ls_func(ListView, PermissionRequiredMixin):
    model = adm_func
    template_name = 'app_ma_ls_funciones.html'

#Vista de creación de nuevo registro de funciones en el sistema
class vst_reg_func(CreateView, PermissionRequiredMixin):
    model = adm_func
    form_class = frm_func
    template_name = 'app_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

#Vista de edición o modificación de funciones registradas en el sistema
class vst_edt_func(UpdateView, PermissionRequiredMixin):
    model = adm_func
    form_class = frm_func
    template_name = 'app_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

#Vista de eliminación o borrado de funciones registradas en el sistema
class vst_elim_func(DeleteView, PermissionRequiredMixin):
    model = adm_func
    template_name = 'app_ma_func_verificacion.html'
    success_url = reverse_lazy('funciones')
