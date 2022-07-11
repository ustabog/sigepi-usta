from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.shortcuts import render, redirect

#----------------- EVALUACIÓN DE UN PROYECTO ------------
def archi_eva(request,id):
#Función para archivar una evaluación de un proyecto
    eva = eva_pry.objects.get(id_eva=id)
    if request.method == 'POST':
        eva.eva_archi= True #Cambia el valor a True en la base de datos 
        eva.save() #Almacena el valor de True en la base de datos para archivar la evaluación de un proyecto
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'eva_pry': eva_pry})

def eli_eva(request,id):
#Función para eliminar una evaluación de un proyecto de la base de datos
    eva = eva_pry.objects.get(id_eva=id)
    if request.method == 'POST':
        eva.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'eva_pry': eva_pry})

#----------------- RANGO DE EVALUACIÓN ------------
def archi_rng(request,id):
#Función para archivar un rango de evaluación de un proyecto
    rng = rango_eva.objects.get(id_rango=id)
    if request.method == 'POST':
        rng.rng_archi= True #Cambia el valor a True en la base de datos 
        rng.save() #Almacena el valor de True en la base de datos para archivar el rango de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'rango_eva': rango_eva})

def eli_rng(request,id):
#Función para eliminar un rango de evaluación de un proyecto de la base de datos
    rng = rango_eva.objects.get(id_rango=id)
    if request.method == 'POST':
        rng.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'rango_eva': rango_eva})

#-----------------   DEFINICIÓN    ------------
def archi_defi(request,id):
#Función para archivar una definción, comentario, recomendación de evaluación de un proyecto
    defin = defi.objects.get(id_def=id)
    if request.method == 'POST':
        defin.defi_archi= True #Cambia el valor a True en la base de datos 
        defin.save() #Almacena el valor de True en la base de datos para archivar la definción
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'defi': defi})

def eli_defi(request,id):
#Función para eliminar una definción, comentario, recomendación de un proyecto de la base de datos
    defin = defi.objects.get(id_def=id)
    if request.method == 'POST':
        defin.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'defi': defi})

#-----------------   CRITERIO    ------------
def archi_crit(request,id):
#Función para archivar un criterio de evaluación de un proyecto
    crit = crit_eva.objects.get(id_crit=id)
    if request.method == 'POST':
        crit.crit_archi= True #Cambia el valor a True en la base de datos 
        crit.save() #Almacena el valor de True en la base de datos para archivar el criterio de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'crit_eva': crit_eva})

def eli_crit(request,id):
#Función para eliminar un criterio de evaluación de un proyecto de la base de datos
    crit = crit_eva.objects.get(id_crit=id)
    if request.method == 'POST':
        crit.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'crit_eva': crit_eva})

#-----------------   RÚBRICA    ------------
def archi_rub(request,id):
#Función para archivar una rúbrica de evaluación de un proyecto
    rub = rubr_eva.objects.get(id_rub=id)
    if request.method == 'POST':
        rub.rub_archi= True #Cambia el valor a True en la base de datos 
        rub.save() #Almacena el valor de True en la base de datos para archivar la rúbrica de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'rubr_eva': rubr_eva})

def eli_rub(request,id):
#Función para eliminar una rúbrica de evaluación de un proyecto de la base de datos
    rub = rubr_eva.objects.get(id_rub=id)
    if request.method == 'POST':
        rub.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'rubr_eva': rubr_eva})

#------------------------ RESULTADO ------------
def eli_res(request,id):
#Función para eliminar el resultado de una evaluación de un proyecto de la base de datos
    res = res_eva.objects.get(id_res=id)
    if request.method == 'POST':
        res.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'res_eva': res_eva})

#------------------------ TIPO DE EVALUACIÓN ------------
def eli_tipo(request,id):
#Función para eliminar el tipo de evaluación de un proyecto de la base de datos
    tipo = tipo_eva.objects.get(id_tipo_eva=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'tipo_eva': tipo_eva})