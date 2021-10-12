from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import *
from .form import *

class PermisoList(ListView): #heredaa de listwview
    model = Permiso
    template_name = 'moduloAdm/permisos/permisos.html'

"""
#si quiero cambiar la consulta
    def get_queryset(self):
        return self.model.objects.all()[:2] #para indicar que mme traiga los ultimos dos registros
"""
class PermisosCreate(CreateView):
    model = Permiso
    form_class = PermisoForm
    template_name = 'moduloAdm/permisos/crearpermiso.html'
    success_url = reverse_lazy('permisos')

class PermisosUpdate(UpdateView):
    model = Permiso
    form_class = PermisoForm
    template_name = 'moduloAdm/permisos/crearpermiso.html'
    success_url = reverse_lazy('permisos')

class PermisosDelete(DeleteView):
    model = Permiso
    template_name = 'moduloAdm/permisos/verificacion.html'
    success_url = reverse_lazy('permisos')


############# listado aplicativo vistas hecgas en clases

class AplicativoList(ListView): #heredaa de listwview
    model = listado_aplicativo
    template_name = 'moduloAdm/aplicativos/listado_aplicativo.html'

class AplicativoCreate(CreateView):
    model = listado_aplicativo
    form_class = AplicativoForm
    template_name = 'moduloAdm/aplicativos/crearaplicativo.html'
    success_url = reverse_lazy('aplicativo')

class AplicativoUpdate(UpdateView):
    model = listado_aplicativo
    form_class = AplicativoForm
    template_name = 'moduloAdm/aplicativos/crearaplicativo.html'
    success_url = reverse_lazy('aplicativo')

class AplicativoDelete(DeleteView):
    model = listado_aplicativo
    template_name = 'moduloAdm/aplicativos/verificacion.html'
    success_url = reverse_lazy('aplicativo')


############# listado apps vistas hechas en clases

class AppList(ListView): #heredaa de listwview
    model = app_mod
    template_name = 'moduloAdm/apps/app.html'

class AppCreate(CreateView):
    model = app_mod
    form_class = AppForm
    template_name = 'moduloAdm/apps/crearapp.html'
    success_url = reverse_lazy('app')

class AppUpdate(UpdateView):
    model = app_mod
    form_class = AppForm
    template_name = 'moduloAdm/apps/crearapp.html'
    success_url = reverse_lazy('app')

class AppDelete(DeleteView):
    model = app_mod
    template_name = 'moduloAdm/apps/verificacion.html'
    success_url = reverse_lazy('app')

"""
class RegistroUsuario(CreateView):
    model = User
    form_class = Custonusercreateform
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

############# listado usuarios vistas hechas en clases

class UsuList(ListView): #heredaa de listwview
    model = usu
    template_name = 'moduloAdm/usuarios/usu.html'

class UsuCreate(CreateView):
    model = usu
    form_class = UsuForm
    template_name = 'adminr/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuUpdate(UpdateView):
    model = usu
    form_class = UsuForm
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('usu')

class UsuDelete(DeleteView):
    model = usu
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('usu')
"""
############ listado rol vistas hechas en clases

class RolList(ListView): #heredaa de listwview
    model = rol
    template_name = 'moduloAdm/roles/roles.html'

class RolCreate(CreateView):
    model = rol
    form_class = RolForm
    template_name = 'moduloAdm/roles/crearrol.html'
    success_url = reverse_lazy('roles')

class RolUpdate(UpdateView):
    model = rol
    form_class = RolForm
    template_name = 'moduloAdm/roles/crearrol.html'
    success_url = reverse_lazy('roles')

class RolDelete(DeleteView):
    model = rol
    template_name = 'moduloAdm/roles/verificacion.html'
    success_url = reverse_lazy('roles')

################ listado de modulo

class modList(ListView): #heredaa de listwview
    model = mod
    template_name = 'moduloAdm/modulos/mod.html'

class modCreate(CreateView):
    model = mod
    form_class = ModForm
    template_name = 'moduloAdm/modulos/crearmod.html'
    success_url = reverse_lazy('index')

class modUpdate(UpdateView):
    model = mod
    form_class = ModForm
    template_name = 'moduloAdm/modulos/crearmod.html'
    success_url = reverse_lazy('index')

