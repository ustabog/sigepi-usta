from django.db import models
from django.contrib.auth.models import User

#Tipo de rol dentro de la plataforma
TIPO_ROL = [
    (0,'Sistema'),
    (1,'Módulo'),
    (2,'Aplicación'),
    (3,'Extensión'),
    (4,'Otro')
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
TIPO_FUENTE = [
    (0,'Externa'),
    (1,'Local'),
    (2,'Remota')
    ]

 #Numerar las posibles extensiones del archivo de instalación 1=".zip";2=".gz",3=".deb";4=".exe"; etc)
TIPO_EXTEN = [
    (0,'.Zip'),
    (1,'.Gz'),
    (2,'.ded'),
    (3,'.exe'),
    (4,'otro'),
    ]

#LIstado de  Horarios
HORARIO = [
    (0,'8am 12pm'),
    (1,'2pm 6pm'),
    (2,'8am 12pm - 2pm 6pm')
    ]


 #Modulo Adminitrativo

class mod(models.Model):
    # clase que almacena todos los modelos del sistema
    id_mod = models.AutoField(primary_key = True) # Identificador único del módulo
    titulo = models.CharField('Título del módulo', max_length=40, null=False, blank = False) # Título del módulo ej. "Administración Plataforma"
    desc  = models.CharField('descripcion del Módulo', max_length=50, null=False, blank = False) # descripcion del Módulo
    url_doc = models.URLField('Sitio url', null=False, blank=False) # sitio url # direción local a la documentación o manual del módulo.
    version = models.DecimalField('Versión de desarrollo ', max_digits=4, decimal_places=2, null=False, blank = False) # Versión de desarrollo del Módulo ej. "0.01.04"
    activo = models.BooleanField('Status del Modulo ', default=False) # estatus de la aplicacion para indicar  el modulo de Administración
    instalado = models.BooleanField('¿el módulo se encuentra instalado?', default=False) # ¿el módulo se encuentra instalado? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.

    class Meta:
        verbose_name = 'mod'
        verbose_name_plural = 'mods'

    def __str__(self):
        return '{}'.format(self.titulo)

class app_mod(models.Model):
    #Clase que almacena los datos del objeto aplicación, las aplicaciones son unidades de
    id_app = models.AutoField(primary_key = True)  # Identificador único de la aplicación.
    titulo = models.CharField('Título de la aplicacion: ', max_length=40, null=False, blank = False) # Título de la aplicacion ej. "Editor de Texto SABER"
    desc  = models.CharField('descricion de la aplicacion: ', max_length=80, null=False, blank = False) # descripcion de la Aplicación.
    url_doc = models.URLField('Direción local a la documentación o manual de la aplicación', null=False, blank=False)  # direción local a la documentación o manual de la aplicación.
    version = models.DecimalField('Versión de desarrollo de la aplicación: ', max_digits=4, decimal_places=2, null=False, blank = False)  # Versión de desarrollo de la aplicación. "0.01.04"
    mod_prin = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)# Id del módulo principal con el cual se integra.
    ver_mod = models.DecimalField('Versión de desarrollo de la aplicación: ', max_digits=4, decimal_places=2, null=False, blank = False)  # Versión mínima del módulo principal con la que la actual versión de la aplicación es compatible.
    activo = models.BooleanField('estatus de la aplicacion ', default=False)# estatus de la aplicacion para indicar  el modulo de Administración
    instalada = models.BooleanField('¿La aplicación se encuentra instalada? ', default=False) # ¿La aplicación se encuentra instalada? sí =True; no= False.
    visible = models.BooleanField('¿Activa o desactiva la visibilidad de la aplicacion.?', default=False)  # Activa o desactiva la visibilidad de la aplicacion.

#NOTA: #nota ls_func foranea, rol
    class Meta:
        verbose_name = 'app_mod'
        verbose_name_plural = 'app_mods'

    def __str__(self):
        return '{}'.format(self.titulo)

class listado_aplicativo(models.Model): #identifica si es app, android, web etc
    id_aplicativo =  models.AutoField(primary_key = True)
    nom_aplicativo= models.CharField('aplicativo nombre: ', max_length=30, null=False, blank = False)
    activoaplicativo = models.BooleanField('¿Activo o desactivo.?', default=False)

    class Meta:
        verbose_name = 'listado_aplicativo'
        verbose_name_plural = 'listado_aplicativo'

    def __str__(self):
        return '{}'.format(self.nom_aplicativo)

class ext_mod(models.Model):
    #Clase que almacena los datos de las Extensiones.
    id_mod_ext = models.AutoField(primary_key = True)  # Identificador único de la aplicación.
    titulo_ext = models.CharField('Título de la aplicacion: ', max_length=40, null=False, blank = False)
    mod_prin_ext = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
#    ls_mods_ext = models.ManyToManyField(mod, help_text="Listado de id de módulos a los que está vinculada la aplicación")

    class Meta:
        verbose_name = 'ext_mod'
        verbose_name_plural = 'ext_mods'

    def __str__(self):
        return '{}'.format(self.titulo_ext)

class ext_app(models.Model):
    #Clase que almacena los datos de las Aplicaciones Externas o Plugins.
    id_app_ext = models.AutoField(primary_key = True)
    titulo_app_ext = models.CharField('Título de la aplicacion: ', max_length=40, null=False, blank = False)
    mod_prin_app_ext = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)
#    ls_mods_app_ext = models.ManyToManyField(app_mod, help_text="Listado de id de módulos a los que está vinculada la aplicación")

    class Meta:
        verbose_name = 'ext_app'
        verbose_name_plural = 'ext_apps'

    def __str__(self):
        return '{}'.format(self.titulo_app_ext)

