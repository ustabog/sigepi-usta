from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render
#from rest_framework import viewsets
from .models import *
from modpry.app_evapry.models import *
from modpry.app_evapry.form import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#------------ registro de una evaluación de proyectos ---------
class vst_reg_evapry(CreateView):
    #Clase de la vista de registro de una evaluación de proyecto
    model = eva_pry
    form_class = frm_evapry
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_evapry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva evaluación de proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_evapry(ListView):
    # clase para listar las evaluaciones de proyectos
    model = eva_pry
    template_name = 'cn_trj_eva.html'
    queryset = eva_pry.objects.filter(eva_archi=0)
    context_object_name = 'lista_evapry'

class vst_add_eva(ListView):
    #clase para añadir información de la evaluación de proyectos desde el botón de añadir de la tarjeta
    template_name = 'mod_pry_add_eva.html'
    queryset = eva_pry.objects.filter(eva_archi=0)
    context_object_name = 'lista_evapry'

class vst_edit_evapry(UpdateView):
    #Clase de la vista para actualizar o editar la evaluación del proyecto
    model = eva_pry
    form_class = frm_evapry
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_evapry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar la evaluación del proyecto' 
        context ['entity'] = 'Evaluación'
        context ['list_url'] = reverse_lazy('cn_evapry')
        context ['action'] = 'edit'
        return context
#----------------------- Para un criterio ----------------
class vst_crear_crit(CreateView):
    #Clase de la vista de registro de un criterio de evaluación
    model = crit_eva
    form_class = frm_criterio
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_crit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nuevo criterio evaluación de proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_crit(ListView):
    # clase para listar los criterios de evaluación
    model = crit_eva
    template_name = 'cn_det_eva.html'
    queryset = eva_pry.objects.order_by('nomb_eva')
    context_object_name = 'lista_evapry'

    def get_context_data(self, **kwargs):
        context = super(vst_ls_evapry, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de evaluación de proyectos'
        return context

class vst_edit_crit(UpdateView):
    #Clase de la vista para actualizar o editar un criterio de evaluación
    model = crit_eva
    form_class = frm_criterio
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_crit')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un criterio de evaluación' 
        context ['entity'] = 'Criterio'
        context ['list_url'] = reverse_lazy('cn_crit')
        context ['action'] = 'edit'
        return context
#----------------------- Para una rúbrica ----------------
class vst_crear_rub(CreateView):
    #Clase de la vista de registro de una rúbrica de evaluación de proyecto
    model = rubr_eva
    form_class = frm_rubrica
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_rub')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Nueva rúbrica de evaluación' 
        context ['action'] = 'add'
        return context

class vst_ls_rub(ListView):
    # clase para listar las rúbricas de evaluación
    model = rubr_eva
    template_name = 'cn_det_eva.html'
    queryset = rubr_eva.objects.order_by('nomb_rub')

    def get_context_data(self, **kwargs):
        context = super(vst_ls_rub, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de rúbricas'
        return context

class vst_edit_rub(UpdateView):
    #Clase de la vista para actualizar o editar la rúbrica de evaluación
    model = rubr_eva
    form_class = frm_rubrica
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_rub')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar la rúbrica de evaluación' 
        context ['list_url'] = reverse_lazy('cn_rub')
        context ['action'] = 'edit'
        return context
#----------------------- Para un rango de evaluación -----
class vst_crear_rango(CreateView):
    #Clase de la vista para crear un rango de evaluación
    model = rango_eva
    form_class = frm_rangoeva
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_rango')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Rango de rúbrica' 
        context ['action'] = 'add'
        return context

class vst_ls_rango(ListView):
    # clase para listar los rangos de evaluación
    model = rango_eva
    template_name = 'cn_det_eva.html'
    queryset = rango_eva.objects.order_by('nombre_rango')

class vst_edit_rng(UpdateView):
    #Clase de la vista para actualizar o editar un rango de evaluación
    model = rango_eva
    form_class = frm_rangoeva
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_rango')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un rango de evaluación' 
        context ['entity'] = 'Rango'
        context ['list_url'] = reverse_lazy('cn_rango')
        context ['action'] = 'edit'
        return context

#----------------------- Para un resultado ---------------
class vst_crear_resul(CreateView):
    #Clase de la vista de resultado de una evaluación de un proyecto
    model = res_eva
    form_class = frm_resultado
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_res')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Resultado de la evaluación de un proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_resultado(ListView):
    # clase para listar los resultados de evaluación
    model = res_eva
    template_name = 'cn_det_eva.html'
    queryset = res_eva.objects.order_by('valor_total')

class vst_edit_res(UpdateView):
    #Clase de la vista para actualizar o editar un resultado de evaluación
    model = res_eva
    form_class = frm_resultado
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_res')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar resultado de una evaluación' 
        context ['entity'] = 'Resultado'
        context ['list_url'] = reverse_lazy('cn_res')
        context ['action'] = 'edit'
        return context
#----------------------- Para tipo de evaluación ---------
class vst_crear_tipoeva(CreateView):
    #Clase de la vista para añadir el tipo de evaluación de un proyecto
    model = tipo_eva
    form_class = frm_tipoeva
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_tipoeva')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Tipo de evaluación de un proyecto' 
        context ['action'] = 'add'
        return context

class vst_ls_tipoeva(ListView):
    # clase para listar los tipos de evaluación
    model = tipo_eva
    template_name = 'cn_det_eva.html'
    queryset = tipo_eva.objects.order_by('tipo_eva')

class vst_edit_tipo(UpdateView):
    #Clase de la vista para actualizar o editar un tipo de evaluación
    model = tipo_eva
    form_class = frm_tipoeva
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_tipoeva')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un tipo de evaluación' 
        context ['entity'] = 'Tipo de evaluación'
        context ['list_url'] = reverse_lazy('cn_tipoeva')
        context ['action'] = 'edit'
        return context

#----------------------- Para una definición ------------
class vst_crear_defi(CreateView):
    #Clase de la vista crear un comentario, definición, comentario, etc
    model = defi
    form_class = frm_defi
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_defi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Definciones, comentarios, recomendaciones, etc' 
        context ['action'] = 'add'
        return context

class vst_ls_defi(ListView):
    # clase para listar las definiciones, comentarios, recomendaciones, etc.
    model = defi
    template_name = 'cn_det_eva.html'
    queryset = defi.objects.order_by('tipo_def')

class vst_edit_defi(UpdateView):
    #Clase de la vista para actualizar o editar una definción, comentario, recomenadación
    model = defi
    form_class = frm_defi
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_defi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar una definción' 
        context ['entity'] = 'Definición'
        context ['list_url'] = reverse_lazy('cn_defi')
        context ['action'] = 'edit'
        return context

