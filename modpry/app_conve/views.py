# App de convenios de un proyecto de investigación - Vistas para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 25-07-2022

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from modpry.app_conve.form import *
from django.urls import reverse_lazy
from .models import *
from modpry.app_conve.models import *

class vst_conve():
    #Clase que procesa las vistas del IU del inicio de la aplicación de convenios de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_conve_iu.html")

#----------- Vistas para el registro de un convenio ----------------

class vts_reg_conve(CreateView):
    #Clase de la vista de registro de un convenio
    model = conve_pry
    form_class = frm_reg_conve
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_conve')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un convenio' 
        context ['action'] = 'add'
        return context

class vst_ls_conve(ListView):
    # clase para listar convenios del sistema en tarjetas
    model = conve_pry
    template_name = 'cn_trj_conve.html'
    context_object_name = 'lista_conve'

    def get_queryset(self):
        return conve_pry.objects.filter(conve_archi=0) # Filtrar los convenios para que solo muestre los que no están archivados

class vts_edit_conve(UpdateView):
    #Clase de la vista para actualizar el registro de un convenio
    model = conve_pry
    form_class = frm_reg_conve
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_conve')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un convenio' 
        context ['list_url'] = reverse_lazy('cnconve')
        context ['action'] = 'edit'
        return context

class vst_ls_detconve(ListView):
    # clase para listar la información en detalle de un convenio
    model = conve_pry
    template_name = 'cn_det_conve.html'
    context_object_name = 'lista_info_conve'
    
    def get_queryset(self):
        return conve_pry.objects.filter(id_usu = self.request.user).filter(conve_archi=0) # Filtrar información por usuario y si esta archivado o no 