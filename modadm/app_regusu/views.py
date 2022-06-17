from django.shortcuts import get_object_or_404, render, redirect
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
from django.contrib.auth import authenticate
from django.contrib.auth.mixins import PermissionRequiredMixin
#from rest_framework import viewsets
from .models import *
from .form import *
from modadm.app_regusu.models import *
#from modcons.app_cons.form import frm_con_usu
#from modcons.app_cons.views import vts_ls_usu

##### CRUD USUARIO ######################################################

class vts_reg_usu(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    def vst_registro(self, request):
        data = {
            'form': frm_reg_usu()
        }
        if request.method == "POST":
            formulario = frm_reg_usu(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                usuario = formulario.cleaned_data.get('username')
                password = formulario.cleaned_data.get('password1')
                usuario = authenticate(username=usuario, password=password)
                login(request, usuario)
                return redirect(to='consulta_usuarios')
            data["form"] = formulario
        return render(request,'app_regusu_frm_nvo_usu.html', data )

class vts_ls_usu(ListView, PermissionRequiredMixin):
    # clase para listar usuarios del sistema
    model = usu
    form_class = frm_con_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

class vst_mod_usu(UpdateView, PermissionRequiredMixin):
    #clase que me modifca los usuarios para registro de usuario
    model = usu
    form_class = frm_con_usu
    exclude = ['passord']
    template_name = 'app_regusu_frm_edt_usu.html'
    success_url = reverse_lazy('consulta_usuarios')

def eli_usu(request, id):
    usuario = get_object_or_404(usu, id=id)
    usuario.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="../cons_usus")

# class vts_eli_usu(DeleteView):
#     #eliminar usuarios
#     model = usu
#     template_name = 'app_regusu_verificacion.html'
#     success_url = reverse_lazy('cn_usu.html')
############FIN - Registro como invitado################

class func_usu():
    #clase que me almacena las vistas de la aplicacion registro de usuario
    #vista para listar usuarios
    def vst_ls_mod_usu(self, solicitud):
        #vista para istar los usuarios
        plt = loader.get_template('app_regusu_ls_usu.html')
        respuesta = plt.render()
        return HttpResponse(respuesta)

class vst_selc_usu_cons(vts_ls_usu, PermissionRequiredMixin):
    #funcion que me pinta la lista para modificar el usuario
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('sl_usu.html')

###################CREAR USUARIO DESDE ADMIN#########################
class infopersCreate(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'app_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super(infopersCreate, self).form_valid(form)

class infoperslList(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = usu_inf_pers
    template_name = 'app_regusu_ls_infopers.html'
    
class infopersUpdate(UpdateView, PermissionRequiredMixin):
    #modificar la información de los usuarios
    model = usu_inf_pers
    form_class = frm_reg_usu_pers
    template_name = 'app_regusu_frm_crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersDelete(DeleteView, PermissionRequiredMixin):
    #eliminar usuarios
    model = usu_inf_pers
    template_name = 'app_regusu_verificacion.html'
    success_url = reverse_lazy('infopers')

########## CRUD DISCAPACIDAD ###############################

class vts_reg_discapacidad(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = discapacidad
    form_class = frm_con_discapacidad
    template_name = 'app_regusu_frm_discapacidad.html'
    success_url = reverse_lazy('cons_discapacidad')
    success_message = 'La discapacidad fue creada satisfactoriamente'
    permission_required = 'discapacidad.add_discapacidad'

class vts_ls_discapacidad(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = discapacidad
    form_class = frm_con_discapacidad
    template_name = 'cn_discapacidad.html'
    success_url = reverse_lazy('cn_discapacidad.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'discapacidad.view_discapacidad'

class vts_edt_discapacidad(UpdateView, PermissionRequiredMixin):
    #clase que almacena los modulos generales del sistema
    model = discapacidad
    form_class = frm_con_discapacidad
    template_name = 'app_regusu_frm_discapacidad.html'
    success_url = reverse_lazy('cons_discapacidad')
    permission_required = 'discapacidad.change_discapacidad'

class vts_del_discapacidad(DeleteView, PermissionRequiredMixin):
    model = discapacidad
    template_name = 'app_regusu_del_discapacidad.html'
    success_url = reverse_lazy('cons_discapacidad')
    permission_required = 'discapacidad.delete_discapacidad'

##### CRUD INFORMACION PERSONAL #######################################

class vts_reg_usu_inf_pers(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = usu_inf_pers
    form_class = frm_con_usu_inf_pers
    template_name = 'app_regusu_frm_infopers.html'
    success_url = reverse_lazy('cons_infopers')
    success_message = 'La discapacidad fue creada satisfactoriamente'
    permission_required = 'usu_inf_pers.add_usu_inf_pers'

class vts_ls_usu_inf_pers(ListView, PermissionRequiredMixin): #hereda de listwview
    #información de las personas
    model = usu_inf_pers
    form_class = frm_con_usu_inf_pers
    template_name = 'cn_infopers.html'
    success_url = reverse_lazy('cn_infopers.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'usu_inf_pers.view_usu_inf_pers'

class vts_edt_usu_inf_pers(UpdateView, PermissionRequiredMixin):
    #clase que almacena los modulos generales del sistema
    model = usu_inf_pers
    form_class = frm_con_usu_inf_pers
    template_name = 'app_regusu_frm_infopers.html'
    success_url = reverse_lazy('cons_infopers')
    permission_required = 'usu_inf_pers.change_usu_inf_pers'

class vts_del_usu_inf_pers(DeleteView, PermissionRequiredMixin):
    model = usu_inf_pers
    template_name = 'app_regusu_del_infopers.html'
    success_url = reverse_lazy('cons_infopers')
    permission_required = 'usu_inf_pers.delete_usu_inf_pers'