class rol(models.Model):

    id_rol = models.AutoField(primary_key = True) # Identificador único del Rol
    etq_rol = models.CharField('Etiqueta: ', max_length=30, null=False, blank = False) # Etiqueta del Rol
    desc = models.CharField('Descripcion del Rol: ', max_length=30, null=False, blank = False) # Descripcion del Rol
    tipo = models.IntegerField(null = False, blank = False, choices = TIPO_ROL, default = 0) # Ver diccionario TIPO_ROL
    id_sis = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de sistema
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de Módulo
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de Aplicación
    id_ext_mod = models.ForeignKey(ext_mod, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de Extensión de módulo
    id_ext_app = models.ForeignKey(ext_app, on_delete=models.CASCADE, null=False, blank =False)  #Identificador de Extensión de aplicación
    req_reg = models.BooleanField('¿Activa o desactiva.?', default=False) # Variable que indica si require registro en aplicativo o plataforma o no.

    class Meta:
        verbose_name = 'rol'
        verbose_name_plural = 'rols'


    def __str__(self):
        return '{}'.format(self.etq_rol)

class param_config(models.Model):
    #Clase que almacena los datos del ojeto parámetro de configuración.
    id_param_config = models.AutoField(primary_key = True)  # Identificador único de la aplicación.
    titulo_param_config = models.CharField('Parametro ', max_length=40, null=False, blank = False)

    class Meta:
        verbose_name = 'param_config'
        verbose_name_plural = 'param_configs'

class Permiso(models.Model): #permisos del aplicativo en general

    id_permisos = models.AutoField(primary_key = True)
    nom_permiso = models.CharField('permisos: ', max_length=30, null=False, blank = False)
    activo = models.BooleanField('¿Activ o desactivo.?', default=False)

    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'

    def __str__(self):
        return '{}'.format(self.nom_permiso)

class rol_permiso(models.Model): #listado de roles con cada permiso

    id_permisos = models.ForeignKey(Permiso, on_delete=models.CASCADE, null=False, blank =False)
    id_rol = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)
    activo = models.BooleanField('¿Activ o desactivo.?', default=False)

    class Meta:
        verbose_name = 'rol_permiso'
        verbose_name_plural = 'rol_permisos'

class func_app(models.Model):

    id_func = models.AutoField(primary_key = True) # identificador único de función
    nom_func = models.CharField('Nombre de la función: ', max_length=30, null=False, blank = False) # Nombre de la función
    lib_func = models.CharField('Librería que contiene la función: ', max_length=30, null=False, blank = False) # Librería que contiene la función
    url_loc = models.URLField('Direción local a la documentación o manual de la aplicación', null=False, blank=False)  # Direción local donde se encuentra la librería que contiene la función
    com_exc = models.CharField('Comando de Ejecución de la Función: ', max_length=20, null=False, blank = False) # Comando de Ejecución de la Función
    text = models.CharField('Nombre de Función: ', max_length=20, null=False, blank = False) # Nombre de Función para menús o etiquetas.
    context = models.CharField('Contexto: ', max_length=20, null=False, blank = False) # Nombre de Función para menús contextuales o emergentes y panel de inf.
    activa = models.BooleanField('¿Activa o desactiva.?', default=False)  # La función está activa o desactiva.
    indice = models.PositiveSmallIntegerField(default= 5) #Índice de selección, para navegar con el tabulador.
    # realizar una tabla de ralcion con rol y pwermisos
    #[[0,False,True,False,False]]
    #listado de los diferentes id_rol de aplicación para los cuales la función estará activa.
    #[,False,,,]¿genera registro en base de datos?;[,,True,,] Permiso de lectura en BD
    #[,,,False,]Permiso de excritura en BD.[,,,,False]Permiso de Ejecución.

    class Meta:
        verbose_name = 'func_app'
        verbose_name_plural = 'func_apps'

    def __str__(self):
        return '{}'.format(self.nom_func)


class rl_mod_app_mod(models.Model):  # relacion Listado de id de aplicaciones vinculadas al módulo.
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
    ls_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)

class rl_mod_rol(models.Model): # relacion Listado de id de roles vinculados al módulo.
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_rol = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)#

class rl_mod_param_cnf(models.Model): # relacion Listado de parámetro de configuración objetos de la clase param_config().
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_param_cnf =  models.ForeignKey(param_config, on_delete=models.CASCADE, null=False, blank =False)## Listado de parámetro de configuración objetos de la clase param_config().

class rl_mod_func(models.Model): #Listado de funciones propias del módulo, objetos de la clase func_app().
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_func =  models.ForeignKey(func_app, on_delete=models.CASCADE, null=False, blank =False)#) # Listado de funciones propias del módulo, objetos de la clase func_app().

##############
class rl_app_mod_mod(models.Model): #Listado de id de módulos a los que está vinculada la aplicación esta repetiad ojooooooo
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_mods = models.ForeignKey(mod,on_delete=models.CASCADE, null=False, blank =False) # Listado de id de módulos a los que está vinculada la aplicación

class rl_app_mod_rol(models.Model): #listado de los diferentes id_rol de aplicación para los cuales la aplicación estará activa.
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_rol = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)#
    activo = models.BooleanField('activo', default = True) # verificar si este campo va

class rl_app_mod_param_cnf(models.Model): # relacion Listado de parámetro de configuración objetos de la clase param_config().
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_param_cnf =  models.ForeignKey(param_config, on_delete=models.CASCADE, null=False, blank =False)

class rl_app_mod_func(models.Model): # relacion Listado de funciones propias del módulo, objetos de la clase func_app().
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)#
    ls_func =  models.ForeignKey(func_app, on_delete=models.CASCADE, null=False, blank =False)#) # Listado de funcion


class usu(models.Model):

    id_usu = models.AutoField(primary_key = True) # Identificador único
    usuario = models.CharField('Nick: ', max_length=30, null=False, blank = False)  # Nick o identificador de usuario
    passusu  = models.CharField('Contraseña: ', max_length=30, null=False, blank = False)  # contraseña
    id_rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo# Identificador del Rol de Usuario de Sistema
    fch_regi = models.DateField('fecha de registro', auto_now = False) # fecha de registro de usurio
    activo = models.BooleanField('¿Activo o desactivado.?', default=False) # estatus del usuario activo (True) inactivo (False)

    class Meta:
        verbose_name = 'usu'
        verbose_name_plural = 'usus'

    def __str__(self):
        return '{}'.format(self.usu)

class mod_adm(models.Model):
# verificar inicio de sesion de django ojo, django todo
    sesion = models.AutoField(primary_key = True) # código o número de id_sesion
    #ls_sesion = [] # listado de sesiones activas
    #log_sesion = [] # listado del registro de sesiones
    id_usu_adm = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # Id del usuario Super Administrador de la plataforma
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
    # nota preguntar mod.__init__(self), donde tomo las sesiones activas etc
    class Meta:
        verbose_name = 'mod_adm'
        verbose_name_plural = 'mod_adms'
    pass

class adm_install(models.Model):
    pass


class log_mod_rol(models.Model):

    id_log =  models.AutoField(primary_key = True) #identificador de repositorio o fuente de instalación
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)
    Direccion = models.URLField('Drección local relativa ', null=False, blank=False)
#tabla contruir modulo, app, direccion relativa (carpetas donde estan las fuentes)) para el log

    class Meta:
        verbose_name = 'log_mod_rol'
        verbose_name_plural = 'log_mod_rols'