class modDelete(DeleteView):
    model = mod
    template_name = 'moduloAdm/modulos/verificacion.html'
    success_url = reverse_lazy('index')

################ listado de relacion entre modulo y rol

class modrolList(ListView): #heredaa de listwview
    model = rl_mod_rol
    template_name = 'moduloAdm/rl_mod_adm/mod_rol/mod_rol.html'

class modrolCreate(CreateView):
    model = rl_mod_rol
    form_class = RlmodrolForm
    template_name = 'moduloAdm/rl_mod_adm/mod_rol/crear_rl_mod_rol.html'
    success_url = reverse_lazy('modrol')

class modrolUpdate(UpdateView):
    model = rl_mod_rol
    form_class = RlmodrolForm
    template_name = 'moduloAdm/rl_mod_adm/mod_rol/crear_rl_mod_rol.html'
    success_url = reverse_lazy('modrol')

class modrolDelete(DeleteView):
    model = rl_mod_rol
    template_name = 'moduloAdm/rl_mod_adm/mod_rol/verificacion.html'
    success_url = reverse_lazy('modrol')

################ listado de informacionde personal

class infoperslList(ListView): #heredaa de listwview
    model = usu_inf_pers
    template_name = 'moduloAdm/usuarios/infopers.html'

class infopersCreate(CreateView):
    model = usu_inf_pers
    form_class = UsuInfoperForm
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersUpdate(UpdateView):
    model = usu_inf_pers
    form_class = UsuInfoperForm
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')

class infopersDelete(DeleteView):
    model = usu_inf_pers
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('infopers')


"""
class infopersCreate(CreateView):
    model = usu_inf_pers
    form_class = UsuInfoperForm
    second_form_class = formregistro
    template_name = 'moduloAdm/usuarios/crearinfopers.html'
    success_url = reverse_lazy('infopers')

    def get_context_data(self, **kwargs):
        context = super(infopersCreate, self).get_context_data(**kwargs)
        if 'form' not in context:
            context['form'] = self.form_class(self.request.GET)
        if 'form2' not in context:
            context['form2'] = self.second_form_class(self.request.GET)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        form = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        if form.is_valid() and form2.is_valid():
            infousuario = form.save(commit=False)
            infousuario.usuario = form2.save()
            infousuario.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form, form2=form2))
"""

################info contacto

class usuinfcontacList(ListView): #heredaa de listwview
    model = usu_inf_contac
    template_name = 'moduloAdm/usuarios/infocontacto.html'

class usuinfcontacCreate(CreateView):
    model = usu_inf_contac
    form_class = infocontactoForm
    template_name = 'moduloAdm/usuarios/crearinfocontc.html'
    success_url = reverse_lazy('infocont')

class usuinfcontacUpdate(UpdateView):
    model = usu_inf_contac
    form_class = infocontactoForm
    template_name = 'moduloAdm/usuarios/crearinfocontc.html'
    success_url = reverse_lazy('infocont')

class usuinfcontacDelete(DeleteView):
    model = usu_inf_contac
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('infocont')

################info academica

class usuinfacaList(ListView): #heredaa de listwview
    model = form_acad
    template_name = 'moduloAdm/usuarios/infoacad.html'

class usuinfacaCreate(CreateView):
    model = form_acad
    form_class = infoacadForm
    template_name = 'moduloAdm/usuarios/crearinfoacad.html'
    success_url = reverse_lazy('infoacad')

class usuinfacaUpdate(UpdateView):
    model = form_acad
    form_class = infoacadForm
    template_name = 'moduloAdm/usuarios/crearinfoacad.html'
    success_url = reverse_lazy('infoacad')

class usuinfacaDelete(DeleteView):
    model = form_acad
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('infoacad')


################ empleos

class empleosList(ListView): #heredaa de listwview
    model = empleos
    template_name = 'moduloAdm/usuarios/empleo.html'

class empleosCreate(CreateView):
    model = empleos
    form_class = empleosForm
    template_name = 'moduloAdm/usuarios/crearempleo.html'
    success_url = reverse_lazy('empleos')

class empleosUpdate(UpdateView):
    model = empleos
    form_class = empleosForm
    template_name = 'moduloAdm/usuarios/crearempleo.html'
    success_url = reverse_lazy('empleos')

class empleosDelete(DeleteView):
    model = empleos
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('empleos')


