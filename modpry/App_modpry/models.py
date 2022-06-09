from django.db import models
#from django.contrib.auth.models import User
from modpry.app_regpry.models import *

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
