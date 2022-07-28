# App del diseño de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
from modpry.app_modpry.models import *
from modpry.app_regpry.models import *
from modadm.app_modadm.dic import *
from modadm.app_modadm.models import *

INF_APP = [
    #Diccionario para la aplicación de diseño de investigación
    ['Titulo', "App Diseño de de un Proyecto Investigación"],
    ['Descripción',"aplicación para la definición del diseño de un proyecto de investigación"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_disinv'],
    ['url_plantilla','app_disinv_iu.html'],
    ['Nombre_url','ini_disinv'],
    ['Versión aplicación','0.1.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', False],
    ['visible', False],
    ]

#Crear funciones de delimitación, delimitación temporal, delimitación temática
class tema(models.Model):
    #Clase que define los temas del proyecto
    id_tema = models.AutoField(primary_key = True)#Id de temas
    tema = models.CharField('Tema:', max_length=100) #Tema
    desc_categ = models.CharField('Descripción de la categoria:', max_length=255) #Descripción de la categoria tematica del proyecto
    categ = models.CharField('Palabras claves:', max_length=255) #Categoria tematica del proyecto
    tema_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el tema es borrado queda como archivado
    
    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'temas'

class defin(models.Model):
    id_def = models.AutoField(primary_key = True)#Id de definiciones
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)
    ver = models.CharField('Versión:', max_length=255)#Versión de las definiciones
    tipo = models.IntegerField(null = False, blank = False, choices = CATG, default = 0)#Tipo de definción
    fch_reg = models.DateField(null=True, blank=True)#Fecha de registro de la definción
    vers1=  models.CharField('Versión 1:', max_length=255)#Versión 1
    vers2=  models.CharField('Versión 2:', max_length=255)#Versión 2
    vers3=  models.CharField('Versión 3:', max_length=255)#Versión 3
    vers4=  models.CharField('Versión 4:', max_length=255)#Versión 4
    vers5=  models.CharField('Versión 5:', max_length=255)#Versión 5
    fch_mod = models.DateField(null=True, blank=True)#Fecha de modificación
    defi_archi = models.BooleanField(null = False, blank = False, default = 0)#Si la definción es borrada queda como archivada
    class Meta:
        verbose_name = 'def'
        verbose_name_plural = 'defs'

class arb_pro(models.Model):
    #Clase del arbol de problemas
    id_arb_pro = models.AutoField(primary_key = True)#Id del árbol de problemas
    tit_ap = models.CharField('Palabras claves:', max_length=255) #Titulo del árbol de problemas
    nomb_arc = models.CharField('Nombre del archivo del árbol de problemas:', max_length=255) #Nombre del archivo del árbol de problemas
    url_arc = models.URLField('URL del archivo del árbol de problemas:', null=False, blank=False)#URL del archivo del árbol de problemas
    ap_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el árbol de problemas es borrado queda como archivado
    class Meta:
        verbose_name = 'arb_pro'
        verbose_name_plural = 'arb_pros'

class arb_obj(models.Model):
    #Clase del arbol de objetivos
    id_arb_obj = models.AutoField(primary_key = True)#Id del árbol de objetivos
    tit_ao = models.CharField('Titulo árbol de objetivos:', max_length=255) #Titulo del árbol de objetivos
    nomb_arc = models.CharField('Nombre del archivo del árbol de objetivos:', max_length=255) #Nombre del archivo del árbol de objetivos
    url_arc = models.URLField('URL del archivo del árbol de objetivos:', null=False, blank=False)#URL del archivo del árbol de objetivos
    ao_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el árbol de objetivos es borrado queda como archivado

    class Meta:
        verbose_name = 'arb_obj'
        verbose_name_plural = 'arb_objs'

class causa(models.Model):
    #Clase que define las causas de un arbol de problemas
    id_cau = models.AutoField(primary_key = True)#Id de la clase causas
    nomb_cau = models.CharField('Nombre de la causa:', max_length=255)#Nombre de la causa
    desc_cau = models.CharField('Descripción de la causa:', max_length=255)#Descripción de la causa
    nivel_cau = models.CharField('Nivel de la causa:', max_length=255)#Nivel primario, secundario o terciario
    defs = models.ForeignKey(defin, on_delete=models.SET_NULL, null=True, blank =False)#Definiciones 
    cau_archi = models.BooleanField(null = False, blank = False, default = 0)#Si la causa es borrada queda como archivada

    class Meta:
        verbose_name = 'causa'
        verbose_name_plural = 'causas'

