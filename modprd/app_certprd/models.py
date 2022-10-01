#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
#Coautor(a):  Milton O. Castro Ch.
#Fecha 16-08-2022


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
    id_med= models.AutoField(primary_key=True, unique=True) #Identificador de la convocatoria de medicion LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, blank=False, null=True, on_delete=models.SET_NULL, db_constraint=True)# Identificador del producto que sera medido
    nom_med= models.CharField('Nombre de la convocatoria: ', max_length=255, null=True, blank=False) #Nombre de la convocatoria
    num_conv= models.IntegerField('Numero de la convocatoria: ', null=True, blank=False, default=0) #Numero de la convocatoria
    fch_ini=models.DateTimeField('Fecha de inicio de la convocatoria: ', null=True, blank=False) #fecha de inicio de la convocatoria
    fch_fin=models.DateTimeField('Fecha de finalizacion de la convocatoria: ', null=True, blank=False) #fecha de finalizacion de la convocatoria
    url_doc=models.URLField('Url de la informacion de la convocatoria: ', null=True, blank=False) #Url de la documentacion necesaria para la informacion de la convocatoria
    url_resul=models.URLField('Url del resultado de la convocatoria: ', null=True, blank=False) #Url de los resultados de la convocatoria
    est_med=models.IntegerField(null = False, blank = False, choices = mediciones_dic, default=0) #Estado de medicion
    desc_med= models.TextField ('Descripcion de la convocatoria: ', null=True, blank=False) # Descripcion de la convocatoria
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro



class prd_etp(models.Model):
    id_etp= models.AutoField(primary_key=True, null=False, blank=False, unique=True) #Identificador de la etapa LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)# Identificador del producto el cual atrievasa la etapa LLAVE FORANEA
    nom_etp=models.CharField('Nombre de la etapa de produccion: ', max_length=255, null=True, blank=False) #Nombre de la etapa
    desc_etp=models.TextField('Descripción de la etapa de produccion: ', null=True, blank=False) #Descripcion de la etapa
    esc_trl =models.IntegerField("Seleccione la escala de TRL del producto: ", choices=TRL_dic,default=TRL_dic[0]) #Estado de la escala de maduracion tecnologica
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro



class supp_cert (models.Model):
    id_soporte= models.AutoField(primary_key=True, null=False, blank=False)# Identificador del soporte del certificado
    Url_supp= models.URLField('Url de la documentacion que valida la certificacion ', null=True, blank=False)#Url de la documentacion necesaria para la certificacion
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro



class prd_cert (models.Model):
    id_cert = models.AutoField(primary_key=True, null=False, blank=False, unique=True)# Identificador de la certificacion LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)# Identificador del produco a certificar
    est_cert=models.IntegerField('Seleccione el estado de la certificacion: ', choices=cert_dic, default=cert_dic[2]) # Estado de la certificacion
    id_soporte=models.ForeignKey(supp_cert,null=True,blank=False, on_delete=models.SET_NULL, db_constraint=True)# Identificador de la certificiacion
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro