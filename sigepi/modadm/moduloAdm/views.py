from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages
from rest_framework import viewsets
from .serializers import *
from .models import *
from .form import *

def modadm(request):
    return render(request,'index_adm.html')

#def loginmodadm(request):
#    return render(request,'registration/login.html')

def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            nombreusu = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username = nombreusu, password = password)
            if usuario is not None:
                login(request, usuario)
                messages.success(request,F"bienvenido {nombreusu}")
                return render(request,'index_adm.html')
            else:
                messages.success(request,F"los datos son incorrectos")
    form = AuthenticationForm()
    return render(request,'registration/login.html', {"form": form})

def salir(request):
    logout(request)
    messages.success(request,F"tu sesión ha cerrado ")
    #return render(request,'registration/login.html')
    return render(request,'registration/login.html')


def iniciorol(request):

    contexto = {
        'rolesusu': rl_usu_inf_apps_rol.objects.all(),
        'roles': rol.objects.all(),
        'usu': User.objects.all()

    }
    return render(request,'moduloAdm/roles/roles.html',contexto)


class RegistroUsuario(CreateView):
    model = User
    form_class = formregistro
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('inicio')

class UsuList(ListView): #heredaa de listwview
    model = User
    template_name = 'moduloAdm/usuarios/usu.html'

class UsuUpdate(UpdateView):
    model = User
    form_class = formregistro
    template_name = 'moduloAdm/usuarios/crearusu.html'
    success_url = reverse_lazy('usuarios')

class UsuDelete(DeleteView):
    model = User
    template_name = 'moduloAdm/usuarios/verificacion.html'
    success_url = reverse_lazy('usuarios')

class permisoViewSet(viewsets.ModelViewSet):
    serializer_class = PermisosSerializer
    queryset = Permiso.objects.all()

class moduloViewSet(viewsets.ModelViewSet):
    serializer_class = ModelSerializer
    queryset = mod.objects.all()

class funcionViewSet(viewsets.ModelViewSet):
    serializer_class = FuncionSerializer
    queryset = func_app.objects.all()

class rolViewSet(viewsets.ModelViewSet):
    serializer_class = RolSerializer
    queryset = rol.objects.all()

class appViewSet(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = app_mod.objects.all()



############################################################3
 #para llamar a todos los objetos del rol en tipo fucniones
"""
def iniciorol(request):
    roles = rol.objects.all()
    contexto = {
        'roles':roles
    }
    return render(request,'roles/roles.html',contexto)

def crearrol(request):
    if request.method == 'GET':
        form = RolForm()
        contexto = {
            'form':form
        }
    else:
        form = RolForm(request.POST)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('roles/roles')
    #    print(form) verificar en consola si llego

    return render(request,'roles/crearrol.html',contexto)

def editarRol(request,id):
    roles = rol.objects.get(id_rol = id)
    if request.method == 'GET':
        form = RolForm(instance = roles)
        contexto = {
            'form':form
        }
    return render(request,'roles/crearrol.html',contexto)


def eliminarrol(request, id):
    roles = rol.objects.get(id_rol = id)
    roles.delete()
    return redirect('roles/roles')
"""
