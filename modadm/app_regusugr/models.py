from django.db import models
from modadm.app_modadm.models import *
from modadm.app_regusu.models import *

#Diccionario de información de instalación de aplicación

INF_APP = [
    ['nom','app_regusugr'],
    ['titulo', "App Registro de Usuario grupo"],
    ['desc',"aplicación para el registro de la información de usuario grupo"],
    ['url_doc','doc'],
    ['url_instal','modadm/app_regusugr'],
    ['url_pl','ini_regusugr_adm.html'],
    ['nom_url','ini_regusugr'],
    ['version','0.7.0'],
    ['ver_mod', 'prueba'],
    ['activo', False],
    ['instalada', True],
    ['visible', True],
    ['externa', False],
    ['tipo_app', 'SIGEPI-BASE'],
    ['ico','#']
    ]

    
#clase de información de usuario grupo.
class usugr_base(models.Model):
    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False, default = 0) # identificador de usuario grupo
    cod_gr = models.PositiveSmallIntegerField(' código único de identificación del grupo', default=8) # código único de identificación del grupo
    tipo_gr = models.IntegerField(choices = TIPO_GR_INV, null = False, blank = False, default = 0) # tipo de grupo, ver diccionario TIPO_GR_INV
    nal = models.CharField('Nacionalidad', max_length=40, null=False, blank = False)  # País principal con el que se identifica el grupo.
    dir_ofi = models.CharField('Direccion de correspondencia ', max_length=40, null=False, blank = False)  # direccion de correspondencia.
    estado = models.IntegerField(choices = ESTADO_DLLO_GR, null = False, blank = False, default=0) # Estado de desarrollo del Grupo. Ver diccionario ESTADO_DLLO_GR
    url_imag = models.URLField('url de la imagen o logo del grupo', null=False, blank=False)  # url de la imagen o logo del grupo.
    zona_hor =  models.CharField('Zona Horaria', max_length=40, null=False, blank = False) #Zona Horaria internacional
    id_gr_padre =  models.CharField('grupo padre', max_length=40, null=False, blank = False, default = 0) #Identificador del grupo padre si lo tiene, de lo contrario es el valor es cero

    class Meta:
        verbose_name = 'usugr_inf_gr'
        verbose_name_plural = 'usugr_inf_grs'

#clase que registra la información de contacto del usuario grupo.
class usugr_contac(models.Model):
    id_usugr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)   # identificador de usuario grupo
    ind_nal = models.CharField('Nacionalidad ', max_length=20, null=False, blank = False)  #Indicativo telefónico de país
    tel = models.CharField('Telefono oficina ', max_length=20, null=False, blank = False)  #Número de telefono fijo de oficina del grupo
    cel = models.CharField('N° Celular ', max_length=20, null=False, blank = False)  #Número celular de contacto del grupo.
    email = models.EmailField('correo', null = False, blank = False) # dirección de correo electrónico del grupo.
    cod_post = models.IntegerField('Codigo Postal ') # Número de código postal de oficina
    ls_hr = models.IntegerField( choices = HORARIO, default =0, null=False, blank = False) #Listado de Horario de reunión semanal[día,hora ini, hora fin]
    web =  models.URLField('página web o blog del grupo ', null=False, blank=False)  # dirección de página web o blog del grupo
    dir_offi = models.TextField('Direccion e oficina', null=False, blank = False) # Dirección de Oficina (país, ciudad, dir)

    class Meta:
        verbose_name = 'usugr_inf_contac'
        verbose_name_plural = 'usugr_inf_contacs'

# Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles
class usugr_apps(models.Model):
    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de grupo
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
    # [0,] id_rol; [,0] id_usu quien autoriza.
    #rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   # Identificador de rol de sistema.
    #app_act = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank =False)  # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)

    class Meta:
        verbose_name = 'usugr_inf_apps'
        verbose_name_plural = 'usugr_inf_appss'

