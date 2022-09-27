#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 18-08-2022

from django.db import models
from modprd.app_regprd.models import *
from modprd.app_certprd.models import *



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

class prd_des (models.Model):
    id_desprd = models.AutoField(primary_key=True, null=False, unique=True) #Identificador del desarrollo de productos LLAVE PRIMARIA
    id_prd_orig = models.ForeignKey(prd_base, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador del producto original LLAVE FORANEA
    id_prd_new=models.ForeignKey(prd_base, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador del producto en desarrollo
    id_etp_prd=models.ForeignKey(prd_etp, null=True, blank=True, on_delete=models.SET_NULL, db_constraint=True) #Identificador de la etapa del producto
    fch_ini=models.DateTimeField('Fecha de inicio de la etapa: ', null=False, blank=False) #fecha de inicio de la etapa
    fch_fin=models.DateTimeField('Fecha de finalizacion de la etapa: ', null=False, blank=False) #fecha de finalizacion de la etapa
    def indic_desa(self):
        return self.id_prd_new.id_prd
