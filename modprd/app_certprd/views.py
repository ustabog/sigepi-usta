# App de certificacion de productos - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_certprd.form import *
from django.urls import reverse_lazy
from modprd.app_certprd.models import *
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *

#----------VISTAS PARA EL REGISTRO DE MEDICIONES SIGEPI------------

#Vista para el registro de medicion

class vst_reg_med(CreateView):
    model= prd_med
    form_class = form_med
    template_name ='mod_cert_frm_registrar_med.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar medicion'
        context['action'] = 'Create'
        return context

#Vista para el listado de mediciones

class vst_list_med(ListView):
    model= prd_base
    template_name ='cn_trj_med.html'
    success_url = reverse_lazy('listar_med')
    context_object_name = 'Busqueda_med'

    def get_queryset(self):
        return prd_base.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar mediciones'
        context['action'] = 'List'
        return context

#Vista para la consulta de mediciones

class vst_cons_med(DetailView):
    model= prd_med
    template_name ='cn_det_med.html'   
    success_url = reverse_lazy('consultar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de mediciones'
        context['action'] = 'Consulte'
        return context
  

#Vista para la edicion de un mediciones

class vst_upd_med(UpdateView):
    model= prd_med
    form_class = form_med
    template_name ='mod_cert_editar_med.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar mediciones'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        return context

#Vista para la eliminacion de una medicion

class vst_del_med (DeleteView):
    model = prd_med
    template_name ='mod_cert_eliminar_med.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de mediciones'
        context['action'] = 'Delete'
        return context

    #----------VISTAS PARA EL REGISTRO DE CERTIFICACIONES SIGEPI------------

#Vista para el registro de medicion

class vst_reg_cert(CreateView):
    model= prd_cert
    form_class = form_cert
    template_name ='mod_cert_frm_registrar_cert.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar medicion'
        context['action'] = 'Create'
        return context

#Vista para la consulta de las certificaciones

class vst_cons_cert(DetailView):
    model= prd_cert
    template_name ='cn_det_cert.html'   
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de certificaciones'
        context['action'] = 'Consulte'
        return context
  

#Vista para la edicion de una certificacion

class vst_upd_cert(UpdateView):
    model= prd_cert
    form_class = form_cert
    template_name ='mod_cert_editar_cert.html'
    success_url = reverse_lazy('consultar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar certificacion'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        return context

#Vista para la eliminacion de una medicion

class vst_del_cert(DeleteView):
    model = prd_cert
    template_name ='mod_cert_eliminar_cert.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de certificacion'
        context['action'] = 'Delete'
        return context