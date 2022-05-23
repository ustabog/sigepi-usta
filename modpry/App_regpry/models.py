from django.db import models
from modpry.App_modpry.models import *
from modadm.App_regusugr.models import *
from modcons.App_cons.models import *

ROL_APP = [
    (0,'Investigador(a) Principal'),
    (1,'Propietario(a) Proy.'),
    (2,'Investigador(a) Secundario'),
    (3,'Colaborador(a)')
    ]
ACT_PRY=[
    (0,'Beneficiario(a) Proy.'),
    (1,'Patrocinador(a) Proy.'),
    (2,'Afectado(a) de Proy.'),
    (3,'Par Inv.'),
    (4,'Control y Vigilancia de Proy.'),
    (5,'Representante Comunidad de Proy.'),
    (6, 'interventor(a)'),
    ]
ESTADO_PRY=[
    (0, 'Borrador'),
    (1, 'Diseño'),
    (2, 'Gestión'),
    (3, 'Diseño y gestión'),
    (4, 'Aprobación'),
    (5, 'Ejecución'),
    (6, 'Ejecutado'),
    (7, 'Archivado'),
    ]
TIPO_PRY=[
    #tipos de Investigación
    (0, 'Ensayo'),
    (1, 'Disertación'),
    (2,'intervención artística o creativa'),
    (3,'Tesis'),
    (4,'Trabajo de grado'),
    (5,'Artículo científico'),
    (6,'Estudio clínico'),
    (7,'Estado de arte'),
    (8,'Prototipo'),
    (9,'Patente'),
    (10,'Propiedad industrial'),
    (11,'Revisión crítica'),
    ]
NIVEL_PRY =[
    #Nivel del proyecto
    (0,'Individual'),
    (1,'Grupal'),
    (2,'Institucional'),
    (3,'Interinstitucional'),
    (4,'Intergrupal'),
    ]
TIPO_INV_FIN=[
    #por fuente de financiación:
    (0,'Estatal'), #Recursos Estatales (Públicos)
    (1,'Privada'), #Recursos privados
    (2,'Personal'),#Recursos propios
    (3,'Comunitaria'), #Recursos comunitarios
    (4,'Mixta PUBPRV'), #Recursos Públicos y Privados
    (5,'Mixta PUBPER'), #Recursos Públicos y Personales
    (6,'Mixta PUBCOM'), #Recursos Públicos y Personales
    (7,'Otra') #Otra categoría de clasificación de financiación
    ]
TIPO_INV_INF=[
    #Por fuente de información:
    (0,'Sin Información'), #Sin información sobre las fuentes
    (1,'Primarias'), #Los datos son propios y se toman de forma directa
    (2,'Secundarias'), #Los datos ajenos y se trabaja con fuentes ajenas, no se recolectan datos de forma directa.
    (3,'Estado de la Cuestión'), #Es un tipo de investigación trasnversal qeu apunta a identificar las producciones documentales realizadas hasta la actualidad sobre un tema de investigación.
    (4,'Mixta'), #Los datos son propios en más del 50% de los casos y ajenos en el resto.
    (5,'Minería'), #Se substrae nueva información de cúmulos de datos existentes.
    (6,'Simulación'), #Se generan datos no experimentales para realizar pruebas simuladas de modelos.
    (7,'Otra') #Otra categoría de clasificación de fuente de información
    ]
