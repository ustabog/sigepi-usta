from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.shortcuts import render, redirect

def archi_pry(request,id):
#Función para archivar un proyecto
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        pry.pry_archi= True
        pry.save()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_archi.html',{'pry_base': pry_base})

def eli_pry(request,id):
#Función para eliminar un proyecto de la base de datos
    pry = pry_base.objects.get(id_pry=id)
    if request.method == 'POST':
        pry.delete()
        return redirect('cn_pry')
    return render (request, 'mod_pry_frm_eli.html',{'pry_base': pry_base})