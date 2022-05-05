from multiprocessing import context
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
#from rest_framework import viewsets
from .models import *
from modpry.App_regpry.models import *
from modpry.App_regpry.form import *

class vts_reg_pry(CreateView):
    #Clase de la vista de registro de proyecto 
    model = pry
    form_class = frm_reg_pry
    template_name = 'prysgp/app_pry/App_regpry_frm_crearpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto' 
        context ['action'] = 'add'
        return context

class vts_ls_pry(ListView):
    # clase para listar usuarios del sistema
    model = pry
    template_name = 'cn_pry.html'
    queryset = pry.objects.order_by('nombre_pry')
    context_object_name = 'lista_pry'
    #success_url = reverse_lazy('cn_pry.html')
    #success_message = 'listado cargado correctamente'

    def get_context_data(self, **kwargs):
        context = super(vts_ls_pry, self).get_context_data(**kwargs)
        context ['titulo_pagina'] = 'Listado de proyectos'
        return context
        
'''
class vts_ls_usu(ListView):
    # clase para listar usuarios del sistema
    model = pry
    template_name = 'cn_pry.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Listado de proyectos'     
 '''


class vts_edit_pry(UpdateView):
    #Clase de la vista para actualizar el registro de proyecto 
    model = pry
    form_class = frm_reg_pry
    template_name = 'prysgp/app_pry/App_regpry_frm_crearpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un proyecto' 
        context ['entity'] = 'pry'
        context ['list_url'] = reverse_lazy('cn_pry')
        context ['action'] = 'edit'
        return context



#---------------------------Se elimina el proyecto de la base datos tambien-----------------------------
#class vts_reg_pry(DeleteView):
    #Clase de la vista para borrar el registro de proyecto 
#    model = proyecto
#    success_url = reverse_lazy('') #Retornar a la pagina de consultar proyecto


'''
class vst_pry():
#Función para eliminar proyecto pero aún se almacena en la base de datos

    def eli_pry(self):
        pry = get_object_or_404(pry)
        pry.delete()
        messages.success(request, "Eliminado correctamente")
        return redirect(to="../cn_pry")
    
    def vts_eli_pry(self, request):
        pry = pry.objects.get(pry)
        pry.delete()
        return redirect('..+cn_pry/')

'''