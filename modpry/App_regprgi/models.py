from django.db import models
from modpry.App_modpry.models import *
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *
from modcons.App_cons.models import *

APP_PRG_INV = [
    #Diccionario para la aplicación de programa de investigación
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

# Clases de la Aplicación Registro de Programas de Investigación

class tipos_prog_inv(models.Model):
    #Clase que contiene los tipos de proyectos Investigación descriptiva y de catalogación.
    #Investigación correlacional, Investigación explicativa, Investigación comparativa
    id_tipoprograma = models.AutoField(primary_key = True)   # indentificador unico de tipo de proyecto
    nomb_tipoprogama =  models.CharField('tipo de programa.', max_length=40, null=False, blank= False)
    desc_tipoprograma =  models.CharField('Descripcion: ', max_length=40, null=False, blank= False)  # descripcionj del tipo de proyecto

    class Meta:
        verbose_name = 'tipos_prog_inv'
        verbose_name_plural = 'tipos_prog_invs'

class inf_prog_inv(models.Model): #verificar esta tabla
    #Clase que contiene toda la informacion referente al proyectoid_pry = models.AutoField(primary_key = True)  # identificador unico para  App Registro de Proyectos
    id_inf_prog_inv = models.AutoField(primary_key = True)  #
    codigo_prog = models.CharField('codigo ', max_length=40, null=False, blank= False) # Código de identificación del proyecto.
    nombre_archivo = models.CharField('Nombre  ', max_length=40, null=False, blank= False) # Nombre del archivo del proyecto.
    url_archivo = models.URLField(' Url del archivo del proyecto.', null=False, blank=False) # Url del archivo del proyecto.
    #    id_lineadeinvestigacion = 0 # Identificador de la linea de investigación
    titulo_prog = models.CharField('Título del programa .  ', max_length=40, null=False, blank= False) # # Título del proyecto. revisar
    id_grup_bd =  models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank =False)  #  # Identificador del grupo de investigación
    id_tipoprograma = models.ForeignKey(tipos_prog_inv, on_delete=models.SET_NULL, null=True,  blank =False) # indentificador unico de tipo de proyecto
    num_inv = models.IntegerField('Número de investigadores(as) involucrados en el proyecto')# Número de investigadores(as) involucrados en el proyecto.
    prom_frm = models.IntegerField(null = False, blank = False, choices = TIPO_FORM_CO, default = 0)  # Nivel de formación promedio del grupo 0:Profesional; 1:esp.; 2:Maestría; 3. Doctorado.
    conv = models.CharField('Convenio propuesto  ', max_length=40, null=False, blank= False)  # Convenio propuesto o previsto para la realización de la investigación.
    dur =  models.IntegerField('Duración del proyecto valores dentro de un rango.') # Duración del proyecto valores dentro de un rango.
    #und_dur =  models.IntegerField(null = False, blank = False, choices = UNIDAD_MED_TIEM, default = 0)   # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
    geo = models.CharField('Aŕea geográfica que abarca el progama.', max_length=40, null=False, blank= False) # Aŕea geográfica que abarca el proyecto.
    resu = models.TextField('Resumen del programa.') # Resumen del proyecto.
    url_ap = models.URLField(' Url de la imágen del árbol de problemas.', null=False, blank=False) # Url de la imágen del árbol de problemas.
    url_ao = models.URLField('Url de la imágen del árbol de objetivos.', null=False, blank=False)  # Url de la imágen del árbol de objetivos.
    pobl_bnd = models.IntegerField('Tamaño de la población beneficiaria directa del proyecto.') #Tamaño de la ppoblación beneficiaria directa del proyecto.
    pobl_bni = models.IntegerField('Tamaño de la población beneficiaria indirecta .') #Tamaño de la población beneficiaria indirecta del proyecto.
    obj_gen = models.CharField('Objetivo general del proyecto..', max_length=40, null=False, blank= False) # Objetivo general del proyecto.
    obj_esp = models.CharField('Objetivos específicos del proyecto.', max_length=40, null=False, blank= False) # Objetivos específicos del proyecto.

    class Meta:
        verbose_name = 'inf_prog_inv'
        verbose_name_plural = 'inf_prog_invs'