TIPO_INV_MET=[
    #Por énfasis metodológico:
    (0,'Sin Información'), #Sin información sobre el énfasis metodológico
    (1,'Cualitativa'), #Se fundamenta en métodos cualitativos, estudios de caso, obervación de campo, etnografía, entre otros.
    (2,'Cuantitativa'), #Su énfasis es cuantitativo, estadístico o probabilístico.
    (3,'Mixta CC'), #Utiliza métodos cuantitativos y cualitativos de forma simultánea.
    (4,'Experimental'), #Sus resultados dependen de los experimentos que deben realizarse durante la investigación.
    (5,'Heurística'), #Se concentra en la ocnstrucción de apoyos a la investigación por medio de principios, reglas y estrategias para resolver problemas qeu aún no cunetan con solución.
    (6,'Exploratoria'), #Es la primera investigación que se realiza sobre el tema o desde ese enfoque metodológico.
    (7,'Clínica'), #Es una investigación derivada de una intervención a partir de un diagnóstico con un método ya probado.
    (8,'IAP'), #Los objetivos,la metodología y los resultados se consensúan con las poblaciones que se intervienen desde la investigación.
    (9,'Teórica'), #Su proceso de validación no requiere de evidencias empíricas, sino que ssus resultados se validan por sus premisas lógicas, que permiten explroar nuevas formas de comprensión de los fenómenos.
    (10,'Otra') #Otra categoría de clasificación metodológica.
    ]
TIPO_INV_TMP=[
    #Por énfasis temporal:
    (0,'Sin Información'),  #Sin información sobre el periodo de estudio.
    (1,'Histórica'), #Se busca acercarse a un objeto de estudio desde una continuidad temporal definida por el equipo de investigación.
    (2,'Genealógica'), #Parte de una exploración multicausal, que puede ser determinada ordenando cronológicamente los sucesos que explican y se relacionan para comprender una situación presente.
    (3,'Actual'), #Establece la situación actual de un fenómeno y el concoimiento que se tien hasta el momento en que se realiza.
    (4,'Proyectiva'), #Permite un abordaje temporal donde la investigación tiene previstos objetivos que se logran por medio del proceso de investigación, busca aproximar el resultado a un estado futuro deseado.
    (5,'Prescriptvia'),#Tiene como principal objetivo la optimizacion de procesos, partiendo de caminos metodológicos o procedimentales ya explorados en contextos determinados.
    (6,'Descriptiva'), #Se delimitan los aspectos o variables a estudiar, pero se privilegia la perspectiva subjetiva del investigador sobre la observación realizada, por lo general acompañan investigaciones preeliminares, exploratorias, etnográficas, artísticas o creativas.
    (7,'Prospectiva'), #Su principal preocupación es el modelado de los posibles desarrollos futuros de los fenómenos, tratando de brindar marcos de predictibilidad.
    (8,'Longitudinal'), #Es una investigación que se realiza de forma continua o de forma repetida durante un periodo largo de tiempo, con unas variables iniciales que se mantienen en el tiempo.
    (9,'Transversal'), #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    (10,'Periódica'), #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    (11,'Seccional'), #Se puede comprender como una variación de un estudio transversal que se reliza por una sola vez.
    (12,'Otra') #Otra categoría de clasificación temporal
    ]
TIPO_INV_VAR=[
    #Por los tipos de variables:
    (0,'Sin Información'),  #Sin información sobre las variables del estudio.
    (1,'Univariada'), #El objeto de estudio tiene una causalidad definida, determinable y se realiza el seguimiento de una variable central.
    (2,'Multivariada'), #El objeto de estudio no tiene una causalidad bien definida, y se relaciona con un conjunto finito de variables que pueden ser susceptibles de medirse.
    (3,'Correlacional'), #Se conocen als principales variables que intervienen en un fenómeno, pero se busca establecer el peso o la incidencia de las varibles en estudio.
    (4,'Estudio de Caso'), #Permite construir con base en el estudio de casos particulares, la construcción de tendencias o situaciones comunes que brindan correlación y generalización a partir de multiplicidad de estos estudios.
    (5,'Análisis Comparado'), #Desde unidades de análisis hermenéuticas, permite establecer correlaciones que facilitan la clasificación de objetos y fenómenos a partir del estudio de sus regularidades y correlaciones.
    (6,'Poblacional'), #Delimita un tiempo determinado para realizar la investigación y puede trabajar multiplicidad de variables.
    (7,'Muestral'), #Es un tipo de investigación que se realiza con un intervalo de tiempo determinado y que tiene unos objtivos definidos por quienes la realizan o financian.
    (8,'Otra') #Otra categoría de clasificación por variables.
    ]
