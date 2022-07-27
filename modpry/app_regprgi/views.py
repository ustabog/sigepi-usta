# App de registro de programas de un proyecto de investigación - Vistas para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 27-07-2022

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from modpry.app_regprgi.form import *
from modpry.app_regprgi.models import *
from django.urls import reverse_lazy
from .models import *

# Create your views here.
class vst_regprgi():
    #Clase que procesa las vistas del IU del inicio de la aplicación de programas de investigación de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_regprgi_iu.html")

#-------------- Vistas para el registro de programas de investigación ----------

class vts_reg_prgi(CreateView):
    #Clase de la vista de registro de un programa de investigación
    model = prgi_base
    form_class = frm_reg_prgi
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_prgi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un programa de investigación' 
        context ['action'] = 'add'
        return context

class vst_ls_prgi(ListView):
    # clase para listar programas de investigaación del sistema en tarjetas
    model = prgi_base
    template_name = 'cn_trj_prgi.html'
    context_object_name = 'lista_prgi'

    def get_queryset(self):
        return prgi_base.objects.filter(prg_archi=0)

class vts_edit_prgi(UpdateView):
    #Clase de la vista para actualizar el registro de un programa de investigación
    model = prgi_base
    form_class = frm_reg_prgi
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_prgi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un programa de investigación' 
        context ['list_url'] = reverse_lazy('cnprgi')
        context ['action'] = 'edit'
        return context

class vst_ls_detprgi(ListView):
    # clase para listar la información en detalle de un programa de investigación
    model = prgi_base
    template_name = 'cn_det_prgi.html'
    context_object_name = 'lista_info_prgi'

    def get_queryset(self):
        return prgi_base.objects.filter(id_usu = self.request.user).filter(prgi_archi=0)