class efecto(models.Model):
    id_efe = models.AutoField(primary_key = True)#Id de la clase efecto
    nomb_efe = models.CharField('Nombre del efecto:', max_length=255)#Nombre del efecto
    desc_efe = models.CharField('Descripción del efecto:', max_length=255)#Descripción del efecto
    nivel_efe = models.CharField('Nivel del efecto:', max_length=255)#Nivel primario, secundario o terciario
    defs = models.ForeignKey(defin, on_delete=models.SET_NULL, null=True, blank =False)#Definiciones 
    efe_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el efecto es borrado queda como archivado

    class Meta:
        verbose_name = 'efecto'
        verbose_name_plural = 'efectos'

class medio(models.Model):
    id_med = models.AutoField(primary_key = True)#Id de la clase medio
    nomb_med = models.CharField('Nombre del medio:', max_length=255)#Nombre del medio
    desc_med = models.CharField('Descripción del medio:', max_length=255)#Descripción del medio
    nivel_med = models.CharField('Nivel del medio:', max_length=255)#Nivel primario, secundario o terciario
    defs = models.ForeignKey(defin, on_delete=models.SET_NULL, null=True, blank =False)#Definiciones 
    med_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el medio es borrado queda como archivado

    class Meta:
        verbose_name = 'medio'
        verbose_name_plural = 'medios'

class fin(models.Model):
    id_fin = models.AutoField(primary_key = True)#Id de la clase fin
    nomb_fin = models.CharField('Nombre del fin:', max_length=255)#Nombre del fin
    desc_fin = models.CharField('Descripción del fin:', max_length=255)#Descripción del fin
    nivel_fin = models.CharField('Nivel del fin:', max_length=255)#Nivel primario, secundario o terciario
    defs = models.ForeignKey(defin, on_delete=models.SET_NULL, null=True, blank =False)#Definiciones 
    fin_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el fin es borrado queda como archivado

    class Meta:
        verbose_name = 'fin'
        verbose_name_plural = 'fines'

class dis_pry(models.Model):
    #Clase del diseño de un proyecto
    id_dis_pry =  models.AutoField(primary_key = True)#Id de la convocatoria
    id_usu = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank = False, db_constraint=False) #Encargado del diseño de un proyecto de investigación
    nomb_dis = models.CharField('Nombre del diseño de investigación:', max_length=255) #Nombre para el registro de un diseño de un proyecto de investigación
    tipo_inv = models.IntegerField(null = False, blank = False, choices = TIPO_PRY, default = 0) #Tipo de investigación del proyecto
    delim_tem = models.CharField('Delimitación temática del proyecto:', max_length=255) #Delimitación tematica del proyecto
    fch_ini_dis = models.DateField(null=True, blank=True)#Fecha de inicio del diseño del proyecto
    fch_fin_dis = models.DateField(null=True, blank=True)#Fecha de finalización del diseño del proyecto
    arb_pro = models.ForeignKey(arb_pro, on_delete=models.SET_NULL, null=True, blank =False)#Id árbol de problemas
    arb_obj = models.ForeignKey(arb_obj, on_delete=models.SET_NULL, null=True, blank =False)#Id árbol de objetivos
    dis_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el diseño del pry es borrado queda como archivado
    
    class Meta:
        verbose_name = 'dis_pry'
        verbose_name_plural = 'dis_prys'

class rl_cau_efe (models.Model):
    #Clase de la relación entre causa y efecto
    id_rl_cau_efe = models.AutoField(primary_key = True)# id de la relación causa-efecto
    id_efe = models.ForeignKey(efecto, on_delete=models.SET_NULL, null=True, blank =False) #Id de efecto
    id_cau = models.ForeignKey(causa, on_delete=models.SET_NULL, null=True, blank =False) #id de causa
    cau_padre = models.CharField('Causa padre', max_length=255)# Causa padre
    cau_hijo = models.CharField('Causa hijo', max_length=255)# Causa hijo

class rl_med_fin(models.Model):
    #Clase de la relacion medio y fin
    id_rl_cau_efe = models.AutoField(primary_key = True)# id de la relación causa-efecto
    id_med = models.ForeignKey(medio, on_delete=models.SET_NULL, null=True, blank =False) #Id de efecto
    id_fin = models.ForeignKey(fin, on_delete=models.SET_NULL, null=True, blank =False) #id de causa
    fin_padre = models.CharField('Fin padre', max_length=255)# Fin padre
    fin_hijo = models.CharField('Fin hijo', max_length=255)# Fin hijo


