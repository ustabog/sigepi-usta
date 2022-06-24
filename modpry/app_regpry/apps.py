from django.db import models
from django.apps import AppConfig
from modpry.app_regpry import *

class AppRegpryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'modpry.app_regpry'