#Clase que registra las etapas de los grupos de investigación en el sistema.
class usugr_etapa(models.Model):
    id_etp = models.AutoField(primary_key = True) #Identificador único de la etapa del grupo de investigacion.
    id_usugr=models.OneToOneField(usugr,on_delete=models.SET_NULL, null=True, blank =True)
    nom =  models.CharField('Nombre del grupo  ', max_length=20, null=False, blank = False)  #Nombre del grupo (puede ser el qeu tuvo en algún momento, se pueden registrar varios nombres según al trayectoria del grupo)
    fch_ini_nom = models.DateField('Fecha en la que se creó el grupo ', auto_now = False) #Fecha en la que se creó el grupo con ese nombre, o en el que cambió a ese nombre.
    fch_fin_nom = models.DateField('Fecha en la que se terminó el grupo', auto_now = False) #Fecha en la que se terminó el grupo con ese nombre, o en el que dejó de usar ese nombre.
    vig = models.BooleanField('El grupo se encuentra vigente en esta etapa', default=True) #El nombre se encuentra vigente, es el que se usa actualmente el grupo.
    sigla = models.CharField('Sigla con la que se identificó(a) el grupo ', max_length=20, null=False, blank = False)  #Sigla con la que se identificó(a) el grupo en esta etapa.
    url_arch = models.URLField('URL del sitio web ', null= False, blank=False) #Url de sitio web o repositorio virtual donde repose el archivo(memoria o sitio web) del grupo.
    gruplac = models.URLField('Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.', null = 'False', blank = 'False') #Url del GrupLac del grupo de Investigación con ese nombre si se está registrado en esa plataforma.

    class Meta:
        verbose_name = 'etapa del grupo'
        verbose_name_plural = 'etapas de los grupos'

    def __str__(self):
        return '{}'.format(self.nom)

#clase que almacena la información de cursos ofertados o procesos de formación realizados por parte de un usuario grupo
class usugr_form(models.Model):
    id_usui = models.OneToOneField(usui,on_delete=models.SET_NULL, null=True, blank = True)  # Nombre de la institucion académica que oferta el curso o evento académico.
    nom_curs = models.CharField('Nombre del Curso o evento académico. ', max_length=30, null=False, blank = False) #Nombre del Curso o evento académico.
    tipo_form = models.IntegerField(choices = TIPO_FORM_GR, null=False, blank = False, default = 0)  #tipo de formación ver diccionario TIPO_FORM_GR
    fch_ini = models.DateField('fecha Inicio', auto_now = False) #fecha de inicio de la formación
    fch_fin = models.DateField('fecha Fin ', auto_now = False) #fecha de finalización de la formación
    certif = models.BooleanField('¿Certificado?', default=True) #¿la formación es certificada?
    nal =models.CharField('Pais: ', max_length=30, blank = False, null = False) #país o nación donde se realiza la formación
    ciudad = models.CharField('Ciudad ', max_length=30, blank = False, null =False)# ciudad (principal si es virtual) donde tiene o tuvo lugar la formación
    modal =  models.IntegerField(choices = MODALIDAD, null=False, blank = False, default=0) # modalidad
    num_est = models.PositiveSmallIntegerField('Cupo de Estudiantes o asistentes', default = 5) #Cupo de Estudiantes o asistentes
    dur = models.PositiveSmallIntegerField('Número total de horas académicas del curso', default = 5) #Número total de horas académicas del curso o evento académico
    mun_ciclos = models.PositiveSmallIntegerField('cuántas veces se realizó o realizará el curso o evento', default =1) #Número de ciclos del curso "cuántas veces se realizará el curso o evento"
    url_prog = models.URLField('página web o blog del grupo ', null=True, blank=True) #Url del documento o sitio web donde se puede localizar el programa del curso o el evento académico.
    inscr = models.URLField('Url del formulario de inscripción.', null =True, blank = True) #Url del formulario de inscripción.

    class Meta:
        verbose_name = 'Fromación'
        verbose_name_plural = 'Formaciones'

