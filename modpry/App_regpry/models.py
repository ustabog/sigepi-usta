from django.db import models
from modpry.App_regpry.models import*
from modpry.App_modpry.models import TIPO_PRY, ESTADO_PRY

#clase base de registro de proyecto
class pry(models.Model):
    id_pry=models.AutoField(primary_key = True) #Identificador unico del proyecto
    cod_pry = models.CharField('Codigo:', max_length= 100, null = False, blank = False) # código unico del proyecto
    nombre_pry=models.CharField('Nombre del proyecto: ', max_length=255)#Nombre proyecto
    desc_pry=models.CharField('Descripción del proyecto: ', max_length=50, null=False, blank=False)#Decripción del proyecto
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
        verbose_name = 'pry'
        verbose_name_plural = 'prys'