TIPO_INV_CNT=[
    #Por contextos de investigación:
    (0,'Sin Información'),  #Sin información sobre las variables del estudio.
    (1,'Laboratorio'), #La investigación se realiza en un entorno controlado (Laboratorio).
    (2,'Campo'), #La investigación se debe desarrollar en un entorno no controlado (terreno o en el lugar donde tienen lugar los sucesos)
    (3,'Aplicada'), #Busca construir escenarios de investigación in situ, donde se puedan controlar los procesos que se están investigando.
    (4,'Operaciones o Procesos'), #Son técnicas de investigación para corrección, intervención u optimización de sistemas dinámicos, que permiten mejorar la funcionalidad y la eficiencia de diseños y estándares, se utilizan generalmente en etapas de desarrollo de productos o líneas de producción ya existentes, así como sistemas dinámicos complejos.
    (5,'Diagnóstica'), #La investigación diagnóstica se fundamenta en enfoques probabilíticos y estadísticos, donde la causalidad es múltiple con probabilidades de correlación similares, lo que influye en los tratamientos o las alternativas de solución.
    (6,'Metodológica'), #Son investigaciones que toman como foco de investigación la forma en que se realizan las investigaciones mismas, sus supuestos teóricos, los problemas de medición, o de interpretación de los datos, en general el cómo de las investigaciones.
    (7,'Forense'), #Es una investigación de corte histórico, busca establecer las situaciones más probables y demostrables, basados en evidencias para establecer responsabiliddes e imputaciones, a los posibles resposables de situaciones punibles o sancionables.
    (8,'Otra') #Otra categoría de clasificación de contextos
    ]
TIPO_INV_MAXLOG=[
    #Por énfasis de marco axiológico
    (0,'Sin Información'),  #Sin información sobre el marco axiológico del estudio.
    (1,'Hermenéutica'), #Investigación que concentra sus esfuerzos en logar la mejor interpretación del sentido de los registros, en función de los contextos a los cuales se traduce e interpreta.
    (2,'Ontológica'), #Indaga sobre los problemas de percepción, subjetividad o distorsión de perspectiva por aprte de quienes realizan la investigacion, en el desarrollo del proceso investigativo.
    (3,'Epistemológica'), #Busca establecer el marco conceptual que sirve de paradigma a los planteamientos teóricos y explicativos que sustentan los sujetos investigadores.
    (4,'Holística'), #La investigación holística reconoce la necesidad de establecer el más amplio márgen de integración de las diferentes perspectivas epistemológicas y hermenéuticas en torno al objeto de estudio.
    (5,'Formal'), #Es aquella que se realiza de forma sistemática y ajustada a reglas qeu permiten su replicación, reproducción o desarrollo. También se utiliza en campos de ciencias puras con altos grados de abstracción, mediante métodos lógicos de validación.
    (6,'Informal'), #Es un tipo de investigación qeu debe improvisar de acuerdo a las circusntancias, contextos y posibilidades del investigador o equipo de investigación, para lograr un abordaje del objeto de estudio.
    (7,'Empírica'), #Se establece en contraposición a la especulación teórica, permitiendo presentar aquello que es sustentable exclusivamente a partir de los hechos registrables, contrastables y comprobables a partir de la experiencia o la experimentación.
    (8,'Analítica'), #El analisis es el método de investigación que busca la descomposición de las unidades ya reconocidas, como un todo que se descompone en partes que permitan comprender causalidades con un mayor nivel de precisión y certidumbre.
    (9,'Deductiva'), #La investigación deductiva parte de la premisa de la existencia de una regla general aplicable a la comprensión de un fenómeno, guiando el diseño de los instrumentos y las premisas de la investigación.
    (10,'Inductiva'), #El proceso de investigación inductiva, parte de una condición particular buscando construir a partir de evidencias las generalziaciones posibles hasta que la evidencia contradiga el marco de explicación que se induce a aprtir de esta.
    (11,'Mixta AD'), #Investigación que utiliza el marco Analítico-Deductivo en su planteamiento.
    (12,'Mixta ID'), #Investigación que utiliza el marco Inductivo-Deductivo en su planteamiento.
    (13,'Hipotética'), #Es una investigación qeu utiliza la construcción de hipótesis para su planteamiento explicativo, metodológico o teórico, la cual tiene por objetivo comprobar o refutar la(s) hipótesis planteada.
    (14,'Actuarial'), #Es un tipo de investigación que se concentra en los impactos posibles derivados de als actuaciones de diversos actores o fenomenos causales, tanto para explicar como predecir las situaciones presentes y futuras, a paertir del estudio de los datos pasados. Generalemente permite la construcción de modelos.
    (15,'Factorial'), #Este tipo de investigación se concentra en la determinación de factores que inciden en un determinado fenómeno, desde una perspectiva fundamentalmente estadística. Ha cobrado relevancia con metodologías de minería de datos y big data.
    (16,'Axiológica'), #Es la investigación qeu se concentra en el peso qeu tienen los actores del proceso investigativo en los resultados y sesgos propios de las investigaciones, derivados de la acción humana en el proceso investigativo.
    (17,'Taxonómica'), #La investigación Taxonómica tiene por objetivo lograr la mejor clasificación de lso objetos o fenómenos de estudio, permitiendo encontrar inconsistencias, coincidencias, correlaciones o alternativas en el proceso de clasificación de lso objetos de estudio o los fenomenos estudiados.
    (18,'Conceptual'), #La investigación conceptual fuera del marco de la cognición y la filosofía, hace referencia a explorar modelos de productos que si bien aún no existen podrían entrar a realizarse. Es el paso previo a la construcción de un prototipo.
    (19,'Crítica'), #La investigación crítica tiene por objetivo encontrar las fisuras e incosistencias de un planteamiento teórico o un modelo existente o propuesto. Cumple una función depuradora de los principios lógicos sobre los que operan las soluciones y los modelos científicos.
    (20,'Otra')  #Otra categoría de clasificación por marco axiológico.
    ]
