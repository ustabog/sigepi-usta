from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.shortcuts import render, redirect

#----------------- CRONOGRAMA ------------------
def archi_crono(request,id):
    crono = crono_pry.objects.get(id_crono_pry=id)
    if request.method == 'POST':
        crono.crono_archi= True #Cambia el valor a True en la base de datos 
        crono.save()#Almacena el valor de True en la base de datos para archivar el cronograma
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'crono_pry': crono_pry})

def eli_crono(request,id):
#Función para eliminar un proyecto de la base de datos
    crono = crono_pry.objects.get(id_crono_pry=id)
    if request.method == 'POST':
        crono.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'crono_pry': crono_pry})

#----------------- ETAPA ------------------
def archi_etapa(request,id):
#Función para archivar una etapa
    eta = etapa.objects.get(id_etapa=id)
    if request.method == 'POST':
        eta.etapa_archi= True #Cambia el valor a True en la base de datos 
        eta.save()#Almacena el valor de True en la base de datos para archivar la etapa
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'etapa': etapa})

def eli_etapa(request,id):
#Función para eliminar una fase de la base de datos
    eta = etapa.objects.get(id_etapa=id)
    if request.method == 'POST':
        eta.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'etapa': etapa})

#----------------- FASE ------------------
def archi_fase(request,id):
#Función para archivar la fase en la base de datos
    eta = etapa.objects.get(id_fase=id)
    if request.method == 'POST':
        eta.etapa_archi= True #Cambia el valor a True en la base de datos 
        eta.save() #Almacena el valor de True en la base de datos para archivar la fase
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'fase': fase})

def eli_fase(request,id):
#Función para eliminar un proyecto de la base de datos
    eta = etapa.objects.get(id_fase=id)
    if request.method == 'POST':
        eta.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'fase': fase})

#--------------- PROCESO ------------------
def archi_proceso(request,id):
#Función para archivar el proceso en la base de datos
    proc = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        proc.proc_archi= True #Cambia el valor a True en la base de datos 
        proc.save() #Almacena el valor de True en la base de datos para archivar el proceso
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'proceso': proceso})

def eli_proceso(request,id):
#Función para eliminar un proceso de la base de datos
    proc = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        proc.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'proceso': proceso})

#--------------------- TAREA ----------------------
def archi_tarea(request,id):
#Función para archivar una tarea en la base de datos
    tar = tarea.objects.get(id_tarea=id)
    if request.method == 'POST':
        tar.tarea_archi= True #Cambia el valor a True en la base de datos 
        tar.save() #Almacena el valor de True en la base de datos para archivar la tarea
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'tarea': tarea})

def eli_tarea(request,id):
#Función para eliminar una tarea de la base de datos
    tar = proceso.objects.get(id_proceso=id)
    if request.method == 'POST':
        tar.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'tarea': tarea})

#------------------- ACTIVIDAD --------------------
def archi_acti(request,id):
#Función para archivar una actividad en la base de datos
    activ = acti.objects.get(id_acti=id)
    if request.method == 'POST':
        activ.acti_archi= True #Cambia el valor a True en la base de datos 
        activ.save() #Almacena el valor de True en la base de datos para archivar la actividad
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_archi.html',{'acti': acti})

def eli_acti(request,id):
#Función para eliminar una actividad de la base de datos
    activ = acti.objects.get(id_acti=id)
    if request.method == 'POST':
        activ.delete()
        return redirect('vercrono')
    return render (request, 'mod_pry_frm_eli.html',{'acti': acti})