from django.db import models
from django.contrib.auth.models import User
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *
from modpry.App_modpry.models import *
from modpry.App_regpryi.models import *
"""
Clases de la Aplicación Gestión de Proyectos
"""

class app_ges_pry(models.Model):
    #Clase que contiene los objetos de la App Gestión de Proyectos

    id_ges_pry =  models.AutoField(primary_key = True)   # identificador unico para App Gestión de Proyectos
    id_mod_pry =  models.ForeignKey(mod_pry, on_delete=models.CASCADE, null=False, blank =False)   # Identificador único ddel modulo proyecto
    nomb_ges_pry  = models.CharField('Nombre de la App ', max_length=40, null=False, blank= False)  # nombre de la App Gestión de Proyectos
    desc_ges_pry =  models.CharField(' descripcion de la App  ', max_length=40, null=False, blank= False)   # descripcion de la App Gestión de Proyectos
    status_ges_pry  = models.BooleanField('si logro el objetivo', default= False) # estatus de la App Gestión de Proyectos

    class Meta:
        verbose_name = 'app_ges_pry'
        verbose_name_plural = 'app_ges_prys'


class inf_ges_pry(models.Model):
    #Clase que contiene lla informacion de la gestion del proyecto

    inf_ges_pry =  models.AutoField(primary_key = True)   # identificador unico para App Gestión de Proyectos
    Cpto_proy = models.CharField('Conceptualización del Proyecto:', max_length=40, null=False, blank= False)  # Conceptualización del Proyecto: Es realizar el marco teórico y coneptual de la o las ideas principaples del proyecto.',
    Form_proy = models.CharField('Formulación o diseño del Proyecto', max_length=40, null=False, blank= False) # Formulación o diseño del Proyecto: Es la expresión de las características y metodologías de un proyecto, expresando la temporalidad en el cual se realiza.',
    Eva_proy = models.CharField('evaluación del Proyecto:', max_length=40, null=False, blank= False)  # evaluación del Proyecto: Se valora el proyecto de acuerdo a los indicadores construidos y acordados para su medición .',
    Eje_proy =  models.CharField('Ejecución del Proyecto', max_length=40, null=False, blank= False) # Ejecución del Proyecto: Es realizar la gestión y accionesestablecidas en la formulación del proyecto.',
    Proy = models.CharField('compilación de de tres momentos', max_length=80, null=False, blank= False) # Es la compilación de de tres momentos de la ejecución de  una idea: Formulación, implementación y evaluación.',
    idproy = models.ForeignKey(inf_pry, on_delete=models.CASCADE, null=False, blank =False)  # Es la compilación de de tres momentos de la ejecución de  una idea: Formulación, implementación y evaluación.',

    class Meta:
        verbose_name = 'inf_ges_pry'
        verbose_name_plural = 'inf_ges_prys'
