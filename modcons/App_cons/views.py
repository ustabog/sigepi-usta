from django.shortcuts import render
#from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .form import *
from modadm.app_regusu.models import usu_inf_apps
from modadm.app_regusugr.models import usugr
from modadm.app_regusui.models import usui
from modadm.app_modadm.models import *

class consulta():
    #Clase que permite una consulta genérica desde la página principal sin estar registrado en el sistema.
    def vst_cons_inv(self,solicitud):
    #función para plantilla de consultas genérica
        return render(solicitud,"consulta.html")



class vts_ls_usu(ListView):
    # clase para listar usuarios del sistema
    model = usu
    form_class = frm_con_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usui(ListView):
    # clase para listar usuarios del sistema
    model = usui
    form_class = frm_con_usui
    template_name = 'cn_usui.html'
    success_url = reverse_lazy('cn_usui.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usugr(ListView):
    # clase que me lsta todos los grupos
    model = usugr
    form_class = frm_con_usugr
    template_name = 'cn_usugr.html'
    success_url = reverse_lazy('cn_usugr.html')
    success_message = 'listado cargado correctamente'

class vts_ls_mod(ListView):
    # clase que me lsta todos los modulos
    model = mod
    form_class = frm_con_mod
    template_name = 'con_mod.html'
    success_url = reverse_lazy('con_mod.html')


class ls_rol_usu(ListView):
    # clase para listar roles de usuarios del sistema
    model = usu_inf_apps
    form_class = frm_rol_usu
    template_name = 'listarrol.html'
    success_url = reverse_lazy('cn_usu')
    success_message = 'listado cargado correctamente'

class mod_usu(UpdateView):
    model = usu
    form_class = frm_con_usu
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('mod_usu.html')
    success_message = 'modificado correctamente'
