from django.db import models
from modadm.app_modadm.models import *
from modcons.app_cons.func import *
from .models import *

#Diccionario de información de instalación de aplicación
INF_APP = [
    ['Titulo', "App Registro de Usuario Individual"],
    ['Descripción',"aplicación para el registro de la información de usuario individual"],
    ['url_documento','doc'],
    ['url_instal','modadm/app_regusu'],
    ['url_plantilla','ini_regusu_adm.html'],
    ['Nombre_url','ini_regusu'],
    ['Versión aplicación','0.7.0'],
    ['id_mod', 0],
    ['Versión_módulo', 'prueba'],
    ['estado', 'en Desarrollo'],
    ['instalada', True],
    ['visible', True]
    ]

ROL_APP = {
    (0, ''),
    (1, ''),
    (1, ''),
    (1, ''),
    (1, '')
}
#Tipos de números de identificación personal
TIPO_NUIP_CO = [
    ('Cédula', 'Cédula'),
    ('Tarjeta de identidad', 'Tarjeta de identidad'),
    ('Cédula de Extranjería', 'Cédula de Extranjería'),
    ('Pasaporte', 'Pasaporte'),
    ('Permiso de Residencia', 'Permiso de Residencia'),
    ]

#Tipos de número de Único de Identificación Institucional
TIPO_NUII_CO = [
    (0,'NIT'), #Número de Identificación tributaria (Colombia)
    (1,'RUT') #Registro Único Tributario.
    ]

