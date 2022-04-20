from django.db import models
from modadm.App_modadm.models import *
from .models import *

#Tipo de rol dentro de la plataforma
TIPO_ROL = [
    (0,'Sistema'),
    (1,'Módulo'),
    (2,'Aplicación'),
    (3,'Extensión'),
    (4,'Otro')
    ]

ROL_APP = {
    (0, 'Adm_App'),
    (1, 'Adm_Usu'),
    (1, 'Docente'), #externo, invitado, investigador
    (1, 'Estudiante'), #egresado, investigador
    (1, 'Invitado')
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
    ('Neutro','Neutro'),
    ('Femenino','Femenino'),
    ('Masculino','Masculino'),
    ('Intergénero','Intergénero'),
    ('Transgénero','Transgénero'),
    ('Sisgénero','Sisgénero'),
    ('Otro','Otro')
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


g_sis = Group.objects.get(name = 'Sistema')
g_admsis = Group.objects.get(name = 'Admin Módulo Administración')
g_appusu = Group.objects.get(name = 'Admin App Usuarios')
g_appgrp = Group.objects.get(name = 'Admin App Grupos')
g_appins = Group.objects.get(name = 'Admin App Instituciones')
g_admapps = Group.objects.get(name = 'Admin Aplicaciones')
g_ext =  Group.objects.get(name = 'Admin Extensión')
g_inv = Group.objects.get(name = 'Invitado')
g_admcons = Group.objects.get(name = 'Admin Módulo Consultas')

class usu_inf_apps(models.Model):
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) #id único de Usuario de sistema
    ls_roles =[[0,0]] #Listado de roles en aplicaciones y módulos autorizados por administradores de paltaforma
        # [0,] id_rol; [,0] id_usu quien autoriza. clave foranea a roles .. muchos
    #rol_sis = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)  # Identificador de rol de sistema.
#    app_act = models.ForeignKey(listado_aplicativo,on_delete=models.CASCADE, null=False, blank =False) # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión, app_mod

    class Meta:
        verbose_name = 'usu_inf_apps'
        verbose_name_plural = 'usu_inf_appss'

class rl_usu_inf_apps_rol(models.Model): #identificar el rol actual del usuario
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    #rol_act = models.ForeignKey(rol, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'rl_usu_inf_apps_rol'
        verbose_name_plural = 'rl_usu_inf_apps_rols'

