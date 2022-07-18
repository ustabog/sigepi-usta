# App de la evaluación de un proyecto de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. de la Evaluación de un Proyecto de Investigación
#Modificar inf. de la Evaluación de un Proyecto de Investigación
#Archivar inf. de la Evaluación de un Proyecto de Investigación
#Eliminar inf. de la Evaluación de un Proyecto de Investigación
#Consultar inf. de la Evaluación de un Proyecto de Investigación
#Clonar inf. de la Evaluación de un Proyecto de Investigación
#Listar inf. de las Evaluaciones de un Proyecto de Investigación
#Listar las Evaluaciones de Proyectos de Investigación
#Importar inf. de las Evaluaciones de un Proyecto de Investigación
#Exportar inf. de las Evaluaciones de un Proyecto de Investigación
#Agregar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Diseñar la jerarquía de una Rúbrica de Evaluación de un Proyecto de Investigación
#Modificar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Archivar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Eliminar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Consultar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Clonar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Listar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Listar las Rúbricas de Evaluación
#Importar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Exportar inf. de la Rúbrica de Evaluación de un Proyecto de Investigación
#Agregar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Modificar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Archivar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Eliminar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Consultar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Clonar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Listar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Listar los criterios de Evaluación
#Importar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Exportar inf. de los criterios de Evaluación de un Proyecto de Investigación
#Agregar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Modificar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Archivar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Eliminar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Consultar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Clonar inf. el Tipo de Evaluación de un Proyecto de Investigación
#Listar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Listar los Tipos de Evaluación
#Importar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Exportar inf. del Tipo de Evaluación de un Proyecto de Investigación
#Agregar inf. del Rango de Evaluación de un Proyecto de Investigación
#Modificar inf. del Rango de Evaluación de un Proyecto de Investigación
#Archivar inf. del Rango de Evaluación de un Proyecto de Investigación
#Eliminar inf. del Rango de Evaluación de un Proyecto de Investigación
#Consultar inf. del Rango de Evaluación de un Proyecto de Investigación
#Clonar inf. del Rango de Evaluación de un Proyecto de Investigación
#Listar inf. del Rango de Evaluación de un Proyecto de Investigación
#Listar los Rangos de Evaluación
#Importar inf. del Rango de Evaluación de un Proyecto de Investigación
#Exportar inf. del Rango de Evaluación de un Proyecto de Investigación
#Agregar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Modificar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Archivar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Eliminar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Consultar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Clonar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Listar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Listar los resultados de las evaluaciones realizadas
#Importar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Exportar inf. del Resultado de la Evaluación de un Proyecto de Investigación
#Agregar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Modificar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Archivar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Eliminar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Consultar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Clonar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Listar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Listar los comentarios de las Evaluaciones 
#Importar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Exportar inf. de los comentarios de una Evaluación de un Proyecto de Investigación
#Vincular un proyecto a una evaluación de proyecto
#Vincular un usuario Evaluador a una evaluación de proyecto
#Vincular un usuario Diseñador de evaluación a una evaluación de proyecto
#Vincular un usuario Evaluado a una evaluación de un proyecto

from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from modpry.app_evapry.models import *
from django.shortcuts import render, redirect
from django.template import context
from re import template
from django.http import HttpResponse

#----------------- EVALUACIÓN DE UN PROYECTO ------------
def fn_archi_eva(request,id):
#Función para archivar una evaluación de un proyecto
    eva = eva_pry.objects.get(id_eva=id)
    if request.method == 'POST':
        eva.eva_archi= True #Cambia el valor a True en la base de datos 
        eva.save() #Almacena el valor de True en la base de datos para archivar la evaluación de un proyecto
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'eva_pry': eva_pry})

def fn_eli_eva(request,id):
#Función para eliminar una evaluación de un proyecto de la base de datos
    eva = eva_pry.objects.get(id_eva=id)
    if request.method == 'POST':
        eva.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'eva_pry': eva_pry})

