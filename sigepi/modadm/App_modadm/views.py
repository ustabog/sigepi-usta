from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from .models import *
from .form import *
from modcons.App_cons.form import frm_con_mod

app_name = "adm"

class backend():
     # inicio del index
    def modadm(request):
        return render(request,'index_adm.html')


class backend_prb():
     # inicio del index prueba
    def modadmprv(request):
        return render(request,'index_adm_prb.html')

class vts_reg_mod(CreateView):
    #clase que almacena los modulos generales del sistema
    form_class = frm_con_mod
    template_name = 'reg_app/nvo_mod_prb.html'
    success_url = reverse_lazy('consulta_usuarios')
    success_message = 'el modelo creado satisfactoriamente'

class funcionList(ListView):
    model = func_app
    template_name = 'backend/registro_mod/funciones/funciones.html'

class funcionCreate(CreateView):
    model = func_app
    form_class = funcionForm
    template_name = 'backend/registro_mod/funciones/crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionUpdate(UpdateView):
    model = func_app
    form_class = funcionForm
    template_name = 'backend/registro_mod/funciones/crearfunciones.html'
    success_url = reverse_lazy('funciones')

class funcionDelete(DeleteView):
    model = func_app
    template_name = 'backend/registro_mod/funciones/verificacion.html'
    success_url = reverse_lazy('funciones')
