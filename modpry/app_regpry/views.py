from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
from requests import request
#from rest_framework import viewsets
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#--------------------------- Registro de proyecto individual ---------------------------------
class vts_reg_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_pry(ListView):
    # clase para listar proyectos del sistema
    model = pry_base
    template_name = 'cn_trj_pry.html'
    context_object_name = 'lista_pry'

    def get_queryset(self):
        return pry_base.objects.filter(id_usu = self.request.user).filter(pry_archi=0)

class vts_edit_pry(UpdateView):
    #Clase de la vista para actualizar el registro de un proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un proyecto' 
        context ['entity'] = 'pry'
        context ['list_url'] = reverse_lazy('cnpry')
        context ['action'] = 'edit'
        return context

class vts_add_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = inf_pry
    form_class = frm_info_pry
    template_name = 'mod_pry_frm_add.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Añadir información de un proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_infopry(ListView):
    # clase para listar la información de los proyectos del sistema
    model = inf_pry
    template_name = 'cn_det_pry.html'
    context_object_name = 'lista_info_pry'

    def get_queryset(self):
        return pry_base.objects.filter(id_usu = self.request.user).filter(pry_archi=0)

 

        
    

