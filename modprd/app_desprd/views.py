# App de desarrollo de productos - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 20 -10 -2022


from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from modprd.app_certprd.form import *
from django.urls import reverse_lazy
from modprd.app_certprd.models import *
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *

    #----------VISTAS PARA EL REGISTRO DE ETAPAS SIGEPI------------

#Vista para el registro de etapa

class vst_reg_etp(CreateView):
    model= prd_etp
    form_class = form_etp
    template_name ='mod_cert_frm_registrar_etp.html'
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar etapa'
        context['action'] = 'Create'
        return context

#Vista para la consulta de las etapas

class vst_cons_etp(DetailView):
    model= prd_etp
    template_name ='cn_det_etp.html'   
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de etapa'
        context['action'] = 'Consulte'
        return context


#Vista para la edicion de una etapa

class vst_upd_etp(UpdateView):
    model= prd_etp
    form_class = form_etp
    template_name ='mod_cert_editar_etp.html'
    success_url = reverse_lazy('consultar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar etp'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        return context

#Vista para la eliminacion de una etapa

class vst_del_etp(DeleteView):
    model = prd_etp
    template_name ='mod_cert_eliminar_etp.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de etapa'
        context['action'] = 'Delete'
        return context

#Vista para la archivacion de certificacions

class vst_archi_etp(TemplateView):
    model = prd_etp
    template_name ='mod_cer_eliminar_cert.html'
    success_url = reverse_lazy('listar_cert')

    def post(self,request,id):
        etp= prd_etp.objects.get(id_etp=id)
        if request.method == 'POST':
            etp.archivo= True
            etp.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar etapa'
        context['action'] = 'Archivar'
        return context

    #----------VISTAS PARA EL REGISTRO DE DESARROLLOS SIGEPI------------

#Vista para el registro de desarrollos

class vst_reg_des(CreateView):
    model= prd_des
    form_class = ''
    template_name ='mod_cert_frm_registrar_etp.html'
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar etapa'
        context['action'] = 'Create'
        return context

#Vista para la consulta de los desarrollos

class vst_cons_des(DetailView):
    model= prd_des
    template_name ='cn_det_etp.html'   
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de etapa'
        context['action'] = 'Consulte'
        return context


#Vista para la edicion de un desarrollo

class vst_upd_etp(UpdateView):
    model= prd_des
    form_class = form_etp
    template_name ='mod_cert_editar_etp.html'
    success_url = reverse_lazy('consultar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar etp'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        return context

#Vista para la eliminacion de un desarrollo

class vst_del_des(DeleteView):
    model = prd_des
    template_name ='mod_cert_eliminar_etp.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de etapa'
        context['action'] = 'Delete'
        return context

#Vista para la archivacion de desarrollos

class vst_archi_etp(TemplateView):
    model = prd_des
    template_name ='mod_cer_eliminar_cert.html'
    success_url = reverse_lazy('listar_cert')

    def post(self,request,id):
        des= prd_des.objects.get(id_desprd=id)
        if request.method == 'POST':
            des.archivo= True
            des.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar etapa'
        context['action'] = 'Archivar'
        return context