class fuente_ins(models.Model):
    #Clase que contiene los campos del objeto fuente de instalación.

    id_rep = models.AutoField(primary_key = True)  #identificador de repositorio o fuente de instalación
    tipo = models.IntegerField(choices = TIPO_NUIP_CO, default = 0, null=False, blank = False)  # Tipo de fuente de inst. Externa, local, remota.
    tipo_arch = models.IntegerField(choices = TIPO_EXTEN, default = 0, null=False, blank = False) # Numerar las posibles extensiones del archivo de instalación 1=".zip";2=".gz",3=".deb";4=".exe"; etc)
    url_loc = models.CharField('Dirección local: ', max_length=5, null=False, blank = False)  # dirección local relativa
    url_rem = models.URLField('Drección remota ', null=False, blank=False)
    url = models.URLField('Drección local relativa ', null=False, blank=False)
    log = [] # lista de valores: archivo,id app o mod, dir relativa
    valid = models.BooleanField('¿fuente valida?', default=False) # fuente validada o no

    class Meta:
        verbose_name = 'fuente_ins'
        verbose_name_plural = 'fuente_inss'

class rl_fuente_ins_param_cnf(models.Model): # Listado de parámetro de configuración objetos de la clase param_config().
    id_rep = models.ForeignKey(fuente_ins, on_delete=models.CASCADE, null=False, blank =False)
    id_param_cnf =models.ForeignKey(param_config, on_delete=models.CASCADE, null=False, blank =False)  # Listado de parámetro de configuración objetos de la clase param_config().

class log_acc_mod(models.Model):

    id_log_acces = models.AutoField(primary_key = True)  # Identificador único de registro de acceso
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)  # Identificador único de usuario
    id_mod = models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del  módulo
    fch_ini = models.DateField('fecha de inicio', auto_now = False)  # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False)  # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_mod'
        verbose_name_plural = 'log_acc_mods'

class log_acc_pltf(models.Model):

    id_acc_pltf = models.AutoField(primary_key = True)  # Identificador único
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de usuario
    fch_ini = models.DateField('fecha de inicio', auto_now = False) # fecha de inicio formato AAAA-MM-DD-HH:MM
    fch_fin = models.DateField('fecha de fin', auto_now = False) # fecha de finalización formato AAAA-MM-DD-HH:MM

    class Meta:
        verbose_name = 'log_acc_pltf'
        verbose_name_plural = 'log_acc_pltfs'

# Clases de la Aplicación Registro de Usuarios
############################################################################


class usu_inf_apps(models.Model):

    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de sistema
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza. clave foranea a roles .. muchos
    rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador de rol de sistema.
    app_act = models.ForeignKey(listado_aplicativo,on_delete=models.CASCADE, null=False, blank =False) # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión, app_mod

    class Meta:
        verbose_name = 'usu_inf_apps'
        verbose_name_plural = 'usu_inf_appss'

class rl_usu_inf_apps_rol(models.Model): #identificar el rol actual del usuario
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)
    rol_act = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)

class discapacidad(models.Model):
    id_disc = models.AutoField(primary_key = True) # identificador de usuario
    tipo_disca = models.CharField('tipo de discapacidad ', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    desc_disca = models.CharField('Descripcion', max_length=30, null=False, blank = False)  # tipo de Número de identificación personal

    class Meta:
        verbose_name = 'discapacidad'
        verbose_name_plural = 'discapacidads'

    def __str__(self):
        return '{}'.format(self.tipo_disca)

class usu_inf_pers(models.Model):

    id_usu = models.OneToOneField(User, on_delete=models.CASCADE) # identificador de usuario
    nuip = models.CharField('número único de identificación personal ', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    tipo_nuip = models.IntegerField( choices = TIPO_NUIP_CO, default = 0, null=False, blank = False) # tipo de Número de identificación personal
    nombres = models.CharField('Nombres ', max_length=60, null=False, blank = False) # nombres de usuario
    apelllidos = models.CharField('Apellidos ', max_length=60, null=False, blank = False) # apellidos de usuario
    nal = models.CharField('Nacionalidad ', max_length=30, null=False, blank = False) # nacionalidad
    fch_naci = models.DateField('fecha de nacimiento', auto_now = False)   # fecha de nacimiento de usuario
    gene = models.IntegerField(choices = GENERO, default = 0, null=False, blank = False)  #genero del usuario
    ocup = models.CharField('Ocupacion ', max_length=30, null = False, blank = False) # ocupación del usuario
    dir = models.CharField('Direccion ', max_length=100, null=False, blank = False) # direccion de residencia
    discap = models.BooleanField('¿Es una persona en condición de discapacidad?', default=False) # Es una persona en condición de discapacidad
    tipo_discap = models.ForeignKey(discapacidad, on_delete=models.CASCADE, null=False, blank =False)  # Tipo de  discapacidad tabla de discapacidad
    url_imag = models.URLField('url de la imagen personal.', null=False, blank=False)  # url de la imagen personal.
    zona_hor = models.CharField('Zona Horaria ', max_length=100, null=False, blank = False) #Zona Horario internacional

    class Meta:
        verbose_name = 'usu_inf_pers'
        verbose_name_plural = 'usu_inf_perss'

class usu_inf_contac(models.Model):

    id_usu = models.OneToOneField(User, on_delete=models.CASCADE)  # identificador de usuario
    ind_nal = models.PositiveSmallIntegerField('Indicativo telefónico de país') #Indicativo telefónico de país
    cel = models.CharField('Número de telefono móvil del usuario',  max_length=30, null=False, blank = False) #Número de telefono móvil del usuario
    wa = models.CharField('Número de WhatsApp',  max_length=30, null=False, blank = False) # Número de WhatsApp
    email = models.EmailField('Correo electrocico',  max_length=30, null=False, blank = False)  # dirección de correo electrónico
    cod_post = models.PositiveSmallIntegerField('Número de código postal', null=False, blank =False)  # Número de código postal
    ls_ha =  models.IntegerField(choices = HORARIO,default = 0, null=False, blank = False) #Listado de Horario de atención [día,hora ini, hora fin]
    web = models.URLField('dirección de página web o blog personal', null=False, blank=False) # dirección de página web o blog personal
    dir_offi = models.CharField('Dirección de Ofiina (país, ciudad, dir) ', max_length=100, null=False, blank = False) # Dirección de Oficina (país, ciudad, dir)

    class Meta:
        verbose_name = 'usu_inf_contac'
        verbose_name_plural = 'usu_inf_contacs'

class red_soc(models.Model):

    id_red = models.AutoField(primary_key = True)
    nombre_red = models.CharField('Dirección de Oficina (país, ciudad, dir) ', max_length=30, null=False, blank = False)
    usuario =  models.CharField('Direcció n de Oficina (país, ciudad, dir) ', max_length=20, null=False, blank = False)  #nick o dirección de usuario
    url = models.URLField('Url de página principal dentro de la red.', null=False, blank=False) #Url de página principal dentro de la red.
    uso = models.CharField('Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3) ', max_length=20, null=False, blank = False)  #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('acceso público de información de red', default=False)  #Acceso público de información de red

    class Meta:
        verbose_name = 'red_soc'
        verbose_name_plural = 'red_socs'

class rl_usu_inf_red_social(models.Model): # relacion Listado de objetos de redes sociales
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_red = models.ForeignKey(red_soc, on_delete=models.CASCADE, null=False, blank =False)   # Listado de objetos de redes sociales


class form_acad(models.Model):

    id_fa =  models.AutoField(primary_key = True) #Id de formación académica
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE)  # identificador de usuario
    instit = models.CharField('Nombre de la institucion ', max_length=25, null=False, blank = False) # Nombre de la institucion académica donde curso la formación
    tipo_form =  models.IntegerField(choices = TIPO_FORM_CO, default = 0, null=False, blank = False) #tipo de formación ver diccionario TIPO_FORM
    fch_ini = models.DateField('fecha de Inicio', auto_now = False)
    fch_fin = models.DateField('fecha de Fin', auto_now = False)
    certif = models.BooleanField('Posees Certificado', default=False)
    nal = models.CharField('Pais ', max_length=20, null=False, blank = False) #país
    ciudad = models.CharField('Ciudad ', max_length=20, null=False, blank = False)
    mod =  models.IntegerField(choices = MODALIDAD, default = 0, null=False, blank = False) # modalidad
    tit = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False) # Título obtenido
    menc =  models.CharField('Mensión ', max_length=20, null=False, blank = False)  # Mensión de honor
    token = models.CharField('token de validación ', max_length=20, null=False, blank = False)  #Token de validación electrónica de certificación de la formación

    class Meta:
        verbose_name = 'form_acad'
        verbose_name_plural = 'form_acads'

