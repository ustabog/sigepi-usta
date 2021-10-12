from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from modcons.App_cons.form import frm_con_usui
from modcons.App_cons.views import vts_ls_usui
from modadm.App_regusui.models import usui
# Create your views here.



class vst_reg_usui(CreateView):
    #Clase que devuelve un formulario para registro de usuario institucion
    form_class = frm_con_usui
    template_name = 'nvo_usui_prb.html'
    success_url = reverse_lazy('cons_usui')
    success_message = "El usuario fue creado correctamente"

class vst_mod_reg_usui(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = usui
    form_class = frm_con_usui
    template_name = 'nvo_usui_prb.html'
    success_url = reverse_lazy('cons_usui')

class vts_selec_usui_cons(vts_ls_usui):
    template_name = 'sl_usui.html'
    success_url = reverse_lazy('sl_usui.html')
