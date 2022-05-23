from django.db import models
from django.contrib.auth.models import User
from modadm.App_regusugr.models import *
from modadm.App_modadm.models import *
from modpry.App_modpry.models import *


"""
Clases de la Aplicación Registro de Productos de Investigación
"""

class tipo_prod_inv(models.Model):
    # Clase que almacena la información de los tipos producciones: ya sea proyecto, revistas, libros,
    #articulos, ponencias etc
    id_produccion = models.AutoField(primary_key = True)   # indentificador unico de tipo de proyecto
    nomb_produccion =  models.CharField('tipo de produccion.', max_length=40, null=False, blank= False)
    desc_produccion=  models.CharField('Descripcion: ', max_length=40, null=False, blank= False)

    class Meta:
        verbose_name = 'tipo_prod_inv'
        verbose_name_plural = 'tipo_prod_invs'

class proc_inv(models.Model):
    #clase que almacena la información de procesos de investigación en los que ha participado un usuario del sistema.
    id_proc = models.AutoField(primary_key = True)  #Identificador único de proceso de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)
    instit = models.CharField('Nombre de la institucion', max_length= 60, null=False, blank= False) # Nombre de la institucion o entidad donde participó en la investigación
    #clas_inv = models.IntegerField(choices=TIPO_INV_FIN, blank=False, null=False) #clasificación de la investigación según los tipos de clasificación de los diccionarios TIPO_INV_***
    fch_ini = models.DateField('Fecha de inicio', auto_now =False)
    fch_fin = models.DateField('Fecha de fin', auto_now =False)
    certif = models.BooleanField('Posees certificado ', default=True)
    nal = models.CharField('Pais ', max_length=35, null=False, blank= False) #país dónde se realizó la investigación
    ciudad = models.CharField('Ciudad ', max_length=40, null=False, blank= False)
    #rol_inv = models.IntegerField(choices=ROL_INV, null=False, blank=False) #Rol de investigación que se asumió en el proceso, ver diccionario ROL_INV
    id_grup_inv = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank=False) #Identificador del grupo de investigación
    num_intg = models.PositiveSmallIntegerField('#Número de integrantes del equipo de investigación.', default=5 ) #Número de integrantes del equipo de investigación.
    horas = models.PositiveSmallIntegerField('Número de horas semanales dedicadas al proyecto', default=5) #Número de horas semanales dedicadas al proyecto
    ciclos = models.PositiveSmallIntegerField('cuántas veces se dictó el curso', default= 5) #Número de ciclos del curso "cuántas veces se dictó el curso"
    url_prog = models.URLField('Sitio web donde se puede localizar el programa del curso ', max_length=80, null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa del curso

    class Meta:
        verbose_name = 'proc_inv'
        verbose_name_plural = 'proc_invs'

class prod_inv(models.Model): #preguntar nombre de la tabla ojo tipo_pro_inv
    #clase que almacena la información de procesos de investigación en los que ha participado.
    #ojo verificar tipo_pro_inv

    id_prod = models.AutoField(primary_key = True)#Identificador único de producto de investigación.
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False) #Identificador único del usuario que realizó el producto
    tipo =  models.ForeignKey(tipo_prod_inv, on_delete=models.SET_NULL, null=True, blank =False)#, null=False, blank=False) # tipo de producto de investigación, ver Diccionario TIPO_PROD_INV
    pub= models.BooleanField('El producto se encuentra publicado',default=False) #El producto se encuentra publicado
    fch_real = models.DateField('Fecha de realización ', auto_now= False) #Fecha de realización.
    fch_pub = models.DateField('fecha de publicación ', default=False) #Fecha de publicación.
    reg = models.BooleanField('El producto se encuentra registrado en Plataforma de Colciencias ', default= False) #El producto se encuentra registrado en Plataforma de Colciencias.
    colab = models.BooleanField('El producto se realizó en colaboración de otros(as), ', default= False) #El producto se realizó en colaboración de otros(as) Autores(as)
    res_inv = models.BooleanField('El producto es resultado de un proyecto de investigación ', default = False) #El producto es resultado de un proyecto de investigación.
    id_proc_inv = models.ForeignKey(proc_inv, on_delete= models.SET_NULL, null=True, blank=False) #Identificador del proceso de investigación del que es derivado.
    horas = models.IntegerField('Número total de horas dedicadas al producto ') #Número total de horas dedicadas al producto.
    url_prod = models.URLField('sitio web donde se puede localizar  ', max_length= 40, null= False, blank=False) #Url del documento o sitio web donde se puede localizar el producto en su verisión digital.
    form = models.IntegerField(choices=TIPO_EXTEN, null=False, blank=False, default = 0) #Extensión del tipo de dpcumento digital (.pdf;.zip;.exe;.mp4;.docx;.txt;.xml;.json;.csv;.jgp;otro)
    rep_pub = models.BooleanField('El archvio digita ', default= True) #El archvio digita

    class Meta:
        verbose_name = 'prod_inv'
        verbose_name_plural = 'prod_invs'

