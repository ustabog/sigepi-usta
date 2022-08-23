# Diccionarios de consulta - Modelos para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a):  Milton O. Castro Ch.
#fecha 19-07-2022

#---------------- Diccionarios para MODADM ---------------

# Roles básicos del SIGEPI

'''
MODELOS_ADM = [
    'mod', 'app_mod', 'listado_aplicativo', 'mod_ext', 'app_ext', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf'
]

MODELOS_USU = [
    'usu', 'usu_inf_apps', 'discapacidad', 'usu_inf_pers', 'usu_inf_contac', 'red_soc', 'form_acad', 'usu_inf_acad', 'curs_dict', 'usu_inf_prof', 'empleos', 'habilidades', 'valid_hab', 'app_reg_usu'
]

MODELOS_USUGR = [
    'etapa_gr', 'usugr', 'usu_nr', 'usugr_inf_apps', 'usugr_inf_gr', 'usugr_inf_contac', 'form_acad_gr', 'curs_ofer', 'app_reg_gr'
]

MODELOS_USUI = [
    'usui', 'usui_inf_apps', 'usui_inf_inst', 'usui_inf_contac', 'prog_ofer', 'conv_inv', 'app_reg_ins' 
]

MODELOS = [
    'mod', 'app_mod', 'listado_aplicativo', 'mod_ext', 'app_ext', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf',
    'usu_inf_apps', 'discapacidad', 'usu_inf_pers', 'usu_inf_contac', 'red_soc', 'form_acad', 'usu_inf_acad', 'curs_dict', 'usu_inf_prof', 'empleos', 'habilidades', 'valid_hab', 'app_reg_usu',
    'etapa_gr', 'usugr', 'usu_nr', 'usugr_inf_apps', 'usugr_inf_gr', 'usugr_inf_contac', 'form_acad_gr', 'curs_ofer', 'app_reg_gr',
    'usui', 'usui_inf_apps', 'usui_inf_inst', 'usui_inf_contac', 'prog_ofer', 'conv_inv', 'app_reg_ins' 

]

PERMISOS = ['view', 'add', 'change', 'delete']

PERMISOS_VA = ['view', 'add']
'''

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

TIPO_ROL = [
    (0, 'Sistema'),#'Administrador(a) de Sistema'
    (1, 'Aplicación'),#'Administrador(a) de Institución'
    (2, 'Aplicación externa'),#'Administrador(a) de grupo'
    (3, 'Modulo'),#'Usuario(a) Individual'
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
    (8, 'otro')
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
    (3,'zzzz')
    ]

#Sector Económico
SECTOR_ECO = [
    (0,'Privado'),
    (1,'Publico'),
    (2,'xxx'),
    (3,'zzzz')
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
    (4,'otro')
    ]

#LIstado de  Horarios
HORARIO = [
    (0,'8am 12pm'),
    (1,'2pm 6pm'),
    (2,'8am 12pm - 2pm 6pm')
    ]

#---------------- Diccionarios para MODPRY ---------------
#---------------- Diciionarios para app_conve ------------
#---------------- Diciionarios para app_convo ------------
#---------------- Diciionarios para app_crono ------------
#---------------- Diciionarios para app_disinv -----------
#---------------- Diciionarios para app_evapry ------------
ESTADO_EVA = [
    (0,'Evaluación finalizada'),
    (1,'Evaluación proceso'),
    (2,'Evaluación preliminar')
]

EVA_PRY = [
    (0,'Cuantitativa'),
    (1,'Cualitativa')
]

CATG = [
    #Lista de categorias
    (0,'Comentario'),
    (1,'Concepto'),
    (2,'Recomendación'),
    (3,'Retroalimentación'),
    (4, 'Definiciones')
]

RES_EVA = [
    (0, 'Aprobado'),
    (1, 'Reprobado')
]

VAR_PLANT_EVA = [
    (0,'Evaluación de proyecto'), 
    (1,'archieva/<id>'), #URL para archivar el proyecto en la base de datos
    (2,'elieva/<id>'), #URL para eliminar el proyecto de la base de datos
    (2,'Rúbrica'),
    (1,'archirub/<id>'), #URL para archivar el proyecto en la base de datos
    (2,'elirub/<id>'), #URL para eliminar el proyecto de la base de datos
    (4,'Criterio'),
    (1,'archicrit/<id>'), #URL para archivar el proyecto en la base de datos
    (2,'elicrti/<id>'), #URL para eliminar el proyecto de la base de datos
    (6,'Resultado'),
    (1,'archires/<id>'), #URL para archivar el proyecto en la base de datos
    (2,'elires/<id>') #URL para eliminar el proyecto de la base de datos
]
#---------------- Diciionarios para app_gespry ------------
TIPO_DEP = [
    (0,'Administrativa'),
    (1,'Investigación'),
    (2, 'Financiera'),
    (3, 'Sindicatura'),
    (4, 'Bienestar'), 
    (5, '')
]
#---------------- Diciionarios para app_mlog ------------
TIPO_PRBL=[
    # tipo de problema que se enfrenta
    (0,'Social'),
    (1,'Investigación'),
    (2,'Normativo'),
    (3,'Político'),
    (4,'Económico'),
    (5,'Administrativo'),
    (6,'Metodológico'),
    (7,'Cultural'),
    (8,'otro')
    ]

