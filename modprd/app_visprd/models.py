#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 12-08-2022

from django.db import models

DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App Registro de Producto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Producto de Investigación"],
    ['url_documento','doc'],
    ['url_install','modprd/app_regprd'],
    #['url_plantilla','app_regprd_iu.html'],
    #['Nombre_url','ini_regprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]
#Clases de la aplicacion de visibilidad del producto

class prd_indic (models.Model):
    id_indic=models.AutoField(primary_key=True, unique=True,null=False, blank=False) #Identificador de los indicadores de visibilidad del proyecto
    nom_ind=models.CharField('Nombre del indicador de visibilidad', max_length=255, null=False, blank=False)#Nombre del indicador
    Desc_indic=models.TextField('descripcion del indicador de visibilidad',null=False, blank=False)#Descripcion del indicador
    url_doc_indic=models.URLField('Url de la documentacion del indicador: ', null=False, blank=False)#Url de la documentacion del indicador
    entidad_med=models.CharField('Entidad de medicion: ',max_length=255, null=False, blank=False)# Entidad de medicion del indicador
    tipo_indic=models.CharField('Tipo de indicador: ',max_length=255, null=False, blank=False)# Tipo de indicador
    val_indic=models.IntegerField('Valor cuantitativo del indicador: ',null=False, Blank=False)#Valor cuantitativo del indicador
    url_fuen_indic=models.URLField('Url de las fuentes de datos del indicador: ', null=False, blank=False)#Url de las fuentes de datos del indicador
    fch_med_indic=models.DateTimeField('Fecha de medicion del indicador: ', null=False, blank=False)#Fecha de medicion del indicador
    resp_indic=models.CharField('responsable de la medicion del indicador: ', null=False, blank=False, max_length=255)#Responsable de la medicion del indicador

class rang_indic (models.Model):
    id_rang_indic = models.AutoField(primary_key=True, null=False, blank=False)#Identificador de rango del indicador LLAVE PRIMARIA
    id_indic=models.ForeignKey(prd_indic, null=False, blank=False) #Idebtificador del indicador al que se le va a sacar el rango LLAVE FORANEA
    rango_indic = models.CharField(max_length=255, null=False, blank=False) #Rango del indicador
     