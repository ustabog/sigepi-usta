from pickle import TRUE
from django.db import models
from modpry.app_modpry.models import *
from modpry.app_regpry.models import *

APP_CONVE_PRY = [
    #Diccionario para la aplicación de convenio de proyecto
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

class convenio_pry(models.Model):
    #Clase que contiene la información de los convenio del proyecto
    id_conv =  models.AutoField(primary_key = True)#Id del convenio del proyecto
    nombre_conv = models.CharField('Nombre del convenio:', max_length=255) #Nombre del convenio
    fch_ini_conv = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio del convenio
    fch_fin_conv =  models.DateField(null=True, blank=True)#Fecha de finalización del convenio
    tipo_recur_conv = models.CharField('recurso: ', max_length=255, null=False, blank=False)
    desc_conv= models.CharField('Descripción del proyecto: ', max_length=255, null=False, blank=False) #Descripción del convenio
    url_archv_conv = models.URLField('url del archivo del convenio',max_length=200) #Url del archivo del convenio
    dep_resp=models.CharField('Dependencia del responsable del convenio: ', max_length=255, null=False, blank=False)#Dependencia responsable del convenio
    cont_conv= models.CharField('contacto: ', max_length=255, null=False, blank=False)#Contacto de la persona con la que se realizo el convenio
    
    class Meta:
        verbose_name = 'convenio_pry'
        verbose_name_plural = 'convenios_prys'

class rel_conv_pry(models.Model):
    id_pry = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    id_conv = models.ForeignKey(convenio_pry, on_delete=models.SET_NULL, null=True, blank =False )

class rel_conv_prod(models.Model):
    id_pry = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=TRUE, blank =False)
    id_conv = models.ForeignKey(convenio_pry,on_delete=models.SET_NULL, null=TRUE, blank =False)