from multiprocessing import context
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DeleteView,ListView,UpdateView,DetailView
from django.urls import reverse_lazy
from modadm.app_regusui.form import FrmNuevoUsuario, frm_cons_usui
from modadm.app_modadm.models import usui as modadm_usui, usu, adm_rol
from modadm.app_regusui.models import usui as regusui, conv_inv, prog_ofer
from django.contrib.auth.models import User, Permission, Group
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from sigepi import settings
from .func import *

#Create your views here.

def vst_reg_usui(request):
    #Clase que devuelve un formulario para registro de usuario institucion
    template_name = 'App_regusui_nvo_usui.html'
    if request.method == 'POST':
        form_class = frm_cons_usui(request.POST)
        data = request.POST
        user_name = "admin."+data['sigla']
        password = User.objects.make_random_password()
        enc_pass=make_password(password)
        User.objects.create(username=user_name,password=enc_pass,email=data['email_inst'])
        
        subject = 'Buen Dia La institución '+data['sigla']+' le ha asignado como administrador'
        message = 'Los datos de ingreso son: Usuario: '+user_name+' Contraseña: '+password
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [data['email_inst'],]
        send_mail(subject,message,email_from,recipent_list)
        
        if form_class.is_valid():
            form_class.save()
            rol= adm_rol.objects.get(id=6)
            usu_reg= User.objects.latest('id')
            usu.objects.create(id_user=usu_reg)
            usu_reg= usu.objects.latest('id_user')
            regusui.objects.create(passinst=password,id_usu_admin=usu_reg,id_rol_app=rol)
            p= modadm_usui.objects.latest('id_user')
            p.id_usu_adm = usu_reg
            p.save()
            
        else:
            print(form_class.errors.as_data())
        return redirect(reverse_lazy('cons_usui'))
    
    contexto = {'form':frm_cons_usui}
    return render(request,template_name,contexto)
    

class vst_mod_reg_usui(UpdateView):
    #clase que me modifca los usuarios para registro de usuario
    model = User
    form_class = frm_cons_usui
    template_name = 'nvo_usui_prb.html'
    success_url = reverse_lazy('cons_usui')


class vts_usui_cons(ListView):
    model = usui
    template_name ='cn_usui.html'
    success_url = reverse_lazy('cn_usui.html')
    success_message = 'listado cargado correctamente'

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

    instituciones=modadm_usui.objects.filter(id_usu_adm=request.user.id)

    if request.method == 'POST':
    
        data = request.POST
        
        #Se generan campos obligatorios faltantes para la creacion de un nuevo usuario
        
        user_name = gen_nom_usui(data["first_name"],data["last_name"],data['inst'])
        password = User.objects.make_random_password()
        enc_pass = make_password(password)
        User.objects.create(username=user_name,password=enc_pass,email=data['email'],first_name=data['first_name'],last_name=data['last_name'])
        
        #Se definen las dependencias del modelo regusui 
        actual_user = usu.objects.get(id_user=request.user.id)
        rol= adm_rol.objects.get(id=6)
        regusui.objects.create(passinst=password,id_usu_admin=actual_user,id_rol_app=rol)

        #Se envia correo de confirmacion al usuario institucional creado
        subject = 'Buen Dia '+data['first_name']+' La institución '+data['inst']+' le ha asignado un usuario'
        message = 'Los datos de ingreso son: Usuario: '+user_name+' Contraseña: '+password
        email_from = settings.EMAIL_HOST_USER
        recipent_list = [data['email'],]

        #Dejar la siguiente linea comentada para hacer pruebas sin enviar email para evitar SPAM
        #send_mail(subject,message,email_from,recipent_list)
        
        #Si no desea Registrar más usuarios se retorna al menu de administracion de la institución
        if 'reg_btn' in request.POST:
            return redirect(reverse_lazy('mis_inst'))

    return render(request, template, context={'form':form, 'inst':instituciones})


def vst_ins_usu(request):
    pass

# ----------- CRUD CONVOCATORIA DE INVERSTIGACIÓN ------------------------
class NuevaConvocatoria(CreateView):
    model = conv_inv
    fields = '__all__'
    template_name = 'App_regusui_nvo_conv.html'
    success_url = reverse_lazy('mis_inst')

class ConsultarConvocatorias(ListView):
    model = conv_inv
    fields = '__all__'
    template_name = 'cn_usui_convinv.html'

#----------- CRUD PROGRAMAS OFERTADOS POR LA INSTITUCIÓN ---------------
class NuevoPrograma(CreateView):
    model = prog_ofer
    fields = '__all__'
    template_name = 'App_regusui_nvo_prog.html'
    success_url = reverse_lazy('mis_inst')

class ConsultarProgramas(ListView):
    model: prog_ofer
    fields = '__all__'
    template_name = 'cn_usui_prog.html'
    