#Tipos de Identidad de Género   
GENERO = [
    (0,'No informa'),
    (1,'Femenino'),
    (2,'Masculino'),
    (3,'Intergénero'),
    (4,'Transgénero'),
    (5,'Sisgénero'),
    (6,'Neutro'),
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
    (1,'Reconocido Inst.'), #Grupo que además de registrado está vinculado y reconocido por una Institución o Entidad.
    (2,'Reconocido COLC'), #Grupo que además de registrado está vinculado y reconocido por Colciencias.
    (3,'Semillero de Inv.'), #Grupo que está reconocido como semillero por una Institución o Entidad.
    (4,'Comunidad'), #Grupo de comunidad de conocimiento abierto o libre.
    (5,'Grupo de Trabajo') #Grupo de trbajo informal que se establecen para realizar desarrollos temáticos. Son grupos de comunidades abiertas con vinculación temporal sin reconocimeinto oficial.
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

RED_SOC =[
    (0,'Google Académico'),
    (1,'Linkedin'),
    (2,'Skype'),
    (3,'WhatsApp'),
    (4,'GitHub'),
    (5,'Facebook'),
    (6,'Telegram'),
    (7,'Twitter'),
    (8,'Instagram'),
    (9,'ResearchGate'),
    (10,'Mendeley'),
    (11,'ORCID'),
    (12,'Zotero'),
    (13,'SlideShare'),
    (14,'otra') 
    ]

USO_RED=[
    (0,'frecuente'),
    (1,'moderado'),
    (2,'poco frecuente'),
    (3,'inactivo')
]
#Tipo de discapacidad
TIPO_DISC=[
    (0,'Discapacidad física'),
    (1,'Discapacidad auditiva'),
    (2,'Discapacidad visual'),
    (3,'Sordoceguera'),
    (0,'Discapacidad intelectual'),
    (0,'Discapacidad psicosocial (mental)'),
    (0,'Discapacidad múltiple')
]
#clases independientes
class discap(models.Model):
    id_disc = models.AutoField(primary_key = True) # identificador de usuario
    tipo_disca = models.IntegerField('Tipo de discapacidad ',choices=TIPO_DISC, null=False, blank = False)  # número único de identificación personal sin puntos
    nom_disc = models.CharField('Denominación de la discapacidad', max_length=120, null=False, blank=False)
    desc_disca = models.CharField('Descripción', max_length=30, null=False, blank = False)  # tipo de Número de identificación personal

    class Meta:
        verbose_name = 'discapacidad'
        verbose_name_plural = 'discapacidads'

    def __str__(self):
        return '{}'.format(self.tipo_disca)

class habil(models.Model):
    #clase que almacena la información de tipos de habilidad
    id_hab = models.AutoField(primary_key = True)
    nom_hab = models.CharField('Nombre de la habilidad', max_length=20, null=False, blank = False)  #Nombre de la habilidad
    desc = models.CharField('Descripción de la Habilidad', max_length=20, null=False, blank = False)  #Descripción de la Habilidad

    class Meta:
        verbose_name = 'habilidades'
        verbose_name_plural = 'habilidadess'

#clases dependientes
class usu_inf_pers(models.Model):
    # Registra la información personal del usuario individual
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE, null=True, blank=True) # identificador de usuario
    nuip = models.CharField('Número único de identificación personal ', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    tipo_nuip = models.CharField( max_length=30, choices = TIPO_NUIP_CO, default =0, null=False, blank = False) # tipo de Número de identificación personal
    #nombres = models.CharField(usu.first_name, max_length=30, null=True, blank = False)
    #apelllidos = models.CharField(usu.last_name, max_length=30, null=True, blank = False)
    nal = models.CharField('Nacionalidad ', max_length=50, null=False, blank = False) # nacionalidad
    fch_naci = models.DateField('Fecha de nacimiento', auto_now = False)   # fecha de nacimiento de usuario
    gene = models.IntegerField('Género', choices = GENERO, default = 0, null=True, blank = True)  #genero del usuario
    ocup = models.CharField('Ocupacion', max_length=50, null = False, blank = False) # ocupación del usuario
    dir_res = models.CharField('Direccion de Residencia', null=False, blank = False, default='Colombia, Bogotá, Carrera 9 n.° 51-11') # direccion de residencia
    disc = models.BooleanField('¿Es una persona en condición de discapacidad?', default=False) # Es una persona en condición de discapacidad
    tipo_discap = models.ForeignKey(discap, on_delete=models.SET_NULL, null=True, blank =True)  # Tipo de  discapacidad tabla de discapacidad
    url_imag = models.URLField('url de la imagen personal.', null=True, blank=True)  # url de la imagen personal.
    zona_hor = models.CharField('Zona Horaria ', max_length=100, null=True, blank = True, default='GMT-5') #Zona Horario internacional
    archi = models.BooleanField(null = False, blank = False, default = False)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'usu_inf_pers'
        verbose_name_plural = 'usu_inf_perss'

class usu_inf_contac(models.Model):
    # Modelo apra el registro d ela información de contacto pública del usuario
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE)  # identificador de usuario
    correo = models.EmailField('Correo personal',max_length = 254, null=True, blank = True)
    correo_ins = models.EmailField('Correo institucional',max_length = 254, null=False, blank = False)
    ind_pais = models.IntegerField('Indicativo del país(Sólo números)', null=False, blank = False)  # número de indicativo
    tel = models.IntegerField('Número telefónico Móvil (Sólo números)', null=False, blank = False)  # número telefónico
    tel_of = models.IntegerField('Número telefónico Oficina (Sólo números)', null=True, blank = True)  # número telefónico
    tel_of_ext = models.IntegerField('Extensión Número telefónico Oficina (Sólo números)', null=True, blank = True)  # Estensión número telefónico
    wa = models.CharField('Número de WhatsApp',  max_length=30, null=True, blank = True) # Número de WhatsApp
    cod_post = models.PositiveSmallIntegerField('Número de código postal', null=True, blank =True)  # Número de código postal
    dias_aten = models.IntegerField(choices = DIAS, default = 0, null=False, blank = False) # Días de la semana que se atienden requerimientos de estudiantes o docentes
    horario_aten =  models.IntegerField(choices = HORARIO, default = 0, null=False, blank = False) #Listado de Horario de atención [día,hora ini, hora fin]
    web = models.URLField('dirección de página web o blog personal', null=False, blank=False) # dirección de página web o blog personal
    dir_offi = models.CharField('Dirección de Ofiina (país, ciudad, dir) ', max_length=100, null=False, blank = False) # Dirección de Oficina (país, ciudad, dir)
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'usu_inf_contac'
        verbose_name_plural = 'usu_inf_contacs'

class usu_form_acad(models.Model):

    id_fa =  models.AutoField(primary_key = True) #Id de formación académica
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE)  # identificador de usuario
    instit = models.CharField('Nombre de la institucion ', max_length=25, null=False, blank = False) # Nombre de la institucion académica donde curso la formación
    tipo_form = models.IntegerField(choices = TIPO_FORM_CO, default = 0, null=False, blank = False) #tipo de formación ver diccionario TIPO_FORM
    fch_ini = models.DateField('Fecha de Inicio', auto_now = False)#fecha de inicio de la formación
    fch_fin = models.DateField('Fecha de Fin', auto_now = False)# Fecha final de la formación
    certif = models.BooleanField('Formación Certificada', default=True) #La fomración se encuentra certificada o no.
    id_lugar= models.IntegerField('Identificador único de lugar', default=0, null=False, blank = False) #identificador de lugar clave valor de lugares (País, Estado, ciudad)
    mod =  models.IntegerField(choices = MODALIDAD, default = 0, null=False, blank = False) # modalidad
    tit = models.CharField('Titulo obtenido ', max_length=120, null=False, blank = False) # Título obtenido
    menc =  models.BooleanField('Mención de Honor', default= False; null=False, blank = False)  # Mensión de honor
    url_cert = models.CharField('Dirección URL del certificado', null=True, blank = True) # Dirección o enlace público del certificado
    token = models.CharField('Token de validación', null=False, blank = False)  #Token de validación electrónica de certificación de la formación

    class Meta:
        verbose_name = 'form_acad'
        verbose_name_plural = 'form_acads'

