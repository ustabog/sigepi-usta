from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse, request
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
from .models import *
from .form import *
from modadm.App_regusu.models import *
#from modcons.App_cons.form import frm_con_usu
#from modcons.App_cons.views import vts_ls_usu

class vts_reg_usu(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    model = usu 
    template_name = 'App_regusu_frm_nvo_usu.html'
    form_class = frm_con_usu
    success_url = reverse_lazy('consulta_usuarios')
    success_message = "El usuario fue creado correctamente"

class vts_ls_usu(ListView):
    # clase para listar usuarios del sistema
    model = usu
    form_class = frm_con_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

class vst_mod_usu(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = usu
    form_class = frm_con_usu
    template_name = 'App_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('consulta_usuarios')

def vts_eli_usu(request, id):
    usuario = usu.objects.get(id = id)
    usuario.delete()
    return redirect('..cons_usus/')

class infopersDelete(DeleteView):
    #eliminar usuarios
    model = usu
    template_name = 'App_regusu_verificacion.html'
    success_url = reverse_lazy('infopers')
############FIN - Registro como invitado################

class func_usu():
    #clase que me almacena las vistas de la aplicacion registro de usuario
    #vista para listar usuarios
    def vst_ls_mod_usu(self, solicitud):
        #vista para istar los usuarios
        plt = loader.get_template('App_regusu_ls_usu.html')
        respuesta = plt.render()
        return HttpResponse(respuesta)

##################Clase traida del modulo de consulta######################

###########################################################################

class vst_selc_usu_cons(vts_ls_usu):
    #funcion que me pinta la lista para modificar el usuario
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('sl_usu.html')

def vts_eli_usu(request, id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    return redirect('..+cons_usus/')

###################CREAR USUARIO DESDE ADMIN#########################

class infopersCreate(CreateView):
    #información de los usuarios creados
    model = usu_inf_pers  
    form_class = frm_reg_usu_pers
    template_name = 'App_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return redirect('/infopers')

class infoperslList(ListView): #hereda de listwview
    #información de las personas
    model = usu_inf_pers
    template_name = 'App_regusu_ls_infopers.html'

class infopersCreate(CreateView):
    #crear información de las personas
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'App_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(infopersCreate, self).form_valid(form)

class infopersUpdate(UpdateView):
    #modificar la información de los usuarios
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'App_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersDelete(DeleteView):
    #eliminar usuarios
    model = usu_inf_pers
    template_name = 'App_regusu_verificacion.html'
    success_url = reverse_lazy('infopers')

###################FIN CREAR USUARIO DESDE ADMIN#####################



# class Torneo_ListView(ListView):
#    template_name = 'torneos/torneo_listar.html'

#    def get_queryset(self, *args, **kwargs):
#        return Torneo.objects.filter(user=self.request.user)
