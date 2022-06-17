from django.db import models

APP_REC_PRY = [
    #Diccionario para la aplicación de recurso de proyecto
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