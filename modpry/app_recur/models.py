# App de recursos de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models

INF_APP = [
    #Diccionario para la aplicación de recursos
    ['Titulo', "App Recurso"],
    ['Descripción',"aplicación para la definición de los recursos de proyecto"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_recur'],
    ['url_plantilla','app_recur_iu.html'],
    ['Nombre_url','ini_recur'],
    ['Versión aplicación','0.1.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', True],
    ['visible', True],
    ]

TIPO_REC = [
    (0, 'Talento humano'),
    (1, 'Recurso material'),
    (2, 'Recurso financiero'),
    (3, 'Recurso organizacional'),
    (4, 'Recurso espacial'), 
    (5, 'Recurso documental'),
    ]

class recu_pry(models.Model):
    #Clase que contiene la información de los recursos de un proyecto
    id_rec_pry =  models.AutoField(primary_key = True)#Id del recurso
    nombre_rec = models.CharField('Nombre del recurso:', max_length=255) #Nombre del recurso
    desc_convo = models.CharField('Descripción de la convocatoria:', max_length=255) #Descripción del recurso
    uti_rec = models.CharField('Utilidad del recurso:', max_length=255)#Utilidad del recurso
    tip_rec = models.IntegerField(null = False, blank = False, choices = TIPO_REC, default = 0)#Tipo de recurso
    cont_rec = models.CharField('Contacto del recurso:', max_length=255)#Contacto del recurso
    
    class Meta:
        verbose_name = 'rec_pry'
        verbose_name_plural = 'rec_prys'