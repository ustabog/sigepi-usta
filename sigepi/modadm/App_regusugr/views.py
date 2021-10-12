from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .form import *
from modadm.App_regusugr.models import usugr
from modcons.App_cons.form import frm_con_usugr
from modcons.App_cons.views import vts_ls_usugr

class vts_reg_usugr(CreateView):
    #Clase que devuelve un formulario para registro de usuario grupo
    form_class = frm_con_usugr
    template_name = 'nvo_usugr_prb.html'
    success_url = reverse_lazy('cons_usugr')
    success_message = "El usuario fue creado correctamente"

class vts_selc_usugr_mod(vts_ls_usugr):
    # clase para heredar la consulta de grupo
    template_name = 'sl_usugr.html'
    success_url = reverse_lazy('sl_usugr.html')

class vts_modf_usugr(UpdateView):
    #clase para modificar grupos
    model = usugr
    form_class = frm_con_usugr
    template_name = 'nvo_usugr_prb.html'
    success_url = reverse_lazy('cons_usugr')
