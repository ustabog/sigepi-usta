from django import forms
from django.contrib.auth.models import User, Permission
from modadm.app_regusu.models import *
from modadm.app_modadm.models import *

class frm_reg_usugr(forms.ModelForm):

    class Meta:
        model = usugr
        fields = '__all__'
        #exclude = ()