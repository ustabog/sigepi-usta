from django.db import models
from modpry.App_regpry.models import *
# Create your models here.

class acti(models.Model):
    # clase que guarda la información de las actividades del proyecto.
    id_activ= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Responsable de la actividad
    nombre_acti =models.CharField('Nombre de la actividad:', max_length=255)#Nombre de la actividad
    desc_acti =models.CharField('Descripción de la actividad:', max_length=255)#Descripción de la actividad
    fch_ini_acti = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio de la actividad
    fch_fin_acti =  models.DateField(null=True, blank=True)#Fecha de finalización de la actividad
    class Meta:
        verbose_name = 'acti'
        verbose_name_plural = 'actis'

 
class tarea(models.Model):
    # clase que guarda la información de las tareas del proyecto.
    id_tarea= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Responsable de la tarea
    nombre_tarea =models.CharField('Nombre de la actividad:', max_length=255)#Nombre de la tarea
    desc_tarea =models.CharField('Descripción de la actividad:', max_length=255)#Descripción de la tarea
    fch_ini_tarea = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio de la tarea
    fch_fin_tarea =  models.DateField(null=True, blank=True)#Fecha de finalización de la tarea
    
    class Meta:
        verbose_name = 'tarea'
        verbose_name_plural = 'tareas'

class crono_pry (models.Model):
    id_crono_pry = models.AutoField(primary_key = True)#Id del cronograma del proyecto
    id_pry = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)#Proyecto base
    resp_pry = models.ForeignKey(usu, on_delete=models.CASCADE, null= True, blank = False)# responsable del proyecto
    nomb_crono = models.CharField('Nombre del cronograma:', max_length=255) #Nombre del cronograma
    desc_crono = models.CharField('Descripción del cronograma:', max_length=255) #Descripción del cronograma
    fch_ini_pry = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio del proyecto
    fch_fin_pry =  models.DateField(null=True, blank=True)#Fecha de finalización del proyecto
    acti = models.ForeignKey(acti, on_delete=models.SET_NULL, null=True, blank =False)
    tarea = models.ForeignKey(tarea, on_delete=models.SET_NULL, null=True, blank =False)

    class Meta:
        verbose_name = 'crono_pry'
        verbose_name_plural = 'crono_prys'


 