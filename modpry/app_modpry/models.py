# App de módulo de proyectos - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
#from django.contrib.auth.models import User
from modpry.app_regpry.models import *



INF_MOD = [
    ['titulo', "Módulo de proyectos SIGEPI"],
    ['nom','modpry'],# debe ser el mismo de la carpeta
    ['desc',"Módulo de proyectos del SIGEPI"],
    ['url_doc','doc'],
    ['version','1.9'],
    ['activo', True],
    ['instalado', True],
    ['externo', True],
    ['visible', True],
    ['ls_param_cnf', []],
    ]

INF_APP = [
    ['nom','app_modpry'],
    ['titulo', "App modulo de proyecto"],
    ['desc',"aplicación para la definición del modulo de proyectos"],
    ['url_doc','doc'],
    ['url_instal','modpry/app_modpry'],
    ['url_pl','app_modpry_iu.html'],
    ['nom_url','ini_modpry'],
    ['version','0.4.0'],
    ['ver_mod', 'prueba'],
    ['activo', False],
    ['instalada', True],
    ['visible', True],
    ['externa', False],
    ['tipo_app', 'SIGEPI-BASE'],
    ['ico','#']
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


