from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
from .models import *
# modelos de usuario base
admin.site.register(usu)
admin.site.register(usugr)
admin.site.register(usui)
# modelos de módulos, aplicaciones, roles y funciones
admin.site.register(adm_mod)
admin.site.register(adm_app)
admin.site.register(adm_rol)
admin.site.register(adm_func)
# modelos de relación 
admin.site.register(rl_func_rol)
# modelos de registros de acceso
admin.site.register(log_acc_pltf)
admin.site.register(log_acc_rol)
admin.site.register(log_acc_func)

