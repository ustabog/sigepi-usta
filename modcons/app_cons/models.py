from datetime import date
from django.db import models
from rest_framework import serializers
from modpry.app_regpry.models import *
from modpry.app_crono.models import *
from dataclasses import dataclass

# Create your models here.

UNIDAD_MED_TIEM = [
    (0, 'Seg'),
    (1, 'Min'),
    (2, 'Horas'),
    (3, 'Meses'),
    (4, 'Años')
    ]

#---------------------------------------------DTO-----------------------------------------
#*************Para el modulo de proyectos*******************
@dataclass
class etapa_dto(models.Model): 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_eta: str
    desc_eta: str
    fch_ini_eta: date
    fch_fin_eta: date

    def __init__(self, etapa):
        self.nombre_eta
        self.desc_eta
        self.fch_ini_eta
        self.fch_fin_eta

class etapa_dto_seri(serializers.Serializer):
#Clase de serializadores de la etapa
    nombre_eta = serializers.CharField()
    desc_eta = serializers.CharField()
    fch_ini_eta = serializers.DateField()
    fch_fin_eta = serializers.DateField()

class fase_dto(models.Model): 
#Clase DTO para mostrar las fases de una etapa
    nombre_fase: str
    desc_fase: str
    fch_ini_fase: date
    fch_fin_fase: date

    def __init__(self, nombre_fase, desc_fase, fch_ini_fase, fch_fin_fase):
        self.nombre_fase
        self.desc_fase
        self.fch_ini_fase
        self.fch_fin_fase    

class fase_dto_seri(serializers.Serializer):
#Clase de los serializadores de la fase 
    nombre_fase = serializers.CharField()
    desc_fase = serializers.CharField()
    fch_ini_fase = serializers.DateField()
    fch_fin_fase = serializers.DateField()

class proceso_dto(models.Model): 
#Clase DTO para mostrar los procesos de de una fase
    nombre_proc: str
    desc_proc: str
    fch_ini_proc: date
    fch_fin_proc: date

    def __init__(self, nombre_proc, desc_proc, fch_ini_proc, fch_fin_proc):
        self.nombre_proc
        self.desc_proc
        self.fch_ini_proc
        self.fch_fin_proc

class proceso_dto_seri(serializers.Serializer):
#Clase de los serializadores de la clase de procesos
    nombre_proc = serializers.CharField()
    desc_proc = serializers.CharField()
    fch_ini_proc = serializers.DateField()
    fch_fin_proc = serializers.DateField()

class tarea_dto(models.Model): 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_tarea: str
    desc_tarea: str
    id_usu: str
    fch_ini_tarea: date
    fch_fin_tarea: date
    id_recurso: str #Mirar para el nombre del recurso
    url_tar: str

    def __init__(self, nombre_tarea, desc_tarea, fch_ini_tarea, fch_fin_tarea):
        self.nombre_tarea
        self.desc_tarea
        self.fch_ini_tarea
        self.fch_fin_tarea
        self.url_tar

class tarea_dto_seri(serializers.Serializer):
#Clase de serializadores de la clase de tareas
    nombre_tarea = serializers.CharField()
    desc_tarea = serializers.CharField()
    id_usu = serializers.CharField()
    fch_ini_tarea = serializers.DateField()
    fch_fin_tarea = serializers.DateField()
    id_recurso = serializers.CharField()
    url_tar = serializers.URLField()

class acti_dto(models.Model): 
#Clase DTO para mostrar las etapas de un cronograma
    nombre_acti: str
    desc_acti: str
    id_usu: str
    fch_ini_acti: date
    fch_fin_acti: date
    id_recurso: str #Mirar para el nombre del recurso
    url_acti: str
    
    def __init__(self, nombre_acti, desc_acti, fch_ini_acti, fch_fin_acti):
        self.nombre_acti
        self.desc_acti
        self.fch_ini_acti
        self.fch_fin_acti
        self.url_acti

class acti_dto_seri(serializers.Serializer):
    nombre_acti = serializers.CharField()
    desc_acti = serializers.CharField()
    id_usu = serializers.CharField()
    fch_ini_acti = serializers.DateField()
    fch_fin_acti = serializers.DateField()
    id_recurso = serializers.CharField()
    url_acti = serializers.CharField()

#------------------------------------------Mapeadores-------------------------------------
class map_etapa():
    #Clase para mapear los valores de la etapa de un cronograma
    map(etapa, ['nombre_eta','desc_eta', 'fch_ini_eta', 'fch_fin_eta'])

class map_fase():
    #Clase para mapear los valores de la fase de un cronograma
    map(fase, ['nombre_fase','desc_fase', 'fch_ini_fase', 'fch_fin_fase'])

class map_proc():
    #Clase para mapear los valores de los procesos de un cronograma
    map(proceso, ['nombre_proc', 'desc_proc', 'fch_ini_proc', 'fch_fin_proc'])

class map_tarea():
    #Clase para mapear los valores de las tareas de un cronograma
    map(tarea, ['nombre_tarea','desc_tara', 'fch_ini_tarea', 'fch_fin_tarea','id_recurso', 'url_tar'])

class map_acti():
    #Clase para mapear los valores de las actividades de un cronograma
    map(acti, ['nombre_acti','desc_acti', 'fch_ini_acti', 'fch_fin_acti','id_recurso', 'url_acti'])