# App de marco lógico de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
from modpry.app_modpry.models import *
from modpry.app_regpry.models import *
from modpry.app_disinv.models import *

INF_APP = [
    #Diccionario para la aplicación de evaluación de proyecto de investigación
    ['Titulo', "App Marco Lógico"],
    ['Descripción',"aplicación para la definición del marco lógico de Proyectos de investigación"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_mlog'],
    ['url_plantilla','app_mlog_iu.html'],
    ['Nombre_url','ini_mlog'],
    ['Versión aplicación','0.1.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
    ]


TIPO_PRBL=[
    # tipo de problema que se enfrenta
    (0,'Social'),
    (1,'Investigación'),
    (2,'Normativo'),
    (3,'Político'),
    (4,'Económico'),
    (5,'Administrativo'),
    (6,'Metodológico'),
    (7,'Cultural'),
    (8,'otro'),
    ]

ESTADO_MLOG=[
    # Estado del Análisis de Marco lógico
    (0,'Borrador'),
    (1,'Básico'),
    (2,'Estructurado'),
    (3,'Fundamentado'),
    (4,'Consolidado'),
    (5,'Depurado'),
    (6,'Validado'),
    (7,'Avanzado'),
    (8,'En reformulación'),
    ]

APP_MLOG = [
    #Diccionario para la aplicación de marco lógico
    (0,'Titulo')
    (1,'Descripción'),
    (2,'url_documento'),
    (3,'url_instal'),3
    (4,'url_plantilla'),
    (5,'Nombre_url'),
    (6,'Versión aplicación'),
    (7,'id_mod'),
    (8,'Versión_módulo'),
    (9,'estado'),
    (10,'instalada')
    (11, 'visible')
    ]

class marco_log(models.Model):
    #clase que almacena la información de elaboración de un análisis desde la metodología de marco lógico
    id_mlog =  models.AutoField(primary_key = True)   # identificador unico para el registro de un análisis de marco lógico
    pry_base  = models.ForeignKey(pry_base, verbose_name='Proyecto Base',on_delete=models.SET_NULL, null=True, blank =False)  # Identificador único del proyecto base al que está vinculado
    arb_pro = models.ForeignKey(arb_pro, verbose_name='árbol de Problemas', on_delete=models.PROTECT, null=True, blank=True) # relación uno a muchos entre el marco lógico y el (los) árbol(es) de problemas
    arb_obj = models.ForeignKey(arb_obj,  verbose_name='árbol de Objetivos', on_delete=models.PROTECT, null=True, blank=True) # relación uno a muchos entre el marco lógico y el (los) árbol(es) de objetivos
    #id_arb_prbl_inv = models.IntegerField(verbose_name='árbol de Problema Inv', help_text='Identificador del árbol de problemas de investigación', null=true, blank=true) # Identificador del arbol de problemas de investigación vinculado al Análisis de Marco Lógico
    #id_arb_obj_inv = models.IntegerField(verbose_name='árbol de Objetivo Inv',help_text='Identificador del árbol de objetivos de investigación', null=true, blank=true) # Identificador del arbol de objetivos de investigación vinculado al Análisis de Marco Lógico
    desc_mlog = models.TextField(verbose_name='Descripcion del Marco Lógico', null=True, blank= True) # descripcion del análisis de marco lógico
    estado_mlog=  models.IntegerField(verbose_name='Estado Marco Lógico',help_text='Estado de avance del análisis de Marco lógico', null = False, blank = False, choices = ESTADO_MLOG, default=0) # Estado de avance del análisis de Marco lógico
