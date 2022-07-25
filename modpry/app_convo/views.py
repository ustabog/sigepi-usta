# App de convocatorias para un proyecto - Vistas para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 25-07-2022

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from modpry.app_convo.form import *
from django.urls import reverse_lazy
from .models import *
from modpry.app_convo.models import *

class vst_convo():
    #Clase que procesa las vistas del IU del inicio de la aplicación de convocatorias de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_convo_iu.html")

#----------- Vistas para el registro de una convocatoria ----------------

class vts_reg_convo(CreateView):
    #Clase de la vista de registro de una convocatoria
    model = convo_pry
    form_class = frm_reg_convo
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_convo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un convocatoria' 
        context ['action'] = 'add'
        return context

class vst_ls_convo(ListView):
    # clase para listar convocatorias del sistema en tarjetas
    model = convo_pry
    template_name = 'cn_trj_convo.html'
    context_object_name = 'lista_convo'

    def get_queryset(self):
        return convo_pry.objects.filter(convo_archi=0) # Filtrar las convocatorias para que solo muestre las que no están archivadas

class vts_edit_convo(UpdateView):
    #Clase de la vista para actualizar el registro de una convocatoria
    model = convo_pry
    form_class = frm_reg_convo
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_convo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un convocatoria' 
        context ['list_url'] = reverse_lazy('cnconvo')
        context ['action'] = 'edit'
        return context

class vst_ls_detconvo(ListView):
    # clase para listar la información en detalle de una convocatoria
    model = convo_pry
    template_name = 'cn_det_convo.html'
    context_object_name = 'lista_info_convo'

    def get_queryset(self):
        return convo_pry.objects.filter(id_usu = self.request.user).filter(convo_archi=0) # Filtrar información por usuario y si esta archivado o no 