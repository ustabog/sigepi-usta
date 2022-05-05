from django.db import models
from modpry.App_modpry.models import *
from modadm.App_regusugr.models import *
from modpry.App_regpryi.models import *

class app_ev_pry(models.Model):
    #Clase que contiene los objetos de la App Evaluación de Proyectos
    id_app_ev_pry =  models.AutoField(primary_key = True)   # identificador unico para App Evaluación de Proyectos
    id_mod_pry  = models.ForeignKey(mod_pry, on_delete=models.CASCADE, null=False, blank =False)  # Identificador único del modulo proyecto
    nomb_app_ev_pry  = models.CharField('nombre de la App Evaluación  ', max_length=40, null=False, blank= False) # nombre de la App Evaluación de Proyectos
    desc_app_ev_pry = models.CharField('descripcion de la App  ', max_length=40, null=False, blank= False) # descripcion de la App Evaluación de Proyectos
    status_app_ev_pry =  models.BooleanField('estatus de la App Evaluación de Proyectos ', default= False) # estatus de la App Evaluación de Proyectos

    class Meta:
        verbose_name = 'app_ev_pry'
        verbose_name_plural = 'app_ev_prys'


class evalucion_pry(models.Model):
        #preguntar sobre el grupo investigador
    #Clase que contiene la forma de evaluacion del proyecto

    id_evalucion =  models.AutoField(primary_key = True)   # identificador unico para el tipo de evalucion
    desc_tipos_evalucion =  models.CharField('descripcion del tipo de evalucion ', max_length=40, null=False, blank= False) # descripcion del tipo de evalucion
    id_grup_bd = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank=False) # identificador del grupo de investigación
    fech_ini =  models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio de la evaluacion
    fecha_fin =  models.DateField('fecha de fin', auto_now = False) # # fecha de fin de la evaluacion

    class Meta:
        verbose_name = 'evalucion_pry'
        verbose_name_plural = 'evalucion_prys'

class tipos_evalucion(models.Model):
    #Clase que contiene la clase de evalucion, interna, externa y comite de etica
    id_ipos_evalucion =  models.AutoField(primary_key = True)   # identificador unico para el tipo de evalucion
    nomb_tipos_evalucion = models.CharField('Nombre del tipo de evalucion ', max_length=40, null=False, blank= False) # nombre del tipo de evaluacion
    desc_tipos_evalucion = models.CharField('descripcion del tipo de evalucion ', max_length=40, null=False, blank= False) # descripcion del tipo de evalucion

    class Meta:
        verbose_name = 'tipos_evalucion'
        verbose_name_plural = 'tipos_evalucions'

class rel_evalucion_pry(models.Model):
    #Clase que contiene la forma de evaluacion individual
    id_evalucion = models.ForeignKey(evalucion_pry, on_delete=models.CASCADE, null=False, blank =False)  # identificador unico para el tipo de evalucion
    id_investigador = models.ForeignKey(User, on_delete=models.CASCADE, null = False, blank = False) # identificador del investigador
    id_tipos_evalucion = models.ForeignKey(tipos_evalucion, on_delete=models.CASCADE, null=False, blank =False)  # tipo de evaluacion

    class Meta:
        verbose_name = 'rel_evalucion_pry'
        verbose_name_plural = 'rel_evalucion_prys'


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

class criterios_pry(models.Model):
    #Clase que contiene los criterios evaluados del proyecto
    id_criterios_pry =  models.ForeignKey(criterios, on_delete=models.CASCADE, null=False, blank =False)   # identificador unico
    id_proyecto =  models.ForeignKey(inf_pry, on_delete=models.CASCADE, null=False, blank =False)   # identificador del proeycto
    objetivo_logrado = models.BooleanField('si logro el objetivo', default= False)  # si logro el objetivo

    class Meta:
        verbose_name = 'criterios_pry'
        verbose_name_plural = 'criterios_prys'
