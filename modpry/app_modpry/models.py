# App de módulo de proyectos - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
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