TIPO_INV_CPR=[
    #Por énfasis de campo (actualizar a los de la OCDE)
    (0,'Sin Información'), #Sin información sobre el campo profesional de la investigacion.
    (1,'Social'),#investigación propia de las ciencias sociales.
    (2,'Educativa'), #Investigación de las ciencias de la Educación.
    (3,'Didáctica'), #Investigación de las ciencias de la Educación.
    (4,'Periodística'), #Investigación propia de profesionales de periodismo.
    (5,'Artística'), #Investigación propia de profesionales de arte, diseño, música.
    (6,'Creativa'), #Es un enfoque de investigación que se concentra en carreras con énfasis creativo, artes plásticas, diseño, arquitectura, literatura, música, ingenierías, comunicación, entre otras.
    (7,'Jurídica'), #Propia de las disciplinas del Derecho, la Ciencia Política, las Ciencias de la Administración, las ciencias económicas, entre otras.
    (8,'Epidemiológica'), #Ciencias de la salud y de la administración.
    (9,'Etnográfica'), #Propia de la Antropología, sociología y ciencias sociales.
    (10,'Lingüística'), #Específica de la Lingüística, la filología, antropología, sociología, comunicación, entre otras.
    (11,'Semiótica'), #Tipo característico de ciencias sociales, artes y ciencias de la comunicación.
    (12,'Genética'), #Investigación propia de las ciencias de la salud, con énfasis en informática.
    (13,'Otra') #Otra categoría de clasificación por campo profesional.
    ]
ROL_GR_INV=[
    #Roles en el proceso de investigación.
    (0,'Sin Información'), #Sin información sobre el rol desempeñado
    (1,'Investigador(a) Principal'), #Responsable del proyecto y del equipo de investigación.
    (2,'Investigador(a) Senior'), #Categoría según Colciencias.
    (3,'Investigador(a) Asociado(a)'), #Categoría según Colciencias.
    (4,'Investigador(a) Junior'), #Categoría según Colciencias.
    (5,'Investigador(a) Emérito(a)'), #Categoría según Colciencias.
    (6,'Jóven Investigador(a)'), #Participación en convocatorias orientadas a jóvenes.
    (7,'Auxiliar de Investigación'), #Se participó ena ctividade relacionadas con la investigación.
    (8,'Investigador(a) independiente') #No se ha estado vinculado institucionalmente, pero se cuenta con productos de investigación.
    ]
