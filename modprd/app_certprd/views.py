# App de certificacion de productos - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 22 -09 -2022

from re import X
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
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
    success_url = reverse_lazy('listar_prd' )

    def get_object(self) :
        instance= self.model.objects.get(id_med=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar mediciones'
        context['action'] = 'update'
        context ['entity'] = 'cert'
        context['object'] = self.get_object()
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

#Vista para la archivacion de certificacions

class vst_archi_med(TemplateView):
    model = prd_categ
    template_name ='mod_cert_eliminar_med.html'
    success_url = reverse_lazy('listar_med')

    def post(self,request,id):
        med= prd_med.objects.get(id_med=id)
        if request.method == 'POST':
            med.archivo= True
            med.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar certificacions'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de certificacions

def vst_search_med( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        medicion= prd_med.objects.filter(nom_med__contains = buscar)
        context = {
        'buscar':buscar,
        'medicion':medicion
        }
        return render(request, 'cn_search_med.html', context)
    else:
        return render(request, 'cn_search_med.html', {})

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

#Vista para la archivacion de certificacions

class vst_archi_cert(TemplateView):
    model = prd_cert
    template_name ='mod_cer_eliminar_cert.html'
    success_url = reverse_lazy('listar_cert')

    def post(self,request,id):
        cert= prd_categ.objects.get(id_cert=id)
        if request.method == 'POST':
            cert.archivo= True
            cert.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar certificacions'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de certificacion

def vst_search_cert( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        certificacion= prd_cert.objects.filter(nom_cert__contains = buscar)
        context = {
        'buscar':buscar,
        'certificacion':certificacion
        }
        return render(request, 'cn_search_cert.html', context)
    else:
        return render(request, 'cn_search_cert.html', {})