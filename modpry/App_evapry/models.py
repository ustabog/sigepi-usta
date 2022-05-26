from django.db import models
from modpry.App_modpry.models import *
from modadm.App_regusugr.models import *
from modpry.App_regpry.models import *

APP_EVA_PRY = [
    #Diccionario para la aplicación de evaluación de proyecto
    (0,'Titulo')
    (1,'Descripción'),
    (2,'url_documento'),
    (3,'url_instal'),
    (4,'url_plantilla'),
    (5,'Nombre_url'),
    (6,'Versión aplicación'),
    (7,'id_mod'),
    (8,'Versión_módulo'),
    (9,'estado'),
    (10,'instalada')
    (11, 'visible')
    ]

class evalucion_pry(models.Model):
    #Clase que contiene la forma de evaluacion del proyecto
    id_evalucion =  models.AutoField(primary_key = True)   # identificador unico para el tipo de evalucion
    desc_tipos_evalucion =  models.CharField('descripcion del tipo de evalucion ', max_length=40, null=False, blank= False) # descripcion del tipo de evalucion
    id_grup_bd = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank=False) # identificador del grupo de investigación
    fech_ini =  models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio de la evaluacion
    fecha_fin =  models.DateField('fecha de fin', auto_now = False) # # fecha de fin de la evaluacion

    class Meta:
        verbose_name = 'evalucion_pry'
        verbose_name_plural = 'evalucion_prys'


class criterios(models.Model):
    #Clase que contiene los tipos de criterios a evaluador
    #Relevancia de los objetivos, Experiencia del equipo de investigación,Viabilidad de la propuesta y de la coordinación
    #adecuación  del  presupuesto,Plan de difusión y transferencia de los resultados, Impacto  socioeconómico,Divulgación etc

    id_criterios_pry =  models.AutoField(primary_key = True)   # identificador unico para criterios del proyecto
    nomb_creterio = models.CharField('Nombre del criterio', max_length=40, null=False, blank= False) # # nombre del criterio
    desc_criterio =  models.CharField('Descripcion del criterio', max_length=40, null=False, blank= False) # descripcion del criterio
    objetivo_lograr =  models.CharField('Objetivo a lograr', max_length=40, null=False, blank= False) # objetivo a lograr
    porcentage_calificacion =  models.CharField('porcentaje de calificacion', max_length=40, null=False, blank= False) # porcentaje de nota del criterio

    class Meta:
        verbose_name = 'criterios'
        verbose_name_plural = 'criterioss'

