import email
from nntplib import GroupInfo
from django.db import models
from django.contrib.auth.models import Group
import datetime
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import AbstractUser
#Diccionario de información de instalación de aplicación

#Diccionario de información de instalación del Móludo
INF_MOD = [
    ['titulo', "Módulo de Administración SIGEPI"],
    ['desc',"Módulo de administración del SIGEPI"],
    ['url_doc','doc'],
    ['version','0.7.0'],
    ['activo', True],
    ['instalado', True],
    ['externo', True],
    ['visible', True],
    ['ls_param_cnf', []],
    ]

INF_APP = [
    ['titulo', "App Módulo de Administración"],
    ['desc',"aplicación para la administración del Sistema"],
    ['url_doc','doc'],
    ['url_instal','modadm/app_modadm'],
    ['url_pl','inicio_adm.html'],
    ['nom_url','inicio_adm'],
    ['version','0.5.0'],
    ['id_mod', 0],
    ['ver_mod', 'prueba'],
    ['activo', False],
    ['instalada', True],
    ['visible', True],
    ]

#Tipo de rol dentro de la plataforma
ROL_BASE = [
    (0,'Adm. Sistema'),
    (1,'Adm. Institución'),
    (2,'Adm. grupo'),
    (3,'Usuario'),
    (4,'Usuario grupo'),
    (5,'Usuario Institucional'),
    (6,'Invitado'),
    (7,'anonimo')
    ]

#Tipos de números de identificación personal
TIPO_NUIP_CO = [
    (0,'Cédula de Ciudadanía'),
    (1,'Tarjeta de Identidad'),
    (2,'Cédula de Extranjería'),
    (3,'Pasaporte'),
    (4,'Permiso de Residencia')
    ]

#Tipos de número de Único de Identificación Institucional
TIPO_NUII_CO = [
    (0,'NIT'), #Número de Identificación tributaria (Colombia)
    (1,'RUT') #Registro Único Tributario.
    ]

#Tipo de aplicativo
TIPO_APP = [
    (0, 'SIGEPI-BASE'),
    (1, 'Web Server'),
    (2, 'Web Cliente'),
    (3, 'Android'),
    (4, 'IOS'),
    (5, 'Escritorio Windows'),
    (6, 'Escritorio Linux'),
    (7, 'Escritorio MAC'),
    (8, 'otro'),
    ]
#Tipos de Identidad de Género
GENERO = [
    (0,'Neutro'),
    (1,'Femenino'),
    (2,'Masculino'),
    (3,'Intergénero'),
    (4,'Transgénero'),
    (5,'Sisgénero'),
    (6,'Otro')
    ]

#tipo de formación Académica
TIPO_FORM_CO = [
    (0,'Universitaria'),
    (1,'Especializacion'),
    (2,'Maestría'),
    (3,'Doctorado'),
    (4, 'PHD'),
    (5,'Posdoctorado'),
    (6,'Básica Secundaria'),
    (7,'Básica Primaria'),
    (8,'Diplomado'),
    (9,'Curso Corto'),
    (10,'Técnica'),
    (11,'tecnológica'),
    (12,'Curso libre')
    ]

#tipo de formación Académica para grupos
TIPO_FORM_GR = [
    (0,'Seminario'),
    (1,'Taller'),
    (2,'Foro'),
    (3,'Charla'),
    (4,'Encuentro'),
    (5,'Simposio'),
    (6,'Panel'),
    (7,'Conferencia'),
    (8,'Diplomado'),
    (9,'Curso Corto'),
    (10,'Congreso'),
    (11,'Socialización'),
    (12,'Coloquio'),
    (13,'Otro')
    ]

#tipo de modalidad de formación Académica
MODALIDAD = [
    (0,'Presencial'),
    (1,'Virtual'),
    (2,'Semipresencial'),
    (3,'A distancia'),
    (4,'Aprendizaje Acompañado')
    ]

