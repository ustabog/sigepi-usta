from django.contrib import admin
from .models import *
#modelos independientes
admin.site.register(discap)
admin.site.register(habil)
# Modelos de información básica de usuario
admin.site.register(usu_inf_pers)
admin.site.register(usu_inf_contac)
admin.site.register(usu_form_acad)
admin.site.register(usu_red_soc)
admin.site.register(usu_empleo)
admin.site.register(usu_curs_dict)
admin.site.register(usu_valid_hab)

#Modelos de relación de la aplicación de registro de usuarios
admin.site.register(rl_usu_rol)
