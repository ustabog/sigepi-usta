from django.db import models
from django.contrib.auth.models import User
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *
from modpry.app_modpry.models import *
from modpry.app_regpry.models import *
"""
Clases de la Aplicación Gestión de Proyectos
"""
APP_GES_PRY = [
    #Diccionario para la aplicación de gestión de proyecto
    (0,'Titulo')
    (1,'Descripción'),
    (2,'url_documento'),
    (3,'url_instal'),
    (4,'url_plantilla'),
    (5,'Nombre_url'),
    (6,'Versión aplicación'),
    (7,'id_mod'),
    (8,'Versión_módulo'),
    (9,'estado'),
    (10,'instalada')
    (11, 'visible')
    ]

TIPO_DEP = [
    (0,'Administrativa'),
    (1,'Investigación'),
    (2, 'Financiera'),
    (3, 'Sindicatura'),
    (4, 'Bienestar'), 
    (5, '')
]

class proceso(models.Model):
    #Clase de un proceso
    id_pro =  models.AutoField(primary_key = True) #ID del proceso
    nombre_pro = models.CharField('Nombre del proceso:', max_length=40, null=False, blank= False)#Nombre del proceso
    desc_pro = models.CharField('Descripción del proceso:', max_length=40, null=False, blank= False)#Descripción del proceso
    encar_pro = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#Encargado del proceso
    pro_padre = models.BooleanField ('¿Proceso padre', default=False) #Si el proceso es padre
    pro_hijo = models.BooleanField ('¿Proceso hijo', default=False) #Si el proceso es hijo

    class Meta:
        verbose_name = 'proceso'
        verbose_name_plural = 'procesos'

class registro(models.Model):
    #Clase que almacena los registros de un proceso
    id_pro =  models.AutoField(primary_key = True) #ID del proceso
    nombre_pro = models.CharField('Nombre del registro:', max_length=40, null=False, blank= False)#Nombre del proceso
    desc_pro = models.CharField('Descripción del registro:', max_length=40, null=False, blank= False)#Descripción del proceso
    tipo_reg = models.CharField('Tipo de registro:', max_length=40, null=False, blank= False)#Especifica el tipo de registro que esta haciendo
    url_doc = models.URLField('URL del documento', null=False, blank=False)#Dirección del documento de registro
    
    class Meta:
        verbose_name = 'registro'
        verbose_name_plural = 'registros'

class actor(models.Model):
    #clase que contiene los actores de un proceso
    id_actor = models.AutoField(primary_key = True)#ID del actor
    class Meta:
        verbose_name = 'actor'
        verbose_name_plural = 'actores'

class dependencia(models.Model):
    #Clase que contiene las dependencias de un proceso
    id_dep =models.AutoField(primary_key = True) #ID de la dependencia
    tipo_dep = models.IntegerField(choices=TIPO_DEP, default = 0, null=False, blank = False)#RTipo de dependencia
    nombre_dep = models.CharField('Nombre de la dependencia:', max_length=255, null=False, blank= False )#Nombre de la dependencia
    class Meta:
        verbose_name = 'dependencia'
        verbose_name_plural = 'dependencias'

class requerimiento(models.Model):
    #Clase que contiene los requerimientos de un proceso
    id_req =models.AutoField(primary_key = True)#ID de requerimientos
    url_docu = models.URLField('URL del documento', null=False, blank=False)#URL del documento
    ima_pro = models.ImageField(upload_to=None)#Imagen para el proceso
    docu_pro = models.FileField(upload_to = None)#Documento para el proceso
    class Meta:
        verbose_name = 'requerimiento'
        verbose_name_plural = 'requerimientos'