#----------------- RANGO DE EVALUACIÓN ------------
def fn_archi_rng(request,id):
#Función para archivar un rango de evaluación de un proyecto
    rng = rango_eva.objects.get(id_rango=id)
    if request.method == 'POST':
        rng.rng_archi= True #Cambia el valor a True en la base de datos 
        rng.save() #Almacena el valor de True en la base de datos para archivar el rango de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'rango_eva': rango_eva})

def fn_eli_rng(request,id):
#Función para eliminar un rango de evaluación de un proyecto de la base de datos
    rng = rango_eva.objects.get(id_rango=id)
    if request.method == 'POST':
        rng.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'rango_eva': rango_eva})

#-----------------   DEFINICIÓN    ------------
def fn_archi_defi(request,id):
#Función para archivar una definción, comentario, recomendación de evaluación de un proyecto
    defin = defi.objects.get(id_def=id)
    if request.method == 'POST':
        defin.defi_archi= True #Cambia el valor a True en la base de datos 
        defin.save() #Almacena el valor de True en la base de datos para archivar la definción
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'defi': defi})

def fn_eli_defi(request,id):
#Función para eliminar una definción, comentario, recomendación de un proyecto de la base de datos
    defin = defi.objects.get(id_def=id)
    if request.method == 'POST':
        defin.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'defi': defi})

#-----------------   CRITERIO    ------------
def fn_archi_crit(request,id):
#Función para archivar un criterio de evaluación de un proyecto
    crit = crit_eva.objects.get(id_crit=id)
    if request.method == 'POST':
        crit.crit_archi= True #Cambia el valor a True en la base de datos 
        crit.save() #Almacena el valor de True en la base de datos para archivar el criterio de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'crit_eva': crit_eva})

def fn_eli_crit(request,id):
#Función para eliminar un criterio de evaluación de un proyecto de la base de datos
    crit = crit_eva.objects.get(id_crit=id)
    if request.method == 'POST':
        crit.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'crit_eva': crit_eva})

#-----------------   RÚBRICA    ------------
def fn_archi_rub(request,id):
#Función para archivar una rúbrica de evaluación de un proyecto
    rub = rubr_eva.objects.get(id_rub=id)
    if request.method == 'POST':
        rub.rub_archi= True #Cambia el valor a True en la base de datos 
        rub.save() #Almacena el valor de True en la base de datos para archivar la rúbrica de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'rubr_eva': rubr_eva})

def fn_eli_rub(request,id):
#Función para eliminar una rúbrica de evaluación de un proyecto de la base de datos
    rub = rubr_eva.objects.get(id_rub=id)
    if request.method == 'POST':
        rub.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'rubr_eva': rubr_eva})

#------------------------ RESULTADO ------------
def fn_archi_res(request,id):
#Función para archivar el resultado de evaluación de un proyecto, solo para evaluador
    res = res_eva.objects.get(id_res=id)
    if request.method == 'POST':
        res.res_archi= True #Cambia el valor a True en la base de datos 
        res.save() #Almacena el valor de True en la base de datos para archivar la rúbrica de evaluación
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_archi.html',{'res_eva': res_eva})

def fn_eli_res(request,id):
#Función para eliminar el resultado de una evaluación de un proyecto de la base de datos
    res = res_eva.objects.get(id_res=id)
    if request.method == 'POST':
        res.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'res_eva': res_eva})

#------------------------ TIPO DE EVALUACIÓN ------------
def fn_eli_tipo(request,id):
#Función para eliminar el tipo de evaluación de un proyecto de la base de datos
    tipo = tipo_eva.objects.get(id_tipo_eva=id)
    if request.method == 'POST':
        tipo.delete()
        return redirect('cn_eva')
    return render (request, 'mod_pry_frm_eli.html',{'tipo_eva': tipo_eva})

#----------------- Función para el template -----------------
def fn_var_plan_eva(request):
    #Función para las variables de la plantilla
    tit_form = models.IntegerField(null = False, blank = False, choices = VAR_PLANT_EVA, default = 0)
    contexto = context({tit_form})
    plantilla = template.render(contexto)
    return HttpResponse(plantilla)



    


