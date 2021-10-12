from django.contrib import admin
from django.contrib.auth.models import User
from .models import *


admin.site.register(etapa_gr)
admin.site.register(usugr)
admin.site.register(usu_nr)
admin.site.register(rel_usugr_ls_etp)
admin.site.register(rel_usugr_ls_usu)
admin.site.register(rel_usugr_ls_usu_nr)
admin.site.register(usugr_inf_apps)
admin.site.register(rl_usugr_inf_rol_Actual)
admin.site.register(usugr_inf_gr)
admin.site.register(usugr_inf_contac)
admin.site.register(usugr_inf_red_social)
admin.site.register(form_acad_gr)
#admin.site.register(rl_usugr_inf_acad)
admin.site.register(curs_ofer)
admin.site.register(rl_usugr_form_acad_gr)
admin.site.register(rl_usugr_curs_ofer)
admin.site.register(app_reg_gr)
