from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView, ListView, DetailView
from django.urls import reverse_lazy
#from djangorequests import request
#from rest_framework import viewsets
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *

class vst_regpry():
    #Clase que procesa las vistas del IU del inicio de registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_regpry_iu.html")

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

#---------------- Información adicional del proyecto -------------------

class vts_add_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = inf_pry
    form_class = frm_inf_pry
    template_name = 'mod_pry_frm_add.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Añadir información de un proyecto' 
        context ['action'] = 'add'
        return context

class vts_edit_infpry(UpdateView):
    #Clase de la vista para actualizar la información adicional de un proyecto 
    model = inf_pry
    form_class = frm_inf_pry
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar información adicional de un proyecto' 
        context ['list_url'] = reverse_lazy('cnpry')
        context ['action'] = 'edit'
        return context

class vst_ls_infopry(ListView):
    # clase para listar la información adicional de los proyectos del sistema
    model = inf_pry
    template_name = 'cn_det_pry.html'
    context_object_name = 'lista_info_pry'

    def get_queryset(self):
        return inf_pry.objects.filter(id_usu = self.request.user).filter(pry_archi=0)

#---------------- Información geográfica del proyecto-------------------
class vts_reg_geo(CreateView):
    #Clase de la vista de registrar información geográfica del proyecto
    model = inf_geo_pry
    form_class = frm_inf_geo
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar información geográfica' 
        context ['action'] = 'add'
        return context

class vts_edit_geo(UpdateView):
    #Clase de la vista para actualizar la información geográfica de un proyecto 
    model = inf_geo_pry
    form_class = frm_inf_geo
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar información geográfica de un proyecto' 
        context ['list_url'] = reverse_lazy('cnpry')
        context ['action'] = 'edit'
        return context

class vst_ls_geopry(ListView):
    # clase para listar la información geográfica de los proyectos del sistema
    model = inf_geo_pry
    template_name = 'cn_det_pry.html'
    context_object_name = 'lista_geo_pry'

    def get_queryset(self):
        return pry_base.objects.filter(id_usu = self.request.user).filter(pry_archi=0)

#---------------- Información de los eventos del proyecto --------------

class vts_reg_even(CreateView):
    #Clase de la vista de registrar eventos del proyecto
    model = even_pry
    form_class = frm_even_pry
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un evento' 
        context ['action'] = 'add'
        return context

class vts_edit_even(UpdateView):
    #Clase de la vista para actualizar los eventos de un proyecto
    model = even_pry
    form_class = frm_even_pry
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar evento' 
        context ['list_url'] = reverse_lazy('cnpry')
        context ['action'] = 'edit'
        return context

class vst_ls_evenpry(ListView):
    # clase para listar los eventos de los proyectos del sistema
    model = even_pry
    template_name = 'cn_det_pry.html'
    context_object_name = 'lista_even_pry'

    def get_queryset(self):
        return pry_base.objects.filter(id_usu = self.request.user).filter(pry_archi=0)

#------ Información de la línea de investigación del proyecto ----------

class vts_reg_lninv(CreateView):
    #Clase de la vista de registrar la línea de investigación del proyecto
    model = lin_inv
    form_class = frm_lin_inv
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar la línea de investigación' 
        context ['action'] = 'add'
        return context

class vts_edit_lninv(UpdateView):
    #Clase de la vista para actualizar la línea de investigación 
    model = lin_inv
    form_class = frm_lin_inv
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar línea de investigación' 
        context ['list_url'] = reverse_lazy('cnpry')
        context ['action'] = 'edit'
        return context

class vst_ls_lninv(ListView):
    # clase para listar las líneas de investigación
    model = lin_inv
    template_name = 'cn_det_pry.html'
    context_object_name = 'lista_ln_inv'

    def get_queryset(self):
        return pry_base.objects.filter(id_usu = self.request.user).filter(pry_archi=0)
 

        
    

