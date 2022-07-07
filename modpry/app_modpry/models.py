# App de módulo de proyectos - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
from numpy import True_
#from django.contrib.auth.models import User
from modpry.app_regpry.models import *

INF_APP = [
    #Diccionario para la aplicación de modulo de proyecto
    ['Titulo', "App modulo de proyecto"],
    ['Descripción',"aplicación para la definición del modulo de proyectos"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_modpry'],
    ['url_plantilla','app_modpry_iu.html'],
    ['Nombre_url','ini_modpry'],
    ['Versión aplicación','0.4.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', True],
    ['visible', True],
    ]

"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Proyectos
"""
ROL_MOD = [
    (0,'Investigador(a) Proy.'),
    (1,'Evaluador(a) Proy.'),
    (2,'Tutor(a) Proy.'),
    (3,'Director(a) Proy.'),
    (4,'Codirector(a) Proy.'),
    (5,'Asesor(a) Proy.'),
    (6,'Gestor(a) de Inv.'),
    (7,'Curador(a)'),
    (8,'Actor Externo'),
    ]

REG_PRY = [
    (0,'Id registro de proyecto'),
    (1,'Nombre del proyecto'),
    (2,'Descripción del proyecto'),
    (3,'Estado del proyecto'),
    ]

APP_MOD_PRY = [
    #Diccionario para la aplicación de módulo de proyecto
    (0,'Titulo'),
    (1,'Descripción'),
    (2,'url_documento'),
    (3,'url_instal'),
    (4,'url_plantilla'),
    (5,'Nombre_url'),
    (6,'Versión aplicación'),
    (7,'id_mod'),
    (8,'Versión_módulo'),
    (9,'estado'),
    (10,'instalada'),
    (11, 'visible'),
    ]