class usu_red_soc(models.Model):
    #información de redes sociales del usuario individual
    id_red = models.AutoField(primary_key = True)
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    red_def = models.IntegerField(choices=RED_SOC, default=0)
    nombre_red = models.CharField('Nombre de Otra red ', max_length=50, null=True, blank =True)
    alias =  models.CharField('Alias o (Nick) de usuario', max_length=50, null=True, blank = True)  #nick o dirección de usuario
    url = models.URLField('Url de página principal de usuario(a) dentro de la red.', null=True, blank=True) #Url de página principal dentro de la red.
    uso = models.IntegerField(choices=USO_RED, null=True, blank = True)  #Uso de la red (frecuente:0; moderado:1; poco frecuente:2; inactivo:3)
    pub = models.BooleanField('¿La información es de acceso público?', default=False)  #Acceso público de información de red sí (True) no (False)
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'red social'
        verbose_name_plural = 'redes sociales'

class usu_empleo(models.Model):
    #Clase que almacena la información de empleos del usuario
    id_empl = models.AutoField(primary_key = True)
    id_usu = models.OneToOneField(usu, on_delete=models.SET_NULL, null=False, blank =False)
    instit = models.CharField('Nombre de la institucion o empresa ', max_length= 100, null=False, blank = False) # Nombre de la institucion académica donde curso la formación
    nom_cargo = models.CharField('Nombre del Cargo ', max_length=100, null=False, blank = False)  #Nombre del Cargo
    fch_ini = models.DateField('fecha de inicio', auto_now = False,null=False, blank = False)
    fch_fin = models.DateField('fecha de Fin', auto_now = False, null=False, blank = False)
    certif = models.BooleanField('Experiencia certificada', default=False)
    nal = models.CharField('Pais ', max_length=20, null=False, blank = False)  #país
    ciudad = models.CharField('Ciudad ', max_length=20, null=False, blank = False)
    tipo_contr =  models.IntegerField(choices = TIPO_CONTR_CO, null=False, blank = False, default = 0)
    tit = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False)  # Título obtenido
    menc = models.CharField('Mensión de honor ', max_length=20, null=False, blank = False)  # Mensión de honor
    token = models.CharField('Token de validación electrónica  ', max_length=20, null=False, blank = False)  #Token de validación electrónica de certificación de la formación
    ret = models.CharField(' Motivo del retiro ', max_length=20, null=False, blank = False)  # Motivo del retiro
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'empleos'
        verbose_name_plural = 'empleoss'

class usu_curs_dict(models.Model):
    #clase que almacena la información de cursos dictados a cargo de un usuario
    id_cd = models.AutoField(primary_key = True)    #Id de formación académica
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE, null=False, blank =False)
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
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    class Meta:
        verbose_name = 'curs_dict'
        verbose_name_plural = 'curs_dicts'

class usu_valid_hab(models.Model):
    #clase que procesa la información de validación social de habilidades
    id_usu = models.OneToOneField(usu, on_delete=models.SET_NULL, null=False, blank =False) # Identificador del Usuario que registra la habilidad
    id_hab = models.ForeignKey(habil, on_delete=models.SET_NULL, null=False, blank =False) #Identificador de la habilidad que se va a validar
    id_usu_val = models.ForeignKey(usu, on_delete=models.SET_NULL, null=False, blank =False)  #Identificador del Usuario que valida la habilidad
    id_esc = models.IntegerField('id de la escala de validación', max_length=20, null=False, blank = False) #Identificador de la escala de validación
    val = models.CharField('Valor', max_length=20, null=False, blank = False) #Valor dentro del rango de la escala de validación
    archi = models.BooleanField(null = False, blank = False, default = 0)#Si el registro está archivada (antes de proceder a borrarlo de la base de datos)
    
    #nota como realizp el dato val, id esc, id:usu_val
    class Meta:
        verbose_name = 'validación de habilidad'
        verbose_name_plural = 'validaciones de habilidades'

class rl_usu_rol(models.Model):
    # Relaciona al usuarios con las aplicaciones a las que puede acceder y los roles de aplicación
    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de sistema
    id_roles = models.ForeignKey(rol, on_delete=models.CASCADE, null=True, blank=True) # id de rol de aplicación al que tiene asignación.
    #[[0,0]] Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza. clave foranea a roles .. muchos
    #rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador de rol de sistema.
    #    app_act = models.ForeignKey(listado_aplicativo,on_delete=models.CASCADE, null=False, blank =False) # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión, app_mod

    class Meta:
        verbose_name = 'Relación Usuario-Rol'
        verbose_name_plural = 'Relaciones Usuario-Roles'
