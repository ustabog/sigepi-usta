from django.db import models
from modpry.App_modpry.models import *
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *

"""
Clases de la Aplicación Registro de Proyectos de Investigación
"""

class tipos_pry(models.Model):
    #Clase que contiene los tipos de proyectos Investigación descriptiva y de catalogación.
    #Investigación correlacional, Investigación explicativa, Investigación comparativa
    id_tipoproyecto = models.AutoField(primary_key = True)   # indentificador unico de tipo de proyecto
    nomb_tipoproyecto =  models.CharField('tipo de proyecto.', max_length=40, null=False, blank= False)
    desc_tipoproyecto =  models.CharField('Descripcion: ', max_length=40, null=False, blank= False)  # descripcionj del tipo de proyecto

    class Meta:
        verbose_name = 'tipos_pry'
        verbose_name_plural = 'tipos_prys'

class inf_pry(models.Model):
        #Clase que contiene toda la informacion referente al proyecto
    id_pry = models.AutoField(primary_key = True)  # identificador unico para  App Registro de Proyectos
    codigo_pry = models.CharField('codigo ', max_length=40, null=False, blank= False) # Código de identificación del proyecto.
    nombre_archivo = models.CharField('Nombre  ', max_length=40, null=False, blank= False) # Nombre del archivo del proyecto.
    url_archivo = models.URLField(' Url del archivo del proyecto.', null=False, blank=False) # Url del archivo del proyecto.
#    id_lineadeinvestigacion = 0 # Identificador de la linea de investigación
    titulo_pry = models.CharField('Título del proyecto.  ', max_length=40, null=False, blank= False) # # Título del proyecto. revisar
    id_grup_bd =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del grupo de investigación #tabla de grupo del modulo adm
    id_tipoproyecto = models.ForeignKey(tipos_pry, on_delete=models.CASCADE, null=False, blank =False)# indentificador unico de tipo de proyecto
    num_inv = models.IntegerField('Número de investigadores(as) involucrados en el proyecto')# Número de investigadores(as) involucrados en el proyecto.
    prom_frm = models.IntegerField(null = False, blank = False, choices = TIPO_FORM_CO, default = 0)  # Nivel de formación promedio del grupo 0:Profesional; 1:esp.; 2:Maestría; 3. Doctorado.
    conv = models.CharField('Convenio propuesto  ', max_length=40, null=False, blank= False)  # Convenio propuesto o previsto para la realización de la investigación.
    dur =  models.IntegerField('Duración del proyecto valores dentro de un rango.') # Duración del proyecto valores dentro de un rango.
    und_dur =  models.IntegerField(null = False, blank = False, choices = UNIDAD_MED_TIEM, default = 0)   # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
    geo = models.CharField('Aŕea geográfica que abarca el proyecto.', max_length=40, null=False, blank= False) # Aŕea geográfica que abarca el proyecto.
    resu = models.TextField('Resumen del proyecto.') # Resumen del proyecto.
    url_ap = models.URLField(' Url de la imágen del árbol de problemas.', null=False, blank=False) # Url de la imágen del árbol de problemas.
    url_ao = models.URLField('Url de la imágen del árbol de objetivos.', null=False, blank=False)  # Url de la imágen del árbol de objetivos.
    pobl_bnd = models.IntegerField('Tamaño de la población beneficiaria directa del proyecto.') #Tamaño de la ppoblación beneficiaria directa del proyecto.
    pobl_bni = models.IntegerField('Tamaño de la población beneficiaria indirecta .') #Tamaño de la población beneficiaria indirecta del proyecto.
    obj_gen = models.CharField('Objetivo general del proyecto..', max_length=40, null=False, blank= False) # Objetivo general del proyecto.
    obj_esp = models.CharField('Objetivos específicos del proyecto.', max_length=40, null=False, blank= False) # Objetivos específicos del proyecto.

    class Meta:
        verbose_name = 'inf_pry'
        verbose_name_plural = 'inf_prys'

class app_reg_pry(models.Model):
    #Clase que contiene los objetos de la App Registro de Proyectos
    id_app_reg_pry = models.AutoField(primary_key = True)  # identificador unico para  App Registro de Proyectos
    id_mod_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False, default = 0)
    id_mod_pry = models.ForeignKey(mod_pry, on_delete=models.CASCADE, null=False, blank =False) # Identificador único ddel modulo proyecto
    nomb_app_reg_pry  = models.CharField('nombre de la App Registro ', max_length=40, null=False, blank= False) # nombre de la App Registro de Proyectos
    desc_app_reg_pry  = models.CharField('Descripcion de la Ap  id_grup_bd = p ', max_length=40, null=False, blank= False) # descripcion de la App Registro de Proyectos
    status_app_reg_pry  =  models.BooleanField('Estatus de la aplicacion', default= True) # estatus de la App Registro de Proyectos

    class Meta:
        verbose_name = 'app_reg_pry'
        verbose_name_plural = 'app_reg_prys'
