from django.db import models
from django.contrib.auth.models import User
#from modadm.App_modadm.models import *
from modadm.App_regusu.models import *

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

class usugr(models.Model): #ojo falta listado de productos y protyectos vinculados al grupo
    #Clase que registra la información básica del usuario grupo en el sistema.

    id_gr = models.AutoField(primary_key = True) #Identificador único del grupo de investigacion.
    passgr  = models.CharField('Descripcion ', max_length=20, null=False, blank = False)  # contraseña para el usuario grupo (diferente a la del usuario del sistema)
    id_usu_admin = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)  #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_gr)
    #id_rol_app = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador del Rol de Usuario grupo dentro de la app_reg_gr
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
    #rol =  models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   #Rol de investigación que se desempeña actualmente
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

    class Meta:
        verbose_name = 'rel_usugr_ls_etp'
        verbose_name_plural = 'rel_usugr_ls_etps'


class rel_usugr_ls_usu(models.Model):#Listado de id_usu integrantes del grupo registrados en el sistema.
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_int_usu = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'rel_usugr_ls_usu'
        verbose_name_plural = 'rel_usugr_ls_usus'

class rel_usugr_ls_usu_nr(models.Model):#Listado de id de integrantes no registrados en el sistema.
    id_gr = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)
    ls_int_nr = models.ForeignKey(usu_nr, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'rel_usugr_ls_usu_nr'
        verbose_name_plural = 'rel_usugr_ls_usu_nrs'


class usugr_inf_apps(models.Model):
    # Clase que almacena y procesa la información de la aplicaciones de usuario institucional y sus respectivos roles

    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de grupo
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
    # [0,] id_rol; [,0] id_usu quien autoriza.
    #rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)   # Identificador de rol de sistema.
    #app_act = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank =False)  # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)

    class Meta:
        verbose_name = 'usugr_inf_apps'
        verbose_name_plural = 'usugr_inf_appss'

class rl_usugr_inf_rol_Actual(models.Model): # identificador del rol actual.
    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de grupo
    #rol_act = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # identificador del rol actual.

class usugr_inf_gr(models.Model):
    #clase de información de usuario grupo.
#preguntar identificador de grupo padre ?
    id_usugr =  models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False, default = 0) # identificador de usuario grupo
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
    cod_post = models.IntegerField('Codigo Postal ') # Número de código postal de oficina
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


# class usugr_inf_acad(models.Model): #ojo dejar o quitar, y pry y prod no las inclui porque no la tengo en modelos
#     #Clase que almacena y procesa la información de actividades académicas y oferta formativa del usuario grupo
#    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)  # identificador único de grupo
#     prod = [] #Listado de id de productos de investigación vinculados al id usugr
#     pry_inv = [] #Listado de id de proyectos de investigación vinculados al id usugr

#    class Meta:
#        verbose_name = 'usugr_inf_acad'
#        verbose_name_plural = 'usugr_inf_acads'


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

class rl_usugr_form_acad_gr(models.Model):  # listado de id procesos de formación realizados
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)
    ls_form_gr = models.ForeignKey(form_acad_gr, on_delete=models.CASCADE, null=False, blank =False)

class rl_usugr_curs_ofer(models.Model):  ##listado de id cursos o eventos acadeḿicos ofertados por el grupo.
    id_usugr = models.ForeignKey(usugr_inf_gr, on_delete=models.CASCADE, null=False, blank =False)
    ls_cursofer =  models.ForeignKey(curs_ofer, on_delete=models.CASCADE, null=False, blank =False)
#    ls_prod = [] #Listado de id de productos de investigación vinculados al id usugr

class app_reg_gr(models.Model):
    #Clase que contiene los objetos de la App Registro de Grupos
    id_app_reg_gr = models.AutoField(primary_key = True)
    nombres = models.CharField('Descripcion.', max_length=40, null=False, blank = False)
    #id_app = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False) # Identificador único de aplicacion por modulo _administrador

    class Meta:
        verbose_name = 'app_reg_gr'
        verbose_name_plural = 'app_reg_grs'
