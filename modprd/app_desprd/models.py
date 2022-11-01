#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 18-08-2022

from django.db import models
from modprd.app_regprd.models import *




DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App del desarrollo del Producto de Investigación"],
    ['Descripción',"Aplicación para el desarrollo del Producto de investigación"],
    ['url_documento','doc'],
    ['url_install','modprd/app_desprd'],
    #['url_plantilla','app_desprd_iu.html'],
    #['Nombre_url','ini_desprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]
#clases de la aplicacion de desarrollo de productos

#Clase para la etapa del desarrollo de un producto

class prd_etp(models.Model):
    id_etp= models.AutoField(primary_key=True, null=False, blank=False, unique=True) #Identificador de la etapa LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)# Identificador del producto el cual atrievasa la etapa LLAVE FORANEA
    nom_etp=models.CharField('Nombre de la etapa de produccion: ', max_length=255, null=True, blank=False) #Nombre de la etapa
    desc_etp=models.TextField('Descripción de la etapa de produccion: ', null=True, blank=False) #Descripcion de la etapa
    esc_trl =models.IntegerField("Seleccione la escala de TRL del producto: ", choices=TRL_dic,default=TRL_dic[0]) #Estado de la escala de maduracion tecnologica
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro

#clase para el desarrollo de un producto

class prd_des (models.Model):
    id_desprd = models.AutoField(primary_key=True, null=False, unique=True) #Identificador del desarrollo de productos LLAVE PRIMARIA
    id_prd = models.ForeignKey(prd_base, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador del producto original LLAVE FORANEA
    id_etp_prd=models.ForeignKey(prd_etp, null=True, blank=True, on_delete=models.SET_NULL, db_constraint=True) #Identificador de la etapa del producto
    fch_ini=models.DateTimeField('Fecha de inicio de la etapa: ', null=False, blank=False) #fecha de inicio de la etapa
    fch_fin=models.DateTimeField('Fecha de finalizacion de la etapa: ', null=False, blank=False) #fecha de finalizacion de la etapa
    def indic_desa(self):
        return self.id_prd_new.id_prd
