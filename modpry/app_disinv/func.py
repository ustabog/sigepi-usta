# App del diseño de un proyecto de investigación - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

# Funciones de la aplicación

#Agregar inf. del diseño de investigación de un Proyecto de Investigación
#Modificar inf. del diseño de investigación de un Proyecto de Investigación
#Archivar inf. del diseño de investigación de un Proyecto de Investigación
#Eliminar inf. del diseño de investigación de un Proyecto de Investigación
#Consultar inf. del diseño de investigación de un Proyecto de Investigación
#Clonar inf. del diseño de investigación de un Proyecto de Investigación
#Listar inf. del diseño de investigación de un Proyecto de Investigación
#Importar inf. del diseño de investigación de un Proyecto de Investigación
#Exportar inf. del diseño de investigación de un Proyecto de Investigación
#Agregar inf. del tema de investigación de un Proyecto de Investigación
#Modificar inf. del tema de investigación de un Proyecto de Investigación
#Archivar inf. del tema de investigación de un Proyecto de Investigación
#Eliminar inf. del tema de investigación de un Proyecto de Investigación
#Consultar inf. del tema de investigación de un Proyecto de Investigación
#Clonar inf. del tema de investigación de un Proyecto de Investigación
#Listar inf. del tema de investigación de un Proyecto de Investigación
#Importar inf. del tema de investigación de un Proyecto de Investigación
#Exportar inf. del tema de investigación de un Proyecto de Investigación
#Agregar inf. de las definiciones de un Proyecto de Investigación
#Modificar inf. de las definiciones de un Proyecto de Investigación
#Archivar inf. de las definiciones de un Proyecto de Investigación
#Eliminar inf. de las definiciones de un Proyecto de Investigación
#Consultar inf. de las definiciones de un Proyecto de Investigación
#Clonar inf. de las definiciones de un Proyecto de Investigación
#Listar inf. de las definiciones de un Proyecto de Investigación
#Importar inf. de las definiciones de un Proyecto de Investigación
#Exportar inf. de las definiciones de un Proyecto de Investigación
#Agregar inf. de las causas de un Proyecto de Investigación
#Modificar inf. de las causas de un Proyecto de Investigación
#Archivar inf. de las causas de un Proyecto de Investigación
#Eliminar inf. de las causas de un Proyecto de Investigación
#Consultar inf. de las causas de un Proyecto de Investigación
#Clonar inf. de las causas de un Proyecto de Investigación
#Listar inf. de las causas de un Proyecto de Investigación
#Importar inf. de las causas de un Proyecto de Investigación
#Exportar inf. de las causas de un Proyecto de Investigación
#Agregar inf. de los efectos de un Proyecto de Investigación
#Modificar inf. de los efectos de un Proyecto de Investigación
#Archivar inf. de los efectos de un Proyecto de Investigación
#Eliminar inf. de los efectos de un Proyecto de Investigación
#Consultar inf. de los efectos de un Proyecto de Investigación
#Clonar inf. de los efectos de un Proyecto de Investigación
#Listar inf. de los efectos de un Proyecto de Investigación
#Importar inf. de los efectos de un Proyecto de Investigación
#Exportar inf. de los efectos de un Proyecto de Investigación
#Agregar inf. del fin de un Proyecto de Investigación
#Modificar inf. del fin de un Proyecto de Investigación
#Archivar inf. el fin de un Proyecto de Investigación
#Eliminar inf. del fin de un Proyecto de Investigación
#Consultar inf. del fin de un Proyecto de Investigación
#Clonar inf. del fin de un Proyecto de Investigación
#Listar inf. del fin de un Proyecto de Investigación
#Importar inf. del fin de un Proyecto de Investigación
#Exportar inf. del fin de un Proyecto de Investigación
#Agregar inf. de los medios de un Proyecto de Investigación
#Modificar inf. de los medios de un Proyecto de Investigación
#Archivar inf. e los medios de un Proyecto de Investigación
#Eliminar inf. de los medios de un Proyecto de Investigación
#Consultar inf. de los medios de un Proyecto de Investigación
#Clonar inf. de los medios de un Proyecto de Investigación
#Listar inf. de los medios de un Proyecto de Investigación
#Importar inf. de los medios de un Proyecto de Investigación
#Exportar inf. de los medios de un Proyecto de Investigación
#Agregar inf. del árbol de problemas de un Proyecto de Investigación
#Modificar inf. del árbol de problemas de un Proyecto de Investigación
#Archivar inf. el árbol de problemas de un Proyecto de Investigación
#Eliminar inf. del árbol de problemas de un Proyecto de Investigación
#Consultar inf. del árbol de problemas de un Proyecto de Investigación
#Clonar inf. del árbol de problemas de un Proyecto de Investigación
#Listar inf. del árbol de problemas de un Proyecto de Investigación
#Importar inf. del árbol de problemas de un Proyecto de Investigación
#Exportar inf. del árbol de problemas de un Proyecto de Investigación
#Agregar inf. del árbol de objetivos de un Proyecto de Investigación
#Modificar inf. del árbol de objetivos de un Proyecto de Investigación
#Archivar inf. el árbol de objetivos de un Proyecto de Investigación
#Eliminar inf. del árbol de objetivos de un Proyecto de Investigación
#Consultar inf. del árbol de objetivos de un Proyecto de Investigación
#Clonar inf. del árbol de objetivos de un Proyecto de Investigación
#Listar inf. del árbol de objetivos de un Proyecto de Investigación
#Importar inf. del árbol de objetivos de un Proyecto de Investigación
#Exportar inf. del árbol de objetivos de un Proyecto de Investigación
#Vincular un proyecto al diseño de investigación
#Vincular un usuario al diseño de investigación

