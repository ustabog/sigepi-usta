#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 12-08-2022

from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from modadm.app_modadm.models import *
from modadm.app_modadm.dic import *


DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App Registro de Producto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Producto de Investigación"],
    ['url_documento','doc'],
    ['url_instal','modprd/app_regprd'],
    #['url_plantilla','app_regprd_iu.html'],
    #['Nombre_url','ini_regprd'],
    ['Versión aplicación','0.0.0'],
    ['id_mod', 5],
    ['Versión_módulo', 'alfa'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
]
# Diccionario de los roles de la aplicacion
ROL_APP = [
    (0,'Investigador(a) Principal'),
    (1,'Propietario(a) Proy.'),
    (2,'Investigador(a) Secundario'),
    (3,'Colaborador(a)')
    ]

# Clases de la aplicacion de registro de productos

class prd_base(models.Model):
    id_prd=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del producto LLAVE PRIMARIA
    nom_prd=models.CharField('Nombre del proyecto :',max_length=255, blank=True, null=False ) # Nombre del producto
    ids_usu=models.ForeignKey('Identificador del propietario: ',User, null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True)# Identificador del propietario
    fech_reg=models.DateTimeField('Fecha de registro: ') #fecha de registro
    fech_entrega=models.DateTimeField('Fecha de entrega: ') #fecha de entrega
    id_etp_prd=models.ForeignKey ('Identificador de la etapa de producto',null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True) #Identificador de la etapa de producto
    id_tipo_prd_minc=models.ForeignKey ('Identificador del tipo de producto',null=True, blank=False, ondelete=models.SET_NULL=True, db_constraint=True) #Identificador del tipo de producto
    mediciones_dic=[
        ('sin', 'sin medicion')
        ('en medicion', 'en medicion')
        ('medido', 'medido')
        ('obsoleto', 'obsoleto')
    ]
    est_med=models.Choices('seleccione estado de medicion'_MAX_LENGTH=11,choices=mediciones_dic,default=mediciones_dic[0]) #Estado de medicion
    ids_med=models.ForeignKey ('Identificadores de las mediciones del producto',null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True)#Identificadores de las mediciones del producto
    id_cert=models.ForeignKey ('Identificador de la certificacion del producto',null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True)#Identificadores de las mediciones del producto
    id_desprd=models.ForeignKey ('Identificador del desarrollo del producto',null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True)#Identificador del desarrollo del producto
    id_rl_prd_campos=models.ForeignKey (null=True,blank=False, ondelete=models.SET_NULL=True, db_constraint=True)#Identificador del campo de descripcion del producto

class prd_tipo(models.Model):
    id_tipo=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del tipo del producto LLAVE PRIMARIA
    nom_tipo=models.CharField('Nombre del tipo de producto: ', max_length=255, blank=True, null=False)# Nombre del tipo de producto
    id_reqexist=models.ForeignKey(null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de existencia
    id_categ=models.ForeignKey(null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador de la categoria
    id_reqcal=models.ForeignKey(null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de calidad
    peso_rel=models.

    

    