class discapacidad(models.Model):
    id_disc = models.AutoField(primary_key = True) # identificador de usuario
    tipo_disca = models.CharField('Tipo de discapacidad ', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    desc_disca = models.CharField('Descripción', max_length=30, null=False, blank = False)  # tipo de Número de identificación personal

    v_disc = Permission.objects.get(codename='view_discapacidad')
    a_disc = Permission.objects.get(codename='add_discapacidad')
    c_disc = Permission.objects.get(codename='change_discapacidad')
    d_disc = Permission.objects.get(codename='delete_discapacidad')
    g_sis.permissions.add(v_disc,a_disc,c_disc,d_disc)
    g_admsis.permissions.add(v_disc,a_disc,c_disc,d_disc)
    g_appusu.permissions.add(v_disc,a_disc,c_disc,d_disc)
    g_appgrp.permissions.add(v_disc,a_disc,c_disc)
    g_appins.permissions.add(v_disc,a_disc,c_disc)
    g_admapps.permissions.add(v_disc,a_disc,c_disc)
    g_ext.permissions.add(v_disc,a_disc,c_disc)
    g_admcons.permissions.add(v_disc,a_disc,c_disc)
    class Meta:
        verbose_name = 'discapacidad'
        verbose_name_plural = 'discapacidads'

    def __str__(self):
        return '{}'.format(self.tipo_disca)

class usu_inf_pers(models.Model):
    
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=True, blank=True) # identificador de usuario
    nuip = models.CharField('Número único de identificación personal ', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    tipo_nuip = models.CharField( max_length=30, choices = TIPO_NUIP_CO, default =0, null=False, blank = False) # tipo de Número de identificación personal
    #nombres = models.CharField(usu.first_name, max_length=30, null=False, blank = False)
    #apelllidos = models.CharField(usu.last_name, max_length=30, null=False, blank = False)
    nal = models.CharField('Nacionalidad ', max_length=30, null=False, blank = False) # nacionalidad
    fch_naci = models.DateField('Fecha de nacimiento', auto_now = False)   # fecha de nacimiento de usuario
    mail = models.EmailField(max_length = 254, null=False, blank = False)
    telefono = models.CharField('Número telefónico', max_length=30, null=False, blank = False)  # número único de identificación personal sin puntos
    gene = models.CharField('Género', choices = GENERO, max_length=30, default = 0, null=False, blank = False)  #genero del usuario
    ocup = models.CharField('Ocupacion ', max_length=30, null = False, blank = False) # ocupación del usuario
    dir = models.CharField('Direccion ', max_length=100, null=False, blank = False) # direccion de residencia
    # discap = models.BooleanField('¿Es una persona en condición de discapacidad?', default=False) # Es una persona en condición de discapacidad
    # tipo_discap = models.ForeignKey(discapacidad, on_delete=models.CASCADE, null=True, blank =True)  # Tipo de  discapacidad tabla de discapacidad
    # url_imag = models.URLField('url de la imagen personal.', null=True, blank=True)  # url de la imagen personal.
    # zona_hor = models.CharField('Zona Horaria ', max_length=100, null=True, blank = True) #Zona Horario internacional

    v_usu_inf_pers = Permission.objects.get(codename='view_usu_inf_pers')
    a_usu_inf_pers = Permission.objects.get(codename='add_usu_inf_pers')
    c_usu_inf_pers = Permission.objects.get(codename='change_usu_inf_pers')
    d_usu_inf_pers = Permission.objects.get(codename='delete_usu_inf_pers')
    g_sis.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers,d_usu_inf_pers)
    g_admsis.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers,d_usu_inf_pers)
    g_appusu.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers,d_usu_inf_pers)
    g_appgrp.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers)
    g_appins.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers)
    g_admapps.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers)
    g_ext.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers)
    g_admcons.permissions.add(v_usu_inf_pers,a_usu_inf_pers,c_usu_inf_pers)

    class Meta:
        verbose_name = 'usu_inf_pers'
        verbose_name_plural = 'usu_inf_perss'

class usu_inf_contac(models.Model):

    id_usu = models.OneToOneField(usu, on_delete=models.CASCADE)  # identificador de usuario
    ind_nal = models.PositiveSmallIntegerField('Indicativo telefónico de país') #Indicativo telefónico de país
    cel = models.CharField('Número de telefono móvil del usuario',  max_length=30, null=False, blank = False) #Número de telefono móvil del usuario
    wa = models.CharField('Número de WhatsApp',  max_length=30, null=False, blank = False) # Número de WhatsApp
    email = models.EmailField('Correo electrocico',  max_length=30, null=False, blank = False)  # dirección de correo electrónico
    cod_post = models.PositiveSmallIntegerField('Número de código postal', null=False, blank =False)  # Número de código postal
    ls_ha =  models.IntegerField(choices = HORARIO,default = 0, null=False, blank = False) #Listado de Horario de atención [día,hora ini, hora fin]
    web = models.URLField('dirección de página web o blog personal', null=False, blank=False) # dirección de página web o blog personal
    dir_offi = models.CharField('Dirección de Ofiina (país, ciudad, dir) ', max_length=100, null=False, blank = False) # Dirección de Oficina (país, ciudad, dir)

    v_usu_inf_contac = Permission.objects.get(codename='view_usu_inf_contac')
    a_usu_inf_contac = Permission.objects.get(codename='add_usu_inf_contac')
    c_usu_inf_contac = Permission.objects.get(codename='change_usu_inf_contac')
    d_usu_inf_contac = Permission.objects.get(codename='delete_usu_inf_contac')
    g_sis.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac,d_usu_inf_contac)
    g_admsis.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac,d_usu_inf_contac)
    g_appusu.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac,d_usu_inf_contac)
    g_appgrp.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac)
    g_appins.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac)
    g_admapps.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac)
    g_ext.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac)
    g_admcons.permissions.add(v_usu_inf_contac,a_usu_inf_contac,c_usu_inf_contac)

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

    v_red_soc = Permission.objects.get(codename='view_red_soc')
    a_red_soc = Permission.objects.get(codename='add_red_soc')
    c_red_soc = Permission.objects.get(codename='change_red_soc')
    d_red_soc = Permission.objects.get(codename='delete_red_soc')
    g_sis.permissions.add(v_red_soc,a_red_soc,c_red_soc,d_red_soc)
    g_admsis.permissions.add(v_red_soc,a_red_soc,c_red_soc,d_red_soc)
    g_appusu.permissions.add(v_red_soc,a_red_soc,c_red_soc,d_red_soc)
    g_appgrp.permissions.add(v_red_soc,a_red_soc,c_red_soc)
    g_appins.permissions.add(v_red_soc,a_red_soc,c_red_soc)
    g_admapps.permissions.add(v_red_soc,a_red_soc,c_red_soc)
    g_ext.permissions.add(v_red_soc,a_red_soc,c_red_soc)
    g_admcons.permissions.add(v_red_soc,a_red_soc,c_red_soc)

    class Meta:
        verbose_name = 'red_soc'
        verbose_name_plural = 'red_socs'

