# App de registro de un proyecto de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. del registro de un proyecto de Investigación
#Modificar inf. del registro de un proyecto de Investigación
#Archivar inf. del registro de un proyecto de Investigación
#Eliminar inf. del registro de un proyecto de Investigación
#Consultar inf. del registro de un proyecto de Investigación
#Agregar inf. del proyecto de Investigación
#Modificar inf. del proyecto de Investigación
#Archivar inf. del proyecto de Investigación
#Eliminar inf. del proyecto de Investigación
#Consultar inf. del proyecto de Investigación
#Agregar inf. de los productos vinculados proyecto de Investigación
#Modificar inf. de los productos vinculados proyecto de Investigación
#Archivar inf. de los productos vinculados proyecto de Investigación
#Eliminar inf. de los productos vinculados proyecto de Investigación
#Consultar inf. de los productos vinculados proyecto de Investigación
#Agregar inf. de los actores vinculados proyecto de Investigación
#Modificar inf. de los actores vinculados proyecto de Investigación
#Archivar inf. de los actores vinculados proyecto de Investigación
#Eliminar inf. de los actores vinculados proyecto de Investigación
#Consultar inf. de los actores vinculados proyecto de Investigación
#Agregar inf. de los eventos del proyecto de Investigación
#Modificar inf. de los eventos del proyecto de Investigación
#Archivar inf. de los eventos del proyecto de Investigación
#Eliminar inf. de los eventos del proyecto de Investigación
#Consultar inf. de los eventos del proyecto de Investigación
#Agregar inf. de los recursos del proyecto de Investigación
#Modificar inf. de los recursos del proyecto de Investigación
#Archivar inf. de los recursos del proyecto de Investigación
#Eliminar inf. de los recursos del proyecto de Investigación
#Consultar inf. de los recursos del proyecto de Investigación
#Agregar inf. de la línea de investigación del proyecto
#Modificar inf. de la línea de investigación del proyecto
#Archivar inf. de la línea de investigación del proyecto
#Eliminar inf. de la línea de investigación del proyecto
#Consultar inf. de la línea de investigación del proyecto
#Vincular un usuario a un proyecto de investigación


from re import template
from django.http import HttpResponse
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.template import context
from django.shortcuts import render, redirect

def fn_archi_pry(request,id):
#Función para archivar un proyecto
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        pry.pry_archi= True
        pry.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'pry_base': pry_base})

def fn_eli_pry(request,id):
#Función para eliminar un proyecto de la base de datos
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        pry.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'pry_base': pry_base})

#----------------- Función para el template -----------------
def fn_var_plan_pry(request):
    #Función para las variables de la plantilla
    tit_form = models.IntegerField(null = False, blank = False, choices = VAR_PLAN_REGPRY, default = 0)
    contexto = context({tit_form})
    plantilla = template.render(contexto)
    return HttpResponse(plantilla)
