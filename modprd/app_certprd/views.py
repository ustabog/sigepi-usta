# App de certificacion de productos - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_certprd.form import *
from django.urls import reverse_lazy
from modprd.app_certprd.models import *
from .models import *
from django.views.generic import *

#----------VISTAS PARA EL REGISTRO DE MEDICIONES SIGEPI------------

#Vista para el registro de medicion

class vst_regprd(CreateView):
    model= prd_med
    form_class = form_med
    template_name ='mod_cert_frm_registrar.html'
    success_url = reverse_lazy('')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar medicion'
        context['action'] = 'Create'
        return context

#Vista para el listado de mediciones

class vst_listprd(ListView):
    model= prd_base
    template_name ='cn_trj_prd.html'
    success_url = reverse_lazy('listar_prd')
    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        return prd_base.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar productos'
        context['action'] = 'List'
        return context

 #Vista para la consulta de mediciones

class vst_cons_prd(DetailView):
    model= prd_base
    template_name ='cn_det_prd.html'   
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de productos'
        context['action'] = 'Consulte'
        return context
  

#Vista para la edicion de un mediciones

class vst_updprd(UpdateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_editar.html'
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar productos'
        context['action'] = 'update'
        context ['entity'] = 'prd'
        context ['list_url'] = reverse_lazy('listar_reqexs')
        return context

#Vista para la eliminacion de una medicion

class vst_delprd (DeleteView):
    model = prd_base
    template_name ='mod_prd_eliminar.html'
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de productos'
        context['action'] = 'Delete'
        return context