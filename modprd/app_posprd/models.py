#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 18-08-2022

from django.db import models
from modadm.app_modadm.models import *
from modprd.app_regprd.models import *
from modprd.app_visprd.models import *



DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App del posicionamiento de los investigadores segun los productos"],
    ['Descripción',"Aplicación para el posicionamiento de los investigadores segun los productos"],
    ['url_documento','doc'],
    ['url_install','modprd/app_posprd'],
    #['url_plantilla','app_posprd_iu.html'],
    #['Nombre_url','ini_posprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]

#Clases de la aplicacion para el posicionamiento de los investigadores segun los productos

class pos_usu (models.Model):
    id_posusu = models.AutoField(primary_key=True, unique=True, null=False)#Identificador del posicionamiento del usuario LLAVE PRIMARIA
    ids_usu=models.ForeignKey(User,'Identificador del propietario: ', null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)#Identificador del usuario LLAVE FORANEA
    ids_prd=models.ForeignKey(prd_base ,'Identificador de los productos: ', null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)#Identificador de los productos LLAVE FORANEA
    ids_rang_indic=models.ForeignKey(rang_indic , null=False,blank=False, ondelete=models.SET_NULL, db_constraint=True)#Identificador de los rangos de los indicadores LLAVE FORANEA
    infor_pos= models.TextField(null=False, blank=False)# Informe del posicionamiento del usuario
    