class usu_inf_acad(models.Model):
#ESTA NO ME PARECE YA
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)  # identificador unico
    nivelform =  models.IntegerField(choices = TIPO_FORM_CO, default = 0, null=False, blank = False) # me indica la formacion qu tiene la usuario

    class Meta:
        verbose_name = 'usu_inf_acad'
        verbose_name_plural = 'usu_inf_acads'

class rl_usu_inf_form_acad(models.Model): # relacion de listado de id procesos de formación realizados
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_form = models.ForeignKey(form_acad, on_delete=models.CASCADE, null=False, blank =False)   #listado de procesos de formación realizados


class curs_dict(models.Model):
    #clase que almacena la información de cursos dictados a cargo de un usuario
    id_cd = models.AutoField(primary_key = True)    #Id de formación académica
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)
    instit =  models.CharField('Nombre de la institucion académica donde dictó el curso. ', max_length=20, null=False, blank = False) # Nombre de la institucion académica donde dictó el curso.
    tipo_form = models.IntegerField(choices = TIPO_FORM_CO, null=False, blank = False, default=0)  #tipo de formación ver diccionario TIPO_FORM
    fch_ini = models.DateField('fecha de inicio', auto_now = False)
    fch_fin = models.DateField('fecha de fin', auto_now = False)
    certif = models.BooleanField('Posees Certificado', default=True)
    nal =  models.CharField('Pais ', max_length=30, null=False, blank = False) #país
    ciudad = models.CharField('Ciudad ', max_length=30, null=False, blank = False)
    mod = models.IntegerField('Modalidad', choices = MODALIDAD, null=False, blank = False, default=0)  # modalidad
    num_est = models.IntegerField('Cantidad de estudiantes')  #Cantidad de Estudiantes
    dur = models.IntegerField('Número total de horas académicas del curso')  #Número total de horas académicas del curso
    nom_curs = models.CharField('Nombre del curso', max_length = 60, null=False, blank = False)  # modalidad #Nombre del Curso
    mun_ciclos = models.IntegerField('cuántas veces se dictó el curso')  #Número de ciclos del curso "cuántas veces se dictó el curso"
    url_prog =  models.URLField('Url del documento o sitio web ', null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa del curso

    class Meta:
        verbose_name = 'curs_dict'
        verbose_name_plural = 'curs_dicts'

class rl_usu_inf_contac_curs_dict(models.Model):  # relacion de LIstado de id Cursos a cargo dictadospor al persona.
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_cursdict = models.ForeignKey(curs_dict, on_delete=models.CASCADE, null=False, blank =False) #LIstado de id Cursos a cargo dictadospor al persona.


class usu_inf_prof(models.Model):
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador unico de usuario
    prof = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False)  # Profesión Actual

    class Meta:
        verbose_name = 'usu_inf_prof'
        verbose_name_plural = 'usu_inf_profs'

class rl_usu_inf_prof_empleos(models.Model):  # relacion listado de procesos de formación realizados
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_empl = models.ForeignKey(curs_dict, on_delete=models.CASCADE, null=False, blank =False)

class empleos(models.Model):

    id_empl = models.AutoField(primary_key = True)
    id_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)
    instit = models.CharField('Nombre de la institucion ', max_length=20, null=False, blank = False) # Nombre de la institucion académica donde curso la formación
    nom_cargo = models.CharField('Nombre del Cargo ', max_length=20, null=False, blank = False)  #Nombre del Cargo
    fch_ini = models.DateField('fecha de inicio', auto_now = False)
    fch_fin = models.DateField('fecha de Fin', auto_now = False)
    certif = models.BooleanField('Posees certificado', default=False)
    nal = models.CharField('Pais ', max_length=20, null=False, blank = False)  #país
    ciudad = models.CharField('Ciudad ', max_length=20, null=False, blank = False)
    tipo_contr =  models.IntegerField(choices = TIPO_CONTR_CO, null=False, blank = False, default = 0)
    tit = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False)  # Título obtenido
    menc = models.CharField('Mensión de honor ', max_length=20, null=False, blank = False)  # Mensión de honor
    token = models.CharField('Token de validación electrónica  ', max_length=20, null=False, blank = False)  #Token de validación electrónica de certificación de la formación
    ret = models.CharField(' Motivo del retiro ', max_length=20, null=False, blank = False)  # Motivo del retiro

    class Meta:
        verbose_name = 'empleos'
        verbose_name_plural = 'empleoss'

class habilidades(models.Model):
    #clase que almacena la información de tipos de habilidad
    id_hab = models.AutoField(primary_key = True)
    nom_hab = models.CharField('Nombre de la habilidad', max_length=20, null=False, blank = False)  #Nombre de la habilidad
    desc = models.CharField('Descripción de la Habilidad', max_length=20, null=False, blank = False)  #Descripción de la Habilidad

    class Meta:
        verbose_name = 'habilidades'
        verbose_name_plural = 'habilidadess'

