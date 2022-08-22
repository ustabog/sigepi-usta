import email
from nntplib import GroupInfo
from django.db import models
from django.contrib.auth.models import Group
import datetime
from django.utils import timezone
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser, User
from .dic import *

#Diccionario de información de instalación de aplicación
INF_APP = [
    ['nom','app_modadm'],
    ['titulo', "App Módulo de Administración"],
    ['desc',"aplicación para la administración del Sistema"],
    ['url_doc','doc'],
    ['url_instal','modadm/app_modadm'],
    ['url_pl','inicio_adm.html'],
    ['nom_url','inicio_adm'],
    ['version','0.5.0'],
    #['id_mod', 0],
    ['ver_mod', 'prueba'],
    ['activo', False],
    ['instalada', True],
    ['visible', True],
    ['externa', False],
    ['tipo_app', 'SIGEPI-BASE'],
    ['ico','#']
    ]

#Diccionario de información de instalación del Móludo
INF_MOD = [
    ['titulo', "Módulo de Administración SIGEPI"],
    ['nom','modadm'],# debe ser el mismo de la carpeta
    ['desc',"Módulo de administración del SIGEPI"],
    ['url_doc','doc'],
    ['version','0.80'],
    ['activo', True],
    ['instalado', True],
    ['externo', True],
    ['visible', True],
    ['ls_param_cnf', []],
    ]

ROL_BASE =[
    #[etq_rol,desc,req_reg,tipo],
    [0,'Adm.Sistema','',''],
    [1,'Adm.Institución','',''],
    [2,'Adm.Grupo','',''],
    [3,'Usuario','',''],
    [4,'Usuario Grupo','',''],
    [5,'Usuario institucional','',''],
    [6,'Invitado','',''],
    [7,'Anonimo','','']
]

