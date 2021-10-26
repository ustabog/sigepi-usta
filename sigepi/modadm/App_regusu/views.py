from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.views.generic.base import View
#from rest_framework import viewsets
from .serializers import *
from .models import *
from .form import *
from plantillas import *

from modadm.App_regusu.models import *
#from modcons.App_cons.form import frm_con_usu
#from modcons.App_cons.views import vts_ls_usu

#vista de prueba
def prueba (request):
    return HttpResponse("Bienvenido")

#vista registro de usuario
class vts_reg_usu_su(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_con_usu
    template_name = 'nvo_usu_prb.html'
    success_url = reverse_lazy('consulta_usuarios')
    success_message = "El usuario fue creado correctamente"


class func_usu():
    #clase que me almacena las vistas de la aplicacion registro de usuario
    #vista para listar usuarios
    def vst_ls_mod_usu(self, solicitud):
        #vista para istar los usuarios
        plt = loader.get_template('sl_usu.html')
        respuesta = plt.render()
        return HttpResponse(respuesta)

#################Clase traida del modulo de consulta#######################
class vts_ls_usu(ListView):
    # clase para listar usuarios del sistema
    model = User
    form_class = frm_con_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'
###########################################################################

class vst_selc_usu_cons(vts_ls_usu):
    #funcion que me pinta la lista para modificar el usuario
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('sl_usu.html')

class vst_mod_reg_usu(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = User
    form_class = frm_con_usu
    template_name = 'nvo_usu_prb.html'
    success_url = reverse_lazy('consulta_usuarios')

class vts_reg_usu_su(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_con_usu
    template_name = 'nvo_usu_prb.html'
    success_url = reverse_lazy('consulta_usuarios')
    success_message = "El usuario fue creado correctamente"

class infoperslList(ListView): #hereda de listwview
    model = usu_inf_pers
    #MODIFICADO
    template_name = 'infopers.html'
    #ORIGINAL
    #template_name = 'moduloAdm/usuarios/infopers.html'

class infopersCree(CreateView):
    model = usu_inf_pers  
    form_class = frm_reg_usu_pers
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')


class infopersCreate(CreateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    #### Original
    #template_name = 'backend/registro_usuario/crearinfopers.html'
    template_name = 'registro_usuario/crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(infopersCreate, self).form_valid(form)

class infopersUpdate(UpdateView):
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersDelete(DeleteView):
    model = usu_inf_pers
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('infopers')

# class Torneo_ListView(ListView):
#    template_name = 'torneos/torneo_listar.html'

#    def get_queryset(self, *args, **kwargs):
#        return Torneo.objects.filter(user=self.request.user)