ESTADO_MLOG=[
    # Estado del Análisis de Marco lógico
    (0,'Borrador'),
    (1,'Básico'),
    (2,'Estructurado'),
    (3,'Fundamentado'),
    (4,'Consolidado'),
    (5,'Depurado'),
    (6,'Validado'),
    (7,'Avanzado'),
    (8,'En reformulación')
    ]
#---------------- Diciionarios para app_modpry-----------
REG_PRY = [
    (0,'Id registro de proyecto'),
    (1,'Nombre del proyecto'),
    (2,'Descripción del proyecto'),
    (3,'Estado del proyecto')
    ]
#---------------- Diciionarios para app_recur ------------
TIPO_REC = [
    (0, 'Talento humano'),
    (1, 'Recurso material'),
    (2, 'Recurso financiero'),
    (3, 'Recurso organizacional'),
    (4, 'Recurso espacial'), 
    (5, 'Recurso documental')
    ]
#---------------- Diciionarios para app_regprgi ------------
#---------------- Diciionarios para app_regpry ------------
ACT_PRY=[
    (0,'Beneficiario(a) Proy.'),
    (1,'Patrocinador(a) Proy.'),
    (2,'Afectado(a) de Proy.'),
    (3,'Par Inv.'),
    (4,'Control y Vigilancia de Proy.'),
    (5,'Representante Comunidad de Proy.'),
    (6, 'interventor(a)')
    ]

ESTADO_PRY=[
    (0, 'Borrador'),
    (1, 'Diseño'),
    (2, 'Gestión'),
    (3, 'Diseño y gestión'),
    (4, 'Aprobación'),
    (5, 'Ejecución'),
    (6, 'Ejecutado'),
    (7, 'Archivado')
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
    (11,'Revisión crítica')
    ]

DEPARTAMENTOS = [
    (0,'Antioquia'),
    (1,'Atlántico'),
    (2,'Abriaquí'),
    (3,'Bogotá D.C'),
    (4,'Boyacá'),
    (5,'Caldas'),
    (6,'Caquetá'),
    (7,'Cauca'),
    (8,'Cesar'),
    (9,'Córdoba'),
    (10,'Cundinamarca'),
    (11,'Chocó'),
    (12,'Huila'),
    (13,'La guajira'),
    (14,'Magdalena'),
    (15,'Meta'),
    (16,'Ñariño'),
    (17,'Norte de Santander'),
    (18,'Quindio'),
    (19,'Risaralda'),
    (20,'Santander'),
    (21,'Sucre'),
    (22,'Tolima'),
    (23,'Valle del Cauca'),
    (24,'Arauca'),
    (25,'Casanare'),
    (26,'Putumayo'),
    (27,'Archipiélago de San Andrés, Providencia y Santa Catalina'),
    (28,'Amazonas'),
    (29,'Guainía'),
    (30,'Guaviare'),
    (31,'Vaupés'),
    (32,'Vichada')
    ]

NIVEL_PRY =[
    #Nivel del proyecto
    (0,'Individual'),
    (1,'Grupal'),
    (2,'Institucional'),
    (3,'Interinstitucional'),
    (4,'Intergrupal')
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
    (5,'Formación')
    ]

TIPO_IMPACTO = [
    #Tipo de impacto del proyecto
    (0,'Tecnológicos'),
    (1,'Institucionales'),
    (2,'Económicos'),
    (3,'Políticos'),
    (4, 'Socio-culturales'),
    (5,'Ambientales')
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
    (7, 'Otro')
    ]

LINEA_TEMA = [
    #Línea temática del proyecto
    (0,'Ciencias naturales'),
    (1,'Ingeniería y tecnología'),
    (2,'Ciencias médicas y de la salud'),
    (3,'Ciencias agrícolas'),
    (4, 'Ciencias sociales'),
    (5,'Humanidades'),
    (7, 'Otro')
    ]

MOD_EVE = [
    #Modalidad del evento 
    (0,'Presencial'),
    (1,'Virtual'),
    (2,'Presencial mediado por TIC (PMT)')
]

EST_LN_INV=[
    (0, 'Activa'),
    (1, 'Archivada'),
    (2, 'No activa')
    ]

VAR_PLAN_REGPRY = [
    #Variables para utilizar dentro de la plantila de eliminar y archivar
    (0,'Proyecto'), #Variable proyecto
    (1,'archipry/<id>'), #URL para archivar el proyecto en la base de datos
    (2,'elipry/<id>') #URL para eliminar el proyecto de la base de datos
]

