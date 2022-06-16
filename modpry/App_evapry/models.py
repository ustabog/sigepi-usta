from django.db import models
from django.forms import CharField
from modpry.app_modpry.models import *
from modadm.App_regusugr.models import *
from modpry.app_regpry.models import *

APP_EVA_PRY = [
    #Diccionario para la aplicación de evaluación de proyecto
    (0,'Titulo'),
    (1,'Descripción'),
    (2,'url_documento'),
    (3,'url_instal'),
    (4,'url_plantilla'),
    (5,'Nombre_url'),
    (6,'Versión aplicación'),
    (7,'id_mod'),
    (8,'Versión_módulo'),
    (9,'estado'),
    (10,'instalada'), 
    (11, 'visible'),
    ]

ESTADO_EVA = [
    (0,'Evaluación finalizada'),
    (1,'Evaluación proceso'),
    (2,'Evaluación preliminar'),
]

EVA_PRY = [
    (0,'Cuantitativa'),
    (1,'Cualitativa'),
]

CATG = [
    #Lista de categorias
    (0,'Comentario'),
    (1,'Concepto'),
    (2,'Recomendación'),
    (3,'Retroalimentación'),
    (4, 'Definiciones'),
]

RES_EVA = [
    (0, 'Aprobado'),
    (1, 'Reprobado'),
]

class rango_eva(models.Model):
    #Clase que contiene los rango de la evaluación del proyecto
    id_rango =  models.AutoField(primary_key = True)#ID del rango de la evaluación de proyectos
    nombre_rango = models.CharField('Nombre del rango', max_length=255, null=False, blank= False)#Nombre para diferenciar los diferentes rangos de evaluación
    c_eva_pry = models.IntegerField(choices = EVA_PRY,default = 0, null=False, blank = False)#Si la evaluación es cuantitativa o cualitativa
    valor_ini = models.FloatField('Valor inicial de la evaluación =', max_length=10, null=False, blank= False)#Valor inicial de la calificación cuantittativa
    valor_fin = models.FloatField('Valor final de la evaluación =', max_length=10, null=False, blank= False)#Valor final de la calificación cuantittativa
    class Meta:
        verbose_name = 'rango_eva'
        verbose_name_plural = 'rango_evas'

class defi(models.Model):
    #Clase que define el tipo de cat que hará el evaluador 
    id_def =  models.AutoField(primary_key = True)#ID de la definción
    resp_defi = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#ID del usuario que realiza la definición
    tipo_def = models.IntegerField(choices = CATG,default = 0, null=False, blank = False)
    vers= models.CharField('Versión=', max_length=10, null=False, blank= False)
    fch_reg= models.DateField('Fecha de registro', auto_now = False) # Fecha de registro 
    vers1 = models.CharField('Descripción', max_length=255, null=False, blank= False)#Descripción de la versión 1
    vers2 = models.CharField('Descripción', max_length=255, null=False, blank= False)#Descripción de la versión 2
    vers3 = models.CharField('Descripción', max_length=255, null=False, blank= False)#Descripción de la versión 3
    vers4 = models.CharField('Descripción', max_length=255, null=False, blank= False)#Descripción de la versión 4
    vers5 = models.CharField('Descripción', max_length=255, null=False, blank= False)#Descripción de la versión 5
    fch_mod= models.DateField('Fecha de registro', auto_now = False) #Fecha de modificación
    class Meta:
        verbose_name = 'definición'
        verbose_name_plural = 'definiciones'

class tipo_eva(models.Model):
    #Clase que contiene el tipo de evaluación de proyectos
    id_tipo_eva = models.AutoField(primary_key = True)#ID del tipo de evaluación
    tipo_eva = models.CharField('Tipo de evaluación:', max_length=100, null=False, blank= False)
    desc_eva = models.CharField('Descripción del tipo de evaluación:', max_length=40, null=False, blank= False)
    class Meta:
        verbose_name = 'tipo_eva'
        verbose_name_plural = 'tipo_evas'

class res_eva(models.Model):
    #Clase de los resultados de evaluación
    id_res = models.AutoField(primary_key = True)#ID de los resultados de la evaluación
    valor_total = models.FloatField('Resultado total = ', max_length=10, null=False, blank=False)#Valor total de la evaluación
    aprobado = models.IntegerField(choices = RES_EVA,default = 0, null=False, blank = False)#Resultado de la  evaluación, si aprobo o no 
    ls_comen = models.ForeignKey(defi, on_delete=models.SET_NULL, null=True, blank =False ) #Lista de las definciones del proyecto
    estado_eva = models.IntegerField(choices = ESTADO_EVA,default = 0, null=False, blank = False)#Estado de la evaluación
    id_usu_eval = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#id de usuario(a) evaluador(a) del proyecto 
    class Meta:
        verbose_name = 'resultado'
        verbose_name_plural = 'resultados'

class crit_eva(models.Model):
    #Clase que recopila la información de los criterios de evaluación del proyecto
    id_crit =  models.AutoField(primary_key = True)   # identificador unico para criterios del proyecto
    nomb_crit= models.CharField('Nombre del criterio', max_length=100, null=False, blank= False) #Nombre del criterio
    class Meta:
        verbose_name = 'criterio'
        verbose_name_plural = 'criterios'