################grupo

class usugrList(ListView): #heredaa de listwview
    model = usugr
    template_name = 'moduloAdm/grupos/grupos.html'

class usugrCreate(CreateView):
    model = usugr
    form_class = usugrForm
    template_name = 'moduloAdm/grupos/creargrupo.html'
    success_url = reverse_lazy('usugr')

class usugrUpdate(UpdateView):
    model = usugr
    form_class = usugrForm
    template_name = 'moduloAdm/grupos/creargrupo.html'
    success_url = reverse_lazy('usugr')

class usugrDelete(DeleteView):
    model = usugr
    template_name = 'moduloAdm/grupos/verificacion.html'
    success_url = reverse_lazy('usugr')

################ etapas grupo

class etapa_grList(ListView): #heredaa de listwview
    model = etapa_gr
    template_name = 'moduloAdm/grupos/etapasgrupo.html'

class etapa_grCreate(CreateView):
    model = etapa_gr
    form_class = etapa_grForm
    template_name = 'moduloAdm/grupos/crearetapasgrupo.html'
    success_url = reverse_lazy('etapa_gr')

class etapa_grUpdate(UpdateView):
    model = etapa_gr
    form_class = etapa_grForm
    template_name = 'moduloAdm/grupos/crearetapasgrupo.html'
    success_url = reverse_lazy('etapa_gr')

class etapa_grDelete(DeleteView):
    model = etapa_gr
    template_name = 'moduloAdm/grupos/verificacion.html'
    success_url = reverse_lazy('etapa_gr')

################ informacion adicional del grupo

class usugr_inf_grList(ListView): #heredaa de listwview
    model = usugr_inf_gr
    template_name = 'moduloAdm/grupos/usugrinf.html'

class usugr_inf_grCreate(CreateView):
    model = usugr_inf_gr
    form_class = usugr_inf_grForm
    template_name = 'moduloAdm/grupos/crearusugr_inf_gr.html'
    success_url = reverse_lazy('usugr_inf_gr')

class usugr_inf_grUpdate(UpdateView):
    model = usugr_inf_gr
    form_class = usugr_inf_grForm
    template_name = 'moduloAdm/grupos/crearusugr_inf_gr.html'
    success_url = reverse_lazy('usugr_inf_gr')

class usugr_inf_grDelete(DeleteView):
    model = usugr_inf_gr
    template_name = 'moduloAdm/grupos/verificacion.html'
    success_url = reverse_lazy('usugr_inf_gr')

################ informacion cursos dictado usuario

class curs_dictList(ListView): #heredaa de listwview
    model = curs_dict
    template_name = 'moduloAdm/usuarios/curs_dict.html'

class curs_dictCreate(CreateView):
    model = curs_dict
    form_class = curs_dictForm
    template_name = 'moduloAdm/usuarios/crearcurs_dict.html'
    success_url = reverse_lazy('curs_dict')

class curs_dictUpdate(UpdateView):
    model = curs_dict
    form_class = curs_dictForm
    template_name = 'moduloAdm/usuarios/crearcurs_dict.html'
    success_url = reverse_lazy('curs_dict')

class curs_dictDelete(DeleteView):
    model = curs_dict
    template_name = 'moduloAdm/grupos/verificacion.html'
    success_url = reverse_lazy('curs_dict')

################ informacion de grupo contacto

class usugr_inf_contacList(ListView): #heredaa de listwview
    model = usugr_inf_contac
    template_name = 'moduloAdm/grupos/usugr_inf_contac.html'

class usugr_inf_contacCreate(CreateView):
    model = usugr_inf_contac
    form_class = usugr_inf_contacForm
    template_name = 'moduloAdm/grupos/crearusugrinfcontact.html'
    success_url = reverse_lazy('usugr_inf_contac')

class usugr_inf_contacCreate(UpdateView):
    model = usugr_inf_contac
    form_class = usugr_inf_contacForm
    template_name = 'moduloAdm/grupos/crearusugrinfcontact.html'
    success_url = reverse_lazy('usugr_inf_contac')

class usugr_inf_contacDelete(DeleteView):
    model = usugr_inf_contac
    template_name = 'moduloAdm/grupos/verificacion.html'
    success_url = reverse_lazy('usugr_inf_contac')
