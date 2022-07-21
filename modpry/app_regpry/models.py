# App de registro de un proyecto de investigación - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 07-07-2022

from django.db import models
from modadm.app_modadm.models import *
from modpry.app_modpry.models import *
from modadm.app_regusugr.models import *
from modadm.app_modadm.dic import *

INF_APP = [
    #Diccionario para la aplicación de registro de proyecto
    ['Titulo', "App Registro de Proyecto de Investigación"],
    ['Descripción',"Aplicación para la definición del registro del Proyecto de Investigación"],
    ['url_documento','doc'],
    ['url_instal','modpry/app_regpry'],
    ['url_plantilla','app_regpry_iu.html'],
    ['Nombre_url','ini_regpry'],
    ['Versión aplicación','0.7.0'],
    ['id_mod', 4],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', True],
    ['visible', True],
    ]

ROL_APP = [
    (0,'Investigador(a) Principal'),
    (1,'Propietario(a) Proy.'),
    (2,'Investigador(a) Secundario'),
    (3,'Colaborador(a)')
    ]

#clase base de registro de proyecto
class pry_base(models.Model):
    #clase base de registro de proyecto
    id_pry=models.AutoField(primary_key = True, null = False, unique= True) #Identificador unico del proyecto
    cod_pry = models.CharField('Código proyecto:', max_length=50) # código unico del proyecto
    nombre_pry = models.CharField('Nombre del proyecto: ', max_length=255)#Nombre proyecto
    desc_pry=models.CharField('Descripción del proyecto: ', max_length=255, null=False, blank=False)#Decripción del proyecto
    tipo_pry=models.IntegerField(null = False, blank = False, choices = TIPO_PRY, default = 0) # Tipo de proyecto - diccionario TIPO_PRY
    id_usu = models.ForeignKey(User, on_delete=models.SET_NULL, null= True, blank = False, db_constraint=False) #Propietario del proyecto
    est_pry = models.IntegerField(null = False, blank = False, choices = ESTADO_PRY, default = 0)
    pry_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el proyecto es borrado queda como archivado
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

class inf_pry(models.Model):
    #Clase que contiene toda la informacion referente al proyecto
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.SET_NULL, null=True, blank =False)#Id del proyecto base 
    id_inf_pry = models.AutoField(primary_key = True)# identificador unico para  App Registro de Proyectos
    nombre_archivo = models.CharField('Nombre del archivo del proyecto: ', max_length=255)# Nombre del archivo del proyecto.
    url_archivo =models.URLField('url del archivo del proyecto',max_length=200)# Url del archivo del proyecto.
    id_gr_inv = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank =False)#identificador del grupo de investgación
    #id_ln_inv = models.ForeignKey(Ln_inv, on_delete=models.CASCADE, null=False, blank =False)#Identificador de la linea de investigación
    #conv =  models.IntegerField(null = False, blank = False, choices = CONVENIO, default = 0)# Convenio propuesto o previsto para la realización de la investigación.
    dat_dep = models.IntegerField(null = False, blank = False, choices = DEPARTAMENTOS, default = 0)#Departamento que hace parte del proyecto
    #geo_nac_cp = models.ForeignKey(leer_dat_geo_cenpobl, on_delete=models.CASCADE, null=False, blank =False)#id registro de centros poblados que abarca el proyecto.
    url_ap =  models.URLField('url de la imágen de árbol de problemas',max_length=200)# Url de la imágen del árbol de problemas.
    url_ao =  models.URLField('url de la imágen de árbol de objetivos', max_length=200)# Url de la imágen del árbol de objetivos.
    # id_ml = models.ForeignKey('ID marco lógico', on_delete=models.SET_NULL, null=True, blank =False)# id de registro de marco lógico
    # id_act = models.ForeignKey('ID marco lógico', on_delete=models.SET_NULL, null=True, blank =False) #identificador de registro de actores proyecto.
    obj_gen = models.CharField('Objetivo general: ', max_length=255)# Objetivo general del proyecto.
    obj_esp = models.CharField('Objetivos especificos: ', max_length=255)# Objetivos específicos del proyecto.
    inf_archi = models.BooleanField(null = False, blank = False, default = 0)#Si la información es borrada queda como archivada

    class Meta:
        verbose_name = 'inf_pry'
        verbose_name_plural = 'inf_prys'

    def __str__(self):
        return '{}'.format(self.nombre_archivo)