class rl_usu_inf_red_social(models.Model): # relacion Listado de objetos de redes sociales
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_red = models.ForeignKey(red_soc, on_delete=models.CASCADE, null=False, blank =False)   # Listado de objetos de redes sociales

    class Meta:
        verbose_name = 'rl_usu_inf_red_social'
        verbose_name_plural = 'rl_usu_inf_red_socials'


class form_acad(models.Model):

    id_fa =  models.AutoField(primary_key = True) #Id de formación académica
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE)  # identificador de usuario
    instit = models.CharField('Nombre de la institucion ', max_length=25, null=False, blank = False) # Nombre de la institucion académica donde curso la formación
    tipo_form =  models.IntegerField(choices = TIPO_FORM_CO, default = 0, null=False, blank = False) #tipo de formación ver diccionario TIPO_FORM
    fch_ini = models.DateField('Fecha de Inicio', auto_now = False)
    fch_fin = models.DateField('Fecha de Fin', auto_now = False)
    certif = models.BooleanField('Posees Certificado', default=False)
    nal = models.CharField('Pais ', max_length=20, null=False, blank = False) #país
    ciudad = models.CharField('Ciudad ', max_length=20, null=False, blank = False)
    mod =  models.IntegerField(choices = MODALIDAD, default = 0, null=False, blank = False) # modalidad
    tit = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False) # Título obtenido
    menc =  models.CharField('Mención ', max_length=20, null=False, blank = False)  # Mensión de honor
    token = models.CharField('Token de validación ', max_length=20, null=False, blank = False)  #Token de validación electrónica de certificación de la formación

    v_form_acad = Permission.objects.get(codename='view_form_acad')
    a_form_acad = Permission.objects.get(codename='add_form_acad')
    c_form_acad = Permission.objects.get(codename='change_form_acad')
    d_form_acad = Permission.objects.get(codename='delete_form_acad')
    g_sis.permissions.add(v_form_acad,a_form_acad,c_form_acad,d_form_acad)
    g_admsis.permissions.add(v_form_acad,a_form_acad,c_form_acad,d_form_acad)
    g_appusu.permissions.add(v_form_acad,a_form_acad,c_form_acad,d_form_acad)
    g_appgrp.permissions.add(v_form_acad,a_form_acad,c_form_acad)
    g_appins.permissions.add(v_form_acad,a_form_acad,c_form_acad)
    g_admapps.permissions.add(v_form_acad,a_form_acad,c_form_acad)
    g_ext.permissions.add(v_form_acad,a_form_acad,c_form_acad)
    g_admcons.permissions.add(v_form_acad,a_form_acad,c_form_acad)

    class Meta:
        verbose_name = 'form_acad'
        verbose_name_plural = 'form_acads'

class usu_inf_acad(models.Model):
#ESTA NO ME PARECE YA
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)  # identificador unico
    nivelform =  models.IntegerField(choices = TIPO_FORM_CO, default = 0, null=False, blank = False) # me indica la formacion qu tiene la usuario

    class Meta:
        verbose_name = 'usu_inf_acad'
        verbose_name_plural = 'usu_inf_acads'

class rl_usu_inf_form_acad(models.Model): # relacion de listado de id procesos de formación realizados
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_form = models.ForeignKey(form_acad, on_delete=models.CASCADE, null=False, blank =False)   #listado de procesos de formación realizados

    class Meta:
        verbose_name = 'rl_usu_inf_form_acad'
        verbose_name_plural = 'rl_usu_inf_form_acads'

