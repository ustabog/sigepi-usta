#app del registro de un producto-Modelos para SIGEPI
#AUTOR Daniel Alejandro Ballesteros Algarra
# Coautor(a):  Milton O. Castro Ch.
#fecha 12-08-2022

from django.db import models

from modadm.app_modadm.models import *
from modadm.app_modadm.dic import *

from modpry.app_regpry.models import *




DIC_APP = [
    #Diccionario de la aplicacion

    ['Titulo', "App Registro de Producto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Producto de Investigación"],
    ['url_documento','doc'],
    ['url_install','modprd/app_regprd'],
    ['url_plantilla','app_regprd_iu.html'],
    ['Nombre_url','ini_regprd'],
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

#Clase para la creacion de los requisitios de existencia de un producto

class prd_req_Exist(models.Model):
    id_reqexs=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del requerimiento de existencia LLAVE PRIMARIA
    nom_reqexs=models.CharField('Nombre del Requerimiento de existencia: ', max_length=255, blank=False,null=False)#Nombre del requerimiento de existencia
    desc_reqexs=models.TextField('Descripcion del Requerimiento de existencia: ', blank=True,null=False)#descripcion del requerimiento de existencia
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro
    
#Clase para la creacion de los requisitios de calidad de un producto

class prd_req_cal(models.Model):
    id_reqcal=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del requerimiento de calidad LLAVE PRIMARIA
    desc_reqcal=models.TextField('Descripcion del Requerimiento de calidad: ', blank=True,null=False)#descripcion del requerimiento de calidad
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro
    
#Clase para la creacion de las categorias de un producto

class prd_categ(models.Model):
    id_categ=models.AutoField(primary_key= True, null=False, unique=True)# Identificador de la categoria LLAVE PRIMARIA
    id_reqcal=models.ForeignKey(prd_req_cal, blank=False, null=True ,on_delete=models.SET_NULL, db_constraint=True)#Identificador del requerimiento de calidad para el registro de la categoria
    nom_categ=models.CharField('Nombre de la categoria: ', max_length=255, blank=False,null=False)#Nombre de la categoria
    peso_rel=models.PositiveIntegerField(null=False, blank=False, default=0)#Peso relativo de la categoria del producto
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro

#Clase para la creacion de campos para un producto

class campo(models.Model):
    id_campo =  models.AutoField(primary_key= True, null=False, unique=True)# Identificador del campo LLAVE PRIMARIA
    #id_tipo_campo= models.ForeignKey(blank=False, null=False ,on_delete=models.SET_NULL, db_constraint=True) #Identificador del tipo de campo
    nom_campo=models.CharField('Nombre del campo: ', max_length=255, blank=False, null=False)#Nombre del campo
    rango = models.CharField('Rango: ', max_length=255, blank=False, null=False) #Rango del campo
    Formato = models.CharField('Formato: ', max_length=255, blank=False, null=False) #Formato del campo
    valor_def = models.PositiveIntegerField('Valor por defecto del campo:', null=False, blank=False, default=0)# Valor por defecto del campo
    desc_campo= models.TextField('descripcion del campo: ', null=False, blank=False)#descripcion del campo
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro   

#Clase para la creacion de las plantillas de los productos segun los campos

class prd_plt_desc(models.Model):
    id_plt_desc = models.AutoField(primary_key= True, null=False, unique=True)# Identificador de la plantilla de la descripcion del producto LLAVE PRIMARIA
    id_campo = models.ForeignKey(campo,blank=False,on_delete=models.SET_NULL, null=True , db_constraint=True)# Identificador de campo de plantilla
    nom_plt=models.CharField('Nombre de la plantilla: ', max_length=255, blank=False, null=False)#Nombre de la plantilla para el producto
    desc_plt=models.TextField('Descripcion de la plantilla: ', blank=False, null=False) #Descripcion de la plantilla de producto
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro

#Clase para la relacion de un producto y un campo 

class rl_prd (models.Model):
    id_rl =models.AutoField(primary_key=True, null=False, unique=True, blank=False )# Identificador de la relacion de producto y campo LLAVE PRIMARIA
    id_Campo= models.ForeignKey(campo, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)#Identificador del campo
    valor_campo= models.IntegerField("Valor de campo: ", null=False, blank=False, default=0)#Valor de campo

#Clase para la creacion de un tipo de producto

class prd_tipo(models.Model):
    id_tipo=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del tipo del producto LLAVE PRIMARIA
    nom_tipo=models.CharField('Nombre del tipo de producto: ', max_length=255, blank=False, null=False)# Nombre del tipo de producto
    id_reqexist=models.ForeignKey(prd_req_Exist,null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de existencia
    id_categ=models.ForeignKey(prd_categ,null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador de la categoria
    id_reqcal=models.ForeignKey(prd_req_cal,null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificadores de los requerimientos de calidad
    peso_abs=models.IntegerField(null=False, blank=False, default=0)#Peso absoluto del producto segun minciencias
    vent_obs=models.PositiveIntegerField(null=False, blank=False, default=0)#ventana de observacion / Tiempo en años para la calificacion del tipo
    id_plt_desc=models.ForeignKey(prd_plt_desc,null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    tipo_cal=models.CharField('clasificacion segun la calidad: ', max_length=10,blank=True, null=False)
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro
    
# Clases de la aplicacion de registro de productos

class prd_base(models.Model):
    id_prd=models.AutoField(primary_key= True, null=False, unique=True)# Identificador del producto LLAVE PRIMARIA
    ids_pry=models.ManyToManyField(pry_base,blank=False, db_constraint=True)# Identificador del propietario
    nom_prd=models.CharField('Nombre del producto :',max_length=255, blank=False, null=False ) # Nombre del producto
    ids_usu=models.ForeignKey(User, null=True,blank=False, on_delete=models.SET_NULL, db_constraint=True)# Identificador del propietario
    fech_reg=models.DateTimeField('Fecha de registro: ', blank=False, null=False, auto_now_add=True) #fecha de registro
    fech_entrega=models.DateTimeField('Fecha de entrega: ') #fecha de entrega
    id_tipo_prd_minc=models.ForeignKey (prd_tipo,null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True) #Identificador del tipo de producto
    id_rl_prd_campos=models.ForeignKey (rl_prd,null=True,blank=False, on_delete=models.SET_NULL, db_constraint=True)#Identificador del campo de descripcion del producto
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0) #Estado de archivo del registro





    

    