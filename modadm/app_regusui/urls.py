from django.urls import path, include
from modadm.app_regusui.views import *

urlpatterns = [
    #url para crear registro de institución
    path('creausui/',vst_reg_usui.as_view(), name = 'crea_usuiprb'),
    path('lsconusui/', vts_selec_usui_cons.as_view(), name = 'cons_usui'),
    path('edi_usui/<int:pk>/', vst_mod_reg_usui.as_view(), name= 'editar_usui'),

]
