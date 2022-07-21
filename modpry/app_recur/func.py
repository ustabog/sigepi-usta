# App de recursos de un proyecto de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. de los recursos de un Proyecto de Investigación
#Modificar inf. de los recursos de un Proyecto de Investigación
#Archivar inf. de los recursos de un Proyecto de Investigación
#Eliminar inf. de los recursos de un Proyecto de Investigación
#Consultar inf. de los recursos de un Proyecto de Investigación
#Clonar inf. de los recursos de un Proyecto de Investigación
#Listar inf. de los recursos de un Proyecto de Investigación
#Exportar inf. de los recursos de un Proyecto de Investigación
#Importar inf. de los recursos de un Proyecto de Investigación
#Vincular un usuario a un recurso
#Vincular un proyecto a un recurso

from modpry.app_recur.models import recu_pry
from django.shortcuts import render, redirect

#------------- Registro de un recurso ---------------

def fn_archi_recu(request,id):
#Función para archivar un recurso
    recu = recu_pry.objects.get(id_rec_pry=id)
    if request.method == 'POST':
        recu.recu_archi= True
        recu.save()
        return redirect('cn_recu')
    return render (request, 'mod_pry_frm_archi.html',{'recu_pry': recu_pry})

def fn_eli_recu(request,id):
#Función para eliminar un recurso de la base de datos
    recu = recu_pry.objects.get(id_rec_pry=id)
    if request.method == 'POST':
        recu.delete()
        return redirect('cn_recu')
    return render (request, 'mod_pry_frm_eli.html',{'recu_pry': recu_pry})
