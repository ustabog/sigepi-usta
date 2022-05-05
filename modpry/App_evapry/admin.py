from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

admin.site.register(app_ev_pry)
admin.site.register(evalucion_pry)
admin.site.register(tipos_evalucion)
admin.site.register(rel_evalucion_pry)
admin.site.register(criterios)
admin.site.register(criterios_pry)