from .models import *
from modpry.app_disinv.models import *
from django.shortcuts import render, redirect

#---------- Funciones para el registro de un diseño de un proyecto --------
def fn_archi_dis(request,id):
#Función para archivar un diseño de un proyecto
    dis = dis_pry.objects.get(id_dis_pry=id)
    if request.method == 'POST':
        dis.dis_archi= True
        dis.save()
        return redirect('cn_dispry')
    return render (request, 'mod_pry_frm_archi.html',{'dis_pry': dis_pry})

def fn_eli_dis(request,id):
#Función para eliminar un diseño de un proyecto
    dis = dis_pry.objects.get(id_dis_pry=id)
    if request.method == 'POST':
        dis.delete()
        return redirect('cn_dispry')
    return render (request, 'mod_pry_frm_eli.html',{'dis_pry': dis_pry})

#---------- Funciones para el registro de un tema --------
def fn_archi_tema(request,id):
#Función para archivar un tema de un proyecto
    tem = tema.objects.get(id_tema=id)
    if request.method == 'POST':
        tem.tema_archi= True
        tem.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'tema': tema})

def fn_eli_tema(request,id):
#Función para eliminar un tema de un proyecto
    tem = tema.objects.get(id_tema=id)
    if request.method == 'POST':
        tem.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'tema': tema})

#---------- Funciones para el registro de una definición --------
def fn_archi_defi(request,id):
#Función para archivar una definición
    defi = defin.objects.get(id_def=id)
    if request.method == 'POST':
        defi.defi_archi= True
        defi.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'defin': defin})

def fn_eli_defi(request,id):
#Función para eliminar una definción
    defi = defin.objects.get(id_def=id)
    if request.method == 'POST':
        defi.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'defin': defin})

#---------- Funciones para el registro de un árbol de problemas --------
def fn_archi_ap(request,id):
#Función para archivar un árbol de problemas 
    arb_p = arb_pro.objects.get(id_arb_pro=id)
    if request.method == 'POST':
        arb_p.ap_archi= True
        arb_p.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'arb_pro': arb_pro})

def fn_eli_ap(request,id):
#Función para eliminar un árbol de problemas
    arb_p = arb_pro.objects.get(id_arb_pro=id)
    if request.method == 'POST':
        arb_p.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'arb_pro': arb_pro})

#---------- Funciones para el registro de un árbol de objetivos --------
def fn_archi_ao(request,id):
#Función para archivar un árbol de objetivos 
    arb_o = arb_obj.objects.get(id_arb_obj=id)
    if request.method == 'POST':
        arb_o.ao_archi= True
        arb_o.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'arb_obj': arb_obj})

def fn_eli_ao(request,id):
#Función para eliminar un árbol de objetivos
    arb_o = arb_obj.objects.get(id_arb_obj=id)
    if request.method == 'POST':
        arb_o.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'arb_obj': arb_obj})

#---------- Funciones para el registro de una causa --------
def fn_archi_cau(request,id):
#Función para archivar una causa
    cau =causa.objects.get(id_cau=id)
    if request.method == 'POST':
        cau.cau_archi= True
        cau.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'causa':causa})

def fn_eli_cau(request,id):
#Función para eliminar una causa
    cau =causa.objects.get(id_cau=id)
    if request.method == 'POST':
        cau.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'causa':causa})

#---------- Funciones para el registro de un efecto --------
def fn_archi_efe(request,id):
#Función para archivar un efecto
    efe =efecto.objects.get(id_efe=id)
    if request.method == 'POST':
        efe.efe_archi= True
        efe.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'efecto':efecto})

def fn_eli_efe(request,id):
#Función para eliminar un efecto
    efe =efecto.objects.get(id_efe=id)
    if request.method == 'POST':
        efe.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'efecto':efecto})

#---------- Funciones para el registro de un medio --------
def fn_archi_med(request,id):
#Función para archivar un medio
    med =medio.objects.get(id_med=id)
    if request.method == 'POST':
        med.med_archi= True
        med.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'medio':medio})

def fn_eli_med(request,id):
#Función para eliminar un medio
    med =medio.objects.get(id_med=id)
    if request.method == 'POST':
        med.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'medio':medio})

#---------- Funciones para el registro de un fin --------
def fn_archi_fin(request,id):
#Función para archivar un fin
    fin_ar =fin.objects.get(id_fin=id)
    if request.method == 'POST':
        fin_ar.fin_archi= True
        fin_ar.save()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_archi.html',{'fin':fin})

def fn_eli_fin(request,id):
#Función para eliminar un fin
    fin_del =fin.objects.get(id_fin=id)
    if request.method == 'POST':
        fin_del.delete()
        return redirect('cn_det_dis')
    return render (request, 'mod_pry_frm_eli.html',{'fin':fin})
