# App de convenios de proyectos de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a): Milton O. Castro Ch.
#fecha 07-07-2022

#Funciones de la aplicación

#Agregar información del convenio de un proyecto
#Modificar información del convenio de un proyecto
#Archivar información del convenio de un proyecto
#Eliminar información del convenio de un proyecto
#Consultar información del convenio de un producto
#Clonar la información del convenio de un producto 
#Listar la información del convenio de un producto 
#Importar la información del convenio de un producto
#Exportar la información del convenio de un producto
#Agregar información del convenio de un producto
#Modificar información del convenio de un producto
#Archivar información del convenio de un producto
#Eliminar información del convenio de un producto
#Consultar información del convenio de un producto
#Clonar la información del convenio de un producto 
#Listar la información del convenio de un producto 
#Importar la información del convenio de un producto
#Exportar la información del convenio de un producto
#Vincular un proyecto a un convenio
#Vincular un producto a un convenio

from modpry.app_conve.models import *
from django.shortcuts import render, redirect

#---------------------- Registro de un convenio ------------
def fn_archi_conve(request,id):
#Función para archivar un convenio
    conve = conve_pry.objects.get(id_conv=id)
    if request.method == 'POST':
        conve.conve_archi= True # Para cambiar el valor de 1 en la base de datos y archivarlo
        conve.save()
        return redirect('cn_conve')
    return render (request, 'mod_pry_frm_archi.html',{'conve_pry': conve_pry})

def fn_eli_conve(request,id):
#Función para eliminar un convenio de la base de datos
    conve = conve_pry.objects.get(id_conv=id)
    if request.method == 'POST':
        conve.delete() # Borrar de la base datos
        return redirect('cn_conve')
    return render (request, 'mod_pry_frm_eli.html',{'conve_pry': conve_pry})