USO_RED=[
    (0,'frecuente'),
    (1,'moderado'),
    (2,'poco frecuente'),
    (3,'inactivo')
    ]
TIPO_FORM_GR = [
    #tipo de formación Académica para grupos
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
TIPO_GR_INV = [
    #Tipos de gupos de Investigación
    (0,'Independiente'), #Grupo registrado en la plataforma como independiente, asociación de usuarios de la plataforma.
    (1,'Reconocido Inst'), #Grupo que además de registrado está vinculado y reconocido por una Institución o Entidad.
    (2,'Reconocido COLC'), #Grupo que además de registrado está vinculado y reconocido por Colciencias.
    (3,'Semillero de Inv.'), #Grupo que está reconocido como semillero por una Institución o Entidad.
    (4,'Comunidad'), #Grupo de comunidad de conocimiento abierto o libre. Con o sin cuotas de participación.
    (5,'Estado del Arte') #Grupo orientado a la construcción de estados del arte temáticos. Son grupos de comunidades abiertas con vinculación temporal y cuotas de participación.
    ]
ROL_GR_INV_COLC = [
    #Integrantes según modelo de Colciencias
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
TIPO_FORM_CO = [
    #tipo de formación Académica
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

TIPO_CONVE = [
    #Tipo de convenios
    (0,'Asociación'),
    (1,'Coopetación'),
    (4,'Divulgación'),
    (5,'Formación'),
    ]

TIPO_IMPACTO = [
    #Tipo de impacto del proyecto
    (0,'Tecnológicos'),
    (1,'Institucionales'),
    (2,'Económicos'),
    (3,'Políticos'),
    (4, 'Socio-culturales'),
    (5,'Ambientales'),
    ]

TIPO_RIESGO = [
    #Tipo de impacto del proyecto
    (0,'Corrupción del alcance'),
    (1,'Bajo desempeño'),
    (2,'Costos elevados'),
    (3,'Factor tiempo'),
    (4, 'Escasez de recursos'),
    (5,'Cambios operativos'),
    (6, 'Falta de claridad'),
    (7, 'Otro'),
    ]
LINEA_TEMA = [
    #Línea temática del proyecto
    (0,'Ciencias naturales'),
    (1,'Ingeniería y tecnología'),
    (2,'Ciencias médicas y de la salud'),
    (3,'Ciencias agrícolas'),
    (4, 'Ciencias sociales'),
    (5,'Humanidades'),
    (7, 'Otro'),
    ]
    
PRY_ARCHIVADO = [
    (0, 'Proyecto no archivado'),
    (1, 'Proyecto archivado'),
    ]

#clase base de registro de proyecto
class pry_base(models.Model):
    #clase base de registro de proyecto
    id_pry=models.AutoField(primary_key = True) #Identificador unico del proyecto
    cod_pry = models.CharField('Código proyecto:', max_length=50) # código unico del proyecto
    nombre_pry=models.CharField('Nombre del proyecto: ', max_length=255)#Nombre proyecto
    desc_pry=models.CharField('Descripción del proyecto: ', max_length=255, null=False, blank=False)#Decripción del proyecto
    tipo_pry=models.IntegerField(null = False, blank = False, choices = TIPO_PRY, default = 0) # Tipo de proyecto - diccionario TIPO_PRY
    prop_pry= models.ForeignKey(usu, on_delete=models.CASCADE, null= False, blank = False) #Propietario del proyecto
    est_pry = models.IntegerField(null = False, blank = False, choices = ESTADO_PRY, default = 0)
    pry_archi = models.IntegerField(null = False, blank = False, choices = PRY_ARCHIVADO, default = 0)#Si el proyecto es borrado queda como archivado
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
    id_inf_pry = models.AutoField(primary_key = True)# identificador unico para  App Registro de Proyectos
    nombre_archivo = models.CharField('Nombre del archivo del proyecto: ', max_length=255)# Nombre del archivo del proyecto.
    url_archivo =models.URLField('url del archivo del proyecto',max_length=200)# Url del archivo del proyecto.
    id_gr_inv = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)#identificador del grupo de investgación
    #id_ln_inv = models.ForeignKey(Ln_inv, on_delete=models.CASCADE, null=False, blank =False)#Identificador de la linea de investigación
    #conv =  models.IntegerField(null = False, blank = False, choices = CONVENIO, default = 0)# Convenio propuesto o previsto para la realización de la investigación.
    dat_dep = models.IntegerField(null = False, blank = False, choices = DEPARTAMENTOS, default = 0)#Lista de los departamentos de Colombia que hacen parte del proyecto
    #geo_nac_cp = models.ForeignKey(leer_dat_geo_cenpobl, on_delete=models.CASCADE, null=False, blank =False)#id registro de centros poblados que abarca el proyecto.
    url_ap =  models.URLField('url de la imágen de árbol de problemas',max_length=200)# Url de la imágen del árbol de problemas.
    url_ao =  models.URLField('url de la imágen de árbol de objetivos', max_length=200)# Url de la imágen del árbol de objetivos.
    id_ml = models.ForeignKey('ID marco lógico', on_delete=models.SET_NULL, null=True)# id de registro de marco lógico
    id_act = models.ForeignKey('ID marco lógico', on_delete=models.CASCADE, null=False, blank =False) #identificador de registro de actores proyecto.
    obj_gen = models.CharField('Objetivo general: ', max_length=255)# Objetivo general del proyecto.
    obj_esp = models.CharField('Objetivos especificos: ', max_length=255)# Objetivos específicos del proyecto.
    
    class Meta:
        verbose_name = 'inf_pry'
        verbose_name_plural = 'inf_prys'

    def __str__(self):
        return '{}'.format(self.nombre_archivo)

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

class rel_geo_proy(models.Model):
    #clase que define la información geográfica del proyecto, recoge los valores de divipola del dane con latitudes y longitudes.
    id_inf_geo = models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    municipio = models.CharField('Objetivos especificos: ', max_length=100)# actividades del proyecto
    dat_dep = models.IntegerField(null = False, blank = False, choices = DEPARTAMENTOS, default = 0)#Lista de los departamentos de Colombia que hacen parte del proyecto 
    #Hacer la función para mostrar codigo y territorio

class inf_detalle(models.Model):
    # clase que guarda la información de actividades del proyecto en un cronograma determinado.
    id_inf_act= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    dur = models.DateField(null=True, blank=True, auto_now=True) # Duración del proyecto valores dentro de un rango.
    und_dur = models.DateField(null=True, blank=True) # unidad de medida del rango de tiempo, 0:seg; 1:min; 2:horas; 3:meses; 4:años.
    actv = models.CharField('Objetivos especificos: ', max_length=255)# actividades del proyecto 
    tareas = models.CharField('Objetivos especificos: ', max_length=255)# Tareas del proyecto
    
    class Meta:
        verbose_name = 'inf_detalle'
        verbose_name_plural = 'inf_detalles'

class activ_pry(models.Model):
    # clase que guarda la información de actividades del proyecto.
    id_activ_pry= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    id_act_pry = models.ForeignKey(inf_act_proy, on_delete=models.CASCADE, null=False, blank =False)
    id_inf_act= models.ForeignKey(inf_detalle, on_delete=models.CASCADE, null=False, blank =False)
    class Meta:
        verbose_name = 'activ_pry'
        verbose_name_plural = 'activ_prys'

class tareas_pry(models.Model):
    # clase que guarda la información de actividades del proyecto.
    id_tareas_pry= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    id_act_pry = models.ForeignKey(inf_act_proy, on_delete=models.CASCADE, null=False, blank =False)
    id_inf_act= models.ForeignKey(inf_detalle, on_delete=models.CASCADE, null=False, blank =False)

    class Meta:
        verbose_name = 'tareas_pry'
        verbose_name_plural = 'tareas_prys'

class eventos_pry(models.Model):
    # clase que guarda la información de los eventos del proyecto.
    id_eventos_pry= models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    id_inf_act= models.ForeignKey(inf_detalle, on_delete=models.CASCADE, null=False, blank =False)
    
    class Meta:
        verbose_name = 'evento_pry'
        verbose_name_plural = 'eventos_prys'

class recur_pry(models.Model):
    # clase que guarda la información de los recursos del proyecto.
    id_recur_pry = models.AutoField(primary_key = True) 
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)
    id_inf_act= models.ForeignKey(inf_detalle, on_delete=models.CASCADE, null=False, blank =False)
    
    class Meta:
        verbose_name = 'recur_pry'
        verbose_name_plural = 'recurs_prys'

class rel_actv_pry(models.Model):
    #lista que relación actores con proyectos
    id_pry_base=models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)#id del proyecto
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)#Id del usuario 
    tarea_encar= models.ForeignKey(activ_pry, on_delete=models.CASCADE, null=False, blank =False)#Encargado de realizar la actividad del proyecto

