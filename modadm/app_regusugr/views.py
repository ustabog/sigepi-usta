from django.shortcuts import render
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from django.urls import reverse_lazy
from .form import *
from modadm.app_regusugr.models import *
from modcons.app_cons.form import frm_cons_usugr
from modcons.app_cons.views import vts_ls_usugr 
from django.http import HttpResponse


## CRUD de usugr

#Clase que devuelve un formulario para registro de usuario grupo
class vts_reg_usugr(CreateView):
    form_class = frm_reg_usugr
    template_name = 'App_regusugr_nvo_usugr.html' 
    success_url = reverse_lazy('cons_usugr')
    success_message = "El usuario fue creado correctamente"

# clase que devuelve una lista de todos los usuarios grupo
class vts_ls_usugr():
    success_url = reverse_lazy('cn_usugr.html')
    success_message = 'listado cargado correctamente'

    def cons_gen(request):
        pk_usu=User.objects.filter(username=request.user.get_username()).values().first().get('id')
        print(pk_usu)
        form = usugr.objects.filter(id_usu_adm=pk_usu).select_related().all()
        template_name = 'cn_usugr.html'
        context = {
            'form':form,
        }
        return render(request, template_name, context)


#clase que permite etitar o modificar el registro de un usuario grupo
class vts_modf_usugr(UpdateView):
    model = usugr
    form_class = frm_cons_usugr
    template_name = 'app_regusugr_nvo_usugr.html'
    success_url = reverse_lazy('cons_usugr')

# clase para heredar la consulta de grupo y seleccionar un usuario grupo
class vts_selc_usugr_mod(vts_ls_usugr):
    template_name = 'sl_usugr.html'
    success_url = reverse_lazy('sl_usugr.html')

# ----------- CRUD CONTACTO USUARIO GRUPO DE INVERSTIGACIÓN ------------------------
class NuevoContacto(CreateView):
    model = usugr_contac
    fields = '__all__'
    template_name = 'App_regusugr_nvo_contac.html'
    success_url = reverse_lazy('usugr_contac')

class ConsultarContacto(ListView):
    model = usugr_contac
    fields = '__all__'
    template_name = 'cn_usui_contacusugr.html'

class ConsultarEspContacto(DetailView):
    model = usugr_contac
    fields = '__all__'
    template_name = 'cn_usui_esp_contacusugr.html'
    success_url = reverse_lazy('usugr_contac')

class EliminarContacto(DeleteView):
    model = usugr_contac
    field = '__all__'
    template_name = 'del_usugr_contacusugr.html'
    success_url = reverse_lazy('usugr_contac')

#----------- CRUD ETAPAS DEL GRUPO DE INVESTIGACION ---------------
class NuevaEtapa(CreateView):
    model = usugr_etapa
    fields = '__all__'
    template_name = 'App_regusugr_nva_etapa.html'
    success_url = reverse_lazy('mis_inst')

class ConsultarEtapas(ListView):
    model: usugr_etapa
    fields = '__all__'
    template_name = 'cn_usugr_etapas.html'
    
class ConsultaEspEtapa(DetailView):
    model = usugr_etapa
    fields = '__all__'
    template_name = 'cn_usugr_esp_etapa.html'
    success_url = reverse_lazy('cons_convinv')

class EliminarEtapa(DeleteView):
    model = usugr_etapa
    field = '__all__'
    template_name = 'del_usugr_prog.html'
    success_url = reverse_lazy('cons_convinv')

# ----------- CRUD CURSOS DE FORMACION REALIZADOS POR EL USUARIO ------------------------
class NuevoCurso(CreateView):
    model = usugr_form
    fields = '__all__'
    template_name = 'App_regusugr_nvo_curso.html'
    success_url = reverse_lazy('cons_usugr_curso')

class ConsultarCurso(ListView):
    model = usugr_form
    fields = '__all__'
    template_name = 'cn_usugr_cursos.html'

class ConsultaEspCurso(DetailView):
    model = usugr_form
    fields = '__all__'
    template_name = 'cn_usui_esp_curso.html'
    success_url = reverse_lazy('cons_usugr_curso')

class EliminarCurso(DeleteView):
    model = usugr_form
    field = '__all__'
    template_name = 'del_usui_curso.html'
    success_url = reverse_lazy('cons_usugr_curso')

#----------- CRUD REDES PUBLICAS DEL GRUPO ---------------
class NuevaRed(CreateView):
    model = usugr_red_soc
    fields = '__all__'
    template_name = 'App_regusugr_nva_red.html'
    success_url = reverse_lazy('mis_inst')

class ConsultarRedes(ListView):
    model: usugr_red_soc
    fields = '__all__'
    template_name = 'cn_usugr_redes.html'
    
class ConsultarEspRed(DetailView):
    model = usugr_red_soc
    fields = '__all__'
    template_name = 'cn_usugr_esp_red.html'
    success_url = reverse_lazy('cons_convinv')

class EliminarRed(DeleteView):
    model = usugr_red_soc
    field = '__all__'
    template_name = 'del_usugr_red.html'
    success_url = reverse_lazy('cons_convinv')