#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
#Coautor(a):  Milton O. Castro Ch.
#Fecha 16-08-2022

from email.policy import default
from django.db import models
from modadm.app_modadm.dic import *
from modadm.app_modadm.models import *
from modprd.app_regprd.models import *


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
    #id_prd = models.ForeignKey(prd_base, 'Identificador del producto a certificar : ', null=False, blank=False)# Identificador del produco que sera medido
    nom_med= models.CharField('Nombre de la convocatoria: ', max_length=255, null=False, blank=False) #Nombre de la convocatoria
    num_conv= models.IntegerField('Numero de la convocatoria: ', null=False, blank=False, default=0) #Numero de la convocatoria
    fch_ini=models.DateTimeField('Fecha de inicio de la convocatoria: ', null=False, blank=False) #fecha de inicio de la convocatoria
    fch_fin=models.DateTimeField('Fecha de finalizacion de la convocatoria: ', null=False, blank=False) #fecha de finalizacion de la convocatoria
    url_doc=models.URLField('Url de la informacion de la convocatoria: ', null=False, blank=False) #Url de la documentacion necesaria para la informacion de la convocatoria
    url_resul=models.URLField('Url del resultado de la convocatoria: ', null=False, blank=False) #Url de los resultados de la convocatoria
    est_med=models.Choices('seleccione estado de medicion',_MAX_LENGTH=11,choices=mediciones_dic,default=mediciones_dic[0]) #Estado de medicion
    desc_med: models.TextField ('Descripcion de la convocatoria: ', null=False, blank=False) # Descripcion de la convocatoria

class prd_cert (models.Model):
    id_cert = models.AutoField(primary_key=True, null=False, blank=False, unique=True)# Identificador de la certificacion LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, 'Identificador del producto a certificar : ', null=False, blank=False)# Identificador del produco a certificar
    est_cert=models.Choices('Seleccione el estado de la certificacion: ',_MAX_LENGTH=16, choices=cert_dic, default=cert_dic[2]) # Estado de la certificacion
    id_soporte=models.ForeignKey('identificador del soporte de la certificacion: ',null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)# Identificador de la certificiacion


class prd_etp(models.Model):
    id_etp= models.AutoField(primary_key=True, null=True, blank=False, unique=True) #Identificador de la etapa LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, 'Identificador del producto a certificar : ', null=False, blank=False)# Identificador del producto el cual atrievasa la etapa LLAVE FORANEA
    nom_etp=models.CharField('Nombre de la etapa de produccion: ', max_length=255, null=False, blank=False) #Nombre de la etapa
    desc_etp=models.TextField('Descripción de la etapa de produccion: ', null=True, blank=False) #Descripcion de la etapa
    esc_trl =models.Choices("Seleccione la escala de TRL del producto: " ,_MAX_LENGTH=11,choices=TRL_dic,default=TRL_dic[0]) #Estado de la escala de maduracion tecnologica
    
class supp_cert (models.Model):
    id_soporte= models.AutoField(primary_key=True, null=False, blank=False)# Identificador del soporte del certificado
    Url_supp= models.URLField('Url de la documentacion que valida la certificacion ', null=False, blank=False)#Url de la documentacion necesaria para la certificacion

