from django.shortcuts import render
#from django.contrib.auth.models import User
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib import messages
from .form import *
from modadm.app_regusu.models import rl_usu_rol
from modadm.app_regusugr.models import usugr
from modadm.app_regusui.models import usui
from modadm.app_modadm.models import *

#Clase que permite una consulta genérica desde la página principal sin estar registrado en el sistema.
class consulta():
    def vst_cons_inv(self,solicitud):
    #función para plantilla de consultas genérica
        return render(solicitud,"consulta.html")

# clase para listar usuarios del sistema
class vts_ls_usu(ListView):
    model = usu
    form_class = frm_cons_usu
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usui(ListView):
    # clase para listar usuarios del sistema
    model = usui
    form_class = frm_cons_usui
    template_name = 'cn_usui.html'
    success_url = reverse_lazy('cn_usui.html')
    success_message = 'listado cargado correctamente'

class vts_ls_usugr(ListView):
    # clase que me lsta todos los grupos
    model = usugr
    form_class = frm_cons_usugr
    template_name = 'cn_usugr.html'
    success_url = reverse_lazy('cn_usugr.html')
    success_message = 'listado cargado correctamente'

class vts_ls_mod(ListView):
    # clase que me lsta todos los modulos
    model = adm_mod
    form_class = frm_cons_mod
    template_name = 'con_mod.html'
    success_url = reverse_lazy('con_mod.html')


class ls_rol_usu(ListView):
    # clase para listar roles de usuarios del sistema
    model = rl_usu_rol
    form_class = frm_cons_rl_rol_usu
    template_name = 'listarrol.html'
    success_url = reverse_lazy('cn_usu')
    success_message = 'listado cargado correctamente'

class mod_usu(UpdateView):
    model = usu
    form_class = frm_cons_usu
    template_name = 'sl_usu.html'
    success_url = reverse_lazy('mod_usu.html')
    success_message = 'modificado correctamente'