class usu_inf_hab(models.Model): # relacion de listado de id de habilidades registradas por le usuario
    # Clase que almacena la información de las habilidades o conocimientos adquiridos y certificados por el usuario
    id_usu=  models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False) # identificador unico de usuario
    ls_habs =  models.ForeignKey(habilidades, on_delete=models.CASCADE, null=False, blank =False)  # listado de id de habilidades registradas por le usuario
    descripcion = models.CharField('Descripción ', max_length=20, null=False, blank = False)  # descripcion del conocimiento o habilidad investigador

    class Meta:
        verbose_name = 'usu_inf_hab'
        verbose_name_plural = 'usu_inf_habs'

class valid_hab(models.Model): # verificar esta
    #clase que procesa la información de validación social de habilidades
#    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # Identificador del Usuario que registra la habilidad
    id_hab = models.ForeignKey(habilidades, on_delete=models.CASCADE, null=False, blank =False) #Identificador de la habilidad que se va a validar
    id_usu_val = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)  #Identificador del Usuario que valida la habilidad
    id_esc = models.CharField('IDENTIFICADOR ', max_length=20, null=False, blank = False) #Identificador de la escala de validación
    val = models.CharField('RANGO ', max_length=20, null=False, blank = False) #Valor dentro del rango de la escala de validación

    #nota como realizp el dato val, id esc, id:usu_val
    class Meta:
        verbose_name = 'valid_hab'
        verbose_name_plural = 'valid_habs'

class app_reg_usu(models.Model):

    app_mod = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)  # identificador de app
    nombre = models.CharField('Nombre de la app ', max_length=20, null=False, blank = False) # nombre del objeto
    descripcion = models.CharField('Descripcion ', max_length=20, null=False, blank = False) # descripcion del objeto
    activo = models.BooleanField('Activo ', default=False) # activo o no

    class Meta:
        verbose_name = 'app_reg_usu'
        verbose_name_plural = 'app_reg_usus'


#Clases de la Aplicación Registro de Grupos
#################################################################################

class etapa_gr(models.Model):
    #Clase que registra las etapas de los grupos de investigación en el sistema.
    id_etp_gr = models.AutoField(primary_key = True) #Identificador único de la etapa del grupo de investigacion.
    nom =  models.CharField('Nombre del grupo  ', max_length=20, null=False, blank = False)  #Nombre del grupo (puede ser el qeu tuvo en algún momento, se pueden registrar varios nombres según al trayectoria del grupo)
    fch_ini_nom = models.DateField('Fecha en la que se creó el grupo ', auto_now = False) #Fecha en la que se creó el grupo con ese nombre, o en el que cambió a ese nombre.
    fch_fin_nom = models.DateField('Fecha en la que se terminó el grupo', auto_now = False) #Fecha en la que se terminó el grupo con ese nombre, o en el que dejó de usar ese nombre.
    vig = models.BooleanField('El nombre se encuentra vigente ', default=True) #El nombre se encuentra vigente, es el que se usa actualmente el grupo.
    sigla = models.CharField('Sigla con la que se identificó(a) el grupo ', max_length=20, null=False, blank = False)  #Sigla con la que se identificó(a) el grupo en esta etapa.
    url_arch = models.URLField('URL del sitio web ', null= False, blank=False) #Url de sitio web o repositorio virtual donde repose el archivo(memoria o sitio web) del grupo.
    gruplac = models.URLField('Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.', null = 'False', blank = 'False') #Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.

    class Meta:
        verbose_name = 'etapa_gr'
        verbose_name_plural = 'etapa_grs'

    def __str__(self):
        return '{}'.format(self.nom)

class usugr(models.Model):
    #Clase que registra la información básica del usuario grupo en el sistema.

    id_gr = models.AutoField(primary_key = True) #Identificador único del grupo de investigacion.
    passgr  = models.CharField('Descripcion ', max_length=20, null=False, blank = False)  # contraseña para el usuario grupo (diferente a la del usuario del sistema)
    id_usu_admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)  #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_gr)
    id_rol_app = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del Rol de Usuario grupo dentro de la app_reg_gr
#    ls_pry =  models.ManyToManyField(pry) #Listado de id de proyectos vinculados al grupo de investigación.
#    ls_prod = models.ManyToManyField(pro) #Listado de id de productos de investigación vinculados al grupo.
    activo = models.BooleanField('Activo ', default=True)  #El grupo se encuentra activo.

    class Meta:
        verbose_name = 'usugr'
        verbose_name_plural = 'usugr'


class usu_nr(models.Model):
    #Clase que registra los datos de investigación de un integrante grupo no registrado en el sistema.
    id_usu_nr = models.AutoField(primary_key = True)  # identificador unico
    nombres = models.CharField('Nombres del integrante no registrado(a).', max_length=40, null=False, blank = False) # Nombres del integrante no registrado(a).
    apellidos = models.CharField('Apellidos del integrante no registrado(a).', max_length=40, null=False, blank = False)  # Apellidos del integrante no registrado(a).
    rol =  models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   #Rol de investigación que se desempeña actualmente
    cvlac =  models.URLField('URL del CVlac del investigador(a).', null=False, blank=False)  #URL del CVlac del investigador(a).
    orcid = models.CharField('ID de ORCID del investigador(a).', max_length=20, null=False, blank = False)  #ID de ORCID del investigador(a).
    ggl = models.URLField('URL Google académico del investigador(a)', null=False, blank=False)  #URL Google académico del investigador(a).

    class Meta:
        verbose_name = 'usu_nr'
        verbose_name_plural = 'usu_nrs'

    def __str__(self):
        return '{}'.format(self.nombres)


class rel_usugr_ls_etp(models.Model): #relacion de Listado histórico de etapas que ha tenido el grupo.
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_etp = models.ForeignKey(etapa_gr, on_delete=models.CASCADE, null=False, blank =False)

class rel_usugr_ls_usu(models.Model):#Listado de id_usu integrantes del grupo registrados en el sistema.
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_int_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)

class rel_usugr_ls_usu_nr(models.Model):#Listado de id de integrantes no registrados en el sistema.
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_int_nr = models.ForeignKey(usu_nr, on_delete=models.CASCADE, null=False, blank =False)

class usugr_inf_apps(models.Model):
    # Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles

    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de grupo
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
    # [0,] id_rol; [,0] id_usu quien autoriza.
    rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   # Identificador de rol de sistema.
    app_act = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank =False)  # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)

    class Meta:
        verbose_name = 'usugr_inf_apps'
        verbose_name_plural = 'usugr_inf_appss'

