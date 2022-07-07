# App del cronograma de un proyecto - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. de las actividades de un Cronograma
#Modificar inf. de las actividades de un Cronograma
#Archivar inf. de las actividades de un Cronograma
#Eliminar inf. de las actividades de un Cronograma
#Consultar inf. de las actividades de un Cronograma
#Agregar inf. de las tareas de un Cronograma
#Modificar inf. de las tareas de un Cronograma
#Archivar inf. de las tareas de un Cronograma
#Eliminar inf. de las tareas de un Cronograma
#Consultar inf. de las tareas de un Cronograma
#Agregar inf. de los procesos de un Cronograma
#Modificar inf. de los procesos de un Cronograma
#Archivar inf. de los procesos de un Cronograma
#Eliminar inf. de los procesos de un Cronograma
#Consultar inf. de los procesos de un Cronograma
#Agregar inf. de las fases de un Cronograma
#Modificar inf. de las fases de un Cronograma
#Archivar inf. de las fases de un Cronograma
#Eliminar inf. de las fases de un Cronograma
#Consultar inf. de las fases de un Cronograma
#Agregar inf. de las etapas de un Cronograma
#Modificar inf. de las etapas de un Cronograma
#Archivar inf. de las etapas de un Cronograma
#Eliminar inf. de las etapas de un Cronograma
#Consultar inf. de las etapas de un Cronograma
#Agregar inf. de un Cronograma
#Modificar inf. de un Cronograma
#Archivar inf. de un Cronograma
#Eliminar inf. de un Cronograma
#Consultar inf. de un Cronograma
#Vincular un proyecto a un Cronograma
#Vincular un usuario o varios usuarios a un Cronograma
#Vincular un usuario a una Tarea
#Vincular un usuario a una Actividad


from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.shortcuts import render, redirect
from re import template
from django.http import HttpResponse
from django.template import context

#----------------- CRONOGRAMA ------------------
def fn_archi_crono(request,id):
    crono = crono_pry.objects.get(id_crono_pry=id)
    if request.method == 'POST':
        crono.crono_archi= True #Cambia el valor a True en la base de datos 
        crono.save()#Almacena el valor de True en la base de datos para archivar el cronograma
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'crono_pry': crono_pry})

def fn_eli_crono(request,id):
#Función para eliminar un proyecto de la base de datos
    crono = crono_pry.objects.get(id_crono_pry=id)
    if request.method == 'POST':
        crono.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'crono_pry': crono_pry})

#----------------- ETAPA ------------------
def fn_archi_etapa(request,id):
#Función para archivar una etapa
    eta = etapa.objects.get(id_etapa=id)
    if request.method == 'POST':
        eta.etapa_archi= True #Cambia el valor a True en la base de datos 
        eta.save()#Almacena el valor de True en la base de datos para archivar la etapa
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'etapa': etapa})

def fn_eli_etapa(request,id):
#Función para eliminar una fase de la base de datos
    eta = etapa.objects.get(id_etapa=id)
    if request.method == 'POST':
        eta.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'etapa': etapa})

#----------------- FASE ------------------
def fn_archi_fase(request,id):
#Función para archivar la fase en la base de datos
    eta = etapa.objects.get(id_fase=id)
    if request.method == 'POST':
        eta.etapa_archi= True #Cambia el valor a True en la base de datos 
        eta.save() #Almacena el valor de True en la base de datos para archivar la fase
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'fase': fase})

def fn_eli_fase(request,id):
#Función para eliminar un proyecto de la base de datos
    eta = etapa.objects.get(id_fase=id)
    if request.method == 'POST':
        eta.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'fase': fase})

#--------------- PROCESO ------------------
def fn_archi_proceso(request,id):
#Función para archivar el proceso en la base de datos
    proc = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        proc.proc_archi= True #Cambia el valor a True en la base de datos 
        proc.save() #Almacena el valor de True en la base de datos para archivar el proceso
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'proceso': proceso})

def fn_eli_proceso(request,id):
#Función para eliminar un proceso de la base de datos
    proc = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        proc.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'proceso': proceso})

#--------------------- TAREA ----------------------
def fn_archi_tarea(request,id):
#Función para archivar una tarea en la base de datos
    tar = tarea.objects.get(id_tarea=id)
    if request.method == 'POST':
        tar.tarea_archi= True #Cambia el valor a True en la base de datos 
        tar.save() #Almacena el valor de True en la base de datos para archivar la tarea
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'tarea': tarea})

def fn_eli_tarea(request,id):
#Función para eliminar una tarea de la base de datos
    tar = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        tar.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'tarea': tarea})

#------------------- ACTIVIDAD --------------------
def fn_archi_acti(request,id):
#Función para archivar una actividad en la base de datos
    activ = acti.objects.get(id_acti=id)
    if request.method == 'POST':
        activ.acti_archi= True #Cambia el valor a True en la base de datos 
        activ.save() #Almacena el valor de True en la base de datos para archivar la actividad
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'acti': acti})

def fn_eli_acti(request,id):
#Función para eliminar una actividad de la base de datos
    activ = acti.objects.get(id_acti=id)
    if request.method == 'POST':
        activ.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'acti': acti})

#----------------- Función para el template -----------------
def fn_var_plan_pry(request):
    #Función para las variables de la plantilla
    tit_form = models.IntegerField(null = False, blank = False, choices = VAR_PLAN_REGPRY, default = 0)
    contexto = context({tit_form})
    plantilla = template.render(contexto)
    return HttpResponse(plantilla)
