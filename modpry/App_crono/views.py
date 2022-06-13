from django.shortcuts import render
from django.shortcuts import render, redirect
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from modpry.app_crono.form import *
#from contexto.lectura import leer_texto
#from rest_framework import viewsets
from .models import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#------------------------------ CRONOGRAMA ---------------------
class vst_crea_crono(CreateView):
    #Clase de la vista para crear un cronograma 
    model = crono_pry
    form_class = frm_crea_crono
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_crearcrono.html'
    success_url= reverse_lazy('consultas/apps_cons/cn_crono')

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

class vts_edit_crpno(UpdateView):
    #Clase de la vista para actualizar o editar el cronograma de un proyecto 
    model = crono_pry
    form_class = frm_crea_crono
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_editcrono.html'
    success_url= reverse_lazy('cn_crono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un cronograma' 
        context ['entity'] = 'crono_pry'
        context ['list_url'] = reverse_lazy('cn_crono')
        context ['action'] = 'edit'
        return context

#------------------------------ ETAPA ---------------------
class vst_crea_etapa(CreateView):
    #Clase de la vista para crear una etapa
    model = etapa
    form_class = frm_crea_etapa
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_funcrono.html' 
    success_url= reverse_lazy('cn_crono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva etapa' 
        context ['action'] = 'add'
        return context

class vst_ls_etapa(ListView):
    # clase para listar las etapas de un cronograma
    model = etapa
    template_name = 'cn_funcrono'
    queryset = etapa.objects.order_by('nombre_eta')
    context_object_name = 'lista_etapa'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_etapa, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Etapas'
        return context

class vts_edit_etapa(UpdateView):
    #Clase de la vista para actualizar o editar la etapa de un cronograma
    model = etapa
    form_class = frm_crea_etapa
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_edifuncrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar etapa' 
        context ['entity'] = 'etapa'
        context ['list_url'] = reverse_lazy('cn_funcrono')
        context ['action'] = 'edit'
        return context

#------------------------------ FASE ---------------------
class vst_crea_fase(CreateView):
    #Clase de la vista para crear una fase
    model = fase
    form_class = frm_crea_fase
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_funcrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva fase' 
        context ['action'] = 'add'
        return context

class vst_ls_fase(ListView):
    # clase para listar las fases de una etapa
    model = fase
    template_name = 'cn_funcrono'
    queryset = fase.objects.order_by('nombre_fase')
    context_object_name = 'lista_etapa'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_fase, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Fases'
        return context

class vts_edit_fase(UpdateView):
    #Clase de la vista para actualizar o editar la fase de una etapa
    model = fase
    form_class = frm_crea_fase
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_edifuncrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar fase' 
        context ['entity'] = 'fase'
        context ['list_url'] = reverse_lazy('cn_funcrono')
        context ['action'] = 'edit'
        return context
#------------------------------ PROCESO ---------------------
class vst_crea_proc(CreateView):
    #Clase de la vista para crear un proceso
    model = proceso
    form_class = frm_crea_proc
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_funcrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nuevo proceso' 
        context ['action'] = 'add'
        return context

class vst_ls_proc(ListView):
    # clase para listar los procesos de una fase
    model = proceso
    template_name = 'cn_funcrono'
    queryset = proceso.objects.order_by('nombre_proc')
    context_object_name = 'lista_proceso'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_proc, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Procesos'
        return context

class vts_edit_proc(UpdateView):
    #Clase de la vista para actualizar o editar un proceso dentro de una etapa
    model = proceso
    form_class = frm_crea_proc
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_edifuncrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar proceso' 
        context ['entity'] = 'proceso'
        context ['list_url'] = reverse_lazy('cn_funcrono')
        context ['action'] = 'edit'
        return context
#------------------------------ TAREA ---------------------
class vst_crea_tarea(CreateView):
    #Clase de la vista para crear una tarea
    model = tarea
    form_class = frm_crea_tarea
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_funcrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva tarea' 
        context ['action'] = 'add'
        return context

class vst_ls_tarea(ListView):
    # clase para listar las tareas de un proceso
    model = tarea
    template_name = 'cn_funcrono'
    queryset = tarea.objects.order_by('nombre_tarea')
    context_object_name = 'lista_tarea'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_tarea, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Tareas'
        return context

class vts_edit_tarea(UpdateView):
    #Clase de la vista para actualizar o editar la tarea de un proceso
    model = tarea
    form_class = frm_crea_tarea
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_edifuncrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar tarea' 
        context ['entity'] = 'tarea'
        context ['list_url'] = reverse_lazy('cn_funcrono')
        context ['action'] = 'edit'
        return context

#------------------------------ ACTIVIDAD ---------------------
class vst_crea_acti(CreateView):
    #Clase de la vista para crear una actividad
    model = acti
    form_class = frm_crea_acti
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_funcrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva actividad' 
        context ['action'] = 'add'
        return context

class vst_ls_acti(ListView):
    # clase para listar las tareas de un proceso
    model = acti
    template_name = 'cn_funcrono'
    queryset = acti.objects.order_by('nombre_acti')
    context_object_name = 'lista_acti'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_acti, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Actividades'
        return context

class vts_edit_acti(UpdateView):
    #Clase de la vista para actualizar o editar una actividad dentro de una tarea
    model = acti
    form_class = frm_crea_acti
    template_name = 'iu_pub/serv_iu/modpry/app_crono_frm_edifuncrono.html'
    success_url= reverse_lazy('cn_funcrono')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar actividad' 
        context ['entity'] = 'acti'
        context ['list_url'] = reverse_lazy('cn_funcrono')
        context ['action'] = 'edit'
        return context
