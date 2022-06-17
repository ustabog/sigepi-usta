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
from modcons.app_cons.form import frm_con_mod
from .roles import roles

class portada_adm():
    #Clase que presenta la portada del administrador de SIGEPI.
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        return render(solicitud,"inicio_adm.html")

    def vst_doc(self, solicitud):
        #función para plantilla de inicio de al documentación del sistema
        respuesta='Documentación del sistema'
        return HttpResponse(respuesta)

    def vst_raiz(self, solicitud):
        #función para plantilla de inicio sin extensión
        plt=loader.get_template('inicio_adm.html')
        respuesta=plt.render()
        return HttpResponse(respuesta)
    


######   CRUD MODULO    ################################

class vts_reg_mod(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = mod
    form_class = frm_reg_mod
    template_name = 'app_ma_frm_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    success_message = 'El modelo fue creado satisfactoriamente'
    permission_required = 'mod.add_mod'   

class vts_ls_mod(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = mod
    form_class = frm_con_mod
    template_name = 'cn_mod.html'
    success_url = reverse_lazy('cn_mod.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'mod.view_mod' 

class vts_edt_mod(UpdateView, PermissionRequiredMixin):
    #clase que almacena los modulos generales del sistema
    model = mod
    form_class = frm_con_mod
    template_name = 'app_ma_frm_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    permission_required = 'mod.change_mod' 
    
class vts_del_mod(DeleteView, PermissionRequiredMixin):
    model = mod
    template_name = 'app_ma_del_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    permission_required = 'mod.delete_mod'

######   CRUD APP MODULO    ################################
class vts_reg_app_mod(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'app_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    success_message = 'La aplicacion de modulos fue creada satisfactoriamente'
    permission_required = 'app_mod.add_app_mod'

class vts_ls_app_mod(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'cn_app_mod.html'
    success_url = reverse_lazy('cn_app_mod.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'app_mod.view_app_mod'

class vts_edt_app_mod(UpdateView, PermissionRequiredMixin):
    #clase que almacena los modulos generales del sistema
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'app_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    permission_required = 'app_mod.change_app_mod'

class vts_del_app_mod(DeleteView, PermissionRequiredMixin):
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'app_ma_del_app_mod.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    permission_required = 'app_mod.delete_app_mod'

###### CRUD ROLES #############################################
class vts_reg_rol(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    #Los estilos estan afectando la vista, en cuanto a seleccion de objetos de la llave foranea
    model = rol
    form_class = frm_con_rol
    template_name = 'app_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    success_message = 'El rol fue creado satisfactoriamente'
    crear_rol = roles.crear_roles(self=None)
    permission_required = 'rol.add_rol'

class vts_ls_rol(ListView, PermissionRequiredMixin): 
    model = rol
    form_class = frm_con_rol
    template_name = 'cn_rol.html'
    success_url = reverse_lazy('cn_rol.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'rol.view_rol'

class vts_edt_rol(UpdateView, PermissionRequiredMixin):
    model = rol
    form_class = frm_con_rol
    template_name = 'app_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    permission_required = 'rol.change_rol'
    
class vts_del_rol(DeleteView, PermissionRequiredMixin):
    model = rol
    form_class = frm_con_rol
    template_name = 'app_ma_del_rol.html'
    success_url = reverse_lazy('consulta_rol')
    permission_required = 'rol.delete_rol'

###### CRUD LISTADO APLICATIVO #############################################

class vts_reg_list_app(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = listado_aplicativo
    form_class = frm_con_list_app
    template_name = 'app_ma_frm_crealsapp.html'
    success_url = reverse_lazy('consulta_lsapp')
    success_message = 'El rol fue creado satisfactoriamente'
    permission_required = 'listado_aplicativo.add_listado_aplicativo'

class vts_ls_list_app(ListView, PermissionRequiredMixin): 
    model = listado_aplicativo
    form_class = frm_con_list_app
    template_name = 'cn_lsapp.html'
    success_url = reverse_lazy('cn_lsapp.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'listado_aplicativo.view_listado_aplicativo'

class vts_edt_list_app(UpdateView, PermissionRequiredMixin):
    model = listado_aplicativo
    form_class = frm_con_list_app
    template_name = 'app_ma_frm_crealsapp.html'
    success_url = reverse_lazy('consulta_lsapp')
    permission_required = 'listado_aplicativo.change_listado_aplicativo'
    
class vts_del_list_app(DeleteView, PermissionRequiredMixin):
    model = listado_aplicativo
    template_name = 'app_ma_del_lsapp.html'
    success_url = reverse_lazy('consulta_lsapp')
    permission_required = 'listado_aplicativo.delete_listado_aplicativo'

###### CRUD EXTENSIONES DE MODULO #############################################

class vts_reg_mod_ext(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = mod_ext
    form_class = frm_con_mod_ext
    template_name = 'app_ma_frm_crearextmod.html'
    success_url = reverse_lazy('consulta_mod_ext')
    success_message = 'La extesion de modulo fue creada satisfactoriamente'
    permission_required = 'mod_ext.add_mod_ext'

class vts_ls_mod_ext(ListView, PermissionRequiredMixin): 
    model = mod_ext
    form_class = frm_con_mod_ext
    template_name = 'cn_extmod.html'
    success_url = reverse_lazy('consulta_mod_ext')
    success_message = 'Listado cargado correctamente'
    permission_required = 'mod_ext.view_mod_ext'

class vts_edt_mod_ext(UpdateView, PermissionRequiredMixin):
    model = mod_ext
    form_class = frm_con_mod_ext
    template_name = 'app_ma_frm_crearextmod.html'
    success_url = reverse_lazy('consulta_mod_ext')
    permission_required = 'mod_ext.change_mod_ext'
    
class vts_del_mod_ext(DeleteView, PermissionRequiredMixin):
    model = mod_ext
    template_name = 'app_ma_del_mod_ext.html'
    success_url = reverse_lazy('consulta_mod_ext')
    permission_required = 'mod_ext.delete_mod_ext'

###### CRUD APLICACIONES EXTERNAS #############################################

class vts_reg_app_ext(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = app_ext
    form_class = frm_con_app_ext
    template_name = 'app_ma_frm_crearextapp.html'
    success_url = reverse_lazy('consulta_app_ext')
    success_message = 'La aplicacion externa fue creada satisfactoriamente'
    permission_required = 'app_ext.add_app_ext'

class vts_ls_app_ext(ListView, PermissionRequiredMixin): 
    model = app_ext
    form_class = frm_con_app_ext
    template_name = 'cn_extapp.html'
    success_url = reverse_lazy('consulta_app_ext')
    success_message = 'Listado cargado correctamente'
    permission_required = 'app_ext.view_app_ext'

class vts_edt_app_ext(UpdateView, PermissionRequiredMixin):
    model = app_ext
    form_class = frm_con_app_ext
    template_name = 'app_ma_frm_crearextapp.html'
    success_url = reverse_lazy('consulta_app_ext')
    permission_required = 'app_ext.change_app_ext'
    
class vts_del_app_ext(DeleteView, PermissionRequiredMixin):
    model = app_ext
    template_name = 'app_ma_del_app_ext.html'
    success_url = reverse_lazy('consulta_app_ext')
    permission_required = 'mod_ext.delete_app_ext'




class funcionList(ListView, PermissionRequiredMixin):
    model = func_app
    template_name = 'app_ma_ls_funciones.html'

class funcionCreate(CreateView, PermissionRequiredMixin):
    model = func_app
    form_class = funcionForm
    template_name = 'app_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionUpdate(UpdateView, PermissionRequiredMixin):
    model = func_app
    form_class = funcionForm
    template_name = 'app_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionDelete(DeleteView, PermissionRequiredMixin):
    model = func_app
    template_name = 'app_ma_func_verificacion.html'
    success_url = reverse_lazy('funciones')
