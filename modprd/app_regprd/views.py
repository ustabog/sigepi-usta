# App de registro de producto - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 19 -08 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_regprd.form import *
from django.urls import reverse_lazy
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *


class ini_regprd():
    def view_prd(request):
        return render(request, 'app_regprd_iu.html')

class vst_regprd(CreateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_frm_registrar.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_base.objects.filter(id_usu =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'registrar un producto'
        context['action'] = 'add'
        return context

class vst_regreqexist(CreateView):
    model= prd_req_Exist
    template_name ='mod_prd_frm_reqexist.html'
    success_url = reverse_lazy('cn_prd')

    def get_queryset(self):
        return prd_req_Exist.objects.filter(id_reqexs =self.request.user)