from unicodedata import name
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
#from rest_framework import viewsets
from .models import *
from .form import *
#from modcons.App_cons.form import frm_con_mod

######   CRUD MODULO    ################################
class vts_reg_mod(CreateView):
    #crear información de las personas
    model = mod
    form_class = frm_reg_mod
    template_name = 'App_ma_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    success_message = 'El modelo fue creado satisfactoriamente'

class vts_ls_mod(ListView): #hereda de listwview
    #información de las personas
    model = mod
    form_class = frm_con_mod
    template_name = 'cn_mod.html'
    success_url = reverse_lazy('cn_mod.html')
    success_message = 'Listado cargado correctamente'

class vts_edt_mod(UpdateView):
    #clase que almacena los modulos generales del sistema
    model = mod
    form_class = frm_con_mod
    template_name = 'App_ma_nvo_mod.html'
    success_url = reverse_lazy('consulta_modulos')
    
class vts_del_mod(DeleteView):
    model = mod
    form_class = frm_con_mod
    template_name = 'App_ma_del_mod.html'
    success_url = reverse_lazy('consulta_modulos')

######   CRUD APP MODULO    ################################
class vts_reg_app_mod(CreateView):
    #crear información de las personas
    model = app_mod
    form_class = frm_reg_app_mod
    template_name = 'App_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    success_message = 'El modelo fue creado satisfactoriamente'

class vts_ls_app_mod(ListView): #hereda de listwview
    #información de las personas
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'cn_app_mod.html'
    success_url = reverse_lazy('cn_app_mod.html')
    success_message = 'Listado cargado correctamente'

class vts_edt_app_mod(UpdateView):
    #clase que almacena los modulos generales del sistema
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'App_ma_frm_crearapp.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')
    
class vts_del_app_mod(DeleteView):
    model = app_mod
    form_class = frm_con_app_mod
    template_name = 'App_ma_del_app_mod.html'
    success_url = reverse_lazy('consulta_aplicaciones_modulos')

###### CRUD ROLES #############################################
class vts_reg_rol(CreateView):
    #crear información de las personas
    model = rol
    form_class = frm_con_rol
    template_name = 'App_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    success_message = 'El rol fue creado satisfactoriamente'

    g_admsis = Group.objects.get(name = 'Admin Módulo Administración')
    v_rol = Permission.objects.get(codename='view_rol')
    a_rol = Permission.objects.get(codename='add_rol')
    c_rol = Permission.objects.get(codename='change_rol')
    d_rol = Permission.objects.get(codename='delete_rol')
    g_admsis.permissions.add(v_rol,a_rol,c_rol,d_rol)
    g_admsis.save()
    

class vts_ls_rol(ListView): 
    model = rol
    form_class = frm_con_rol
    template_name = 'cn_rol.html'
    success_url = reverse_lazy('cn_rol.html')
    success_message = 'Listado cargado correctamente'
    

class vts_edt_rol(UpdateView):
    model = rol
    form_class = frm_con_rol
    template_name = 'App_ma_frm_crearrol.html'
    success_url = reverse_lazy('consulta_rol')
    
class vts_del_rol(DeleteView):
    model = rol
    form_class = frm_con_rol
    template_name = 'App_ma_del_rol.html'
    success_url = reverse_lazy('consulta_rol')

class funcionList(ListView):
    model = func_app
    template_name = 'App_ma_ls_funciones.html'

class funcionCreate(CreateView):
    model = func_app
    form_class = funcionForm
    template_name = 'App_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionUpdate(UpdateView):
    model = func_app
    form_class = funcionForm
    template_name = 'App_ma_crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionDelete(DeleteView):
    model = func_app
    template_name = 'App_ma_func_verificacion.html'
    success_url = reverse_lazy('funciones')
