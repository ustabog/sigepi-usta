from django.urls import path, include
from modadm.App_regusui.views import *

urlpatterns = [
    #url para crear registro de institución
    path('creausuiprb/',vst_reg_usui.as_view(), name = 'crea_usuiprb'),
    path('lsconusui/', vts_selec_usui_cons.as_view(), name = 'consu_usui_mod'),
    path('edi_usui/<int:pk>/', vst_mod_reg_usui.as_view(), name= 'editar_usui'),

]
