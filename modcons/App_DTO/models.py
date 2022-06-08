import string
from django.db import models
from modpry.App_regpry.models import *
from modpry.App_crono.models import *

#---------------------------------------------DTO-----------------------------------------
#*************Para el modulo de proyectos*******************

class etapa: 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_eta: string
    desc_eta: string
    fch_ini_eta: float
    fch_fin_eta: float

    def __init__(self, nombre_eta, desc_eta, fch_ini_eta, fch_fin_eta):
        self.nombre_eta
        self.desc_eta
        self.fch_ini_eta
        self.fch_fin_eta

class fase: 
#Clase DTO para mostrar las fases de una etapa
    nombre_fase: string
    desc_fase: string
    fch_ini_fase: float
    fch_fin_fase: float 

    def __init__(self, nombre_fase, desc_fase, fch_ini_fase, fch_fin_fase):
        self.nombre_fase
        self.desc_fase
        self.fch_ini_fase
        self.fch_fin_fase

class proceso: 
#Clase DTO para mostrar los procesos de de una fase
    nombre_proc: string
    desc_proc: string
    fch_ini_proc: float
    fch_fin_proc: float

    def __init__(self, nombre_proc, desc_proc, fch_ini_proc, fch_fin_proc):
        self.nombre_proc
        self.desc_proc
        self.fch_ini_proc
        self.fch_fin_proc

class tarea: 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_tarea: string
    desc_tarea: string
    id_usu: string
    fch_ini_tarea: float
    fch_fin_tarea: float
    id_recurso: string #Mirar para el nombre del recurso
    url_tar: string

    def __init__(self, nombre_tarea, desc_tarea, fch_ini_tarea, fch_fin_tarea):
        self.nombre_tarea
        self.desc_tarea
        self.fch_ini_tarea
        self.fch_fin_tarea
        self.url_tar

class acti: 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_acti: string
    desc_acti: string
    id_usu: string
    fch_ini_acti: float
    fch_fin_acti: float
    id_recurso: string #Mirar para el nombre del recurso
    url_acti: string
    
    def __init__(self, nombre_acti, desc_acti, fch_ini_acti, fch_fin_acti):
        self.nombre_acti
        self.desc_acti
        self.fch_ini_acti
        self.fch_fin_acti
        self.url_acti


#------------------------------------------Mapeadores-------------------------------------
class map_etapa:
    #Clase para mapear los valores de la etapa de un cronograma
    map(etapa, ['nombre_eta','desc_eta', 'fch_ini_eta', 'fch_fin_eta'])

class map_fase:
    #Clase para mapear los valores de la fase de un cronograma
    map(fase, ['nombre_fase','desc_fase', 'fch_ini_fase', 'fch_fin_fase'])

class map_proc:
    #Clase para mapear los valores de los procesos de un cronograma
    map(proceso, ['nombre_proc', 'desc_proc', 'fch_ini_proc', 'fch_fin_proc'])

class map_tarea:
    #Clase para mapear los valores de las tareas de un cronograma
    map(tarea, ['nombre_tarea','desc_tara', 'fch_ini_tarea', 'fch_fin_tarea','id_recurso', 'url_tar'])

class map_acti:
    #Clase para mapear los valores de las actividades de un cronograma
    map(acti, ['nombre_acti','desc_acti', 'fch_ini_acti', 'fch_fin_acti','id_recurso', 'url_acti'])