class curs_dict(models.Model):
    #clase que almacena la información de cursos dictados a cargo de un usuario
    id_cd = models.AutoField(primary_key = True)    #Id de formación académica
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
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

    v_curs_dict = Permission.objects.get(codename='view_curs_dict')
    a_curs_dict = Permission.objects.get(codename='add_curs_dict')
    c_curs_dict = Permission.objects.get(codename='change_curs_dict')
    d_curs_dict = Permission.objects.get(codename='delete_curs_dict')
    g_sis.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict,d_curs_dict)
    g_admsis.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict,d_curs_dict)
    g_appusu.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict,d_curs_dict)
    g_appgrp.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict)
    g_appins.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict)
    g_admapps.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict)
    g_ext.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict)
    g_admcons.permissions.add(v_curs_dict,a_curs_dict,c_curs_dict)

    class Meta:
        verbose_name = 'curs_dict'
        verbose_name_plural = 'curs_dicts'

class rl_usu_inf_contac_curs_dict(models.Model):  # relacion de LIstado de id Cursos a cargo dictadospor al persona.
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_cursdict = models.ForeignKey(curs_dict, on_delete=models.CASCADE, null=False, blank =False) #LIstado de id Cursos a cargo dictadospor al persona.


class usu_inf_prof(models.Model):
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador unico de usuario
    prof = models.CharField('Titulo obtenido ', max_length=20, null=False, blank = False)  # Profesión Actual

    v_usu_inf_prof = Permission.objects.get(codename='view_usu_inf_prof')
    a_usu_inf_prof = Permission.objects.get(codename='add_usu_inf_prof')
    c_usu_inf_prof = Permission.objects.get(codename='change_usu_inf_prof')
    d_usu_inf_prof = Permission.objects.get(codename='delete_usu_inf_prof')
    g_sis.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof,d_usu_inf_prof)
    g_admsis.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof,d_usu_inf_prof)
    g_appusu.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof,d_usu_inf_prof)
    g_appgrp.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof)
    g_appins.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof)
    g_admapps.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof)
    g_ext.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof)
    g_admcons.permissions.add(v_usu_inf_prof,a_usu_inf_prof,c_usu_inf_prof)

    class Meta:
        verbose_name = 'usu_inf_prof'
        verbose_name_plural = 'usu_inf_profs'

class rl_usu_inf_prof_empleos(models.Model):  # relacion listado de procesos de formación realizados
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador de usuario
    ls_curs = models.ForeignKey(curs_dict, on_delete=models.CASCADE, null=False, blank =False)

class empleos(models.Model):

    id_empl = models.AutoField(primary_key = True)
    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
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

    v_empleos = Permission.objects.get(codename='view_empleos')
    a_empleos = Permission.objects.get(codename='add_empleos')
    c_empleos = Permission.objects.get(codename='change_empleos')
    d_empleos = Permission.objects.get(codename='delete_empleos')
    g_sis.permissions.add(v_empleos,a_empleos,c_empleos,d_empleos)
    g_admsis.permissions.add(v_empleos,a_empleos,c_empleos,d_empleos)
    g_appusu.permissions.add(v_empleos,a_empleos,c_empleos,d_empleos)
    g_appgrp.permissions.add(v_empleos,a_empleos,c_empleos)
    g_appins.permissions.add(v_empleos,a_empleos,c_empleos)
    g_admapps.permissions.add(v_empleos,a_empleos,c_empleos)
    g_ext.permissions.add(v_empleos,a_empleos,c_empleos)
    g_admcons.permissions.add(v_empleos,a_empleos,c_empleos)

    class Meta:
        verbose_name = 'empleos'
        verbose_name_plural = 'empleoss'