'''
class inf_ges_pry(models.Model):
    #Clase que contiene la informacion de la gestion del proyecto
    id_ges_pry =  models.AutoField(primary_key = True)   # identificador unico para App Gestión de Proyectos
    Form_proy = models.CharField('Formulación o diseño del Proyecto', max_length=40, null=False, blank= False) # Formulación o diseño del Proyecto: Es la expresión de las características y metodologías de un proyecto, expresando la temporalidad en el cual se realiza.',
    Eva_proy = models.CharField('evaluación del Proyecto:', max_length=40, null=False, blank= False)  # evaluación del Proyecto: Se valora el proyecto de acuerdo a los indicadores construidos y acordados para su medición .',
    Eje_proy =  models.CharField('Ejecución del Proyecto', max_length=40, null=False, blank= False) # Ejecución del Proyecto: Es realizar la gestión y accionesestablecidas en la formulación del proyecto.',
    Proy = models.CharField('compilación de de tres momentos', max_length=80, null=False, blank= False) # Es la compilación de de tres momentos de la ejecución de  una idea: Formulación, implementación y evaluación.',
    idproy = models.ForeignKey(inf_pry, on_delete=models.SET_NULL, null=True, blank =False)  # Es la compilación de de tres momentos de la ejecución de  una idea: Formulación, implementación y evaluación.',

    class Meta:
        verbose_name = 'inf_ges_pry'
        verbose_name_plural = 'inf_ges_prys'

class obj_esp(models.Model):
    #Clase que define los objetivos especificos 
    id_obj_esp_pry = models.AutoField(primary_key = True) # Id de la metodología de los objetivos especificos 
    objesp1 = models.CharField('Objetivo específico 1 del proyecto:', max_length=255) # Objetivo específico 1 del proyecto
    objesp2 = models.CharField('Objetivo específico 2 del proyecto:', max_length=255) # Objetivo específico 2 del proyecto
    objesp3 = models.CharField('Objetivo específico 3 del proyecto:', max_length=255) # Objetivo específico 3 del proyecto
    
    class Meta:
        verbose_name = 'obj_esp'
        verbose_name_plural = 'objs_esps'

class mar_teo(models.Model):
    #Clase que almacena el marco teórico
    id_mar_teo = models.AutoField(primary_key = True) # Id del marco teórico
    conc1 = models.CharField('Concepto 1:', max_length=255) # Concepto 1
    conc2 = models.CharField('Concepto 2:', max_length=255) # Concepto 2
    conc3 = models.CharField('Concepto 3:', max_length=255) # Concepto 3
    fnt_pri= models.CharField('Fuente principal:', max_length=255) # Fuente principal
    fnt_sec = models.CharField('Fuente secundaria:', max_length=255) # Fuente secuendaria

    class Meta:
        verbose_name = 'mar_teo'
        verbose_name_plural = 'mars_teos'

class mar_con(models.Model):
    #Clase que almacena el marco conceptual
    id_mar_teo = models.AutoField(primary_key = True) # Id del marco conceptual
    conc1 = models.CharField('Concepto 1:', max_length=255) # Concepto 1
    conc2 = models.CharField('Concepto 2:', max_length=255) # Concepto 2
    conc3 = models.CharField('Concepto 3:', max_length=255) # Concepto 3
    fnt_pri= models.CharField('Fuente principal:', max_length=255) # Fuente principal
    fnt_sec = models.CharField('Fuente secundaria:', max_length=255) # Fuente secuendaria

    class Meta:
        verbose_name = 'mar_con'
        verbose_name_plural = 'mars_cons'

class cpto_pry(models.Model):
    #Clase que almacena los datos de la conceptualización del proyecto
    id_cpto_proy = models.AutoField(primary_key = True)#Identificador de la conceptualización del proyecto
    nombre_plan = models.CharField('Nombre del plan del proyecto', max_length=40, null=False, blank= False)
    desc_plan = models.CharField('Descripción del plan del proyecto', max_length=40, null=False, blank= False)
    obj_gen = models.CharField('Objetivo general del proyecto:', max_length=40, null=False, blank= False)
    obj_esp = models.ForeignKey(obj_esp, on_delete=models.SET_NULL, null=True, blank =False) #Objetivos específicos
    fch_ini = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio del proyecto
    fch_fin =  models.DateField(null=True, blank=True)#Fecha de finalización del proyecto
    mar_teo = models.ForeignKey(mar_teo, on_delete=models.SET_NULL, null=True, blank =False)
    mar_con =  models.ForeignKey(mar_con, on_delete=models.SET_NULL, null=True, blank =False)
    class Meta:
        verbose_name = 'cpto_pry'
        verbose_name_plural = 'cpto_prys'

'''
