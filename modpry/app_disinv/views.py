# App de diseño de un proyecto de investigación - Vistas para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 28 -07-2022

from django.shortcuts import render
from django.views.generic import UpdateView, CreateView, ListView
from django.urls import reverse_lazy
from .models import *
from modpry.app_disinv.models import *
from modpry.app_disinv.form import *

class vst_disinv():
    #Clase que procesa las vistas del IU del inicio de la aplicación de diseño de proyecto de investigación de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_disinv_iu.html")

# ------------ Vistas para registrar un diseño de un proyecto --------------
class vts_reg_dispry(CreateView):
#Clase de la vista de registro de un diseño de un proyecto
    model = dis_pry
    form_class = frm_reg_dispry
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_dispry')

    def get_queryset(self):
        return dis_pry.objects.filter(id_usu = self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un diseño de investigación' 
        context ['action'] = 'add'
        return context

class vst_ls_dispry(ListView):
# clase para listar diseños de proyectos de investigación en tarjeta 
    model = dis_pry
    template_name = 'cn_trj_dispry.html'
    context_object_name = 'lista_dispry'

    def get_queryset(self):
        return dis_pry.objects.filter(id_usu = self.request.user).filter(dis_archi=0)

class vts_edit_dispry(UpdateView):
#Clase de la vista para actualizar el registro de un diseño de investigación
    model = dis_pry
    form_class = frm_reg_dispry
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_dispry')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un diseño' 
        context ['entity'] = 'dispry'
        context ['list_url'] = reverse_lazy('cndispry')
        context ['action'] = 'edit'
        return context

class vts_ls_detdis(ListView):
    #Clase de la vista de una consulta en detalle de un diseño de investigación
    model = dis_pry
    form_class = frm_reg_dispry
    template_name = 'mod_pry_add_regdis.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Añadir información del diseño de un proyecto' 
        context ['action'] = 'add'
        return context

# ------------ Vistas para un tema --------------
class vts_reg_tema(CreateView):
#Clase de la vista de registro de un tema de un proyecto
    model = tema
    form_class = frm_reg_tema
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un tema' 
        context ['action'] = 'add'
        return context

class vst_ls_tema(ListView):
    # clase para listar temas del sistema
    model = tema
    template_name = 'cn_det_dispry.html'
    queryset = tema.objects.filter(tema_archi=0)#Mostar los temas que no han sido archivados
    context_object_name = 'lista_tema'

class vts_edit_tema(UpdateView):
#Clase de la vista para actualizar el registro de un tema de investigación
    model = tema
    form_class = frm_reg_tema
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un tema' 
        context ['entity'] = 'tema'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para una definición --------------
class vts_reg_defi(CreateView):
#Clase de la vista de registro de una definición de un proyecto
    model = defin
    form_class = frm_reg_defi
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar una definición' 
        context ['action'] = 'add'
        return context

class vst_ls_defi(ListView):
    # clase para listar definiciones del sistema
    model = defin
    template_name = 'cn_det_dispry.html'
    queryset = defin.objects.filter(defi_archi=0)#Mostar las definciones que no han sido archivados
    context_object_name = 'lista_defi'

class vts_edit_defi(UpdateView):
#Clase de la vista para actualizar el registro de una definición 
    model = defin
    form_class = frm_reg_defi
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar una definición' 
        context ['entity'] = 'definición'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context
        
# ------------ Vistas para un árbol de problemas --------------
class vts_reg_ap(CreateView):
#Clase de la vista de registro de un árbol de problemas de un proyecto
    model = arb_pro
    form_class = frm_reg_ap
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un árbol de problemas' 
        context ['action'] = 'add'
        return context

class vst_ls_ap(ListView):
    # clase para listar los árboles de problemas del sistema
    model = arb_pro
    template_name = 'cn_det_dispry.html'
    queryset = arb_pro.objects.filter(ap_archi=0)#Mostar los árboles de problemas que no han sido archivados
    context_object_name = 'lista_ap'

class vts_edit_ap(UpdateView):
#Clase de la vista para actualizar el registro de un árbol de problemas 
    model = arb_pro
    form_class = frm_reg_ap
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un árbol de problemas' 
        context ['entity'] = 'árbol de problemas'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para un árbol de objetivos --------------
class vts_reg_ao(CreateView):
#Clase de la vista de registro de un árbol de objetivos  de un proyecto
    model = arb_obj
    form_class = frm_reg_ao
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un árbol de objetivos' 
        context ['action'] = 'add'
        return context

class vst_ls_ao(ListView):
    # clase para listar los árboles de problemas del sistema
    model = arb_obj
    template_name = 'cn_det_dispry.html'
    queryset = arb_obj.objects.filter(ao_archi=0)#Mostar los árboles de objetivos que no han sido archivados
    context_object_name = 'lista_ao'

class vts_edit_ao(UpdateView):
#Clase de la vista para actualizar el registro de un árbol de objetivos
    model = arb_obj
    form_class = frm_reg_ao
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un árbol de objetivos' 
        context ['entity'] = 'árbol de objetivos'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para causas --------------
class vts_reg_cau(CreateView):
#Clase de la vista de registro de las causas de un proyecto
    model = causa
    form_class = frm_reg_causa
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar una causa' 
        context ['action'] = 'add'
        return context

class vst_ls_cau(ListView):
    # clase para listar las causas de un proyecto
    model = causa
    template_name = 'cn_det_dispry.html'
    queryset = causa.objects.filter(cau_archi=0)#Mostar las causas que no han sido archivadas
    context_object_name = 'lista_cau'

class vts_edit_cau(UpdateView):
#Clase de la vista para actualizar el registro de una causa
    model = causa
    form_class = frm_reg_causa
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar una causa' 
        context ['entity'] = 'causa'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para efectos --------------
class vts_reg_efe(CreateView):
#Clase de la vista de registro de los efectos de un proyecto
    model = efecto
    form_class = frm_reg_efecto
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cndetdis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un efecto' 
        context ['action'] = 'add'
        return context

class vst_ls_efe(ListView):
    # clase para listar los efectos de un proyecto
    model = efecto
    template_name = 'cn_det_dispry.html'
    queryset = efecto.objects.filter(efe_archi=0)#Mostar los efectos que no han sido archivados
    context_object_name = 'lista_efe'

class vts_edit_efe(UpdateView):
#Clase de la vista para actualizar el registro de un efecto
    model = efecto
    form_class = frm_reg_efecto
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un efecto' 
        context ['entity'] = 'efecto'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para medios --------------
class vts_reg_med(CreateView):
#Clase de la vista de registro de los medios de un proyecto
    model = medio
    form_class = frm_reg_medio
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un medio' 
        context ['action'] = 'add'
        return context

class vst_ls_med(ListView):
    # clase para listar los medios de un proyecto
    model = medio
    template_name = 'cn_det_dispry.html'
    queryset = medio.objects.filter(med_archi=0)#Mostar los medios que no han sido archivados
    context_object_name = 'lista_med'

class vts_edit_med(UpdateView):
#Clase de la vista para actualizar el registro de un medio 
    model = medio
    form_class = frm_reg_medio
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un medio' 
        context ['entity'] = 'medio'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context

# ------------ Vistas para fines --------------

class vts_reg_fin(CreateView):
#Clase de la vista de registro de los fines de un proyecto
    model = fin
    form_class = frm_reg_fin
    template_name = 'mod_pry_frm_crear.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Registrar un fin' 
        context ['action'] = 'add'
        return context

class vst_ls_fin(ListView):
    # clase para listar los medios de un proyecto
    model = fin
    template_name = 'cn_det_dispry.html'
    queryset = fin.objects.filter(fin_archi=0)#Mostar los fines que no han sido archivados
    context_object_name = 'lista_fin'

class vts_edit_fin(UpdateView):
#Clase de la vista para actualizar el registro de un fin 
    model = fin
    form_class = frm_reg_fin
    template_name = 'mod_pry_frm_editar.html'
    success_url= reverse_lazy('cn_det_dis')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['title'] = 'Editar un fin' 
        context ['entity'] = 'fin'
        context ['list_url'] = reverse_lazy('cndetdis')
        context ['action'] = 'edit'
        return context