class rel_tarea_pry(models.Model):
    #lista que relación actores con proyectos
    id_pry_base=models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)#id del proyecto
    id_usu=models.ForeignKey(usu, on_delete=models.CASCADE, null=False, blank =False)#Id del usuario 
    tarea_encar= models.ForeignKey(tareas_pry, on_delete=models.CASCADE, null=False, blank =False)#Encargado de realizar la tarea del proyecto

class lin_inv(models.Model):
    #Clase de las líneas de investigación de un proyecto
    id_linea_inv = models.AutoField(primary_key = True) #Identificador de la línea de investigación
    fch_ini_li = models.DateField(null=True, blank=True, auto_now=True)#Fecha de inicio de la línea de investigación
    fch_fin_li = models.DateField(null=True, blank=True)#Fecha de finalización de la línea de investigación
    fch_mdf_li = models.DateField(null=True, blank=True)#Fecha de modificación de la línea de investigación
    nombre_lin_inv = models.CharField('Nombre de la línea de investigación: ', max_length=255) #Nombre de la línea de investigación
    desc_lin_inv = models.CharField('Descripción de la línea de investigación: ', max_length=255)#Descripción de la línea de investigación
    #res_lin_inv = #Responsable de la línea de investigación
    #invs_lin_inv = #Investigadores de la línea de investigación
    #cmp_disc_ocdi = models.IntegerField(leer_dat_ocde, null = False, blank = False, default = 0)#código del municipio#Campos disciplinarios OCDI
    #cmp_disc_minc = models.IntegerField(leer_dat_minciencias, null = False, blank = False, default = 0)#Campos disciplinarios MINCIENCIAS
    #id_padre_li = models.ForeignKey('id padre de la línea de investigación', null=False, blank =False))#Id padre de la línea de investigación
    #id_hijo = #Id hijo
    #estado_lin_inv = #Estado de la línea de investigación, se define con relación a si tiene productos o proyectos dentro de la línea
    #tipo_mod_lin_inv = #Tipo de modificación de la línea de investigación
    id_pry=models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False) #id proyecto
    #id_grp = #id del grupo de investigación
    id_grp_prin = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)#id del grupo de investigación principal
    id_grp_vinpry = models.ForeignKey(usugr, on_delete=models.CASCADE, null=False, blank =False)#identificador de los grupos que estan viunculados a la linea de investigación

class rel_pry_lninv(models.Model):
    #clase de relación proyecto con la línea de investigación
    id_pry_base = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)#id del proyecto
    id_linea_inv = models.ForeignKey(pry_base, on_delete=models.CASCADE, null=False, blank =False)#id de la línea de investigación 

'''