#Clase que registra la información de redes sociales públicas del grupo
class usugr_red_soc(models.Model):  # Listado de objetos de redes sociales
     #información de redes sociales del usuario grupo
    id_red = models.AutoField(primary_key = True)
    id_usugr = models.OneToOneField(usugr, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario grupo
    red_def = models.IntegerField(choices=RED_SOC, default=0) #red desde el listado por defecto
    nombre_red = models.CharField('Nombre de Otra red ', max_length=50, null=True, blank =True) # Nombre de otra red
    alias =  models.CharField('Alias o (Nick) de usuario(a)', max_length=50, null=True, blank = True)  #nick o dirección de usuario grupo
    url = models.URLField('Url de página principal de usuario(a) dentro de la red.', null=True, blank=True) #Url de página principal dentro de la red.
    uso = models.IntegerField(choices=USO_RED, null=True, blank = True)  #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('¿La información es de acceso público?', default=False)  #Acceso público de información de red sí (True) no (False)
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'red social de grupo'
        verbose_name_plural = 'redes sociales de los grupos'

#Clase que registra los datos de investigación de un integrante grupo no registrado en el sistema.
class usugr_usu_nr(models.Model):
    id_usu_nr = models.AutoField(primary_key = True)  # identificador unico
    nombres = models.CharField('Nombres del integrante no registrado(a).', max_length=40, null=False, blank = False) # Nombres del integrante no registrado(a).
    apellidos = models.CharField('Apellidos del integrante no registrado(a).', max_length=40, null=False, blank = False)  # Apellidos del integrante no registrado(a).
    #rol =  models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   #Rol de investigación que se desempeña actualmente
    cvlac =  models.URLField('URL del CVlac del investigador(a).', null=False, blank=False)  #URL del CVlac del investigador(a).
    orcid = models.CharField('ID de ORCID del investigador(a).', max_length=20, null=False, blank = False)  #ID de ORCID del investigador(a).
    ggl = models.URLField('URL Google académico del investigador(a)', null=False, blank=False)  #URL Google académico del investigador(a).

    class Meta:
        verbose_name = 'usu_nr'
        verbose_name_plural = 'usu_nrs'

    def __str__(self):
        return '{}'.format(self.nombres)

## Relación entre entidades del modelo usugr ##
#relacion de Listado histórico de etapas que ha tenido el grupo.
class rl_usugr_etp(models.Model): 
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_etp = models.ForeignKey(usugr_etapa, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'Relación Usuario grupo con Etapa del grupo'
        verbose_name_plural = 'Relaciones Usuarios grupo con Etapas de los grupos'

#Relación de integrantes del grupo registrados en el sistema.
class rl_usugr_ls_usu(models.Model):
    id_gr = models.ForeignKey(usugr, on_delete=models.SET_NULL, null=True, blank =True)
    ls_int_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =True)

    class Meta:
        verbose_name = 'Integrante de Grupo'
        verbose_name_plural = 'Integrantes de Grupos'

#Relación de integrantes no registrados en el sistema con los grupos.
class rl_usugr_ls_usu_nr(models.Model):
    id_gr = models.OneToOneField(usugr, on_delete=models.SET_NULL, null=True, blank =True)
    ls_int_nr = models.OneToOneField(usugr_usu_nr, on_delete=models.SET_NULL, null=True, blank =True)

    class Meta:
        verbose_name = 'Integrante no registrado de Grupo'
        verbose_name_plural = 'Integrantes no registrados de Grupos'

#Relación de usuarios(as) individuales formados por los grupos.
class rl_usu_form(models.Model):  # listado de id procesos de formación realizados
    id_usu = models.ForeignKey(usu, on_delete=models.SET_NULL, null=True, blank =True)
    id_red_soc = models.ForeignKey(usugr_red_soc, on_delete=models.SET_NULL, null=True, blank =True)