class inf_geo_pry(models.Model):
    #clase que define la información geográfica del proyecto, recoge los valores de divipola del dane con latitudes y longitudes.
    id_inf_geo = models.AutoField(primary_key = True) 
    dat_dep = models.IntegerField(null = False, blank = False, choices = DEPARTAMENTOS, default = 0)#Lista de los departamentos de Colombia que hacen parte del proyecto 
    municipio = models.CharField('Municipio:', max_length=150)#Municipio donde se desarrolla el proyecto
    ciudad = models.CharField('Ciudad:', max_length=150)# Ciudad donde se desarrolla el proyecto
    geo_archi = models.BooleanField(null = False, blank = False, default = 0)#Si la información geográfica es borrada queda como archivada

class rl_geo_pry(models.Model):
    id_rl_geo_pry = models.AutoField(primary_key = True) 
    id_inf_geo = models.ForeignKey(inf_geo_pry, on_delete=models.CASCADE, null=False, blank =False)
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)

class even_pry(models.Model):
    # clase que guarda la información de los eventos del proyecto.
    id_even_pry= models.AutoField(primary_key = True) 
    even_pry = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)#Proyecto que hara parte del evento
    enc_eve=models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank =False)#Encargado del evento
    nomb_eve = models.CharField('Nombre del evento:', max_length=255)# Ciudad donde se desarrolla el proyecto#Nombre del evento
    desc_eve = models.CharField('Descripción del evento:', max_length=400)# Ciudad donde se desarrolla el proyecto#Descripción del evento
    fch_eve = models.DateField('Fecha del evento:', null=True, blank=True )#Fecha del evento
    hora_eve = models.TimeField('Hora del evento:',null=True, blank=True)#Hora del evento
    lugar_eve = models.CharField('Lugar del evento:', max_length=255)# Ciudad donde se desarrolla el proyecto#Lugar del evento
    dir_eve = models.CharField('Dirección del evento:', max_length=400)# Dirección del evento
    mod_eve = models.IntegerField(null = False, blank = False, choices = MOD_EVE, default = 0)# Modalidad del evento (Presencial, virtual)
    inf_adi = models.CharField('Información adicional:', max_length=400)#Información adicional
    even_archi = models.BooleanField(null = False, blank = False, default = 0)#Si el evento es borrado queda como archivado
    class Meta:
        verbose_name = 'evento_pry'
        verbose_name_plural = 'eventos_prys'

class lin_inv(models.Model):
    #Clase de las líneas de investigación de un proyecto
    id_ln_inv = models.AutoField(primary_key = True) #Identificador de la línea de investigación
    #id_pry_base = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank =False)
    #id_grp_vinpry = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank =False)#identificador de los grupos que estan vinculados a la linea de investigación
    nomb_ln_inv = models.CharField('Nombre de la línea de investigación: ', max_length=255) #Nombre de la línea de investigación
    desc_ln_inv = models.CharField('Descripción de la línea de investigación: ', max_length=255)#Descripción de la línea de investigación
    fch_ini_ln = models.DateField('Fecha de inicio de la línea:', auto_now=False)#Fecha de inicio de la línea de investigación
    fch_fin_ln = models.DateField('Fecha de finalización de la línea:', auto_now=False)#Fecha de finalización de la línea de investigación
    fch_mod_ln = models.DateField('Fecha de modificación de la línea:',auto_now=False)#Fecha de modificación de la línea de investigación
    #res_ln_inv = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Responsable de la línea de investigación
    #invs_ln_inv = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)#Investigadores de la línea de investigación
    cmp_dis_ocde = models.IntegerField(null = False, blank = False, choices = LN_INV_OCDE, default = 0)#Campos disciplinarios OCDI
    cmp_dis_minc = models.IntegerField(null = False, blank = False, choices = LN_INV_MINCI, default = 0)#Campos disciplinarios MINCIENCIAS
    est_ln_inv = models.IntegerField(null = False, blank = False, choices = EST_LN_INV, default = 0)#Estado de la línea de investigación, se define con relación a si tiene productos o proyectos dentro de la línea
    ln_archi = models.BooleanField(null = False, blank = False, default = 0)#Si la línea es borrada queda como archivado

    class Meta:
        verbose_name = 'linea_investigación'
        verbose_name_plural = 'lineas_investigación'

