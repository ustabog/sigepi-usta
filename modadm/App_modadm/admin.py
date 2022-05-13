from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User
from .models import *

admin.site.register(mod)
admin.site.register(app_mod)
admin.site.register(listado_aplicativo)
admin.site.register(mod_ext)
admin.site.register(app_ext)
admin.site.register(rol)
admin.site.register(usu)
#admin.site.register(param_config)
#admin.site.register(permiso)
#admin.site.register(rol_permiso)
admin.site.register(func_app)
admin.site.register(rl_mod_app_mod)
admin.site.register(rl_mod_rol)
#admin.site.register(rl_mod_param_cnf)
admin.site.register(rl_mod_func)
admin.site.register(rl_app_mod_rol)
#admin.site.register(rl_app_mod_param_cnf)
admin.site.register(rl_app_mod_func)
admin.site.register(mod_adm)
#admin.site.register(adm_install)
#admin.site.register(log_mod_rol)
#admin.site.register(fuente_ins)
admin.site.register(log_acc_mod)
admin.site.register(log_acc_pltf)
