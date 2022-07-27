# App de recursos de un proyecto de investigación - Vistas para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 21-07-2022

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from modpry.app_recur.form import *
from django.urls import reverse_lazy
from .models import *
from modpry.app_recur.models import *


class vst_recur():
    #Clase que procesa las vistas del IU del incio de la aplicación de recursos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_recur_iu.html")

#-------------- Vistas para el registro de un recurso ----------

class vts_reg_recu(CreateView):
    #Clase de la vista de registro de un recurso 
    model = recu_pry
    form_class = frm_reg_recur
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_recu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un recurso' 
        context ['action'] = 'add'
        return context

class vst_ls_recu(ListView):
    # clase para listar recursos del sistema
    model = recu_pry
    template_name = 'cn_trj_recu.html'
    context_object_name = 'lista_recu'

    def get_queryset(self):
        return recu_pry.objects.filter(recu_archi=0)

class vts_edit_recu(UpdateView):
    #Clase de la vista para actualizar el registro de un recurso
    model = recu_pry
    form_class = frm_reg_recur
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_recu')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un recurso' 
        context ['entity'] = 'recu'
        context ['list_url'] = reverse_lazy('cnrecu')
        context ['action'] = 'edit'
        return context

class vst_ls_detrecu(ListView):
    # clase para listar la información en detalle de un recurso
    model = recu_pry
    template_name = 'cn_det_recu.html'
    context_object_name = 'lista_info_recu'

    def get_queryset(self):
        return recu_pry.objects.filter(id_usu = self.request.user).filter(recu_archi=0)