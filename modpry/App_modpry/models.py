from django.db import models
#from django.contrib.auth.models import User
from modpry.App_regpry.models import *

"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Proyectos
"""
ROL_MOD = [
    (0,'Investigador(a) Proy.'),
    (1,'Evaluador(a) Proy.'),
    (2,'Tutor(a) Proy.'),
    (3,'Director(a) Proy.'),
    (4,'Codirector(a) Proy.'),
    (5,'Asesor(a) Proy.'),
    (6,'Gestor(a) de Inv.'),
    (7,'Curador(a)'),
    (8,'Actor Externo'),
    ]

REG_PRY = [
    (0,'Id registro de proyecto'),
    (1,'Nombre del proyecto'),
    (2,'Descripción del proyecto'),
    (3,'Estado del proyecto'),
    ]

#Clases del Módulo Proyectos de SIGEPI
class mod_pry(models.Model):
    #Clase de la aplicación de módulo de proyecto
    id_mod_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_mod_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicacion
    desc_mod_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion del aplicacion
    status_mod_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicacion
    
    class Meta:
        verbose_name = 'mod_pry'
        verbose_name_plural = 'mod_prys'

class conv_pry(models.Model):
    #Clase de la aplicación de convenios del módulo de proyecto
    id_mod_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_conv_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicacion de convenios del módulo de proyectos
    desc_conv_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion del aplicacion de convenios del módulo de proyectos
    status_conv_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicacion de convenios del módulo de proyectos
    
    class Meta:
        verbose_name = 'conv_pry'
        verbose_name_plural = 'conv_prys'

class crono_pry(models.Model):
    #Clase de la aplicación cronograma del módulo de proyecto
    id_crono_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_crono_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicacion cronograma del módulo de proyectos
    desc_crono_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion del aplicacion cronograma del módulo de proyectos
    status_crono_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicacion cronograma del módulo de proyectos
    
    class Meta:
        verbose_name = 'crono_pry'
        verbose_name_plural = 'crono_prys'

class dis_inv_pry(models.Model):
    #Clase de la aplicación diseño de investigación del módulo de proyecto
    id_disinv_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_disinv_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicacion diseño de investigación del módulo de proyecto
    desc_disinv_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la aplicacion diseño de investigación del módulo de proyecto
    status_disinv_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicacion diseño de investigación del módulo de proyecto
    
    class Meta:
        verbose_name = 'dis_inv_pry'
        verbose_name_plural = 'dis_inv_prys'  

class eva_pry(models.Model):
    #Clase de la aplicación de evaluación de proyectos 
    id_eva_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_eva_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicación de evaluación de proyectos 
    desc_eva_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la aplicación de evaluación de proyectos 
    status_eva_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicación de evaluación de proyectos 
    
    class Meta:
        verbose_name = 'eva_pry'
        verbose_name_plural = 'eva_prys' 

class ges_pry(models.Model):
    #Clase de la aplicación de gestión de proyectos 
    id_ges_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_ges_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicación de gestión de proyectos 
    desc_ges_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la aplicación de gestión de proyectos 
    status_ges_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicación de gestión de proyectos 
    
    class Meta:
        verbose_name = 'ges_pry'
        verbose_name_plural = 'ges_prys' 

class mlog_pry(models.Model):
    #Clase de la aplicación de marco lógico
    id_mlog_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_mlog_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicación de marco lógico del proyecto
    desc_mlog_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la aplicación de marco lógico del proyecto
    status_mlog_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicación de marco lógico del proyecto
    
    class Meta:
        verbose_name = 'mlog_pry'
        verbose_name_plural = 'mlog_prys'   

class recur_pry(models.Model):
    #Clase de la aplicación de recursos del proyecto
    id_recur_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_recur_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicación de recursos del proyecto
    desc_recur_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la aplicación de recursos del proyecto
    status_recur_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicación de recursos del proyecto
    
    class Meta:
        verbose_name = 'recur_pry'
        verbose_name_plural = 'recur_prys' 

class regprgi(models.Model):
    #Clase de la Aplicación Registro de Programas de Investigación
    id_regprgi = models.AutoField(primary_key = True) # Identificador único
    nomb_regprgi = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la Aplicación Registro de Programas de Investigación
    desc_regprgi  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion de la Aplicación Registro de Programas de Investigación
    status_regprgi = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la Aplicación Registro de Programas de Investigación
    
    class Meta:
        verbose_name = 'regprgi_pry'
        verbose_name_plural = 'regprgi_prys'
