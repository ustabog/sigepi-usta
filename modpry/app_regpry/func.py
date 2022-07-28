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
#Listar inf. del registro de un proyecto de Investigación
#Agregar inf. del proyecto de Investigación
#Modificar inf. del proyecto de Investigación
#Archivar inf. del proyecto de Investigación
#Eliminar inf. del proyecto de Investigación
#Consultar inf. del proyecto de Investigación
#Clonar inf. del proyecto de Investigación
#Listar inf. del proyecto de Investigación
#Exportar inf. del proyecto de Investigación
#Importar inf. del proyecto de Investigación
#Agregar inf. de los productos vinculados proyecto de Investigación
#Modificar inf. de los productos vinculados proyecto de Investigación
#Archivar inf. de los productos vinculados proyecto de Investigación
#Eliminar inf. de los productos vinculados proyecto de Investigación
#Consultar inf. de los productos vinculados proyecto de Investigación
#Clonar inf. de los productos vinculados proyecto de Investigación
#Listar inf. de los productos vinculados proyecto de Investigación
#Exportar inf. de los productos vinculados proyecto de Investigación
#Importar inf. de los productos vinculados proyecto de Investigación
#Agregar inf. de los actores vinculados proyecto de Investigación
#Modificar inf. de los actores vinculados proyecto de Investigación
#Archivar inf. de los actores vinculados proyecto de Investigación
#Eliminar inf. de los actores vinculados proyecto de Investigación
#Consultar inf. de los actores vinculados proyecto de Investigación
#Clonar inf. de los actores vinculados proyecto de Investigación
#Listar inf. de los actores vinculados proyecto de Investigación
#Exportar inf. de los actores vinculados proyecto de Investigación
#Importar inf. de los actores vinculados proyecto de Investigación
#Agregar inf. de los eventos del proyecto de Investigación
#Modificar inf. de los eventos del proyecto de Investigación
#Archivar inf. de los eventos del proyecto de Investigación
#Eliminar inf. de los eventos del proyecto de Investigación
#Consultar inf. de los eventos del proyecto de Investigación
#Clonar inf. de los eventos del proyecto de Investigación
#Listar inf. de los eventos del proyecto de Investigación
#Exportar inf. de los eventos del proyecto de Investigación
#Importar inf. de los eventos del proyecto de Investigación
#Agregar inf. de los recursos del proyecto de Investigación
#Modificar inf. de los recursos del proyecto de Investigación
#Archivar inf. de los recursos del proyecto de Investigación
#Eliminar inf. de los recursos del proyecto de Investigación
#Consultar inf. de los recursos del proyecto de Investigación
#Clonar inf. de los recursos del proyecto de Investigación
#Listar inf. de los recursos del proyecto de Investigación
#Exportar inf. de los recursos del proyecto de Investigación
#Importar inf. de los recursos del proyecto de Investigación
#Agregar inf. de la línea de investigación del proyecto
#Modificar inf. de la línea de investigación del proyecto
#Archivar inf. de la línea de investigación del proyecto
#Eliminar inf. de la línea de investigación del proyecto
#Consultar inf. de la línea de investigación del proyecto
#Clonar inf. de la línea de investigación del proyecto
#Listar inf. de la línea de investigación del proyecto
#Exportar inf. de la línea de investigación del proyecto
#Importar inf. de la línea de investigación del proyecto
#Vincular un usuario a un proyecto de investigación
#Clonar un proyecto de investigación

from django import template
from django.http import HttpResponse
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.template import context
from django.shortcuts import render, redirect
from modadm.app_modadm.dic import *

#------------- Registro de un proyecto ---------------

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

#------------- inf adicional de un proyecto ---------------

def fn_archi_infpry(request,id):
#Función para archivar la información adicional de un proyecto
    pry_info = inf_pry.objects.get(id_inf_pry=id)
    if request.method == 'POST':
        pry_info.inf_archi= True
        pry_info.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'inf_pry': inf_pry})

def fn_eli_infpry(request,id):
#Función para eliminar la información adicional de un proyecto de la base de datos
    pry_info = inf_pry.objects.get(id_inf_pry=id)
    if request.method == 'POST':
        pry_info.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'inf_pry': inf_pry})

#---------------- Información geográfica del proyecto -----------------

def fn_archi_geo(request,id):
#Función para archivar la información geográfica de un proyecto
    geo = inf_geo_pry.objects.get(id_inf_geo=id)
    if request.method == 'POST':
        geo.geo_archi= True
        geo.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'inf_geo_pry': inf_geo_pry})

def fn_eli_geo(request,id):
#Función para eliminar la información geográfica de un proyecto de la base de datos
    geo = inf_geo_pry.objects.get(id_inf_geo=id)
    if request.method == 'POST':
        geo.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'inf_geo_pry': inf_geo_pry})

#---------------- Información de los eventos del proyecto --------------
def fn_archi_even(request,id):
#Función para archivar un evento de un proyecto
    evento = even_pry.objects.get(id_even_pry=id)
    if request.method == 'POST':
        evento.even_archi= True
        evento.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'even_pry': even_pry})

def fn_eli_even(request,id):
#Función para eliminar un evento de la base de datos
    evento = even_pry.objects.get(id_even_pry=id)
    if request.method == 'POST':
        evento.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'even_pry': even_pry})

#------ Información de la línea de investigación del proyecto ----------

def fn_archi_lninv(request,id):
#Función para archivar la línea de investigación
    linea = lin_inv.objects.get(id_ln_inv=id)
    if request.method == 'POST':
        linea.ln_archi= True
        linea.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'lin_inv': lin_inv})

def fn_eli_lninv(request,id):
#Función para eliminar la línea de investigación de la base de datos
    linea = lin_inv.objects.get(id_ln_inv=id)
    if request.method == 'POST':
        linea.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'lin_inv': lin_inv})

#----------------- Función para el template -----------------

def fn_var_plan_pry(request):
    #Función para las variables de la plantilla
    tit_form = models.IntegerField(null = False, blank = False, choices = VAR_PLAN_REGPRY, default = 0)
    contexto = context({tit_form})
    plantilla = template.render(contexto)
    return HttpResponse(plantilla)

#--------------- Función para el diccionario ---------------
def fn_val_dic(request, dicc, item):
    #REVISAR
    dicc = TIPO_PRY
    item = pry_base.objects.get(tipo_pry = dicc)#Traer el valor del diccionario para mostrar en la tarjeta
    print(item)
    return request ('cn_trj_pry.html', item,{'item' : item})
