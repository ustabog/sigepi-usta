from django.urls import path
from .models import *
from modprd.app_regprd.views import *

urlpatterns = [
    path('iniprd', ini_regprd().view_prd, name='ini_prd'), 
    #path('crearprd/', vst_regprd().as_view, name='crear_prd') 
]