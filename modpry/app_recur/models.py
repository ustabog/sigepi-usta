# App de recursos de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
from modadm.app_modadm.dic import *


INF_APP = [
    ['nom','app_recur'],
    ['titulo', "App Recurso"],
    ['desc',"aplicación para la definición de los recursos de proyecto"],
    ['url_doc','doc'],
    ['url_instal','modpry/app_recur'],
    ['url_pl','app_recur_iu.html'],
    ['nom_url','ini_recur'],
    ['version','0.1.0'],
    ['ver_mod', 'prueba'],
    ['activo', False],
    ['instalada', True],
    ['visible', True],
    ['externa', False],
    ['tipo_app', 'SIGEPI-BASE'],
    ['ico','#']
    ]

class recu_pry(models.Model):
    #Clase que contiene la información de los recursos de un proyecto
    id_rec_pry =  models.AutoField(primary_key = True)#Id del recurso
    nombre_rec = models.CharField('Nombre del recurso:', max_length=255) #Nombre del recurso
    desc_rec = models.CharField('Descripción del recurso:', max_length=255) #Descripción del recurso
    uti_rec = models.CharField('Utilidad del recurso:', max_length=255)#Utilidad del recurso
    tip_rec = models.IntegerField(null = False, blank = False, choices = TIPO_REC, default = 0)#Tipo de recurso
    cont_rec = models.CharField('Contacto del recurso:', max_length=255)#Contacto del recurso
    num_cont = models.IntegerField('Número de contacto',null = False, blank = False)#Número de contacto
    recu_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el recurso es borrado queda como archivado
    
    class Meta:
        verbose_name = 'rec_pry'
        verbose_name_plural = 'rec_prys'