class rl_usugr_inf_rol_Actual(models.Model): # identificador del rol actual.
    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de grupo
    rol_act = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # identificador del rol actual.

class usugr_inf_gr(models.Model):
    #clase de información de usuario grupo.
#preguntar identificador de grupo padre ?
    id_usugr = models.AutoField(primary_key = True)
    id_grupo =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False, default = 0) # identificador de usuario grupo
    cod_gr = models.PositiveSmallIntegerField(' código único de identificación del grupo', default=8) # código único de identificación del grupo
    tipo_gr = models.IntegerField(choices = TIPO_GR_INV, null = False, blank = False, default = 0) # tipo de grupo, ver diccionario TIPO_GR_INV
    id_etp_gr = models.ForeignKey(etapa_gr, on_delete=models.CASCADE, null=False, blank =False)  # Identificador de etapa vigente del grupo
    nal = models.CharField('Nacionalidad', max_length=40, null=False, blank = False)  # País principal con el que se identifica el grupo.
    dir = models.CharField('Direccion de correspondencia ', max_length=40, null=False, blank = False)  # direccion de correspondencia.
    estado = models.IntegerField(choices = ESTADO_DLLO_GR, null = False, blank = False, default=0) # Estado de desarrollo del Grupo. Ver diccionario ESTADO_DLLO_GR
    url_imag = models.URLField('url de la imagen o logo del grupo', null=False, blank=False)  # url de la imagen o logo del grupo.
    zona_hor =  models.CharField('Zona Horaria', max_length=40, null=False, blank = False) #Zona Horaria internacional
    id_gr_padre =  models.CharField('grupo padre', max_length=40, null=False, blank = False, default = 0) #Identificador del grupo padre si lo tiene, de lo contrario es el valor es cero

    class Meta:
        verbose_name = 'usugr_inf_gr'
        verbose_name_plural = 'usugr_inf_grs'

class usugr_inf_contac(models.Model):

    id_usugr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)   # identificador de usuario grupo
    ind_nal = models.CharField('Nacionalidad ', max_length=20, null=False, blank = False)  #Indicativo telefónico de país
    tel = models.CharField('Telefono oficina ', max_length=20, null=False, blank = False)  #Número de telefono fijo de oficina del grupo
    cel = models.CharField('N° Celular ', max_length=20, null=False, blank = False)  #Número celular de contacto del grupo.
    email = models.EmailField('correo', null = False, blank = False) # dirección de correo electrónico del grupo.
    cod_post = models.PositiveSmallIntegerField('Codigo Postal ', default = 5) # Número de código postal de oficina
    ls_hr = models.IntegerField( choices = HORARIO, default =0, null=False, blank = False) #Listado de Horario de reunión semanal[día,hora ini, hora fin]
    web =  models.URLField('página web o blog del grupo ', null=False, blank=False)  # dirección de página web o blog del grupo
    dir_offi = models.TextField('Direccion e oficina', null=False, blank = False) # Dirección de Oficina (país, ciudad, dir)

    class Meta:
        verbose_name = 'usugr_inf_contac'
        verbose_name_plural = 'usugr_inf_contacs'

class usugr_inf_red_social(models.Model):  # Listado de objetos de redes sociales
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)
    ls_red = models.ForeignKey(red_soc, on_delete=models.CASCADE, null=False, blank =False)

class form_acad_gr(models.Model):
    #clase que almacena la información de formación académica de un usuario grupo //verificar si es academica en general o solo del grupo
    id_form_acad_gr = models.AutoField(primary_key = True)
    tipo_form = models.IntegerField(choices = TIPO_FORM_GR, null=False, blank = False, default=0) #tipo de formación ver diccionario TIPO_FORM_GR
    fch_ini = models.DateField('Fecha de inicio ', auto_now = False)
    fch_fin = models.DateField('Fecha de fin: ', auto_now = False)
    certif = models.BooleanField('Posees Ceertificado: ', default= True)
    nal = models.CharField('Pais ', max_length = 25, null = False, blank = False) #país
    ciudad = models.CharField('Ciudad: ', max_length=25, null = False, blank = False)
    mod = models.IntegerField(choices = MODALIDAD, blank = False, null = False, default = 0) # modalidad
    asis = models.PositiveSmallIntegerField('Número de asistentes', default = 5) # Número de asistentes
    hora = models.PositiveSmallIntegerField(' Número de horas académicas', default = 5) # Número de horas académicas
    mem = models.URLField('url de las memorias del tipo de formación', null = False, blank = False) #url de las memorias del tipo de formación.
    token = models.CharField('Token de validación electrónica', null = False, blank=False, max_length= 30) #Token de validación electrónica de certificación de la formación

    class Meta:
        verbose_name = 'form_acad_gr'
        verbose_name_plural = 'form_acad_gr'

class usugr_inf_acad(models.Model): #ojo dejar o quitar, y pry y prod no las inclui porque no la tengo en modelos
    # Clase que almacena y procesa la información de actividades académicas y oferta formativa del usuario grupo
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)  # identificador único de grupo
    #prod = [] #Listado de id de productos de investigación vinculados al id usugr
    #pry_inv = [] #Listado de id de proyectos de investigación vinculados al id usugr

    class Meta:
        verbose_name = 'usugr_inf_acad'
        verbose_name_plural = 'usugr_inf_acads'


class curs_ofer(models.Model):
    #clase que almacena la información de cursos ofertados por parte de un usuario grupo
    instit = models.CharField('Nombre de la institucion académica ', max_length=20, null=False, blank = False)  # Nombre de la institucion académica que oferta el curso o evento académico.
    tipo_form_gr = models.IntegerField(choices = TIPO_FORM_GR, null=False, blank = False, default = 0)  #tipo de formación ver diccionario TIPO_FORM_GR
    fch_ini = models.DateField('fecha Inicio', auto_now = False)
    fch_fin = models.DateField('fecha Fin ', auto_now = False)
    certif = models.BooleanField('Activo ', default=True)
    nal =models.CharField('Pais: ', max_length=30, blank = False, null = False) #país
    ciudad = models.CharField('Ciudad ', max_length=30, blank = False, null =False)
    mod =  models.IntegerField(choices = MODALIDAD, null=False, blank = False, default=0) # modalidad
    num_est = models.PositiveSmallIntegerField('Cupo de Estudiantes o asistentes', default = 5) #Cupo de Estudiantes o asistentes
    dur = models.PositiveSmallIntegerField('Número total de horas académicas del curso', default = 5) #Número total de horas académicas del curso o evento académico
    nom_curs = models.CharField('Nombre del Curso o evento académico. ', max_length=30, null=False, blank = False) #Nombre del Curso o evento académico.
    mun_ciclos = models.PositiveSmallIntegerField('cuántas veces se realizará el curso o evento', default =5) #Número de ciclos del curso "cuántas veces se realizará el curso o evento"
    url_prog = models.URLField('página web o blog del grupo ', null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa del curso o el evento académico.
    inscr = models.URLField('Url del formulario de inscripción.', null = 'False', blank = False) #Url del formulario de inscripción.

    class Meta:
        verbose_name = 'curs_ofer'
        verbose_name_plural = 'curs_ofers'

class usugr_form_acad_gr(models.Model):  # listado de id procesos de formación realizados
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)
    ls_form_gr = models.ForeignKey(form_acad_gr, on_delete=models.CASCADE, null=False, blank =False)

