from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

admin.site.register(pry_base)
admin.site.register(mod_pry)
