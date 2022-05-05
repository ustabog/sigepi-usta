from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

admin.site.register(tipo_prod_inv)
admin.site.register(proc_inv)
admin.site.register(prod_inv)
admin.site.register(red_div)
admin.site.register(usu_inf_inv)
admin.site.register(rl_usu_inf_inv_proc_inv)
admin.site.register(rl_prod_usu)
admin.site.register(rl_usu_inf_inv_ls_red_div)