class usugr_curs_ofer(models.Model):  ##listado de id cursos o eventos acadeḿicos ofertados por el grupo.
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)
    ls_cursofer =  models.ForeignKey(curs_ofer, on_delete=models.CASCADE, null=False, blank =False)
#    ls_prod = [] #Listado de id de productos de investigación vinculados al id usugr

class app_reg_gr(models.Model):
    #Clase que contiene los objetos de la App Registro de Grupos
    id_app_reg_gr = models.AutoField(primary_key = True)
    nombres = models.CharField('Descripcion.', max_length=40, null=False, blank = False)
    id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de aplicacion por modulo _administrador

    class Meta:
        verbose_name = 'app_reg_gr'
        verbose_name_plural = 'app_reg_grs'

#Clases de la Aplicación Registro de Instituciones
###############################################################

class usui(models.Model):
    # Clase que almacena y procesa la información de un usuario institucional
    id_usuinst = models.AutoField(primary_key = True) # Identificador único del usuario institucionnal
    passinst  = models.CharField('Contraseña ', null = False, blank = False, max_length = 15) # contraseña para el usuario institucional (diferente a la del usuario del sistema)
    id_usu_admin = models.ForeignKey(User, on_delete=models.CASCADE, null= False, blank = False) #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_ins)
    id_rol_app = models.ForeignKey(rol, on_delete = models.CASCADE, null= False, blank = False) # Identificador del Rol de Usuario Institucional dentro de la app_reg_ins
    fch_regi = models.DateField('fecha de registro de usurio: ', auto_now = False) # fecha de registro de usurio
    activo = models.BooleanField(' estatus del usuario activo', default = True) # estatus del usuario activo (True) inactivo (False)

    class Meta:
        verbose_name = 'usui'
        verbose_name_plural = 'usuis'


class usui_inf_apps(models.Model):
    # Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank = False) #id único de Usuario de sistema
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza.
    rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank = False) # Identificador de rol de sistema.
    app_act = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank = False) # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)
    #rol_act = 0 # identificador del rol actual.

    class Meta:
        verbose_name = 'usui_inf_apps'
        verbose_name_plural = 'usui_inf_appss'

class usui_rol_actual(models.Model): #relacion qu me almacena el rol actual
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank = False) #
    rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank = False)

class usui_inf_inst(models.Model):
    #clase de información de usuario institucional.

    id_usui =   models.ForeignKey(usui, on_delete = models.CASCADE, null= False, blank = False) # identificador de usuario institucional
    nuii = models.CharField('número único de identificación institucional sin puntos', max_length=30, blank= False, null = False) # número único de identificación institucional sin puntos
    tipo_nuii = models.IntegerField('Tipo de Número de identificación Institucional', choices= TIPO_NUII_CO, default= 0, null=False, blank= False) # Tipo de Número de identificación Institucional
    rs = models.CharField('Razón Social de la Institución', max_length= 30, null=False, blank= False) # Razón Social de la Institución
    sigla = models.CharField('Sigla institucional', max_length=20, blank= False, null=False) # Sigla institucional
    repleg = models.CharField('Nombre Completo del representante legal', max_length= 60, null=False, blank=False) #Nombre Completo del representante legal
    nal = models.CharField('nacionalidad', max_length= 25, null=False, blank= False) # nacionalidad
    fch_ini = models.DateField('fecha de inicio de la institución', auto_now = False)  # fecha de inicio de la institución
    fch_reg = models.DateField('fecha de registro de la institución en al plataforma', auto_now=False)  # fecha de registro de la institución en al plataforma
    tipo_inst = models.IntegerField('Tipo de institución o entidad', choices = TIPO_NUIP_CO, default= 0, null=False) # Tipo de institución o entidad. Ver diccionario TIPO_INS
    sector = models.IntegerField('sector de desempeño de la entidad o institución ', choices= SECTOR_ECO, default= 0) # sector de desempeño de la entidad o institución. Ver Diccionario SECTOR_ECO
    dir = models.TextField('direccion sede administrativa', null=False, blank= False) # direccion sede administrativa
    url_imag = models.URLField('url de la imagen institucional o logo', blank=False, null=False) # url de la imagen institucional o logo.
    zona_hor = models.CharField('Zona Horario internacional', max_length=60, null=False, blank=False) #Zona Horario internacional

    class Meta:
        verbose_name = 'usui_inf_inst'
        verbose_name_plural = 'usui_inf_insts'


class usui_inf_contac(models.Model):

    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False)  # identificador de usuario institucional
    ind_nal = models.CharField('Indicativo telefónico de país', max_length=5, null=False, blank=False) #Indicativo telefónico de país
    tel = models.CharField('Número de telefono fijo', max_length=20, null=False, blank=False) #Número de telefono fijo del usuario Institucional
    cel = models.CharField('Número de telefono móvil', max_length=20, null=False, blank=False) #Número de telefono móvil del usuario Institucional
    email = models.EmailField('correo ', max_length=40, null=False, blank=False) # dirección de correo electrónico de información y contacto
    cod_post = models.PositiveSmallIntegerField('código postal ', default= 8) # Número de código postal
    ls_ha = models.IntegerField(choices= HORARIO, blank=False, default=0, null=False) #Listado de Horario de atención [día,hora ini, hora fin]
    web = models.URLField(' dirección de página web o blog institucional', max_length=60, null=False, blank=False) # dirección de página web o blog institucional
    dir_pri = models.TextField('Dirección de sede principal (país, ciudad, dir. ', null=False, blank=False) # Dirección de sede principal (país, ciudad, dir)

    class Meta:
        verbose_name = 'usui_inf_contac'
        verbose_name_plural = 'usui_inf_contacs'

