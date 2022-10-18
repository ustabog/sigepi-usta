from multiprocessing import context
from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from modadm.app_regusui.form import frm_cons_usui
from modadm.app_modadm.models import usui
from django.contrib.auth.models import User, Permission, Group
#Create your views here.



class vst_reg_usui(CreateView):
    #Clase que devuelve un formulario para registro de usuario institucion
    form_class = frm_cons_usui
    template_name = 'App_regusui_nvo_usui.html'
    success_url = reverse_lazy('cons_usui')
    success_message = "El usuario fue creado correctamente"

class vst_mod_reg_usui(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = User
    form_class = frm_cons_usui
    template_name = 'nvo_usui_prb.html'
    success_url = reverse_lazy('cons_usui')


class vts_usui_cons(ListView):
    model = usui
    form_class = frm_cons_usui
    template_name ='cn_usui.html'
    success_url = reverse_lazy('cn_usui.html')
    success_message = 'listado cargado correctamente'
    context = {'object_list':form_class}

def vts_ls_inst(request):
    user_inst = usui.objects.get(id_usu_adm=request.user.id)
    template = 'cn_usui.html'
    context = {'instituciones': user_inst}
    return render(request, template, context)


class vts_selec_usui_cons(ListView):
    # clase para listar usuarios del sistema
    model = User
    form_class = frm_cons_usui
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

# class vts_selec_usui_cons(vts_ls_usui):
#     template_name = 'sl_usui.html'
#     success_url = reverse_lazy('sl_usui.html')
