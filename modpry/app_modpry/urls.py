# App del módulo de proyectos de investigación - URL's para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a): Milton O. Castro Ch.
#fecha 07-07-2022

from django.urls import path
from django.contrib.auth.views import *
#from rest_framework.routers import DefaultRouter
from modpry.app_regpry.views import *
from modpry.app_regpry.func import *
from modpry.app_regpry.urls import *
from modpry.app_modpry.views import *
from modpry.app_modpry.urls import *
from modpry.app_crono.views import *
from modpry.app_crono.func import *
from modpry.app_crono.urls import *
from modpry.app_evapry.views import *
from modpry.app_evapry.func import *
from modpry.app_evapry.urls import *
from modpry.app_conve.views import *
from modpry.app_conve.func import *
from modpry.app_conve.urls import *
from modpry.app_convo.views import *
from modpry.app_convo.func import *
from modpry.app_convo.urls import *
from modpry.app_disinv.views import *
from modpry.app_disinv.func import *
from modpry.app_disinv.urls import *
#from modpry.app_gespry.views import *
#from modpry.app_gespry.urls import *
#from modpry.app_gespry.func import *
#from modpry.app_mlog.views import *
#from modpry.app_mlog.func import *
#from modpry.app_mlog.urls import *
from modpry.app_recur.views import *
from modpry.app_recur.func import *
from modpry.app_recur.urls import *
from modpry.app_regprgi.views import *
from modpry.app_regprgi.func import *
from modpry.app_regprgi.urls import *
from modprd.app_regprd.views import *
from .models import *

