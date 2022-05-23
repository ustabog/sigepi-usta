from django.db import models
from django.contrib.auth.models import User
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *
from modpry.App_modpry.models import *
from modpry.App_regpry.models import *
"""
Clases de la Aplicación Gestión de Proyectos
"""

class app_ges_pry(models.Model):
    #Clase que contiene los objetos de la App Gestión de Proyectos

    id_ges_pry =  models.AutoField(primary_key = True)   # identificador unico para App Gestión de Proyectos
    id_mod_pry =  models.ForeignKey(mod_pry, on_delete=models.SET_NULL, null=True, blank =False)   # Identificador único del modulo proyecto
    nomb_ges_pry  = models.CharField('Nombre de la App ', max_length=40, null=False, blank= False)  # nombre de la App Gestión de Proyectos
    desc_ges_pry =  models.CharField(' descripcion de la App  ', max_length=40, null=False, blank= False)   # descripcion de la App Gestión de Proyectos
    status_ges_pry  = models.BooleanField('si logro el objetivo', default= False) # estatus de la App Gestión de Proyectos

    class Meta:
        verbose_name = 'app_ges_pry'
        verbose_name_plural = 'app_ges_prys'


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