class fn_app_regpry(models.Model):
    #Clase para las funciones de la aplicación del registro de proyecto
    id_func = models.AutoField(primary_key = True) # identificador único de función
    nom_func = models.CharField('Nombre de la función: ', max_length=30, null=False, blank = False) # Nombre de la función
    lib_func = models.CharField('Librería que contiene la función: ', max_length=30, null=False, blank = False) # Librería que contiene la función
    url_loc = models.URLField('Direción local a la documentación o manual de la aplicación', null=False, blank=False)  # Direción local donde se encuentra la librería que contiene la función
    com_exc = models.CharField('Comando de Ejecución de la Función: ', max_length=20, null=False, blank = False) # Comando de Ejecución de la Función
    text = models.CharField('Nombre de Función: ', max_length=20, null=False, blank = False) # Nombre de Función para menús o etiquetas.
    context = models.CharField('Contexto: ', max_length=20, null=False, blank = False) # Nombre de Función para menús contextuales o emergentes y panel de inf.
    activa = models.BooleanField('¿Activa o desactivada?', default=False)  # La función está activa o desactiva.
    indice = models.IntegerField() #Índice de selección, para navegar con el tabulador.

    class Meta:
        verbose_name = 'fn_app_regpry'
        verbose_name_plural = 'fn_app_regprys'

    def __str__(self):
        return '{}'.format(self.nom_func)
'''
class inf_prod_pry(models.Model):
    #Clase que contiene toda la informacion referente a los productos vinculados al proyecto
    id_prod_pry = models.AutoField(primary_key = True)  # Identificador único
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    prod_pry= models.ForeignKey(productos_vinculados, on_delete=models.CASCADE, null=False, blank =False)# productos vinculados al proyecto y su estado
    id_gest_prod= models.ForeignKey(inf_ges_pry, on_delete=models.CASCADE, null=False, blank =False)#identificador de gestión de producto
    coment= models.CharField('Objetivos especificos: ', max_length=255)#comentarios

    class Meta:
        verbose_name = 'inf_prod_pry'
        verbose_name_plural = 'inf_prods_prys'

class rel_pry_prod(models.Model):
    #lista que relación actores con proyectos
    id_pry_base = models.AutoField(primary_key = True)
    id_usu_res=  models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)# identificador del usuario o investigador responsable principal del producto
    id_prod= models.ForeignKey(prod, on_delete=models.CASCADE, null=False, blank =False)
    tipo_prod= models.IntegerField(null = False, blank = False, choices = TIPO_PROD, default = 0)
    est_prod= models.IntegerField(null = False, blank = False, choices = EST_PROD, default = 0)#Estado del producto [compremetido, pendiente, descartado, realizado, realizado y avalado]


class inf_act_proy(models.Model):
    #clase que define la información de los actores del proyecto
    id_act_pry = models.AutoField(primary_key = True)# id actores del proyecto
    act_inv = models.IntegerField(null = False, blank = False, choices = ROL_INV, default = 0)# listado de Investigadores y roles de investigación dentro del proyecto
    act_bnf = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)#listado de beneficiarios del proyecto
    act_afc = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de actores afectados directos o indirectos del proyecto
    act_ptrc = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de patrocinadores dentro del proyecto
    act_ev = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de evaluadores del proyecto
    act_par = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de pares que trabajn temas similares al proyecto
    act_vc = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de actores de vigilancia y control del proyecto
    act_pry_acd = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)# listado de actores que intervienen en un proyecto de tipo académico.

    class Meta:
        verbose_name = 'inf_act_pry'
        verbose_name_plural = 'inf_acts_prys'

    def __str__(self):
        return '{}'.format(self.id_act_pry)

class rel_act_pry(models.Model):
    #lista que relación actores con proyectos
    id_pry_base = models.AutoField(primary_key = True) # id del proyecto
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    rol_inv= models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)#Listado de los investigadores del proyecto
    rol_act= models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)#Listado de los actores del proyecto
    rol_inv_acdm = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False) #Listado de investigador acdm
'''