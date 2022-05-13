from django.db import models
#from django.contrib.auth.models import User
from modpry.App_regpry.models import *

"""
Listas únicas, Conjuntos y Diccionarios del Módulo de Proyectos
"""
ROL_MOD = [
    (0,'Investigador(a) Proy.'),
    (1,'Evaluador(a) Proy.'),
    (4,'Tutor(a) Proy.'),
    (5,'Director(a) Proy.'),
    (6,'Codirector(a) Proy.'),
    (7,'Asesor(a) Proy.'),
    (8,'Gestor(a) de Inv.'),
    (9,'Curador(a)'),
    (10,'Actor Externo'),
    ]


#Clases del Módulo Proyectos de SIGEPI
class mod_pry(models.Model):
    id_mod_pry = models.AutoField(primary_key = True) # Identificador único
    nomb_mod_pry = models.CharField('Nombre ', max_length=40, null=False, blank = False) # nombre de la aplicacion
    desc_mod_pry  = models.CharField('Decripcion ', max_length=40, null=False, blank = False) # descripcion del aplicacion
    status_mod_pry = models.BooleanField('¿status de la aplicacion.?', default=False)  # estatus de la aplicacion
    
    class Meta:
        verbose_name = 'mod_pry'
        verbose_name_plural = 'mod_prys'

class pry_base(models.Model):
    #clase base de registro de proyecto
    id_pry=models.AutoField(primary_key = True) #Identificador unico del proyecto
    cod_pry = models.CharField('Código proyecto:', max_length=50) # código unico del proyecto
    nombre_pry=models.CharField('Nombre del proyecto: ', max_length=255)#Nombre proyecto
    desc_pry=models.CharField('Descripción del proyecto: ', max_length=255, null=False, blank=False)#Decripción del proyecto
    tipo_pry=models.IntegerField(null = False, blank = False, choices = TIPO_PRY, default = 0) # Tipo de proyecto - diccionario TIPO_PRY
    prop_pry=models.CharField('Propietario del proyecto: ', max_length=255)#Propietario del proyecto
    est_pry = models.IntegerField(null = False, blank = False, choices = ESTADO_PRY, default = 0)
    #estado - por defecto borrador
    # debe esta diseño y gestion como opción, DIVIDIR LA CLASE EN PARTICIPANTES, beneficiarios, 
    #el ususario puede crear nuevos tipos, ejemplo otros 
    #campo saber, campo disciplinar, nuevo conocimiento 
    #programa: categoria de proyectos, ampliar, perosnas, grupos, divisiones, div academ y adminis, dependencias,
    #tipos progr categorias
    #información de usuario: clasificar el rol con rol de investigador, procesos(estado del proceso)
    #cvalc ordic otra clase de visibilidad o publicidad del investigador, mirar desde ad,, enlace de esa información, 
    
    class Meta:
        verbose_name = 'pry_base'
        verbose_name_plural = 'proyectos base'