#Tipo de Contratación
TIPO_CONTR_CO = [
    (0,'Término Indefinido'),
    (1,'Término Fijo'),
    (2,'Temporal'),
    (3,'Orden de Servicio'),
    (4,'Contrato de Obra'),
    (5,'Asesoría'),
    (6,'Consultoría'),
    (7,'independiente')
    ]

#Tipos de gupos de Investigación
TIPO_GR_INV = [
    (0,'Independiente'), #Grupo registrado en la plataforma como independiente, asociación de usuarios de la plataforma.
    (1,'Reconocido Inst'), #Grupo que además de registrado está vinculado y reconocido por una Institución o Entidad.
    (2,'Reconocido COLC'), #Grupo que además de registrado está vinculado y reconocido por Colciencias.
    (3,'Semillero de Inv.'), #Grupo que está reconocido como semillero por una Institución o Entidad.
    (4,'Comunidad'), #Grupo de comunidad de conocimiento abierto o libre. Con o sin cuotas de participación.
    (5,'Estado del Arte') #Grupo orientado a la construcción de estados del arte temáticos. Son grupos de comunidades abiertas con vinculación temporal y cuotas de participación.
    ]

#Integrantes según modelo de Colciencias
INTEGR_GR_COLC = [
    (0,'Investigador Emérito'), # Cumple con las características de Investigador Emérito - Se le asigna vinculación.
    (1,'Investigador Sénior'), # Cumple con las características de Investigador Sénior - Se le asigna vinculación.
    (2,'Investigador Asociado'), # Cumple con las características de Investigador Asociado - Se le asigna vinculación.
    (3,'Investigador Junior'), # Cumple con las características de Investigador Junior - Se le asigna vinculación.
    (4,'Integrante vinculado'), # Cumple con las características de Integrante vinculado con doctorado - Se le asigna vinculación.
    (5,'Estudiante de doctorado'), # Cumple con las características de Estudiante de doctorado - Se le asigna vinculación.
    (6,'Integrante vinculado'), # Cumple con las características de Integrante vinculado con maestría o especialidad clínica - Se le asigna vinculación."":
    (7,'Estudiante de maestría o especialidad clínica'), # Cumple con las características de Estudiante de maestría o especialidad clínica - Se le asigna vinculación."":
    (8,'Integrante vinculado con especialización'), # Cumple con las características de Integrante vinculado con especialización - Se le asigna vinculación.
    (9,'Integrante vinculado con pregrado'), # Cumple con las características de Integrante vinculado con pregrado - Se le asigna vinculación.
    (10,'Estudiante de pregrado'), # Cumple con las características de Estudiante de pregrado - Se le asigna vinculación.
    (11,'ninguna de las anteriores') # No cumple ninguna de las anteriores características - Se vincula como Integrante vinculado.
    ]

#Estado de desarrollo del grupo.
ESTADO_DLLO_GR = [
    (0,'Creado'), #El grupo apenas se está convocando y aún no ha culminado al etapa de conformación.
    (1,'Desarrollo Temprano'),
    (2,'Dearrollo Medio'),
    (3,'Desarrollo Alto'),
    (4,'Consolidado'),
    (5,'Ramificado'),
    (6,'Fusionado'),
    (7,'Disgregado'),
    (8,'Disuelto'),
    (9,'liquidado'),
    (10,'Abandonado')
    ]

#Tipo de Institución o entidad
TIPO_INS = [
    (0,'Privada'),
    (1,'Publica'),
    (2,'xxx'),
    (3,'zzzz'),
    ]

#Sector Económico
SECTOR_ECO = [
    (0,'Privado'),
    (1,'Publico'),
    (2,'xxx'),
    (3,'zzzz'),
    ]

# Tipo de fuente de inst. Externa, local, remota.
TIPO_FUENTE_INST = [
    (0,'Externa'),
    (1,'Local'),
    (2,'Remota')
    ]

 #Numerar las posibles extensiones del archivo de instalación 1=".zip";2=".gz",3=".deb";4=".exe"; etc)