class habilidades(models.Model):
    #clase que almacena la información de tipos de habilidad
    id_hab = models.AutoField(primary_key = True)
    nom_hab = models.CharField('Nombre de la habilidad', max_length=20, null=False, blank = False)  #Nombre de la habilidad
    desc = models.CharField('Descripción de la Habilidad', max_length=20, null=False, blank = False)  #Descripción de la Habilidad

    v_habilidades = Permission.objects.get(codename='view_habilidades')
    a_habilidades = Permission.objects.get(codename='add_habilidades')
    c_habilidades = Permission.objects.get(codename='change_habilidades')
    d_habilidades = Permission.objects.get(codename='delete_habilidades')
    g_sis.permissions.add(v_habilidades,a_habilidades,c_habilidades,d_habilidades)
    g_admsis.permissions.add(v_habilidades,a_habilidades,c_habilidades,d_habilidades)
    g_appusu.permissions.add(v_habilidades,a_habilidades,c_habilidades,d_habilidades)
    g_appgrp.permissions.add(v_habilidades,a_habilidades,c_habilidades)
    g_appins.permissions.add(v_habilidades,a_habilidades,c_habilidades)
    g_admapps.permissions.add(v_habilidades,a_habilidades,c_habilidades)
    g_ext.permissions.add(v_habilidades,a_habilidades,c_habilidades)
    g_admcons.permissions.add(v_habilidades,a_habilidades,c_habilidades)

    class Meta:
        verbose_name = 'habilidades'
        verbose_name_plural = 'habilidadess'

class rl_usu_inf_hab(models.Model): # relacion de listado de id de habilidades registradas por le usuario
    # Clase que almacena la información de las habilidades o conocimientos adquiridos y certificados por el usuario
    id_usu=  models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # identificador unico de usuario
    ls_habs =  models.ForeignKey(habilidades, on_delete=models.CASCADE, null=False, blank =False)  # listado de id de habilidades registradas por le usuario
    descripcion = models.CharField('Descripción ', max_length=20, null=False, blank = False)  # descripcion del conocimiento o habilidad investigador

    class Meta:
        verbose_name = 'rl_usu_inf_hab'
        verbose_name_plural = 'rl_usu_inf_habs'

class valid_hab(models.Model): # verificar esta
    #clase que procesa la información de validación social de habilidades
#    id_usu = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False) # Identificador del Usuario que registra la habilidad
    id_hab = models.ForeignKey(habilidades, on_delete=models.CASCADE, null=False, blank =False) #Identificador de la habilidad que se va a validar
    id_usu_val = models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)  #Identificador del Usuario que valida la habilidad
    id_esc = models.CharField('IDENTIFICADOR ', max_length=20, null=False, blank = False) #Identificador de la escala de validación
    val = models.CharField('RANGO ', max_length=20, null=False, blank = False) #Valor dentro del rango de la escala de validación

    v_valid_hab = Permission.objects.get(codename='view_valid_hab')
    a_valid_hab = Permission.objects.get(codename='add_valid_hab')
    c_valid_hab = Permission.objects.get(codename='change_valid_hab')
    d_valid_hab = Permission.objects.get(codename='delete_valid_hab')
    g_sis.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab,d_valid_hab)
    g_admsis.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab,d_valid_hab)
    g_appusu.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab,d_valid_hab)
    g_appgrp.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab)
    g_appins.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab)
    g_admapps.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab)
    g_ext.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab)
    g_admcons.permissions.add(v_valid_hab,a_valid_hab,c_valid_hab)

    #nota como realizp el dato val, id esc, id:usu_val
    class Meta:
        verbose_name = 'valid_hab'
        verbose_name_plural = 'valid_habs'

class app_reg_usu(models.Model):

    #app_mod = models.ForeignKey(app_mod, on_delete=models.CASCADE, null=False, blank =False)  # identificador de app
    nombre = models.CharField('Nombre de la app ', max_length=20, null=False, blank = False) # nombre del objeto
    descripcion = models.CharField('Descripcion ', max_length=20, null=False, blank = False) # descripcion del objeto
    activo = models.BooleanField('Activo ', default=False) # activo o no

    v_app_reg_usu = Permission.objects.get(codename='view_app_reg_usu')
    a_app_reg_usu = Permission.objects.get(codename='add_app_reg_usu')
    c_app_reg_usu = Permission.objects.get(codename='change_app_reg_usu')
    d_app_reg_usu = Permission.objects.get(codename='delete_app_reg_usu')
    g_sis.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu,d_app_reg_usu)
    g_admsis.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu,d_app_reg_usu)
    g_appusu.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu,d_app_reg_usu)
    g_appgrp.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu)
    g_appins.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu)
    g_admapps.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu)
    g_ext.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu)
    g_admcons.permissions.add(v_app_reg_usu,a_app_reg_usu,c_app_reg_usu)

    class Meta:
        verbose_name = 'app_reg_usu'
        verbose_name_plural = 'app_reg_usus'
