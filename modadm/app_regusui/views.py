from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from modadm.app_regusui.form import FrmNuevoUsuario, frm_cons_usui
from modadm.app_modadm.models import usui, usu, adm_rol
from modadm.app_regusui.models import usui as regusui
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from sigepi import settings

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
    template = 'inicio_usui.html'
    return render(request, template)


class vts_selec_usui_cons(ListView):
    # clase para listar usuarios del sistema
    model = User
    form_class = frm_cons_usui
    template_name = 'cn_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'listado cargado correctamente'

def vst_cre_usu(request):
    form = FrmNuevoUsuario
    template = 'App_regusui_frm_rel_usu.html'
    success_url = reverse_lazy('cn_usu.html')
    success_message = 'Usuario Registrado a la institución'

    instituciones=usui.objects.filter(id_usu_adm=request.user.id)

    if request.method == 'POST':
    
        data = request.POST
        
        #Se generan campos obligatorios faltantes para la creacion de un nuevo usuario
        user_name = data['email']
        password = User.objects.make_random_password()
        enc_pass = make_password(password)
        User.objects.create(username=user_name,password=enc_pass,email=data['email'],first_name=data['first_name'],last_name=data['last_name'])
        
        #Se definen las dependencias del modelo regusui 
        actual_user = usu.objects.get(id_user=request.user.id)
        rol= adm_rol.objects.get(id=6)
        regusui.objects.create(passinst=password,id_usu_admin=actual_user,id_rol_app=rol)

        #Se envia correo de confirmacion al usuario institucional creado
        subject = 'Buen Dia '+data['first_name']+' La institución '+data['inst']+' le ha asignado un usuario'
        message = 'Los datos de ingreso son: Usuario: '+data['email']+' Contraseña: '+password
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [data['email'],]
        #send_mail(subject,message,email_from,recipent_list) -- Dejar esta linea comentada para hacer pruebas sin enviar email para evitar SPAM
        
        #Si no desea Registrar más usuarios se retorna al menu de administracion de la institución
        if 'reg_btn' in request.POST:
            return redirect(reverse_lazy('mis_inst'))

    return render(request, template, context={'form':form, 'inst':instituciones})