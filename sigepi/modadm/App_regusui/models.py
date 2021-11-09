from django.db import models
from django.contrib.auth.models import User
from modadm.App_modadm.models import *
from modadm.App_regusu.models import *
from modadm.App_regusugr.models import *

#Clases de la Aplicación Registro de Instituciones
###############################################################

ROL_APP = [
    (0,'Administrador de aplicación'),
    (1,'Invitado Instución'),
    (2,'Administrador de grupo'),
    (3,'Otro'),
    ]


class usui(models.Model):
    # Clase que almacena y procesa la información de un usuario institucional
    id_usuinst = models.AutoField(primary_key = True) # Identificador único del usuario institucionnal
    passinst  = models.CharField('Contraseña ', null = False, blank = False, max_length = 15) # contraseña para el usuario institucional (diferente a la del usuario del sistema)
    id_usu_admin = models.ForeignKey(User, on_delete=models.CASCADE, null= False, blank = False) #Identificador del usuario administrador (debe estar registrado y se le asignan permisos de administración de app_reg_ins)
    id_rol_app = models.ForeignKey(rol, on_delete = models.CASCADE, null= False, blank = False)
    #id_rol_app = models.ForeignKey(rol, on_delete = models.CASCADE, null= False, blank = False)
    #  # Identificador del Rol de Usuario Institucional dentro de la app_reg_ins
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
#    app_act = models.ForeignKey(listado_aplicativo, on_delete=models.CASCADE, null=False, blank = False) # identificador de funcionalidad actual (Sistema, módulo, aplicacion, extensión)
    #rol_act = 0 # identificador del rol actual.

    class Meta:
        verbose_name = 'usui_inf_apps'
        verbose_name_plural = 'usui_inf_appss'

class rl_usui_rol_actual(models.Model): #relacion qu me almacena el rol actual
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

class rl_usui_red_social(models.Model): #relacion de listado de red social
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False)
    id_red_social = models.ForeignKey(red_soc, on_delete=models.CASCADE, null=False, blank=False)

    class Meta:
        verbose_name = 'rl_usui_red_social'
        verbose_name_plural = 'rl_usui_red_socials'

class rl_usui_inf_acad(models.Model):
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

class rl_usuo_prog_ofer(models.Model): #Listado de id de programas ofertados por la entidad o Institución.
    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE ) # identificador unico
    id_prog_ofer = models.ForeignKey(prog_ofer, on_delete=models.CASCADE, default = 0) # identificador unico

    class Meta:
        verbose_name = 'rl_usuo_prog_ofer'
        verbose_name_plural = 'rl_usuo_prog_ofers'
#class usui_inf_inv(models.Model): #esta ya no seria buena
    # Clase que almacena y procesa la información académica del usuario
#    id_usui = models.ForeignKey(usui, on_delete=models.CASCADE, null=False, blank=False) # identificador unico
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