LN_INV_OCDE = [
    (0, 'Matemáticas'),
    (1, 'Computación y ciencias de la información'),
    (2, 'Ciencias físicas'),
    (3, 'Ciencias químicas'),
    (4, 'Ciencias de las tierra y medio ambientales'),
    (5, 'Ciencias biológicas'),
    (6, 'Otras ciencias naturales'),
    (7, 'Ingeniería civil'),
    (8, 'Ingenierías eléctrica, electrónica e informática'),
    (9, 'Ingeniería mecánica'),
    (10, 'Ingeniería química'),
    (11, 'Ingeniería de los materiales'),
    (12, 'Ingeniería médica'),
    (13, 'Ingeniería ambiental'),
    (14, 'Biotecnología Medio ambiental'),
    (15, 'Biotecnología industrial'),
    (16, 'Nanotecnología'),
    (17, 'Otras ingenierías y tecnologías'),
    (18, 'Medicina básica'),
    (19, 'Medicina clínica'),
    (20, 'Ciencias de la salud'),
    (21, 'Biotecnología en salud'),
    (22, 'Otras ciencias médicas'),
    (23, 'Agricultura, silvicultura y pesca'),
    (24, 'Ciencias animales y lechería'),
    (25, 'Ciencias veterinaria'),
    (26, 'Biotecnología agrícola'),
    (27, 'Otras ciencias'),
    (28, 'Psicología'),
    (29, 'Economía y negocios'),
    (30, 'Ciencias de la educación'),
    (31, 'Sociología'),
    (32, 'Derecho'),
    (33, 'Ciencias políticas'),
    (34, 'Geografía social y económica'),
    (35, 'Periodismo y comunicaciones'),
    (36, 'Otras ciencias sociales'),
    (37, 'Historia'),
    (38, 'Idiomas y literatura'),
    (39,'Arte'),
    (40, 'Otras historias'),
    (41,'Otras humanidades')
    ]

LN_INV_MINCI = [
    (0, 'Matemática'),
    (1, 'Computación y ciencias de la información'),
    (2, 'Ciencias físicas'),
    (3, 'Ciencias químicas'),
    (4, 'Ciencias de las tierra y medio ambientales'),
    (5, 'Ciencias biológicas'),
    (6, 'Otras ciencias'),
    (7, 'Ingeniería civil'),
    (8, 'Ingenierías eléctrica, electrónica e informática'),
    (9, 'Ingeniería mecánica'),
    (10, 'Ingeniería química'),
    (11, 'Ingeniería de los materiales'),
    (12, 'Ingeniería médica'),
    (13, 'Ingeniería ambiental'),
    (14, 'Biotecnología ambiental'),
    (15, 'Biotecnología industrial'),
    (16, 'Nanotecnología'),
    (17, 'Otras ingenierías y tecnologías'),
    (18, 'Medicina básica'),
    (19, 'Medicina clínica'),
    (20, 'Ciencias de la salud'),
    (21, 'Biotecnología en salud'),
    (22, 'Otras ciencias médicas'),
    (23, 'Agricultura, silvicultura y pesca'),
    (24, 'Ciencias animales y lechería'),
    (25, 'Ciencias'),
    (26, 'Biotecnología agrícola'),
    (27, 'Otras ciencias'),
    (28, 'Psicología'),
    (29, 'Economía y negocios'),
    (30, 'Ciencias de la educación'),
    (31, 'Sociología'),
    (32, 'Derecho'),
    (33, 'Ciencias políticas'),
    (34, 'Geografía social y económica'),
    (35, 'Periodismo y comunicaciones'),
    (36, 'Otras ciencias sociales'),
    (37, 'Historia'),
    (38, 'Idiomas y literatura'),
    (39, 'Otras historias'),
    (40,'Arte'),
    (41,'Otras humanidades')
    ]

# mediciones_dic=[
#     (0, 'sin medicion') 
#     (1, 'en medicion')
#     (2, 'medido')
#     (3, 'obsoleto')
#     ]

# cert_dic=[
#     (0, 'Certificado') 
#     (1, 'En certificacion')
#     (2, 'No certificado')
#     ]

# TRL_dic=[
#     (0, "No revisado")
#     (1, 'Principios basicos observados')
#     (2, 'Concepto de tecnologia y/o aplicacion formulada')
#     (3, 'Pruebas de concepto')
#     (4, 'Validacion de pruebas')
#     (5, 'Validacion en un entorno relevante')
#     (6, 'Validacion en un entorno en condiciones cercanas a las reales')
#     (7, 'Demostracion en un entorno operativo real  ')
#     (8, 'Sistema completo y calificado en un ambiente operacional')
#     (9, 'Sistema aprobado y operando con exito en un entorno real')
#     ]