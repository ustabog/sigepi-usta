from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
#from rest_framework import viewsets
from .models import *
from modpry.App_evapry.models import *
from modpry.App_evapry.form import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#---- registro de una evaluación de proyectos ---------
class vts_reg_evapry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = eva_pry
    form_class = frm_reg_evapry
    template_name = 'iu_pub/serv_iu/App_regpry_frm_evapry.html'
    success_url= reverse_lazy('cn_evapry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva evaluación de proyecto' 
        context ['action'] = 'add'
        return context

class vts_ls_evapry(ListView):
    # clase para listar las evaluaciones de proyectos
    model = eva_pry
    template_name = 'cn_evapry.html'
    queryset = pry_base.objects.order_by('nombre_eva')
    context_object_name = 'lista_evapry'

    def get_context_data(self, **kwargs):
        context = super(vts_ls_evapry, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de proyectos'
        return context
