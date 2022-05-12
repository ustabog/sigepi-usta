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
from modadm.App_regusu.models import *
#from modcons.App_cons.form import frm_con_usu
#from modcons.App_cons.views import vts_ls_usu

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
        return render(request,'App_regusu_frm_nvo_usu.html', data )

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
    exclude = ['password']
    template_name = 'App_regusu_frm_edt_usu.html'
    success_url = reverse_lazy('consulta_usuarios')

def eli_usu(request, id):
    usuario = get_object_or_404(usu, id=id)
    usuario.delete()
    messages.success(request, "Eliminado correctamente")
    return redirect(to="../cons_usus")

class func_usu():
    #clase que me almacena las vistas de la aplicacion registro de usuario
    #vista para listar usuarios
    def vst_ls_mod_usu(self, solicitud):
        #vista para istar los usuarios
        plt = loader.get_template('App_regusu_ls_usu.html')
        respuesta = plt.render()
        return HttpResponse(respuesta)

class vst_selc_usu_cons(vts_ls_usu, PermissionRequiredMixin):
    #funcion que me pinta la lista para modificar el usuario
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('sl_usu.html')

########## CRUD DISCAPACIDAD ###############################

class vts_reg_discapacidad(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = discapacidad
    form_class = frm_con_discapacidad
    template_name = 'App_regusu_frm_discapacidad.html'
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
    template_name = 'App_regusu_frm_discapacidad.html'
    success_url = reverse_lazy('cons_discapacidad')
    permission_required = 'discapacidad.change_discapacidad'

class vts_del_discapacidad(DeleteView, PermissionRequiredMixin):
    model = discapacidad
    template_name = 'App_regusu_del_discapacidad.html'
    success_url = reverse_lazy('cons_discapacidad')
    permission_required = 'discapacidad.delete_discapacidad'

##### CRUD INFORMACION PERSONAL #######################################

class vts_reg_usu_inf_pers(CreateView, PermissionRequiredMixin):
    #crear información de las personas
    model = usu_inf_pers
    form_class = frm_con_usu_inf_pers
    template_name = 'App_regusu_frm_infopers.html'
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
    template_name = 'App_regusu_frm_infopers.html'
    success_url = reverse_lazy('cons_infopers')
    permission_required = 'usu_inf_pers.change_usu_inf_pers'

##### CRUD INFORMACION DE CONTACTO #######################################

class vts_reg_contc(CreateView, PermissionRequiredMixin):
    # Clase para crear informacion de contacto del usuario
    model = usu_inf_contac
    form_class = frm_con_info_contact
    template_name = 'App_regusu_frm_infocontc.html'
    success_url = reverse_lazy('cons_infocontc')
    success_message = 'La discapacidad fue creada satisfactoriamente'
    permission_required = 'usu_inf_contac.add_usu_inf_contac'

class vts_ls_contc(ListView, PermissionRequiredMixin): #hereda de listwview
    # Consulta de informacion de contacto del usuario
    model = usu_inf_contac
    form_class = frm_con_info_contact
    template_name = 'cn_infcontc.html'
    success_url = reverse_lazy('cn_infocontc.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'usu_inf_contac.view_usu_inf_contac'

class vts_edt_contc(UpdateView, PermissionRequiredMixin):
    # Clase que edita la informacion de contacto del usuario
    model = usu_inf_contac
    form_class = frm_con_info_contact
    template_name = 'App_regusu_frm_infocontc.html'
    success_url = reverse_lazy('cons_infocontc')
    permission_required = 'usu_inf_contac.change_usu_inf_contac'

##### CRUD INFORMACION DE CONTACTO #######################################

class vts_reg_red_soc(CreateView, PermissionRequiredMixin):
    # Clase para crear informacion de contacto del usuario
    model = red_soc
    form_class = frm_con_red_social
    template_name = 'App_regusu_frm_red_soc.html'
    success_url = reverse_lazy('cons_red_soc')
    success_message = 'La discapacidad fue creada satisfactoriamente'
    permission_required = 'red_soc.add_red_soc'

class vts_ls_red_soc(ListView, PermissionRequiredMixin): #hereda de listwview
    # Consulta de informacion de contacto del usuario
    model = red_soc
    form_class = frm_con_red_social
    template_name = 'cn_red_soc.html'
    success_url = reverse_lazy('cn_red_soc.html')
    success_message = 'Listado cargado correctamente'
    permission_required = 'red_soc.view_usu_red_soc'

class vts_edt_red_soc(UpdateView, PermissionRequiredMixin):
    # Clase que edita la informacion de contacto del usuario
    model = red_soc
    form_class = frm_con_red_social
    template_name = 'App_regusu_frm_red_soc.html'
    success_url = reverse_lazy('cons_red_soc')
    permission_required = 'red_soc.change_red_soc'

