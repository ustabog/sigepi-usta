# App de los convenios de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from pickle import TRUE
from django.db import models
from numpy import True_
from modpry.app_modpry.models import *
from modpry.app_regpry.models import *

INF_APP = [
    #Diccionario para la aplicación de convenio
    ['Titulo', "App Convenio"],
    ['Descripción',"aplicación para la definición de un convenio de un proyecto o producto"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_conve'],
    ['url_plantilla','app_conve_iu.html'],
    ['Nombre_url','ini_conve'],
    ['Versión aplicación','0.1.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
    ]

class conve_pry(models.Model):
    #Clase que contiene la información de los convenio del proyecto
    id_conv =  models.AutoField(primary_key = True)#Id del convenio del proyecto
    nombre_conv = models.CharField('Nombre del convenio:', max_length=255) #Nombre del convenio
    desc_conv = models.CharField('Descripción del convenio:', max_length=255) #Descripción del convenio
    fch_ini_conv = models.DateField(null=True, blank=True)#Fecha de inicio del convenio
    fch_fin_conv =  models.DateField(null=True, blank=True)#Fecha de finalización del convenio
    tipo_recur_conv = models.CharField('Tipo de recurso del convenio: ', max_length=255, null=False, blank=False)
    url_archv_conv = models.URLField('url del archivo del convenio',max_length=200) #Url del archivo del convenio
    dep_resp=models.CharField('Dependencia del responsable del convenio: ', max_length=255, null=False, blank=False)#Dependencia responsable del convenio
    cont_conv= models.CharField('contacto: ', max_length=255, null=False, blank=False)#Contacto de la persona con la que se realizo el convenio
    conve_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el convenio es borrado queda como archivado

    class Meta:
        verbose_name = 'convenio_pry'
        verbose_name_plural = 'convenios_prys'

class rl_conv_pry(models.Model):
    id_rl_conve_pry = models.AutoField (primary_key= True) #Id relación convenio proyecto
    id_pry = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)
    id_conv = models.ForeignKey(conve_pry, on_delete=models.SET_NULL, null=True, blank =False )

class rl_conv_prod(models.Model):
    id_rl_conve_prod = models.AutoField (primary_key= True) #Id relación convenio producto
    #id_prod = models.ForeignKey(prod_base, on_delete=models.SET_NULL, null=TRUE, blank =False)
    id_conv = models.ForeignKey(conve_pry,on_delete=models.SET_NULL, null=TRUE, blank =False)