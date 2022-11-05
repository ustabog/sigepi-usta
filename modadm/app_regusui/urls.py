from django.urls import path, include
from modadm.app_regusui.views import *

urlpatterns = [
    #url para crear registro de institución
    path('creausui/',vst_reg_usui, name = 'creausui'),
    path('lsconusui/', vts_usui_cons.as_view(), name = 'cons_usui'),
    #path('lsconusui/<int:pk>', vts_usui_cons.as_view(), name = 'cons_det_usui'),
    path('edi_usui/<int:pk>/', vst_mod_reg_usui.as_view(), name= 'editar_usui'), 
    path('mis_inst/', vts_ls_inst, name='mis_inst'),
    

    #CRUD para la administración de los usuarios ligados a la institución
    
    #Registar nuevo usuario a la intitucion
    path('new_usui_usu/', vst_cre_usu, name='new_usui_usuario'),
    #Consultar los usuarios registrados de la institución 
    path('inst_usui/', vst_ins_usu, name='inst_usui'),
    
    #CRUD Convocatorias de investigación.
    #Regisrar una convocatoria de investgacion
    path('nuevo_conv/', NuevaConvocatoria.as_view(), name='nueva_conv'),
    #Consular las convocatorias de investigación de la institución
    path('cons_convinv/', ConsultarConvocatorias.as_view(), name='cons_convinv'),

    #CRUD Programas ofertados por la institución.
    #Registrar una programa 
    path('nuevo_prog/',NuevoPrograma.as_view(),name='nuevo_prog'),
    #Consultar los programas ofertados por la institución
    path('cons_prog/', ConsultarProgramas.as_view(),name='cons_prog'),
]