# Tipo de extensión del archivo de instalación.
TIPO_EXT = [
    (0,'.Zip'),
    (1,'.Gz'),
    (2,'.msi'),
    (3,'.exe'),
    (3,'.deb'),
    (3,'.rpm'),
    (3,'.tar'),
    (4,'otro'),
    ]

#LIstado de  Horarios
HORARIO = [
    (0,'8am 12pm'),
    (1,'2pm 6pm'),
    (2,'8am 12pm - 2pm 6pm')
    ]

#Usuarios básicos del sistema

#Usuario individual
class usu(AbstractUser):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    #username = models.CharField('Nombres', max_length=100, unique=True)
    #first_name = models.CharField(max_length=45)
    #last_name = models.CharField(max_length=80)
    #email = models.EmailField(max_length = 254)
    #id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_reg = models.DateField('fecha de registro', auto_now = True) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o desactivado.?', default=True) # estatus del usuario activo (True) inactivo (False)
    
    class Meta:
        verbose_name = 'usurio individual'
        verbose_name_plural = 'usuarios individuales'

    # def __str__(self):
    #     return '{}'.format(self.usu)

#Usuario de grupo
class usugr(AbstractUser):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField('usuario (Sigla del Grupo)', max_length=100, unique=True)
    first_name = models.CharField('Nombre del Grupo', max_length=254)
    #last_name = models.CharField(max_length=80)
    email = models.EmailField('Correo-e del Grupo', max_length = 254) #Correo elect´ronico del grupo de investigación
    #id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_reg = models.DateField('fecha de registro', auto_now = True) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o inactivo?', default=True) # estatus del usuario(a) activo (True) inactivo (False)
    id_usu_adm = models.OneToOneField(usu, on_delete=models.SET_NULL, null=True, blank=True) # Usuario(a) principal que administra el grupo
    id_usu_asig = models.OneToOneField(usu, on_delete=models.SET_NULL, null=True, blank=True) # Usuario(a) asignado como administrador(a) del grupo
    
    class Meta:
        verbose_name = 'usurio de grupo'
        verbose_name_plural = 'usuarios de grupos'

    # def __str__(self):
    #     return '{}'.format(self.usu)

#Usuario de Institución
class usui(AbstractUser):
    #user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    username = models.CharField('usuario (Sigla de la Institución)', max_length=100, unique=True)
    first_name = models.CharField('Nombre de la Institución', max_length=254)
    #last_name = models.CharField(max_length=80)
    email = models.EmailField('Correo-e de soporte técnico de la Institución',max_length = 254)
    #id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_reg = models.DateField('fecha de registro', auto_now = True) # fecha de registro de usuario
    activo = models.BooleanField('¿Activo o desactivado.?', default=True) # estatus del usuario(a) activo (True) inactivo (False)
    id_usu_adm = models.OneToOneField(usu,on_delete=models.SET_NULL, null=True, blank=True) # Usuario(a) principal que administra la Institución
    id_usu_asig = models.OneToOneField(usu,on_delete=models.SET_NULL, null=True, blank=True) # Usuario(a) asignado como administrador(a) de la Institución
 
    class Meta:
        verbose_name = 'usurio institucional'
        verbose_name_plural = 'usuarios institucionales'

    # def __str__(self):
    #     return '{}'.format(self.usu)

#Modelos para el registro de módulos, aplicaciones, roles y funciones