class rubr_eva(models.Model):
    #Clase de la rubrica de la evaluación del proyecto
    id_rub = models.AutoField(primary_key = True)#ID de la rúbrica de la evaluación de un proyecto
    nomb_rub = models.CharField('Nombre de la rúbrica de evaluación: ', max_length=255, null=False, blank= False)#Nombre de la rúbrica de evaluación
    desc_rub = models.CharField('Descripción de la rúbrica de evaluación: ', max_length=255, null=False, blank= False)#Descripción de la rúbrica de evaluación
    arb_crit = models.ForeignKey(crit_eva, on_delete=models.SET_NULL, null=True, blank =False)#Árbol de criterios
    #matriz_resu = #Matriz que relaciona la calificación con el criterio
    arb_crit = models.ForeignKey(crit_eva, on_delete=models.SET_NULL, null=True, blank =False)#Árbol de criterios listado de relaciones de criterios con la rúbrica, debe contemer al menos un criterio padre
    #matriz_val_eval = #Matriz que relaciona el peso de cada criterio dentro de la evaluación, valores numéricos del árbol de criterios de la rúbrica
    id_usu_dis = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#Usuario que diseña la evaluación
    vers = models.CharField('Descripción', max_length=10, null=False, blank= False)#versión de la rúbrica
    class Meta:
        verbose_name = 'rubrica'
        verbose_name_plural = 'rubricas'

class eva_pry(models.Model):
    #Clase que contiene la forma de evaluacion del proyecto
    id_eva =  models.AutoField(primary_key = True)   # identificador unico para el tipo de evalucion
    pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False )#Lista de proyectos
    eval = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#evaluador del proyecto  
    ls_prys = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False )#Lista de proyectos a ser evaluados
    Ls_evalds = models.ForeignKey(usu, on_delete=models.SET_NULL, null= True, blank = False)#listado de ids de usuarios(as) evaluadores(as) del proceso de evaluación  
    nomb_eva = models.CharField('Nombre de la evaluación del proyecto', max_length = 255, null = False, blank = False)#Nombre de la evaluación del proyecto 
    desc_eva = models.CharField('Descripcion del tipo de evalucion ', max_length = 255, null = False, blank= False) #Descripción de la evaluación
    criterio = models.ForeignKey(crit_eva, on_delete=models.SET_NULL, null=True, blank =False )#id de citerios
    rubrica = models.ForeignKey(rubr_eva, on_delete=models.SET_NULL, null=True, blank =False )#ID de rúbrica
    resultado = models.ForeignKey(res_eva, on_delete=models.SET_NULL, null=True, blank =False )#ID de resultados de la evaluación
    ls_pry_res_eva = models.ForeignKey(resultado, on_delete=models.SET_NULL, null=True, blank =False )#listado de resultdo de evaluación por proyecto ls[id_pry, id_res_eva]
    tipo_eva = models.ForeignKey(tipo_eva, on_delete=models.SET_NULL, null=True, blank =False )#ID del tipo de evaluación
    fch_ini =  models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio de la evaluacion
    fch_fin =  models.DateField('fecha de fin', auto_now = False) # # fecha de fin de la evaluacion
    estado_eva = models.IntegerField(choices = ESTADO_EVA,default = 0, null=False, blank = False)#Estado de la evaluación

    class Meta:
        verbose_name = 'evalucion_pry'
        verbose_name_plural = 'evalucion_prys'

class list_crit_cali(models.Model):
    #Relación entre la clase de criterios y resultados
    id_lis_crit_cali = models.AutoField(primary_key = True)#ID de la lista de los criterios con cu calificación
    crit = models.ForeignKey(crit_eva, on_delete=models.SET_NULL, null=True, blank =False )#id del criterio de evaluación de un proyecto
    calif_rel = models.IntegerField('Calificación relativa = ', null=False, blank= False) #Calificación relativa en la rúbrica de evaluación (de 0% a 100%)
    calif_abs = models.IntegerField('Calificación absoluta = ', null=False, blank= False)#Calificación absoluta, calculado de acuerdo a la posición del criterio en la rúbrica de evaluación.
    ls_comen = models.ForeignKey(defi, on_delete=models.SET_NULL, null=True, blank =False ) #Lista de las definciones del proyecto
    estado_eva = models.IntegerField(choices = ESTADO_EVA,default = 0, null=False, blank = False)#Estado de la evaluación

class rl_crit_rub(models.Model):
    #Relación entre la clase de criterios y rúbricas
    id_rel_rub_cri = models.AutoField(primary_key = True)#ID de la relación entre la rubrica y el criterio
    nomb_crit = models.ForeignKey(crit_eva, on_delete=models.SET_NULL, null=True, blank =False )#id del criterio de evaluación de un proyecto
    rubrica =models.ForeignKey(rubr_eva, on_delete=models.SET_NULL, null=True, blank =False )#id de la rúbrica de evaluación de un proyecto
    #id_crit_padre = models.ForeignKey(criterio, on_delete=models.SET_NULL, null=True, blank =False )#ID del criterio padre
    #id_crit_hijo = models.ForeignKey(criterio, on_delete=models.SET_NULL, null=True, blank =False )#ID del criterio hijo
    valor_rel = models.IntegerField('Valor relativo = ',null=False, blank= False) #Valor relativo en la rúbrica de evlauación ( de 0% a 100%)
    valor_abs = models.IntegerField('Valor absoluto = ', null=False, blank= False)#Valor absoluto, calculado de acuerdo a la posición del criterio en la rúbrica de evaluación.