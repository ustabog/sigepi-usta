from django.db import models
from modadm.app_regusu.models import *
from modpry.app_regpry.models import *
from modpry.app_recur.models import *

APP_CRONO_PRY = [
    #Diccionario para la aplicación de cronograma
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

class acti(models.Model):
    # clase que guarda la información de las actividades del proyecto.
    id_activ= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    resp_acti = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Responsable de la actividad
    nombre_acti =models.CharField('Nombre de la actividad:', max_length=255)#Nombre de la actividad
    desc_acti =models.CharField('Descripción de la actividad:', max_length=255)#Descripción de la actividad
    fch_ini_acti = models.DateField('Fecha de inicio de la actividad', auto_now=False)#Fecha de inicio de la actividad
    fch_fin_acti =  models.DateField('Fecha de finalización de la actividad', auto_now=False)#Fecha de finalización de la actividad
    recurso = models.ForeignKey(recu_pry, on_delete=models.SET_NULL, null=True, blank =False)#Id del recurso de la actividad
    url_acti = models.URLField('URL de la evidencia de la actividad', null=False, blank=False)#URL de la evidencia de la actividad
    #ima_acti = models.ImageField('Imagen de la evidencia de la actividad',upload_to=None)#Imagen de la evidencia de la actividad
    #docu_acti = models.FileField('Archivo de la evidencia de la actividad',upload_to = None)#Documento de la evidencia de la actividad
    class Meta:
        verbose_name = 'actividad'
        verbose_name_plural = 'actividades'

class tarea(models.Model):
    # clase que guarda la información de las tareas del proyecto.
    id_tarea= models.AutoField(primary_key = True) #id de la tarea
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    resp_tarea=models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Responsable de la tarea
    nombre_tarea =models.CharField('Nombre de la actividad:', max_length=255)#Nombre de la tarea
    desc_tarea =models.CharField('Descripción de la actividad:', max_length=255)#Descripción de la tarea
    fch_ini_tarea = models.DateField('Fecha de inicio de la tarea', auto_now=False)#Fecha de inicio de la tarea
    fch_fin_tarea =  models.DateField('Fecha de finalización de la tarea', auto_now=False)#Fecha de finalización de la tarea
    recurso = models.ForeignKey(recu_pry, on_delete=models.SET_NULL, null=True, blank =False)#Id del recurso de la tarea
    acti =  models.ForeignKey(acti, on_delete=models.SET_NULL, null=True, blank =False)#id de la actividad del proyecto
    url_tarea = models.URLField('URL de la evidencia de la tarea', null=False, blank=False)#URL de la evidencia de la tarea
    #ima_tar = models.ImageField('Imagen de la evidencia de la tarea',upload_to=None)#Imagen de la evidencia de la tarea
    #docu_tar = models.FileField('Archivo de la evidencia de la tarea',upload_to = None)#Documento de la evidencia de la tarea
    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'

class proceso(models.Model):
    id_proceso = models.AutoField(primary_key = True) #Id del proceso del proyecto
    nombre_proc =models.CharField('Nombre del proceso:', max_length=255)#Nombre del proceso
    desc_proc =models.CharField('Descripción del proceso:', max_length=255)#Descripción del proceso
    fch_ini_proc = models.DateField('Fecha de inicio del proceso', auto_now=False)#Fecha de inicio del proceso
    fch_fin_proc =  models.DateField('Fecha de finalización del proceso', auto_now=False)#Fecha de finalización del proceso
    tarea = models.ForeignKey(tarea, on_delete=models.SET_NULL, null=True, blank =False )#id de la tarea
    class Meta:
        verbose_name = 'proceso'
        verbose_name_plural = 'procesos'

class fase(models.Model):
    #Clase que contiene los datos de la fase
    id_fase = models.AutoField(primary_key= True)#Identificador de la fase
    nombre_fase =models.CharField('Nombre del proceso:', max_length=255)#Nombre de la fase
    desc_fase =models.CharField('Descripción del proceso:', max_length=255)#Descripción de la fase
    fch_ini_fase = models.DateField('Fecha de inicio de la fase', auto_now=False)#Fecha de inicio de la fase
    fch_fin_fase =  models.DateField('Fecha de finalización de la fase', auto_now=False)#Fecha de finalización de la fase
    proceso = models.ForeignKey(proceso, on_delete=models.SET_NULL, null=True, blank =False )#id de la proceso
    
    class Meta:
        verbose_name = 'fase'
        verbose_name_plural = 'fases'

class etapa(models.Model):
    #Clase que contiene los datos de la etapa
    id_etapa = models.AutoField(primary_key= True)#Identificador de la etapa
    nombre_eta =models.CharField('Nombre del proceso:', max_length=255)#Nombre de la etapa
    desc_eta =models.CharField('Descripción del proceso:', max_length=255)#Descripción de la etapa
    fch_ini_eta = models.DateField('Fecha de inicio de la etapa', auto_now=False)#Fecha de inicio de la etapa
    fch_fin_eta =  models.DateField('Fecha de finalización de la etapa', auto_now=False)#Fecha de finalización de la etapa
    fase = models.ForeignKey(fase, on_delete=models.SET_NULL, null=True, blank =False )#id de la tarea
    class Meta:
        verbose_name = 'etapa'
        verbose_name_plural = 'etapas'

class crono_pry (models.Model):
    id_crono_pry = models.AutoField(primary_key = True)#Id del cronograma del proyecto
    nombre_pry = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)#Nombre del proyecto 
    resp_pry = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)# responsable del proyecto
    nomb_crono = models.CharField('Nombre del cronograma:', max_length=255) #Nombre del cronograma
    desc_crono = models.CharField('Descripción del cronograma:', max_length=255) #Descripción del cronograma
    fch_ini_pry = models.DateField('Fecha de inicio del proyecto', auto_now=False)#Fecha de inicio del proyecto
    fch_fin_pry =  models.DateField('Fecha de finalización del proyecto', auto_now=False)#Fecha de finalización del proyecto
    etapa = models.ForeignKey(etapa, on_delete=models.SET_NULL, null=True, blank =False )#id de la etapa
    
    class Meta:
        verbose_name = 'crono_pry'
        verbose_name_plural = 'crono_prys'