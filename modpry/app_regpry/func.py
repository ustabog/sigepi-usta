from re import template
from django.http import HttpResponse
from .models import *
from modpry.app_regpry.models import *
from modpry.app_regpry.form import *
from django.template import context
from django.shortcuts import render, redirect

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

#----------------- Función para el template -----------------
def fn_var_plan_pry(request):
    #Función para las variables de la plantilla
    tit_form = models.IntegerField(null = False, blank = False, choices = VAR_PLAN_REGPRY, default = 0)
    contexto = context({tit_form})
    plantilla = template.render(contexto)
    return HttpResponse(plantilla)
