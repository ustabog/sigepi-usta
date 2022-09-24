from django.shortcuts import render
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from .form import *
from modadm.app_regusugr.models import usugr
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

