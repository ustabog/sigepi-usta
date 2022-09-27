from django.urls import path, include
from modadm.app_regusui.views import *

urlpatterns = [
    #url para crear registro de institución
    path('creausui/',vst_reg_usui.as_view(), name = 'creausui'),
    path('lsconusui/', vts_usui_cons.as_view(), name = 'cons_usui'),
    #path('lsconusui/<int:pk>', vts_usui_cons.as_view(), name = 'cons_det_usui'),
    path('edi_usui/<int:pk>/', vst_mod_reg_usui.as_view(), name= 'editar_usui'), 

]
