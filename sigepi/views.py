#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Creado: 21-04-2021
Última Modificación: 21-04-2021 08:02
Autor: Milton castro
colaboración: María Fernanza Zambrano; Juan Sebastian Cely;
Hora:04:24

Vistas (views.py) aplicación principal SIGEPI

"""
#Librerías de sistema
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView,ListView,UpdateView
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth import views as auth_views
from django.contrib import messages

from modadm.app_modadm.models import usu
from .form import *
from django.contrib.auth.models import Group
from modadm.app_conf.stlapp import estilo
# from modadm.app_regusu.models import usu_inf_apps

class front():
#Clase que procesa las vistas del front de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        stl=estilo()
        ctx=stl.DevolverDict()
        return render(solicitud,"inicio.html",ctx)

    def vst_doc(self, solicitud):
        #función para plantilla de inicio de al documentación del sistema
        respuesta='Documentación del sistema'
        return HttpResponse(respuesta)

    def vst_raiz(self, solicitud):
        #función para plantilla de inicio sin extensión
        plt=loader.get_template('inicio.html')
        ctx=Context()
        respuesta=plt.render()
        return HttpResponse(respuesta)

    def vst_ingreso(self, solicitud):
        #Función que redirige al usuario si puede ingresar
        if solicitud.method == "POST":
            form = AuthenticationForm(solicitud, data=solicitud.POST)
            if form.is_valid():
                nombreusu = form.cleaned_data.get("username")
                password = form.cleaned_data.get("password")
                usuario = authenticate(solicitud, username = nombreusu, password = password)
                if usuario is not None:

                    if User.objects.get(username=nombreusu).last_login is None:
                        print("Primera vez")
                        login(solicitud, usuario)
                        messages.success(solicitud,F"Bienvenido {nombreusu}")
                        return redirect(reverse_lazy('change_password'))
                    else:
                        print("Ya se ha logeado")
                        login(solicitud, usuario)
                        messages.success(solicitud,F"Bienvenido {nombreusu}")
                        return render(solicitud,'inicio.html')
                else:
                    messages.success(solicitud,F"Los datos son incorrectos")
            else:
                messages.success(solicitud,F"Los datos son incorrectos")
        form = AuthenticationForm()
        return render(solicitud,'frm_ingreso_iu.html', {"form": form} )


    def change_password(self,request):
        #función que reasigna la contraseña a un usuario que recibio sus credenciales via mail
        form = PasswordChangeForm(request.user)
        template = 'frm_ingreso_iu.html'

        if request.method == 'POST':
            #Formulario default de Django para el cambio de contraseña
            form = PasswordChangeForm(request.user, data=request.POST)
            if form.is_valid():
                #Se almacena la nueva contraseña
                form.save()
                return render(request, 'inicio.html')
            else:
                print(form.errors)
                print('No se ha cambiado la contraseña')



        return render(request,template,{'form':form})


    def vst_registro(self, request):
        data = {
            'form': frm_reg_usu()
        }
        if request.method == "POST":
            formulario = frm_reg_usu(data=request.POST)
            
            #Si el formulario se diligencio correctamente
            if formulario.is_valid():
                #Almacenar el continido del formulario
                formulario.save()
                usuario = formulario.cleaned_data.get('username')
                password = formulario.cleaned_data.get('password1')
                #Se le asigna el rol por defecto ÏNVITADO
                grp_iv = Group.objects.get(name="Invitado")
                usuario = authenticate(username=usuario, password=password)
                usuario.groups.add(grp_iv)
                id_reg=User.objects.latest('id')
                print(id_reg)

                #Se registra el usurio registrado en el modelo usu

                p=usu(id_user=id_reg)
                p.save()
                login(request, usuario)
                return redirect(to='inicio')
            data["form"] = formulario
        return render(request,'frm_registro_iu.html', data )
    
    def vst_registro_inv(self, request):
        data = {
            'form': frm_reg_usu()
        }
        if request.method == "POST":
            formulario = frm_reg_usu(request, data=request.POST)
            if formulario.is_valid():
                formulario.save()
                usuario = formulario.cleaned_data.get('username')
                password = formulario.cleaned_data.get('password1')
                grp_inv = Group.objects.get(name="Investigador")
                usuario = authenticate(username=usuario, password=password)
                usuario.groups.add(grp_inv)
                login(request, usuario)
                return redirect(to='inicio')
            data["form"] = formulario
        return render(request,'frm_registro_iu.html', data )

    def vst_registro_grp(self, request):
        data = {
            'form': frm_reg_usu()
        }
        if request.method == "POST":
            formulario = frm_reg_usu(data=request.POST)
            if formulario.is_valid():
                formulario.save()
                usuario = formulario.cleaned_data.get('username')
                password = formulario.cleaned_data.get('password1')
                grp_inv = Group.objects.get(name="Investigador")
                usuario = authenticate(username=usuario, password=password)
                usuario.groups.add(grp_inv)
                login(request, usuario)
                return redirect(to='inicio')
            data["form"] = formulario
        return render(request,'frm_registro_iu.html', data )

    def vst_cerrar(self, solicitud):
        logout(solicitud.user)
        messages.success(solicitud,"tu sesión ha cerrado ")
        return render(solicitud,'index_front.html')

    def vst_vue(self, solicitud):
        stl=estilo()
        ctx=stl.DevolverDict()
        return render(solicitud,"apivue.html",ctx)


class ls_rolusu():
    #clase que retoma el listado de roles de acceso de la clase ls_rolusu

    def ls_roles(id):
        model = User.objects.get(id)
        ctx=[]
        for obj in model:
            ctx.append(obj.etq_rol)
        return HttpResponse(ctx)


class vst_frm_reg_usu_su(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_reg_usu_su
    template_name = 'nvo_usu.html'
    success_url = reverse_lazy('ingresop')
    success_message = "El usuario fue creado correctamente"

class vst_frm_reg_usu_adm(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_reg_usu_adm
    template_name = 'nvo_usu.html'
    success_url = reverse_lazy('ingresop')
    success_message = "El usuario fue creado correctamente, intenta ingresar."

class vst_frm_reg_usu(CreateView):
    #Clase que devuelve un formulario para registro de usuario
    form_class = frm_reg_usu
    template_name = 'nvo_usu.html'
    success_url = reverse_lazy('ingresop')
    success_message = "El usuario fue creado correctamente"