urlpatterns = [
    # ------------------------------ URL's para convenios --------------------
    path('inicio',vst_conve().vst_inicio, name = 'ini_conve'), #inicio de la app de convenios
    path('crearconve/',vts_reg_conve.as_view(), name = 'crea_conve'), #Crea el convenio 
    path('cnconve/', vst_ls_conve.as_view(), name='cn_conve'), #Lista de convenios
    path('cndetconve/', vst_ls_detconve.as_view(), name = 'cn_det_conve'),# Información de un convenio
    path('editconve/<int:pk>/',vts_edit_conve.as_view(), name = 'edit_conve'), #Actualizar convenio
    path('archiconve/<id>',fn_archi_conve, name = 'archi_conve'), #Archivar un convenio
    path('eliconve/<id>',fn_eli_conve, name = 'eli_conve'),#Eliminar un convenio

    #------------------------------- URL's para convocatorias -------------------
    path('inicio',vst_convo().vst_inicio, name = 'ini_convo'), #inicio de la app de convocatorias
    path('inicio',vst_convo().vst_inicio, name = 'ini_convo'), #inicio de la app de convocatoria
    path('crearconvo/',vts_reg_convo.as_view(), name = 'crea_convo'), #Crea la convocatoria 
    path('cnconvo/', vst_ls_convo.as_view(), name='cn_convo'), #Lista de convocatorias
    path('cndetconvo/', vst_ls_detconvo.as_view(), name = 'cn_det_convo'), # Información de una convocatoria
    path('editconvo/<int:pk>/',vts_edit_convo.as_view(), name = 'edit_convo'), #Actualizar convocatoria
    path('archiconvo/<id>',fn_archi_convo, name = 'archi_convo'), #Archivar una convocatoria
    path('eliconvo/<id>',fn_eli_convo, name = 'eli_convo'),#Eliminar una convocatoria

    #URL para las funciones de un cronograma
    path('inicio',vst_crono().vst_inicio, name = 'ini_crono'), #inicio de la app de cronograma
    #URL para cronogramas
    path('creacrono/',vst_crea_crono.as_view(), name = 'creacrono'), #Crear cronograma 
    path('cncrono/',vst_ls_crono.as_view(), name = 'vercrono'),#Lista de cronograma
    path('addcrono/',vst_add_crono.as_view(), name = 'addcrono'),#Añadir al cronograma
    path('editcrono/<int:pk>/',vst_edit_crono.as_view(), name = 'edit_crono'),#Editar cronograma
    path('archicrono/<id>/',fn_archi_crono, name = 'archi_crono'), #Archivar cronograma
    path('elicrono/<id>/',fn_eli_crono, name = 'eli_crono'), #Eliminar cronograma
    #URL para etapas
    path('creaeta/',vst_crea_etapa.as_view(), name = 'creaeta'), #Crear etapa de un cronograma
    path('cndetcrono/',vst_ls_etapa.as_view(), name = 'veretapa'),#Lista de etapas
    path('editeta/<int:pk>/',vst_edit_etapa.as_view(), name = 'edit_etapa'),#Editar etapa
    path('archieta/<id>/',fn_archi_etapa, name = 'archi_etapa'), #Archivar etapa
    path('elieta/<id>/',fn_eli_etapa, name = 'eli_etapa'), #Eliminar etapa
    #URL para fases
    path('creafase/',vst_crea_fase.as_view(), name = 'creafase'), #Crear fase de una etapa
    path('cndetcrono/',vst_ls_fase.as_view(), name = 'verfase'),#Lista de fases
    path('editfase/<int:pk>/',vst_edit_fase.as_view(), name = 'edit_fase'),#Editar fase
    path('archifase/<id>/',fn_archi_fase, name = 'archi_fase'), #Archivar fase
    path('elifase/<id>/',fn_eli_fase, name = 'eli_fase'), #Eliminar fase
    #URL para procesos
    path('creaproc/',vst_crea_proc.as_view(), name = 'creaproc'), #Crea el proceso de una fase
    path('cndetcrono/',vst_ls_proc.as_view(), name = 'verproc'),#Lista de procesos
    path('editproc/<int:pk>/',vst_edit_proc.as_view(), name = 'edit_proc'),#Editar procesos
    path('archiproc/<id>/',fn_archi_proceso, name = 'archi_proc'), #Archivar proceso
    path('eliproc/<id>/',fn_eli_proceso, name = 'eli_proc'), #Eliminar proceso
    #URL para tareas
    path('creatar/',vst_crea_tarea.as_view(), name = 'creatar'), #Crea la tarea de un proceso
    path('cndetcrono/',vst_ls_tarea.as_view(), name = 'vertarea'),#Lista de tareas
    path('editar/<int:pk>/',vst_edit_tarea.as_view(), name = 'edit_tarea'),#Editar tarea
    path('architar/<id>/',fn_archi_tarea, name = 'archi_tar'), #Archivar tarea
    path('elitar/<id>/',fn_eli_tarea, name = 'eli_tar'), #Eliminar tarea
    #URL para actividades
    path('creacti/',vst_crea_acti.as_view(), name = 'creacti'), #Crea la actividad de una tarea
    path('cndetcrono/',vst_ls_acti.as_view(), name = 'veracti'),#Lista de actividades
    path('editacti/<int:pk>/',vst_edit_acti.as_view(), name = 'edit_acti'),#Editar actividad
    path('archiacti/<id>/',fn_archi_acti, name = 'archi_acti'), #Archivar actividad
    path('eliacti/<id>/',fn_eli_acti, name = 'eli_acti'), #Eliminar actividad

    #----------- URL's para la aplicación de diseño de proyecto de investigación ----------
    path('inicio',vst_disinv().vst_inicio, name = 'ini_disinv'), #inicio de la app de diseño de proyecto de investigación
        
    #URL para el registro de un diseño de investigación
    path('creadis/',vts_reg_dispry.as_view(), name = 'crea_dis'), #Crea el diseño de un proyecto 
    path('cndis/', vst_ls_dispry.as_view(), name='cn_dispry'), #Lista de diseños de proyectos
    path('cndetdis/', vts_ls_detdis.as_view(), name='cn_det_dis'), #Añadir información del diseño de un proyecto
    path('editdis/<int:pk>/',vts_edit_dispry.as_view(), name = 'edit_dis'), #Actualizar diseño de un proyecto
    path('archidis/<id>',fn_archi_dis, name = 'archi_dis'), #Archivar un diseño de un proyecto
    path('elidis/<id>',fn_eli_dis, name = 'eli_dis'),#Eliminar un diseño de un proyecto

    #URL para el registro de un tema
    path('createma/',vts_reg_tema.as_view(), name = 'crea_tema'), #Crea el tema
    path('cntema/', vst_ls_tema.as_view(), name='cn_tema'), #Lista de los tema
    path('editema/<int:pk>/',vts_edit_tema.as_view(), name = 'edit_tema'), #Actualiza el tema
    path('architema/<id>',fn_archi_tema, name = 'archi_tema'), #Archivar un tema
    path('elitema/<id>',fn_eli_tema, name = 'eli_tema'),#Eliminar un tema

    #URL para el registro de una definición
    path('creadefin/',vts_reg_defi.as_view(), name = 'crea_defin_dis'), #Crea la definición
    path('cndefin/', vst_ls_defi.as_view(), name='cn_defin_dis'), #Lista de laa definiciones
    path('edirdefin/<int:pk>/',vts_edit_defi.as_view(), name = 'edit_defin_dis'), #Actualiza una definición
    path('archidefin/<id>',fn_archi_defi, name = 'archi_defin_dis'), #Archivar una definición
    path('elidefin/<id>',fn_eli_defi, name = 'eli_defin_dis'),#Eliminar una definición

    #URL para el registro de un árbol de problemas
    path('creaap/',vts_reg_ap.as_view(), name = 'crea_arb_pro'), #Crea un árbol de problemas
    path('cnap/', vst_ls_ap.as_view(), name='cn_arb_pro'), #Lista los árboles de problemas
    path('edirap/<int:pk>/',vts_edit_ap.as_view(), name = 'edit_arb_pro'), #Actualiza un árbol de problemas
    path('archiap/<id>',fn_archi_ap, name = 'archi_arb_pro'), #Archivar un árbol de problemas
    path('eliap/<id>',fn_eli_ap, name = 'eli_arb_pro'),#Eliminar un árbol de problemas

    #URL para el registro de un árbol de objetivos
    path('creaao/',vts_reg_ao.as_view(), name = 'crea_arb_obj'), #Crea un árbol de objetivos
    path('cnao/', vst_ls_ao.as_view(), name='cn_arb_obj'), #Lista los árboles de objetivos
    path('edirao/<int:pk>/',vts_edit_ao.as_view(), name = 'edit_arb_obj'), #Actualiza un árbol de objetivos
    path('archiao/<id>',fn_archi_ao, name = 'archi_arb_obj'), #Archivar un árbol de objetivos
    path('eliao/<id>',fn_eli_ao, name = 'eli_arb_obj'),#Eliminar un árbol de objetivos

    #URL para el registro de causas
    path('creacau/',vts_reg_cau.as_view(), name = 'crea_causa'), #Crea una causa
    path('cncau/', vst_ls_cau.as_view(), name='cn_causa'), #Lista las causas
    path('edircau/<int:pk>/',vts_edit_cau.as_view(), name = 'edit_causa'), #Actualiza una causa
    path('archicau/<id>',fn_archi_cau, name = 'archi_causa'), #Archivar una causa
    path('elicau/<id>',fn_eli_cau, name = 'eli_causa'),#Eliminar una causa

    #URL para el registro de un efecto
    path('creaefe/',vts_reg_efe.as_view(), name = 'crea_efecto'), #Crea un efecto
    path('cnefe/', vst_ls_efe.as_view(), name='cn_efecto'), #Lista las efecto
    path('editefe/<int:pk>/',vts_edit_efe.as_view(), name = 'edit_efecto'), #Actualiza un efecto
    path('archiefe/<id>',fn_archi_efe, name = 'archi_efecto'), #Archivar un efecto
    path('eliefe/<id>',fn_eli_efe, name = 'eli_efecto'),#Eliminar un efecto

    #URL para el registro de un medio
    path('creamed/',vts_reg_med.as_view(), name = 'crea_medio'), #Crea un medio
    path('cnmed/', vst_ls_med.as_view(), name='cn_medio'), #Lista las medio
    path('editmed/<int:pk>/',vts_edit_med.as_view(), name = 'edit_medio'), #Actualiza un medio
    path('archimed/<id>',fn_archi_med, name = 'archi_medio'), #Archivar un medio
    path('elimed/<id>',fn_eli_med, name = 'eli_medio'),#Eliminar un medio

    #URL para el registro de un fin
    path('creafin/',vts_reg_fin.as_view(), name = 'crea_fin'), #Crea un fin
    path('cnfin/', vst_ls_fin.as_view(), name='cn_fin'), #Lista las fin
    path('editfin/<int:pk>/',vts_edit_fin.as_view(), name = 'edit_fin'), #Actualiza un fin
    path('archifin/<id>',fn_archi_fin, name = 'archi_fin'), #Archivar un fin
    path('elifin/<id>',fn_eli_fin, name = 'eli_fin'),#Eliminar un fin

    #-------------------- URL para las funciones de la evaluación de un proyecto --------
    path('inicio',vst_evapry().vst_inicio, name = 'inicio_pry'), #inicio de la app de proyectos
    #URL para la evaluación de un proyecto
    path('creaeva/', vst_reg_evapry.as_view(), name = 'crear_eva'), #Crear evaluación de un proyecto
    path('cneva/', vst_ls_evapry.as_view(), name = 'cn_evapry'), #Consultar evaluación de un proyecto
    path('addeva/', vst_add_eva.as_view(), name = 'add_eva'), #Añadir información a una evaluación de un proyecto
    path('editeva/<int:pk>/',vst_edit_evapry.as_view(), name = 'edit_eva'), #Editar la evaluación de un proyecto
    path('archieva/<id>',fn_archi_eva, name = 'archi_eva'), #Archivar la evaluación de un proyecto
    path('elieva/<id>',fn_eli_eva, name = 'eli_eva'),#Eliminar la evaluación de un proyecto
    #URL para rúbrica de evaluación
    path('crearub/', vst_crear_rub.as_view(), name = 'crear_rub'), #Crear rúbrica
    path('cndeteva/', vst_ls_rub.as_view(), name = 'cn_rub'), #Consultar rúbrica
    path('editrub/<int:pk>/',vst_edit_rub.as_view(), name = 'edit_rub'), #Editar la rúbrica de evaluación de un proyecto
    path('archirub/<id>',fn_archi_rub, name = 'archi_rub'), #Archivar la rúbrica de evaluación de un proyecto
    path('elirub/<id>',fn_eli_rub, name = 'eli_rub'),#Eliminar la rúbrica de evaluación de un proyecto
    #URL para criterio de evaluación
    path('creacrit/', vst_crear_crit.as_view(), name = 'crear_crit'), #Crear criterios de la rúbrica
    path('cndeteva/', vst_ls_crit.as_view(), name = 'cn_crit'), #Consultar criterios evaluación de un proyecto
    path('editcrti/<int:pk>/',vst_edit_crit.as_view(), name = 'edit_crit'), #Editar el criterio de evaluación de un proyecto
    path('archicrit/<id>',fn_archi_crit, name = 'archi_crit'), #Archivar el criterio de evaluación de un proyecto
    path('elicrti/<id>',fn_eli_crit, name = 'eli_crit'),#Eliminar el criterio de evaluación de un proyecto
    #URL para rango de evaluación
    path('crearango/', vst_crear_rango.as_view(), name = 'crear_rango'), #Crear un rango de evaluación 
    path('cndeteva/', vst_ls_rango.as_view(), name = 'cn_rango'), #Consultar rango de evaluación de un proyecto
    path('editrng/<int:pk>/',vst_edit_rng.as_view(), name = 'edit_rng'), #Editar el rango de evaluación de un proyecto
    path('archirng/<id>',fn_archi_rng, name = 'archi_rng'), #Archivar el rango de evaluación de un proyecto
    path('elirng/<id>',fn_eli_rng, name = 'eli_rng'),#Eliminar el rango de evaluación de un proyecto
    #URL para resultado de evaluación
    path('crearesul/', vst_crear_resul.as_view(), name = 'crear_resul'), #Crear un resultado de evaluación
    path('cndeteva/', vst_ls_resultado.as_view(), name = 'cn_res'), #Consultar resultado de una evaluación de un proyecto
    path('editres/<int:pk>/',vst_edit_res.as_view(), name = 'edit_res'), #Editar el rsultado de una evaluación de un proyecto
    path('archires/<id>',fn_archi_res, name = 'archi_res'), #Archivar el resultado de evaluación de un proyecto, solo para el rol de evaluadores
    path('elires/<id>',fn_eli_res, name = 'eli_res'),#Eliminar el resultado de evaluación de un proyecto
    #URL para tipo de evaluación
    path('creatipo/', vst_crear_tipoeva.as_view(), name = 'crear_tipo'), #Crear tipo de evaluación
    path('cndeteva/', vst_ls_tipoeva.as_view(), name = 'cn_tipoeva'), #Consultar tipo de evaluación de un proyecto
    path('editipo/<int:pk>/',vst_edit_tipo.as_view(), name = 'edit_tipo'), #Editar el tipo de evaluación de un proyecto
    path('elitipo/<id>',fn_eli_tipo, name = 'eli_tipo'),#Eliminar el tipo de evaluación de un proyecto
    #URL para definciónes, comentarios, ect, de evaluación
    path('creardefi/', vst_crear_defi.as_view(), name = 'crear_defi'), #Crear definición, comentario, recomendación
    path('cndeteva/', vst_ls_defi.as_view(), name = 'cn_defi'), #Consultar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('editdefi/<int:pk>/',vst_edit_defi.as_view(), name = 'edit_defi'), #Editar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('archidefi/<id>',fn_archi_defi, name = 'archi_defi'), #Archivar definciónes, comentarios, ect, de la evaluación de un proyecto
    path('elidefi/<id>',fn_eli_defi, name = 'eli_defi'),#Eliminar definciónes, comentarios, ect, de la evaluación de un proyecto

    #URL's para la aplicación de gestión de proyecto de investigación
    #path('inicio',vst_gespry().vst_inicio, name = 'ini_gespry'), #inicio de la app de gestión de proyectos

    #URL's para la aplicación de marco lógico
    #path('inicio',vst_mlog().vst_inicio, name = 'ini_mlog'), #inicio de la app de marco lógico

    #------------------------- URL's para la aplicación de recursos -------------------
    path('inicio',vst_recur().vst_inicio, name = 'ini_recur'), #inicio de la app de recursos
    path('crearecu/',vts_reg_recu.as_view(), name = 'crea_recu'), #Crea el recurso 
    path('cnrecu/', vst_ls_recu.as_view(), name='cn_recu'), #Lista de recursos
    path('cndetrecu/',vst_ls_detrecu.as_view(), name = 'cn_det_recu'),
    path('editrecu/<int:pk>/',vts_edit_recu.as_view(), name = 'edit_recu'), #Actualizar recurso
    path('archirecu/<id>',fn_archi_recu, name = 'archi_recu'), #Archivar un recurso
    path('elirecu/<id>',fn_eli_recu, name = 'eli_recu'),#Eliminar un recurso

    # ------------- URL's para la aplicación de registro de programa de investigación------
    path('inicio',vst_regprgi().vst_inicio, name = 'ini_regprgi'), #inicio de la app de registro de programa de investigación
    path('creaprgi/',vts_reg_prgi.as_view(), name = 'crea_prgi'), #Crea el programa de investigación                                                                                                                                               
    path('cnprgi/', vst_ls_prgi.as_view(), name='cn_prgi'), #Lista de programas de investigación
    path('cndetprgi/',vst_ls_detprgi.as_view(), name = 'cn_det_prgi'), #Información en detalle de un programa de investigación
    path('editprgi/<int:pk>/',vts_edit_prgi.as_view(), name = 'edit_prgi'), #Actualizar un programa de investigación
    path('archiprgi/<id>',fn_archi_prgi, name = 'archi_prgi'), #Archivar un programa de investigación
    path('eliprgi/<id>',fn_eli_prgi, name = 'eli_prgi'),#Eliminar un programa de investigación

    # ------------------------- URL para registro de un proyecto -----------------------
    path('inireg',vst_regpry().vst_inicio, name = 'ini_regpry'), #inicio de la app de proyectos
    path('creapry/',vts_reg_pry.as_view(), name = 'crea_pry'), #Crea el proyecto 
    path('cnpry/', vst_ls_pry.as_view(), name='cn_pry'), #Lista de proyectos
    path('cndetpry/', vst_ls_infopry.as_view(), name='cn_det_pry'), #Lista de la información de los proyectos
    path('editpry/<int:pk>/',vts_edit_pry.as_view(), name = 'edit_pry'), #Actualizar proyecto
    path('archipry/<id>',fn_archi_pry, name = 'archi_pry'), #Archivar un proyecto
    path('elipry/<id>',fn_eli_pry, name = 'eli_pry'),#Eliminar un proyecto

    #URL para la información adicional de un proyecto
    path('addpry/',vts_add_pry.as_view(), name = 'add_pry'),#Añadir información del proyecto
    path('cninf/', vst_ls_infopry.as_view(), name = 'cn_infpry'),#Consultar información adicional de un proyecto
    path('editinf/<int:pk>/', vts_edit_infpry.as_view(), name = 'edit_inf'),#Editar información de un proyecto
    path('archinf/<id>',fn_archi_infpry, name = 'archi_inf_pry'), #Archivar la información adicional de un proyecto
    path('elinf/<id>',fn_eli_infpry, name = 'eli_inf_pry'),#Eliminar la información adicional de un proyecto

    #URL para la información geográfica de un proyecto
    path('addgeo/',vts_reg_geo.as_view(), name = 'add_geo'),#Añadir información geográfica del proyecto
    path('cngeo/', vst_ls_geopry.as_view(), name = 'cn_geo'),#Consultar información geográfica  de un proyecto
    path('editgeo/<int:pk>/', vts_edit_geo.as_view(), name = 'edit_geo'),#Editar información geográfica de un proyecto
    path('archigeo/<id>',fn_archi_geo, name = 'archi_geo'), #Archivar la información geográfica de un proyecto
    path('eligeo/<id>',fn_eli_geo, name = 'eli_geo'),#Eliminar la información geográfica de un proyecto

    #URL para los eventos de un proyecto
    path('addeven/',vts_reg_even.as_view(), name = 'add_even'),#Añadir eventos de un proyecto
    path('cneven/', vst_ls_evenpry.as_view(), name = 'cn_even'),#Consultar eventos de un proyecto
    path('editeven/<int:pk>/', vts_edit_even.as_view(), name = 'edit_even'),#Editar eventos de un proyecto
    path('archieven/<id>',fn_archi_even, name = 'archi_even'), #Archivar eventos de un proyecto
    path('elieven/<id>',fn_eli_even, name = 'eli_even'),#Eliminar eventos de un proyecto

    #URL para la línea de investigación
    path('addlninv/',vts_reg_lninv.as_view(), name = 'add_lninv'),#Añadir línea de investigación
    path('cnlninv/', vst_ls_lninv.as_view(), name = 'cn_lninv'),#Consultar línea de investigación
    path('editlninv/<int:pk>/', vts_edit_lninv.as_view(), name = 'edit_lninv'),#Editar línea de investigación
    path('archilninv/<id>',fn_archi_lninv, name = 'archi_lninv'), #Archivar línea de investigación
    path('elilninv/<id>',fn_eli_lninv, name = 'eli_lninv'),#Eliminar línea de investigación

    #URL para el registro de un producto
    path('iniprd', ini_regprd().view_prd, name='ini_prd'), 
    path('crearprd/', vst_regprd.as_view(), name='crear_prd') 
]


