from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from modpry.App_crono.form import *
#from rest_framework import viewsets
from .models import *


#------------------------------ CRONOGRAMA ---------------------
class vst_crea_crono(CreateView):
    #Clase de la vista para crear un cronograma 
    model = crono_pry
    form_class = frm_crea_crono
    template_name = 'iu_pub/serv_iu/App_crono_frm_crearcrono.html'
    success_url= reverse_lazy('cn_crono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nuevo cronograma' 
        context ['action'] = 'add'
        return context


class vst_ls_crono(ListView):
    # clase para listar los cronogramas de un usuario
    model = crono_pry
    template_name = 'cn_crono.html'
    queryset = crono_pry.objects.order_by('nomb_crono')
    context_object_name = 'lista_crono'


    def get_context_data(self, **kwargs):
        context = super(vst_ls_crono, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Cronogramas'
        return context


#------------------------------ ETAPA ---------------------
class vst_crea_etapa(CreateView):
    #Clase de la vista para crear una etapa
    model = etapa
    form_class = frm_crea_etapa
    template_name = 'iu_pub/serv_iu/App_regcrono_frm_crearcrono.html' 
    success_url= reverse_lazy('etapa_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva etapa' 
        context ['action'] = 'add'
        return context

class vst_ls_etapa(ListView):
    # clase para listar las etapas de un cronograma
    model = etapa
    template_name = 'cn_etapa'
    queryset = etapa.objects.order_by('nombre_eta')
    context_object_name = 'lista_etapa'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_etapa, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Etapas'
        return context
'''
#------------------------------ FASE ---------------------
class vst_crea_fase(CreateView):
    #Clase de la vista para crear una fase
    model = fase
    form_class = frm_crea_fase
    template_name = 'iu_pub/serv_iu/App_regcrono_frm_crearcrono.html' 
    success_url= reverse_lazy('fase_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva fase' 
        context ['action'] = 'add'
        return context

class vst_ls_fase(ListView):
    # clase para listar las fases de una etapa
    model = fase
    template_name = 'cn_fase'
    queryset = fase.objects.order_by('nombre_fase')
    context_object_name = 'lista_etapa'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_fase, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Fases'
        return context
#------------------------------ PROCESO ---------------------
class vst_crea_proc(CreateView):
    #Clase de la vista para crear un proceso
    model = proceso
    form_class = frm_crea_proc
    template_name = 'iu_pub/serv_iu/App_regcrono_frm_crearcrono.html' 
    success_url= reverse_lazy('proceso_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nuevo proceso' 
        context ['action'] = 'add'
        return context

class vst_ls_proc(ListView):
    # clase para listar los procesos de una fase
    model = proceso
    template_name = 'cn_proceso'
    queryset = proceso.objects.order_by('nombre_proc')
    context_object_name = 'lista_proceso'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_proc, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Procesos'
        return context
#------------------------------ TAREA ---------------------
class vst_crea_tarea(CreateView):
    #Clase de la vista para crear una tarea
    model = tarea
    form_class = frm_crea_tarea
    template_name = 'iu_pub/serv_iu/App_regcrono_frm_crearcrono.html' 
    success_url= reverse_lazy('tarea_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva tarea' 
        context ['action'] = 'add'
        return context

class vst_ls_tarea(ListView):
    # clase para listar las tareas de un proceso
    model = tarea
    template_name = 'cn_tarea'
    queryset = tarea.objects.order_by('nombre_tarea')
    context_object_name = 'lista_tarea'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_tarea, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Tareas'
        return context

#------------------------------ ACTIVIDAD ---------------------
class vst_crea_acti(CreateView):
    #Clase de la vista para crear una actividad
    model = acti
    form_class = frm_crea_acti
    template_name = 'iu_pub/serv_iu/App_regcrono_frm_crearcrono.html' 
    success_url= reverse_lazy('proceso_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva actividad' 
        context ['action'] = 'add'
        return context

class vst_ls_acti(ListView):
    # clase para listar las tareas de un proceso
    model = acti
    template_name = 'cn_acti'
    queryset = acti.objects.order_by('nombre_acti')
    context_object_name = 'lista_acti'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_acti, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Actividades'
        return context
'''