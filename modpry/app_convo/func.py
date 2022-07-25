# App de convocatorias para un proyecto - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar información de la convocaria
#Modificar información de la convocaria
#Archivar información de la convocaria
#Eliminar información de la convocaria
#Consultar información de la convocaria
#Clonar la información de la convocaria 
#Importar la información de la convocaria 
#Exportar la información de la convocaria 
#Vincular un proyecto a una convocatoria
#Diseñar un proyecto con una plantilla de una convocatoria
from modpry.app_convo.models import *
from django.shortcuts import render, redirect

#---------------------- Registro de una convocatoria ------------
def fn_archi_convo(request,id):
#Función para archivar una convocatoria
    convo = convo_pry.objects.get(id_convo=id)
    if request.method == 'POST':
        convo.convo_archi= True # Para cambiar el valor de 1 en la base de datos y archivarlo
        convo.save()
        return redirect('cn_convo')
    return render (request, 'mod_pry_frm_archi.html',{'convo_pry': convo_pry})

def fn_eli_convo(request,id):
#Función para eliminar una convocatoria de la base de datos
    convo = convo_pry.objects.get(id_convo=id)
    if request.method == 'POST':
        convo.delete() # Borrar de la base datos
        return redirect('cn_convo')
    return render (request, 'mod_pry_frm_eli.html',{'convo_pry': convo_pry})
