# App de indicarrollo de visualizacion de investigadores - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#Fecha 8 -11 -2022

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from modprd.app_visprd.models import *
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *
from modprd.app_visprd.models import *
from itertools import chain
 
   
    #----------VISTAS PARA EL REGISTRO DE INDICADORES SIGEPI------------

#Vista para el registro de indicadores

class vst_reg_indic(CreateView):

    model= prd_indic
    form_class = ''
    template_name ='mod_cert_frm_registrar_etp.html'
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar etapa'
        context['action'] = 'Create'
        return context

#Vista para la consulta de los indicadores

class vst_cons_indic(DetailView):
    
    model= prd_indic
    template_name ='cn_det_etp.html'   
    success_url = reverse_lazy('listar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de etapa'
        context['action'] = 'Consulte'
        return context


#Vista para la edicion de un indicarrollo

class vst_upd_indic(UpdateView):

    model= prd_indic
    form_class = form_indic
    template_name ='mod_cert_editar_etp.html'
    success_url = reverse_lazy('consultar_etp')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar etp'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        return context

#Vista para la eliminacion de un indicarrollo

class vst_del_indic(DeleteView):
    model = prd_indic
    template_name ='mod_cert_eliminar_etp.html'
    success_url = reverse_lazy('listar_med')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de etapa'
        context['action'] = 'Delete'
        return context

#Vista para la archivacion de indicadores

class vst_archi_etp(TemplateView):
    model = prd_indic
    template_name ='mod_cer_eliminar_cert.html'
    success_url = reverse_lazy('listar_cert')

    def post(self,request,id):
        indic= prd_indic.objects.get(id_indicprd=id)
        if request.method == 'POST':
            indic.archivo= True
            indic.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar etapa'
        context['action'] = 'Archivar'
        return context

def vst_search_indic( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        indic= prd_base.objects.filter(nom_prd__contains = buscar)
        context = {
        'buscar':buscar,
        'medicion':indic
        }
        return render(request, 'cn_search_med.html', context)
    else:
        return render(request, 'cn_search_med.html', {})