class red_div(models.Model):
    # Clase que almacena el objeto red de divulgación científica o repositorio
    id_red_div = models.AutoField(primary_key = True)
    nombre_red = models.CharField('Nombre de la red ', max_length=60, null=False, blank= False)
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank=False)
    usuario = models.CharField('Nick ', null=False, blank=False, max_length=60 ) #nick o dirección de usuario
    url = models.URLField('Url de página principal dentro de la red ', max_length=60, null=False, blank=False) #Url de página principal dentro de la red o repositorio.
    #uso = models.IntegerField('Uso de la red ', choices=USO_RED, default=0, null=False, blank=False) #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('Acceso público de información de red ', default=False) #Acceso público de información de red

    class Meta:
        verbose_name = 'red_div'
        verbose_name_plural = 'red_divs'

class usu_inf_inv(models.Model):
    # Clase que almacena y procesa la información de investigación del usuario
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)  # Identificador único de usuario # identificador unico
    rol = models.ForeignKey(rol, on_delete=models.SET_NULL, null=True, blank =False)  #Rol que se desempeña actualmente.
    cvlac = models.URLField(' URL del CVlac del investigador(a)..', null=False, blank=False)  #URL del CVlac del investigador(a).
    orcid =  models.CharField('ID de ORCID del investigador(a). ', max_length=40, null=False, blank= False)  #ID de ORCID del investigador(a).
    ggl = models.URLField('URL Google académico del investigador(a).', null=False, blank=False) #URL Google académico del investigador(a).

    class Meta:
        verbose_name = 'usu_inf_inv'
        verbose_name_plural = 'usu_inf_invs'

class rl_usu_inf_inv_proc_inv(models.Model): #listado de id procesos de investigación realizados
    id_proc = models.ForeignKey(proc_inv, on_delete=models.SET_NULL, null=True, blank =False)
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)

    class Meta:
        verbose_name = 'rl_usu_inf_inv_proc_inv'
        verbose_name_plural = 'rl_usu_inf_inv_proc_invs'

class rl_prod_usu(models.Model): #Listado de id productos de investigación realizado
    prod_inv = models.ForeignKey(prod_inv, on_delete=models.SET_NULL, null=True, blank =False)
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)

    class Meta:
        verbose_name = 'rl_prod_usu'
        verbose_name_plural = 'rl_prod_usus'

class rl_usu_inf_inv_ls_red_div(models.Model): #Listado de id productos de investigación realizado
    ls_red_div = models.ForeignKey(red_div, on_delete=models.SET_NULL, null=True, blank =False)
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =False)

    class Meta:
        verbose_name = 'rl_usu_inf_inv_ls_red_div'
        verbose_name_plural = 'rl_usu_inf_inv_ls_red_divs'
