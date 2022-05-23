from multiprocessing import context
from django.views.generic import UpdateView,FormView, CreateView, ListView
from django.urls import reverse_lazy
#from rest_framework import viewsets
from .models import *
from modpry.App_regpry.models import *
from modpry.App_regpry.form import *

'''
class vts_reg_pryi(CreateView):
    #Clase de la vista de registro de proyecto 
    model = inf_ pry
    form_class = frm_reg_pryi
    template_name = 'prysgp/app_pry/App_regpry_frm_crearpry.html'
    success_url= reverse_lazy('cn_pry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un proyecto' 
        context ['action'] = 'add'
        return context
'''