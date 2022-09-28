# App de registro de producto - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 19 -08 -2022

from django.shortcuts import render
from django.http import HttpResponse
from modprd.app_regprd.form import *
from django.urls import reverse_lazy
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *

#Vista principal del registro de productos 
class ini_regprd():
    def view_prd(request):
        return render(request, 'app_regprd_iu.html')

#----------VISTAS PARA EL REGISTRO DE PRODUCTOS SIGEPI------------

#Vista para el registro de producto

class vst_regprd(CreateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_frm_registrar.html'
    success_url = reverse_lazy('listar_prd')

#Vista para el listado de productos

class vst_listprd(ListView):
    model= prd_base
    template_name ='cn_trj_prd.html'
    success_url = reverse_lazy('listar_prd')
    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        return prd_base.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar productos'
        context['action'] = 'List'
        return context

 #Vista para la consulta de productos

class vst_cons_prd(DetailView):
    model= prd_base
    template_name ='cn_det_prd.html'   
    success_url = reverse_lazy('listar_prd')

    def get_object(self) :
        instance= self.model.objects.get(id_prd=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de productos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context
  

#Vista para la edicion de un producto 

class vst_updprd(UpdateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_editar.html'
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar productos'
        context['action'] = 'update'
        context ['entity'] = 'prd'
        context ['list_url'] = reverse_lazy('listar_reqexs')
        return context

#Vista para la eliminacion de un producto

class vst_delprd (DeleteView):
    model = prd_base
    template_name ='mod_prd_eliminar.html'
    success_url = reverse_lazy('listar_prd')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de productos'
        context['action'] = 'Delete'
        return context

#----------VISTAS PARA EL REGISTRO DE UN REQUERIMIENTO DE EXISTENCIA SIGEPI------------

#Vista para el registro de un requerimiento de existencia

class vst_regreqexist(CreateView):
    model= prd_req_Exist
    form_class = form_req_exist
    template_name ='mod_prd_frm_requexist.html'
    success_url = reverse_lazy('listar_reqexs')

    def get_queryset(self):
        return prd_req_Exist.objects.filter(nom_reqexs =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar requerimiento'
        context['action'] = 'Create'
        return context

#Vista para el listado de requerimientos de existencia

class vst_list_reqexist(ListView):
    model= prd_req_Exist
    template_name ='cn_trj_reqexist.html'
    success_url = reverse_lazy('listar_reqexs')
    context_object_name = 'Busqueda de requerimiento de existencia'

    def get_queryset(self):
        return prd_req_Exist.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de requerimientos'
        context['action'] = 'Consulte'
        return context

#Vista para la consulta de requerimientos de existencia

class vst_cons_reqexist(DetailView):
    model= prd_req_Exist
    template_name ='cn_det_reqexist.html'   
    success_url = reverse_lazy('listar_reqexs')

    def get_object(self) :
        instance= self.model.objects.get(id_reqexs=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de requerimientos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context

#Vista para la edicion de un requerimiento de existencia

class vst_upd_reqexist(UpdateView):
    model= prd_req_Exist
    form_class = form_req_exist
    template_name ='mod_prd_editar_exist.html'
    success_url = reverse_lazy('listar_reqexs')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edicion de requerimienntos'
        context['action'] = 'Edit'
        context ['entity'] = 'prd'
        context ['list_url'] = reverse_lazy('listar_reqexs')
        return context
        
#Vista para la eliminacion de un requerimiento de existencia

class vst_del_reqexist (DeleteView):
    model = prd_req_Exist
    template_name ='mod_prd_eliminar_exist.html'
    success_url = reverse_lazy('listar_reqexs')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de requerimientos'
        context['action'] = 'Delete'
        return context

#----------VISTAS PARA EL REGISTRO DE UN REQUERIMIENTO DE CALIDAD SIGEPI------------

#Vista para el registro de un requerimiento de calidad

class vst_regreqcal(CreateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('listar_reqcal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creacion de requerimientos'
        context['action'] = 'create'
        return context


#Vista para el listado de requerimientos de calidad

class vst_list_reqcal(ListView):
    model= prd_req_cal
    template_name ='cn_trj_reqcal.html'
    success_url = reverse_lazy('listar_reqcal')
    context_object_name = 'Busqueda_reqcal'

    def get_queryset(self):
        return prd_req_cal.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar un requerimiento'
        context['action'] = 'List'
        return context

#Vista para la consulta de requerimientos de calidad

class vst_cons_reqcal(DetailView):
    model= prd_req_cal
    template_name ='cn_det_reqcal.html'   
    success_url = reverse_lazy('listar_reqcal')

    def get_object(self) :
        instance= self.model.objects.get(id_reqcal=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de productos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context

#Vista para la edicion de un requerimiento de calidad

class vst_upd_reqcal(UpdateView):
    model= prd_req_cal
    form_class = form_req_cal
    template_name ='mod_prd_frm_reqcal.html'
    success_url = reverse_lazy('listar_reqcal')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar requerimiento'
        context['action'] = 'Update'
        return context

#Vista para la eliminacion de un requerimiento de calidad

class vst_del_reqcal (DeleteView):
    model = prd_req_cal
    template_name ='mod_prd_eliminar_cal.html'
    success_url = reverse_lazy('listar_reqcal')

    #def get_queryset(self):
     #   return prd_base.objects.filter(ids_usu =self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar requerimiento'
        context['action'] = 'Delete'
        return context

#----------VISTAS PARA EL REGISTRO DE UNA CATEGORIA DE PRODUCTO SIGEPI------------

# vista para el registro del requerimiento de la categoria
class vst_regcateg(CreateView):
    model= prd_categ
    form_class = form_categ
    template_name ='mod_prd_frm_categ.html'
    success_url = reverse_lazy('listar_categ')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar categoria'
        context['action'] = 'Create'
        return context

#Vista para el listado de categorias

class vst_list_categ(ListView):
    model= prd_categ
    template_name ='cn_trj_categ.html'

    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        return prd_categ.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar una categoria'
        context['action'] = 'list'
        return context

#Vista para la consulta de categorias

class vst_cons_categ(DetailView):
    model= prd_categ
    template_name ='cn_det_categ.html'   
    success_url = reverse_lazy('listar_categ')

    def get_object(self) :
        instance= self.model.objects.get(id_categ=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de categorias'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context

#Vista para la edicion de categorias

class vst_upd_categ(UpdateView):
    model= prd_categ
    form_class = form_categ
    template_name ='mod_prd_editar_categ.html'
    success_url = reverse_lazy('listar_categ')

    #def get_queryset(self):
      #  return prd_base.objects.filter(ids_usu =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar una categoria'
        context['action'] = 'Create'
        return context

#Vista para la eliminacion de categorias

class vst_del_categ (DeleteView):
    model = prd_categ
    template_name ='mod_prd_eliminar_categ.html'
    success_url = reverse_lazy('listar_categ')

    def post(self, request, pk, *args, **kwargs):
        prd = prd_categ.objects.get (id=pk)
        prd.estado = False
        prd.save()
        return self.success_url


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar categoria'
        context['action'] = 'Delete'
        return context


#----------VISTAS PARA EL REGISTRO DE UN TIPO DE PRODUCTO SIGEPI------------

#vista para el registro de tipo de producto

class vst_regtipo(CreateView):
    model= prd_tipo
    form_class = form_tipo
    template_name ='mod_prd_frm_tipo.html'
    success_url = reverse_lazy('listar_tipo')


#Vista para el listado de tipos de producto

class vst_list_tipo(ListView):
    model= prd_tipo
    template_name ='cn_trj_tipo.html'
    success_url = reverse_lazy('listar_tipo')
    context_object_name = 'Busqueda_tipoprd'

    def get_queryset(self):
        return prd_tipo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de tipos'
        context['action'] = 'list'
        return context
    
#Vista para la consulta de tipos de producto

class vst_cons_tipo(DetailView):
    model= prd_tipo
    template_name ='cn_det_tipo.html'   
    success_url = reverse_lazy('listar_tipo')

    def get_object(self) :
        instance= self.model.objects.get(id_tipo=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de tipos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context
#Vista para la edicion de tipos de producto

class vst_upd_tipo(UpdateView):
    model= prd_tipo
    form_class = form_tipo
    template_name ='mod_prd_editar_tipo.html'
    success_url = reverse_lazy('listar_tipo')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar tipo'
        context['action'] = 'update'
        return context

#Vista para la eliminacion de tipos de productos

class vst_del_tipo (DeleteView):
    model = prd_tipo
    template_name ='mod_prd_eliminar_tipo.html'
    success_url = reverse_lazy('listar_tipo')

    #def get_queryset(self):
     #   return prd_base.objects.filter(ids_usu =self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar tipo'
        context['action'] = 'delete'
        return context

#----------VISTAS PARA EL REGISTRO DE UN CAMPO PARA PRODUCTO SIGEPI------------

#Vista para el registro de campos de productos

class vst_regcampo(CreateView):
    model= campo
    form_class = form_campo
    template_name ='mod_prd_frm_campo.html'
    success_url = reverse_lazy('listar_campo')

    #def get_queryset(self):
     #   return prd_req_cal.objects.filter(id_categ =self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar campo'
        context['action'] = 'Create'
        return context

#Vista para el listado de campos de productos

class vst_list_camp(ListView):
    model= prd_base
    template_name ='cn_trj_campo.html'
    success_url = reverse_lazy('listar_campo')
    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        return campo.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar campos'
        context['action'] = 'List'
        return context

#Vista para la consulta de campos de productos

class vst_cons_campo(DetailView):
    model= campo
    template_name ='cn_det_campo.html'   
    success_url = reverse_lazy('listar_campo')

    def get_object(self) :
        instance= self.model.objects.get(id_campo=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de campos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context


#Vista para la edicion de campos de productos

class vst_upd_camp(UpdateView):
    model= campo
    form_class = form_campo
    template_name ='mod_prd_editar_campo.html'
    success_url = reverse_lazy('listar_campo')

    #def get_queryset(self):
     #   return prd_base.objects.filter(ids_usu =self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar campo'
        context['action'] = 'update'
        return context

#Vista para la eliminacion de campos de productos

class vst_del_camp (DeleteView):
    model = campo
    template_name ='mod_prd_eliminar_campo.html'
    success_url = reverse_lazy('listar_campo')

    #def get_queryset(self):
     #   return prd_base.objects.filter(ids_usu =self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar campo'
        context['action'] = 'Delete'
        return context

#----------VISTAS PARA EL REGISTRO DE UNA PLANTILLA PARA PRODUCTOS SIGEPI------------

#Vista para el registro de plantillas de productos

class vst_regplt(CreateView):
    model = prd_plt_desc
    form_class = form_template
    template_name ='mod_prd_frm_plt.html'
    success_url = reverse_lazy('listar_plantilla')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Registrar plantilla'
        context['action'] = 'Create'
        return context

#Vista para el listado de campos de productos

class vst_list_plt(ListView):
    model = prd_plt_desc
    template_name ='cn_trj_plt.html'
    success_url = reverse_lazy('listar_plantilla')

    def get_queryset(self):
        return prd_plt_desc.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listar plantillas'
        context['action'] = 'List'
        return context

#Vista para la consulta de plantillas

class vst_cons_plt(DetailView):
    model= prd_plt_desc
    template_name ='cn_det_plt.html'   
    success_url = reverse_lazy('listar_plantilla')

    def get_object(self) :
        instance= self.model.objects.get(id_plt_desc=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de plantillas'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        return context

#Vista para la edicion de campos de productos

class vst_upd_plt(UpdateView):
    model = prd_plt_desc
    form_class = form_template
    template_name ='mod_prd_editar_plt.html'
    success_url = reverse_lazy('listar_plantilla')

    def get_queryset(self):
        return prd_base.objects.filter(ids_usu =self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar plantilla'
        context['action'] = 'update'
        return context

#Vista para la eliminacion de plantillas

class vst_del_plt(DeleteView):
    model = prd_plt_desc
    template_name ='mod_prd_eliminar_plt.html'
    success_url = reverse_lazy('listar_plantilla')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar plantilla'
        context['action'] = 'Delete'
        return context