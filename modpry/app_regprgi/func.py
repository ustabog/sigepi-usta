# App de registro de un programa de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. del programa de Investigación
#Modificar inf. del programa de Investigación
#Archivar inf. del programa de Investigación
#Eliminar inf. del programa de Investigación
#Consultar inf. del programa de Investigación
#Clonar inf. del programa de Investigación
#Listar inf. del programa de Investigación
#Exportar inf. del programa de Investigación
#Importar inf. del programa de Investigación
#Agregar inf. del tipo de programa de Investigación
#Modificar inf. del tipo de programa de Investigación
#Archivar inf. del tipo de programa de Investigación
#Eliminar inf. del tipo de programa de Investigación
#Consultar inf. del tipo de programa de Investigación
#Clonar inf. del tipo de programa de Investigación
#Listar inf. del tipo de programa de Investigación
#Exportar inf. del tipo de programa de Investigación
#Importar inf. del tipo de programa de Investigación
#Vincular un usuario a un programa de investigación
#Clonar un programa de investigación

from modpry.app_regprgi.models import *
from django.shortcuts import render, redirect

#------------- Registro de un programa de investigación ---------------

def fn_archi_prgi(request,id):
#Función para archivar un programa de investigación
    prg = prgi_base.objects.get(id_prgi=id)
    if request.method == 'POST':
        prg.prg_archi= True
        prg.save()
        return redirect('cn_prgi')
    return render (request, 'mod_pry_frm_archi.html',{'prgi_base': prgi_base})

def fn_eli_prgi(request,id):
#Función para eliminar un programa de investigación de la base de datos
    prg = prgi_base.objects.get(id_prgi=id)
    if request.method == 'POST':
        prg.delete()
        return redirect('cn_prgi')
    return render (request, 'mod_pry_frm_eli.html',{'prgi_base': prgi_base})