class usui_red_social(models.Model): #relacion de listado de red social
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False)
    id_red_social = models.ForeignKey(red_soc, on_delete=models.CASCADE, null=False, blank=False)

class usui_inf_acad(models.Model):
    # Clase que almacena y procesa la información académica del usuario
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
    nivelform = models.IntegerField('Nivel de formacion ',choices=TIPO_FORM_CO, default = 0, null=False, blank=False) # me indica la formacion que tiene el usuario

    class Meta:
        verbose_name = 'usui_inf_acad'
        verbose_name_plural = 'usui_inf_acads'

class prog_ofer(models.Model):
    #clase que almacena la información de los programas ofertados a cargo de un usuario Institucional
    id_prog = models.AutoField(primary_key=True) # identificado único de programa.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # Id del usuario institucion .
    tipo_form = models.IntegerField(choices=TIPO_FORM_CO, default= 0, null=False, blank=False) #tipo de formación ver diccionario TIPO_FORM
    fch_ini = models.DateField('fecha de inscripcion', auto_now=False) #Incripciones
    fch_fin = models.DateField('fecha de Cierre de la inscripcion', auto_now=False) #Cierre de Inscripciones
    certif = models.BooleanField('Posee certificado', default= True)
    nal = models.CharField('Pais: ', max_length= 30, null=False, blank=False) #país
    ciudad =models.CharField('Ciudad ', max_length=40, null=False, blank=False)
    mod = models.IntegerField('MODALIDAD', choices=MODALIDAD, default = 0, null=False, blank=False) # modalidad
    num_est = models.PositiveSmallIntegerField('cantidad d estudiantes ', default=5 ) #Cantidad de Estudiantes
    dur = models.PositiveSmallIntegerField('Número total de horas', default= 4) #Número total de horas académicas del programa
    dur_sem = models.PositiveSmallIntegerField('Número total de semestres', default=4) #Número total de semestres del programa
    nom_prog = models.CharField('Nombre del Programa', max_length=30, null=False, blank=False) #Nombre del Programa
    acred = models.BooleanField('El programa se encuentra acreditado', default = True) #El programa se encuentra acreditado
    ven_acrd = models.PositiveSmallIntegerField('Año de vencimiento de la acreditación', default = 5) #Año de vencimiento de la acreditación
    url_prog = models.URLField('sitio web donde se puede localizar el programa', max_length=80, null=False, blank=False) #Url del documento o sitio web donde se puede localizar el programa

    class Meta:
        verbose_name = 'prog_ofer'
        verbose_name_plural = 'prog_ofers'

class usuo_prog_ofer(models.Model): #Listado de id de programas ofertados por la entidad o Institución.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE ) # identificador unico
    id_prog_ofer = models.ForeignKey(prog_ofer, on_delete=models.CASCADE, default = 0) # identificador unico

class usui_inf_inv(models.Model): #esta ya no seria buena
    # Clase que almacena y procesa la información académica del usuario
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
#    ls_pry_inv = [] #Listado de id de proyectos de investigación vinculados a la entidad o Institución.
#    ls_prod_inv = [] #Listado de id de productos de investigación vinculados a la entidad o Institución.


class conv_inv(models.Model):
    #clase que almacena la información de los programas ofertados a cargo de un usuario Institucional
    id_conv = models.AutoField(primary_key=True)  # identificado único de convocatoria.
    id_usui = models.ForeignKey(usui,on_delete=models.CASCADE, null=False, blank=False) # Id del usuario institucion .
    val_min = models.IntegerField() #valor mínimo
    val_max = models.IntegerField()#valor máximo
    fch_ini = models.DateField('Fecha de inicio Incripciones: ', auto_now=False) #Fecha de inicio Incripciones
    fch_fin = models.DateField('Fecha de Cierre de Inscripciones: ', auto_now=False) #Fecha de Cierre de Inscripciones
    pltf = models.BooleanField('Se puede registrar desde la plataforma: ', null=False, default =False, blank=False) #Se puede registrar desde la plataforma.
    nal = models.CharField('Pais ', null=False, blank=False, max_length=30) #país
    ciudad = models.CharField('Ciudad ', null=False, blank=False, max_length=30)
    mod = models.IntegerField('Modalidad ', null=False, blank=False, choices=MODALIDAD, default=0) # modalidad
    und_acdm = models.CharField('Nombre de la unidad académica ', max_length= 60, null=False, blank= False) #Nombre de la unidad académica o dependencia encargada de la convocatoria
    resp = models.CharField('Nombre de la persona responsable ', max_length= 60, null=False, blank= False) #Nombre de la persona responsable de la convocatoria.
    correo = models.EmailField('Correo ', null=False, blank=False) #correo electrónico para informacion
    nom_conv =  models.CharField('Nombre de la convocatori ', max_length= 60, null=False, blank= False)  #Nombre de la convocatoria
    url_conv = models.URLField('sitio web donde se puede localizar los términos de al convocatoria', max_length = 80, blank=False, null=False) #Url del documento o sitio web donde se puede localizar los términos de al convocatoria.
    url_insc = models.URLField('Url del formulario de inscripción', max_length = 80, blank=False, null=False) #Url del formulario de inscripción.

    class Meta:
        verbose_name = 'conv_inv'
        verbose_name_plural = 'conv_invs'

class rl_usui_usugr(models.Model): # relacion de Listado de id de grupos de inv. vinculados a la entidad o Institución.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
    ls_usugr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank=False) # identificador unico #Listado de id de grupos de inv. vinculados a la entidad o Institución.

class rl_usui_usu(models.Model): #Listado de id de usuarios vinculados a la entidad o Institución.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
    ls_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)

class rl_usui_conv_inv(models.Model):  #relacion Listado de id de convocatorias de investigación vinculados a la entidad o Institución.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
    ls_conv_inv = models.ForeignKey(conv_inv, on_delete=models.CASCADE, null=False, blank=False)

class app_reg_ins(models.Model):

    app_reg_ins = models.AutoField(primary_key = True)  # identificador unico para App Registro de Instituciones
    id_aplicacion_administrador =  models.ForeignKey(mod, on_delete=models.CASCADE, null=False, blank =False) # Identificador único ddel modulo administrador
    nomb_app_reg_ins = models.CharField('Nombre  ', max_length=20, null=False, blank = False)  # nombre de la App Registro de Instituciones
    desc_app_reg_ins = models.CharField('Descripcion  ', max_length=20, null=False, blank = False)  # descripcion de la App Registro de Instituciones
    status_app_reg_ins = models.BooleanField('Activo ', default=False)# estatus de la App Registro de Instituciones

    class Meta:
        verbose_name = 'app_reg_ins'
        verbose_name_plural = 'app_reg_inss'