# clase que almacena todos los modulos del sistema
class adm_mod(models.Model):
    id_mod = models.AutoField(primary_key = True) # Identificador único del módulo
    titulo = models.CharField('Título del módulo', max_length=40, null=False, blank = False) # Título del módulo ej. "Administración Plataforma"
    desc  = models.CharField('Descripcion del Módulo', max_length=50, null=False, blank = False) # descripcion del Módulo
    url_doc = models.URLField('URL Documentación', null=False, blank=False) # sitio url # direción local a la documentación o manual del módulo.
    version = models.DecimalField('Versión de desarrollo ', max_digits=4, decimal_places=2, null=False, blank = False) # Versión de desarrollo del Módulo ej. "0.01.04"
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
    titulo = models.CharField('Título de la aplicación: ', max_length=40, null=False, blank = False) # Título de la aplicacion ej. "Editor de Texto SABER"
    desc  = models.CharField('descripcion de la aplicación: ', max_length=80, null=False, blank = False) # descripcion de la Aplicación.
    url_doc = models.URLField('URL de la documentación o manual de la aplicación', null=False, blank=False)  # direción local a la documentación o manual de la aplicación.
    url_instal = models.URLField('Url aplicación', null=False, blank=False)  # direción local relativa a la carpeta donde está instalada la aplicación.
    url_pl = models.URLField('Url plantilla de aplicación', null=True, blank=True)  #Nombre de la plantilla  de la aplicación ej. 'app_mod_ej.html' sólo para apps django.
    nom_url = models.URLField('Nombre de la Url de plantilla de aplicación', null=True, blank=True)  #Nombre de la dirección de la aplicación ej. 'app_ej' apps django.
    version = models.CharField('Versión de desarrollo de la aplicación: ', max_length=20, default='0.0.1', null=False, blank = False)  # Versión de desarrollo de la aplicación. "0.01.04"
    id_mod = models.ForeignKey(adm_mod, on_delete=models.CASCADE, null=False, blank =False)# Id del módulo principal con el cual se integra.
    ver_mod = models.DecimalField('Versión de desarrollo de la aplicación: ', max_digits=4, decimal_places=2, null=False, blank = False)  # Versión mínima del módulo principal con la que la actual versión de la aplicación es compatible.
    activo = models.BooleanField('la aplicacion está activa o no', default=False)# estatus de la aplicacion para indicar  el modulo de Administración
    instalada = models.BooleanField('¿La aplicación se encuentra instalada? ', default=False) # ¿La aplicación se encuentra instalada? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.
    externa = models.BooleanField('¿La aplicación es externa?', default=False) # ¿La aplicación es externa, o hace parte de la base del sistema? sí =True; no= False.
    tipo_app = models.IntegerField(null = False, blank = False, choices = TIPO_APP, default = 0) # Ver diccionario TIPO_APP)
    ico = models.CharField('nombre del la imagen del ícono a utilizar', max_length=40) #nombre del ícono a utilizar según las fuentes disponibles ej. 'person' (material icons por defecto)
    id_usu_reg = models.OneToOneField(usu, on_delete=models.SET_NULL, null=True, blank=True) #Usuario(a) quien registra la app
    
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
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de usuario
    fch_ini = models.DateField('fecha de inicio', auto_now = False) # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False) # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_pltf'
        verbose_name_plural = 'log_acc_pltfs'

#Registros de acceso a cada rol
class log_acc_rol(models.Model):
    id_acc_rol = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.OneToOneField(usu, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador único de usuario
    id_rol = models.ForeignKey(adm_rol, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador de rol
    fch_ini = models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'registro de acceso por rol'
        verbose_name_plural = 'registros de acceso por roles'

#Registros de acceso a cada función
class log_acc_func(models.Model):
    id_acc_func = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.OneToOneField(usu, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador único de usuario
    id_func = models.ForeignKey(adm_func, on_delete=models.SET_NULL , null=True, blank =True)  # Identificador de rol
    bk_uso = models.IntegerField('Respaldo Uso', default=0, null=True, blank =True) # Respaldo del Número de veces que la función fue utilizada por el usuario
    uso = models.IntegerField('Uso', default=0, null=True, blank =True) # Número de veces que la función due utilizada por el usuario
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM
    fch_bk = models.DateField('fecha de respaldo', auto_now = False)  # fecha del último respaldo de uso formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'registro de acceso a la función'
        verbose_name_plural = 'registros de acceso a las funciones'

