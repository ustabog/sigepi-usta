# App de registro de producto - Vistas para SIGEPI
#Autor: Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 19 -08 -2022
#Edicion 4/10/2022

from pipes import Template
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from modprd.app_certprd.models import prd_med
from modprd.app_regprd.form import *
from django.urls import reverse_lazy
from modprd.app_regprd.models import *
from .models import *
from django.views.generic import *
from itertools import chain

#Vista principal del registro de productos

class ini_regprd():
    def view_prd(request):
        return render(request, 'app_regprd_iu.html')

#----------VISTAS PARA EL REGISTRO DE PRODUCTOS SIGEPI------------

# def vst_searchprd( request):
#     if request.method == 'POST':
#         buscar= request.POST['buscar']
#         productos= prd_base.objects.filter(nom_prd__contains = buscar)
#         context = {
#         'buscar':buscar,
#         'productos':productos
#         }
#         return render(request, 'cn_search_prd.html', context)
#     else:
#         return render(request, 'cn_search_prd.html', {})

#Vista para el registro de producto

class vst_regprd(CreateView):
    model= prd_base
    form_class = form_reg_prd
    template_name ='mod_prd_frm_registrar.html'
    success_url = reverse_lazy('listar_prd')

    def post(self,request) :
        
        super(vst_regprd, self).post(request)   
        form= self.form_class(request.POST)

        if request.method == 'POST':  
            instance = prd_med(est_med=0, id_prd= prd_base.objects.latest('id_prd'))  
            instance.save()

        return HttpResponseRedirect(self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'crear productos'
        context['action'] = 'Create'
        print(context)
        return context

#Vista para el listado de productos

class vst_listprd(ListView):
    model= prd_base
    template_name ='cn_trj_prd.html'
    success_url = reverse_lazy('listar_prd')
    context_object_name = 'Busqueda_prd'

    def get_queryset(self):
        queryset1= prd_base.objects.all()
        return queryset1

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

    def get_queryset(self):
        queryset1=m2m_pry.objects.filter(producto_id = self.kwargs['pk'])
        queryset2=m2m_user.objects.filter(producto_id = self.kwargs['pk'])
        return list(chain(queryset1, queryset2))

    def get_object(self) :
        instance= self.model.objects.get(id_prd=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de productos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        context['object_list'] = self.get_queryset()
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

    # def post(self,request) :
    #     super(vst_regprd, self).post(request)   

    #     if request.method == 'POST':  
    #         instance = prd_med(est_med=0, id_prd= prd_base.objects.latest('id_prd'))  
    #         instance.save()
    #     return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminacion de productos'
        context['action'] = 'Delete'
        return context

#Vista para la archivacion de productos

class vst_archiprd(TemplateView):
    model = prd_base
    template_name = 'mod_prd_eliminar.html'
    success_url = reverse_lazy('listar_prd')

    def post(self,request,id):
        prd= prd_base.objects.get(id_prd=id)
        if request.method == 'POST':
            prd.archivo= True
            prd.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs)
        context['title'] = 'archivar productos'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de productos 
# class vst_searchprd(TemplateView):
#     model = prd_base
#     template_name = 'cn_search_prd.html'
#     success_url = reverse_lazy('buscar_prd')

def vst_searchprd( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        productos= prd_base.objects.filter(nom_prd__contains = buscar)
        context = {
        'buscar':buscar,
        'productos':productos
        }
        return render(request, 'cn_search_prd.html', context)
    else:
        return render(request, 'cn_search_prd.html', {})


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

#Vista para la archivacion de requerimientos de existencia

class vst_archi_reqexist(TemplateView):
    model = prd_req_Exist
    template_name = 'mod_prd_eliminar_exist.html'
    success_url = reverse_lazy('listar_reqexs')

    def post(self,request,id):
        req= prd_req_Exist.objects.get(id_reqexs=id)
        if request.method == 'POST':
            req.archivo= True
            req.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar requerimientos'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de requerimientos de existencia

def vst_search_reqexist( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        requerimiento= prd_req_Exist.objects.filter(nom_reqexs__contains = buscar)
        context = {
        'buscar':buscar,
        'requerimiento':requerimiento
        }
        return render(request, 'cn_search_reqexist.html', context)
    else:
        return render(request, 'cn_search_reqexist.html', {})

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

#Vista para la archivacion de requerimientos de calidad

class vst_archi_reqcal(TemplateView):
    model = prd_req_cal 
    template_name = 'mod_prd_eliminar_cal.html'
    success_url = reverse_lazy('listar_reqcal')

    def post(self,request,id):
        req= prd_req_cal.objects.get(id_reqcal=id)
        if request.method == 'POST':
            req.archivo= True
            req.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar requerimientos'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de requerimientos de calidad

def vst_search_reqcal( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        requerimiento= prd_req_cal.objects.filter(desc_reqcal__contains = buscar)
        context = {
        'buscar':buscar,
        'requerimiento':requerimiento
        }
        return render(request, 'cn_search_reqcal.html', context)
    else:
        return render(request, 'cn_search_reqcal.html', {})


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

    def get_queryset(self) :
        return m2m_reqcal.objects.filter(categoria_id = self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de categorias'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        context['object_list'] = self.get_queryset()
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

#Vista para la archivacion de categorias

class vst_archi_categ(TemplateView):
    model = prd_categ
    template_name ='mod_prd_eliminar_categ.html'
    success_url = reverse_lazy('listar_categ')

    def post(self,request,id):
        categ= prd_categ.objects.get(id_categ=id)
        if request.method == 'POST':
            categ.archivo= True
            categ.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar Categorias'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de categorias

def vst_search_categ( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        categoria= prd_categ.objects.filter(nom_categ__contains = buscar)
        context = {
        'buscar':buscar,
        'categoria':categoria
        }
        return render(request, 'cn_search_categ.html', context)
    else:
        return render(request, 'cn_search_categ.html', {})

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

    def get_queryset(self):
        return m2m_reqexist.objects.filter(tipo_id = self.kwargs['pk']) 

    def get_object(self) :
        instance= self.model.objects.get(id_tipo=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de tipos'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        context['object_list'] = self.get_queryset()
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

#Vista para la archivacion de tipos de producto

class vst_archi_tipo(TemplateView):
    model = prd_tipo
    template_name = 'mod_prd_eliminar_tipo.html'
    success_url = reverse_lazy('listar_tipo')

    def post(self,request,id):
        tipo= prd_tipo.objects.get(id_tipo=id)
        if request.method == 'POST':
            tipo.archivo= True
            tipo.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar tipos'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de tipos de producto

def vst_search_tipo( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        tipo= prd_tipo.objects.filter(nom_tipo__contains = buscar)
        context = {
        'buscar':buscar,
        'tipo':tipo
        }
        return render(request, 'cn_search_tipo.html', context)
    else:
        return render(request, 'cn_search_tipo.html', {})
        
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

#Vista para la archivacion de campos de un producto

class vst_archi_campo(TemplateView):
    model = campo
    template_name = 'mod_prd_eliminar_campo.html'
    success_url = reverse_lazy('listar_campo')

    def post(self,request,id):
        req= campo.objects.get(id_campo=id)
        if request.method == 'POST':
            campo.archivo= True
            campo.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar campos'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de campos de plantillas

def vst_search_campo( request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        campos= campo.objects.filter(nom_campo__contains = buscar)
        context = {
        'buscar':buscar,
        'campo':campos
        }
        return render(request, 'cn_search_campo.html', context)
    else:
        return render(request, 'cn_search_campo.html', {})

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

    def get_queryset(self):
        return m2m_campo.objects.filter(campo_id=self.kwargs['pk'])

    def get_object(self) :
        instance= self.model.objects.get(id_plt_desc=self.kwargs['pk'])
        return instance

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Consulta de plantillas'
        context['action'] = 'Consulte'
        context['object'] = self.get_object()
        context['object_list'] = self.get_queryset()
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

#Vista para la archivacion de plantillas

class vst_archi_plt(TemplateView):
    model = prd_plt_desc
    template_name = 'mod_prd_eliminar_plt.html'
    success_url = reverse_lazy('listar_plantilla')

    def post(self,request,id):
        plt= prd_plt_desc.objects.get(id_plt_desc=id)
        if request.method == 'POST':
            plt.archivo= True
            plt.save()
        return HttpResponseRedirect(self.success_url)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'archivar Plantillas'
        context['action'] = 'Archivar'
        return context

#Vista para la busqueda de plantillas

def vst_search_plt(request):
    if request.method == 'POST':
        buscar= request.POST['buscar']
        plantilla= prd_plt_desc.objects.filter(nom_plt__contains = buscar)
        context = {
        'buscar':buscar,
        'plantilla':plantilla
        }
        return render(request, 'cn_search_plt.html', context)
    else:
        return render(request, 'cn_search_plt.html', {})