## Usuarios básicos del sistema ##
#Usuario individual
class usu(models.Model):
    id_user = models.OneToOneField(User, primary_key = True, on_delete=models.CASCADE, null=False, blank=False)
    fch_reg = models.DateField('fecha de registro', default=timezone.now) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o desactivado.?', default=True) # estatus del usuario activo (True) inactivo (False)
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivado (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'usurio individual'
        verbose_name_plural = 'usuarios individuales'

#Usuario de grupo
class usugr(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, null=False, blank=False)
    sigla = models.CharField('usuario (Sigla del Grupo)', max_length=50, unique=True)
    nom_grup = models.CharField('Nombre del Grupo', max_length=254, null=False, blank=False)
    emailgr = models.EmailField('Correo-e del Grupo', max_length = 254, null=True, blank=True) #Correo elect´ronico del grupo de investigación
    id_usu_adm = models.IntegerField('Id de usuario Director(a) Adm. Grupo', null=True, blank=True) # Usuario(a) principal que administra el grupo
    id_usu_asig = models.IntegerField('Id de usuario asignado para Adm. Grupo', null=True, blank=True) # Usuario(a) asistente para administración del grupo
    fch_reg = models.DateField('fecha de registro', default=timezone.now) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o inactivo?', default=True, null=False, blank=False) # estatus del usuario(a) activo (True) inactivo (False)
    archi = models.BooleanField('¿Usuario archivado?', default = 0, null=False, blank=False)#Si el registro está archivado (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'usurio de grupo'
        verbose_name_plural = 'usuarios de grupos'

    # def __str__(self):
    #     return '{}'.format(self.usu)

#Usuario de Institución
class usui(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key = True, null=False, blank=False)
    sigla = models.CharField('usuario (Sigla de la Institución)', max_length=100, unique=True)
    nom_inst = models.CharField('Nombre de la Institución', max_length=254)
    id_usu_adm = models.IntegerField('Id de usuario Principal Adm. Institución', null=True, blank=True) # Usuario(a) principal que administra la Institución
    id_usu_asig = models.IntegerField('Id de usuario asignado Adm. Institución', null=True, blank=True) # Usuario(a) asignado para administración de la cuenta Institución
    email_inst = models.EmailField('Correo-e de soporte técnico de la Institución',max_length = 254)
    fch_reg = models.DateField('fecha de registro', default=timezone.now) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o desactivado.?', default=True) # estatus del usuario(a) activo (True) inactivo (False)
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivado (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'usurio institucional'
        verbose_name_plural = 'usuarios institucionales'

    # def __str__(self):
    #     return '{}'.format(self.usu)

#Modelos para el registro de módulos, aplicaciones, roles y funciones

# clase que almacena todos los modulos del sistema
class adm_mod(models.Model):
    id_mod = models.AutoField(primary_key = True) # Identificador único del módulo
    nom = models.CharField('Nombre', max_length=40, null=False, blank = False) # Título del módulo ej. "Administración Plataforma"
    titulo = models.CharField('Título del módulo', max_length=40, null=False, blank = False) # Título del módulo ej. "Administración Plataforma"
    desc  = models.CharField('Descripcion del Módulo', max_length=50, null=False, blank = False) # descripcion del Módulo
    url_doc = models.URLField('URL Documentación', null=False, blank=False) # sitio url # direción local a la documentación o manual del módulo.
    version = models.CharField('Versión de desarrollo ', max_length=5, null=False, blank = False) # Versión de desarrollo del Módulo ej. "0.01.04"
    activo = models.BooleanField('Activo', default=False) # estatus de la aplicacion para indicar  el modulo de Administración
    instalado = models.BooleanField('¿El módulo se encuentra instalado?', default=False) # ¿el módulo se encuentra instalado? sí =True; no= False.
    externo = models.BooleanField('¿El módulo es externo?', default=False) # ¿el módulo es externo, o hace parte de la base del sistema? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.
    ls_param_cnf = models.CharField('Listado de parámetros de configuración', max_length=100, null=False, blank = False, default='0')

    class Meta:
        verbose_name = 'módulo'
        verbose_name_plural = 'módulos'

    def __str__(self):
        return '{}'.format(self.titulo)

#Clase que almacena los datos del objeto aplicación, las aplicaciones son unidades de los módulos
class adm_app(models.Model):
    id_app = models.AutoField(primary_key = True)  # Identificador único de la aplicación.
    nom = models.CharField('Nombre de la aplicación: ', max_length=40, null=False, blank = False) # "Nombre de la carpeta y de registro de la aplicación"
    titulo = models.CharField('Título de la aplicación: ', max_length=40, null=False, blank = False) # Título de la aplicacion ej. "Editor de Texto SABER"
    desc  = models.CharField('descripcion de la aplicación: ', max_length=80, null=False, blank = False) # descripcion de la Aplicación.
    url_doc = models.URLField('URL de la documentación o manual de la aplicación', null=False, blank=False)  # direción local a la documentación o manual de la aplicación.
    url_instal = models.URLField('Url aplicación', null=False, blank=False)  # direción local relativa a la carpeta donde está instalada la aplicación.
    url_pl = models.URLField('Url plantilla de aplicación', null=True, blank=True)  #Nombre de la plantilla  de la aplicación ej. 'app_mod_ej.html' sólo para apps django.
    nom_url = models.URLField('Nombre de la Url de plantilla de aplicación', null=True, blank=True)  #Nombre de la dirección de la aplicación ej. 'app_ej' apps django.
    version = models.CharField('Versión de desarrollo de la aplicación: ', max_length=20, default='0.0.1', null=False, blank = False)  # Versión de desarrollo de la aplicación. "0.01.04"
    id_mod = models.ForeignKey(adm_mod, on_delete=models.CASCADE, null=True, blank =True)# Id del módulo principal con el cual se integra.
    ver_mod = models.CharField('Versión de desarrollo de la aplicación: ', max_length=8, null=False, blank = False)  # Versión mínima del módulo principal con la que la actual versión de la aplicación es compatible.
    activo = models.BooleanField('la aplicacion está activa o no', default=False)# estatus de la aplicacion para indicar  el modulo de Administración
    instalada = models.BooleanField('¿La aplicación se encuentra instalada? ', default=False) # ¿La aplicación se encuentra instalada? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.
    externa = models.BooleanField('¿La aplicación es externa?', default=False) # ¿La aplicación es externa, o hace parte de la base del sistema? sí =True; no= False.
    tipo_app = models.IntegerField(null = False, blank = False, choices = TIPO_APP, default = 0) # Ver diccionario TIPO_APP)
    ico = models.CharField('nombre del la imagen del ícono a utilizar', max_length=40) #nombre del ícono a utilizar según las fuentes disponibles ej. 'person' (material icons por defecto)
    id_usu_reg = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True) #Usuario(a) quien registra la app
    
    class Meta:
        verbose_name = 'app_mod'
        verbose_name_plural = 'app_mods'

    def __str__(self):
        return '{}'.format(self.titulo)

#Clase que almacena los datos del objeto rol, los roles son definidos por cada aplicación y los permisos de acceso a los modelos de cada app
#hereda de grupos, creando un grupo cada vez que se registra un nuevo rol. Se define en el diccionario ROL_APP de cada app.
class adm_rol(Group):
    etq_rol = models.CharField('Etiqueta: ', max_length=30, null=False, blank = False) # Etiqueta del Rol
    desc = models.CharField('Descripcion del Rol: ', max_length=30, null=False, blank = False) # Descripcion del Rol
    tipo = models.IntegerField(null = False, blank = False, choices = ROL_BASE, default = 0) # Ver diccionario TIPO_ROL
    id_mod = models.ForeignKey(adm_mod, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Módulo
    id_app = models.ForeignKey(adm_app, on_delete=models.CASCADE, null=True, blank =True)  #Identificador de Aplicación
    req_reg = models.BooleanField('¿Usuario(a) registrado(a)?', default=False) # Variable que indica si el rol require estar registrado y con sesión activa en plataforma o no.
    class Meta:
        verbose_name = 'rol de usuario'
        verbose_name_plural = 'roles de usuario'

    def __str__(self):
        return '{}'.format(self.etq_rol)

class adm_func(models.Model):
    id_func = models.AutoField(primary_key = True) # identificador único de función
    nom_func = models.CharField('Nombre de la función: ', max_length=30, null=False, blank = False) # Nombre de la función
    lib_func = models.CharField('directorio y Librería que contiene la función: ', max_length=50, null=False, blank = False) # Librería que contiene la función ej. 'modadm/app_regusu/func.py'
    url_loc = models.URLField('Direción local a la documentación o manual de la aplicación', null=False, blank=False)  # Direción local donde se encuentra la librería que contiene la función
    com_exc = models.CharField('Comando de Ejecución de la Función: ', max_length=20, null=False, blank = False) # Comando de Ejecución de la Función
    text = models.CharField('Nombre de Función: ', max_length=20, null=False, blank = False) # Nombre de Función para menús o etiquetas.
    context = models.CharField('Contexto: ', max_length=20, null=False, blank = False) # Nombre de Función para menús contextuales o emergentes y panel de inf.
    activa = models.BooleanField('¿Activa o desactivada?', default=False)  # La función está activa o desactiva.
    indice = models.IntegerField('Número de índice en la aplicación',null=True, blank = True) #Índice de selección, para navegar con el tabulador.
    id_app = models.OneToOneField(adm_app, on_delete=models.CASCADE, null=False, blank = False) #identificador de aplicación
    ico = models.CharField('nombre del la imagen del ícono a utilizar', max_length=40) #nombre del ícono a utilizar según las fuentes disponibles ej. 'person' (material icons por defecto)
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la función?', default=False)  # Activa o desactiva la visibilidad de la funcion.
    class Meta:
        verbose_name = 'func_app'
        verbose_name_plural = 'func_apps'

    def __str__(self):
        return '{}'.format(self.nom_func)

#Relación de funciones permitidas a cada rol.
class rl_func_rol(models.Model): 
    id_func = models.OneToOneField(adm_func, on_delete=models.CASCADE, null=False, blank =False)# identificador de la función
    id_rol =  models.OneToOneField(adm_rol, on_delete=models.CASCADE, null=False, blank =False)#) Identificador del rol

    class Meta:
        verbose_name = 'Relación rol y función'
        verbose_name_plural = 'Relaciones entre roles y funciones'


#Modelos para el registro de acceso a plataforma, roles y funciones

#Registros de acceso a plataforma
class log_acc_pltf(models.Model):
    id_acc_pltf = models.AutoField(primary_key = True)  # Identificador único
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de usuario
    fch_ini = models.DateField('fecha de inicio', auto_now = False) # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False) # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_pltf'
        verbose_name_plural = 'log_acc_pltfs'

#Registros de acceso a cada rol
class log_acc_rol(models.Model):
    id_acc_rol = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.OneToOneField(User, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador único de usuario
    id_rol = models.ForeignKey(adm_rol, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador de rol
    fch_ini = models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'registro de acceso por rol'
        verbose_name_plural = 'registros de acceso por roles'

#Registros de acceso a cada función
class log_acc_func(models.Model):
    id_acc_func = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.OneToOneField(User, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador único de usuario
    id_func = models.ForeignKey(adm_func, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador de rol
    bk_uso = models.IntegerField('Respaldo Uso', default=0, null=True, blank =True) # Respaldo del Número de veces que la función fue utilizada por el usuario
    uso = models.IntegerField('Uso', default=0, null=True, blank =True) # Número de veces que la función due utilizada por el usuario
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM
    fch_bk = models.DateField('fecha de respaldo', auto_now = False)  # fecha del último respaldo de uso formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'registro de acceso a la función'
        verbose_name_plural = 'registros de acceso a las funciones'

