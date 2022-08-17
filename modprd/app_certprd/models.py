#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
#Coautor(a):  Milton O. Castro Ch.
#Fecha 16-08-2022

from email.policy import default
from django.db import models
from app_regprd import *
from ..app_regprd.models import prd_base

DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App validacion y certificacion de Producto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Producto de Investigación"],
    ['url_documento','doc'],
    ['url_install','modprd/app_certprd'],
    #['url_plantilla','app_regprd_iu.html'],
    #['Nombre_url','ini_regprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]

#Clases de la aplicacion de validacion y certificacion de productos
class prd_med (models.Model):
    id_med= models.AutoField(primary_key=True, unique=True, null=False) #Identificador de la convocatoria de medicion LLAVE PRIMARIA
    nom_med= models.CharField('Nombre de la convocatoria: ', max_length=255, null=False, blank=False) #Nombre de la convocatoria
    num_conv= models.IntegerField('Numero de la convocatoria: ', null=False, blank=False, default=0) #Numero de la convocatoria
    fch_ini=models.DateTimeField('Fecha de inicio de la convocatoria: ', null=False, blank=False) #fecha de inicio de la convocatoria
    fch_fin=models.DateTimeField('Fecha de finalizacion de la convocatoria: ', null=False, blank=False) #fecha de finalizacion de la convocatoria
    url_doc=models.URLField('Url de la informacion de la convocatoria: ', null=False, blank=False) #Url de la documentacion necesaria para la informacion de la convocatoria
    url_resul=models.URLField('Url del resultado de la convocatoria: ', null=False, blank=False) #Url de los resultados de la convocatoria
    desc_med: models.TextField ('Descripcion de la convocatoria: ', null=False, blank=False) # Descripcion de la convocatoria

class prd_cert (models.Model):
    id_cert = models.AutoField(primary_key=True, null=False, blank=False, unique=True)# Identificador de la certificacion LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, 'Identificador del producto a certificar : ', null=False, blank=False)# Identificador del produco a certificar
    cert_dic=[
        ('si', 'Certificado') 
        ('en', 'En certificacion')
        ('no', 'No certificado')
    ]
    est_cert=models.Choices('Seleccione el estado de la certificacion: ',_MAX_LENGTH=16, choices=cert_dic, default=cert_dic[2]) # Estado de la certificacion
    id_soporte=models.ForeignKey('identificador del soporte de la certificacion: ',null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)# Identificador de la certificiacion

