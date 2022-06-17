from django.shortcuts import render, redirect
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
#from rest_framework import viewsets
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *

class vst_pry():
    #Clase que procesa las vistas del IU del registro de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_pry_iu.html")

#--------------------------- Registro de proyecto individual ---------------------------------
class vts_reg_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'iu_pub/serv_iu/modpry/mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto' 
        context ['action'] = 'add'
        return context

class vts_ls_pry(ListView):
    # clase para listar proyectos del sistema
    model = pry_base
    template_name = 'cn_general.html'
    queryset = pry_base.objects.order_by('nombre_pry')
    context_object_name = 'lista_pry'

    def get_context_data(self, **kwargs):
        context = super(vts_ls_pry, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de proyectos'
        return context

class vts_edit_pry(UpdateView):
    #Clase de la vista para actualizar el registro de un proyecto 
    model = pry_base
    form_class = frm_reg_pry
    template_name = 'iu_pub/serv_iu/modpry/mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_general')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un proyecto' 
        context ['entity'] = 'pry'
        context ['list_url'] = reverse_lazy('cn_general')
        context ['action'] = 'edit'
        return context

'''
Eliminar el proyecto de la base de datos
class vts_reg_pry(DeleteView):
    Clase de la vista para borrar el registro de proyecto 
    model = proyecto
    success_url = reverse_lazy('') #Retornar a la pagina de consultar proyecto
'''

def eli_pry(request,id):
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        PRY_ARCHIVADO == 1
        pry.delete()
        return redirect('cn_general')
    return render (request, 'pry/app_pry/modpry/mod_pry_frm_eli.html',{'pry_base': pry_base})

