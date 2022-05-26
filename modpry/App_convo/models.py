from django.db import models
from modpry.App_modpry.models import *
from modpry.App_regpry.models import *
from modcons.App_cons.models import *

APP_CONVO_PRY = [
    #Diccionario para la aplicación de convocatoria de proyecto
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

class convoca_pry(models.Model):
    #Clase que contiene la información de las convocatorias del proyecto
    id_convo =  models.AutoField(primary_key = True)#Id de la convocatoria
    nombre_convo = models.CharField('Nombre de la convocatoria:', max_length=255) #Nombre de la convocatoria
    desc_convo = models.CharField('Descripción de la convocatoria:', max_length=255) #Descripción de la convocatoria
    fch_ini_convo = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio de la convocatoria
    fch_fin_convo =  models.DateField(null=True, blank=True)#Fecha de finalización de la convocatoria
    # rl_info_convoca = models.ForeignKey(rl_info_convoca, null=False, blank =False)
    class Meta:
        verbose_name = 'convoca_pry'
        verbose_name_plural = 'convoca_prys'

class obj_esp_pry(models.Model):
    #Clase que define la metodología del proyecto
    id_obj_esp_pry = models.AutoField(primary_key = True) # Id de la metodología del proyecto
    objes1_metod = models.CharField('Objetivo específico 1 del proyecto:', max_length=255) # Objetivo específico 1 del proyecto
    objes2_metod = models.CharField('Objetivo específico 2 del proyecto:', max_length=255) # Objetivo específico 2 del proyecto
    objes3_metod = models.CharField('Objetivo específico 3 del proyecto:', max_length=255) # Objetivo específico 3 del proyecto
    
    class Meta:
        verbose_name = 'obj_esp_pry'
        verbose_name_plural = 'objs_esps_pry'

class metod_pry(models.Model):
    #Clase que define la metodología del proyecto
    id_metod_pry = models.AutoField(primary_key = True) # Id de la metodología del proyecto
    desc_metod = models.CharField('Descripción de la metodología del proyecto:', max_length=255)#Descripción de la metodología del proyecto
    obj1_metod = models.CharField('Objetivo específico 1 de la metodología:', max_length=255) # Objetivo específico 1 de la  metodología
    obj2_metod = models.CharField('Objetivo específico 2 de la metodología:', max_length=255) # Objetivo específico 2 de la  metodología
    obj3_metod = models.CharField('Objetivo específico 3 de la metodología:', max_length=255) # Objetivo específico 3 de la  metodología
    
    class Meta:
        verbose_name = 'metod_pry'
        verbose_name_plural = 'metod_prys'

class riesgo_pry(models.Model):
    #Clase que define los riesgos del proyecto
    id_riesgo_pry = models.AutoField(primary_key = True) # Id del riesgo del proyecto
    tipo_riesgo = models.IntegerField(null = False, blank = False, choices = TIPO_RIESGO, default = 0)#Tipo de riesgo del proyecto
    ries1 = models.CharField('Riesgo número 1 del proyecto:', max_length=255) #Riesgo 1 de la convocatoria
    ries2 = models.CharField('Riesgo número 2 del proyecto:', max_length=255) #Riesgo 2 de la convocatoria
    ries3 = models.CharField('Riesgo número 3 del proyecto:', max_length=255) #Riesgo 3 de la convocatoria

    class Meta:
        verbose_name = 'riesgo_pry'
        verbose_name_plural = 'riesgos_pry'


class impacto_pry(models.Model):
    #Clase que define los impactos del proyecto
    id_impacto_pry = models.AutoField(primary_key = True) # Id del impacto del proyecto
    tipo_imp = models.IntegerField(null = False, blank = False, choices = TIPO_IMPACTO, default = 0)#Tipo de impacto del proyecto
    imp1 = models.CharField('Impacto número 1 del proyecto:', max_length=255) #Impacto 1 de la convocatoria
    imp2 = models.CharField('Impacto número 2 del proyecto:', max_length=255) #Impacto 2 de la convocatoria
    imp3 = models.CharField('Impacto número 3 del proyecto:', max_length=255) #Impacto 3 de la convocatoria

    class Meta:
        verbose_name = 'impacto_pry'
        verbose_name_plural = 'impactos_pry'

class refe_pry(models.Model):
    #Clase que define las referencias del proyecto
    id_refe_pry = models.AutoField(primary_key = True) # Id del riesgo del proyecto
    refe1 = models.CharField('Referencia 1 del proyecto:', max_length=255) #Referencia 1 del proyecto
    refe2 = models.CharField('Referencia 2 del proyecto:', max_length=255) #Referencia 2 del proyecto
    refe3 = models.CharField('Referencia 3 del proyecto:', max_length=255) #Referencia 3 del proyecto

    class Meta:
        verbose_name = 'refe_pry'
        verbose_name_plural = 'refes_pry'

class info_convoca(models.Model):
    #Clase que contiene la información de la información necesaria para participar dentro de la convocatoria
    id_info_convo =  models.AutoField(primary_key = True)#Id de la información de la convocatoria
    titulo_pry = models.CharField('Titulo del proyecto:', max_length=255) # Titulo del proyecto
    fch_ini_pry = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio del proyecto
    fch_fin_fin =  models.DateField(null=True, blank=True)#Fecha de finalización del proyecto
    # inf_geo = models.IntegerField(null = False, blank = False, choices = DEPARTAMENTOS, default = 0) #Departamento donde se realizó el proyecto
    lin_tem = models.IntegerField(null = False, blank = False, choices = LINEA_TEMA, default = 0) #Línea temática
    justi_lin_tem = models.CharField('Justificación de la línea temática:', max_length=255)#Justificación de la línea temática
    inv_prin = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False) #Investigador principal
    resu_eje = models.CharField('Resumen ejecutivo del proyecto:', max_length=255) #Resumen ejecutivo
    obje_gen = models.CharField('Objetivo general del proyecto:', max_length=255)#Objetivo general
    obj_esp_pry = models.ForeignKey(obj_esp_pry, on_delete=models.SET_NULL, null=True, blank =False) #Objetivos específicos del proyecto
    plan_prob = models.CharField('Planteamiento del problema:', max_length=255)#Planteamiento del problema
    just_pry = models.CharField('Justificación del proyecto:', max_length=255)#Justificación del proyecto
    metod_pry = models.ForeignKey(metod_pry, on_delete=models.SET_NULL, null=True, blank =False)#Metodología del proyecto
    Est_desa = models.CharField('Descripción del estado de desarrollo del proyecto:', max_length=255)#Descripción del estado del desarrollo del proyecto
    estado_arte =  models.CharField('Estado de arte:', max_length=255)# Estado de arte 
    # estu_merca = models.ForeignKey(riesgo_pry, on_delete=models.SET_NULL, null=True, blank =False)
    resul_espe = models.CharField('Resultados esparados del proyecto:', max_length=255)#Resultados que se esperan del proyecto
    impacto_pry = models.ForeignKey(impacto_pry, on_delete=models.SET_NULL, null=True, blank =False)#Impacto del proyecto
    riesgo_pry = models.ForeignKey(riesgo_pry,  on_delete=models.SET_NULL, null=True, blank =False)#Riesgos del proyecto
    refe_pry = models.ForeignKey(refe_pry, on_delete=models.SET_NULL, null=True, blank =False) #Referencias del proyecto
    
    class Meta:
        verbose_name = 'info_convo'
        verbose_name_plural = 'info_convos'

class rl_info_convoca(models.Model):
    id_rel_info_conv = models.AutoField(primary_key = True) # Id de la relación entre la convocatoria y la información de la convocatoria
    id_info_convo = models.ForeignKey(info_convoca, on_delete=models.SET_NULL, null=True, blank =False)
    id_convo = models.ForeignKey(convoca_pry, on_delete=models.SET_NULL, null=True, blank =False)
