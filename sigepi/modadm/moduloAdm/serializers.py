from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User

class PermisosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = mod
        fields = '__all__'

class FuncionSerializer(serializers.ModelSerializer):
    class Meta:
        model = func_app
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_mod
        fields = '__all__'

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol
        fields = '__all__'

class listado_aplicativoSerializer(serializers.ModelSerializer):
    class Meta:
        model = listado_aplicativo
        fields = '__all__'

class ext_modSerializer(serializers.ModelSerializer):
    class Meta:
        model = ext_mod
        fields = '__all__'

class ext_appSerializer(serializers.ModelSerializer):
    class Meta:
        model = ext_app
        fields = '__all__'

class param_configSerializer(serializers.ModelSerializer):
    class Meta:
        model = param_config
        fields = '__all__'

class rol_permisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = rol_permiso
        fields = '__all__'

class func_appSerializer(serializers.ModelSerializer):
    class Meta:
        model = func_app
        fields = '__all__'

class rl_mod_app_modSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_mod_app_mod
        fields = '__all__'

class rl_mod_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_mod_rol
        fields = '__all__'

class rl_mod_param_cnfSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_mod_param_cnf
        fields = '__all__'

class rl_mod_funcSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_mod_func
        fields = '__all__'

class rl_app_mod_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_app_mod_rol
        fields = '__all__'

class rl_app_mod_param_cnfSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_app_mod_param_cnf
        fields = '__all__'

class rl_app_mod_funcSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_app_mod_func
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class usuSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu
        fields = '__all__'

class adm_installSerializer(serializers.ModelSerializer):
    class Meta:
        model = adm_install
        fields = '__all__'

class log_mod_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = log_mod_rol
        fields = '__all__'

class fuente_insSerializer(serializers.ModelSerializer):
    class Meta:
        model = fuente_ins
        fields = '__all__'

class log_acc_modSerializer(serializers.ModelSerializer):
    class Meta:
        model = log_acc_mod
        fields = '__all__'

class log_acc_pltfSerializer(serializers.ModelSerializer):
    class Meta:
        model = log_acc_pltf
        fields = '__all__'

class usu_inf_appsSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_apps
        fields = '__all__'

class rl_usu_inf_apps_rolSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_usu_inf_apps_rol
        fields = '__all__'

class discapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = discapacidad
        fields = '__all__'

class usu_inf_persSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_pers
        fields = '__all__'

class usu_inf_persSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_pers
        fields = '__all__'

class usu_inf_contacSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_contac
        fields = '__all__'

class red_socSerializer(serializers.ModelSerializer):
    class Meta:
        model = red_soc
        fields = '__all__'

class rl_usu_inf_red_socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_usu_inf_red_social
        fields = '__all__'

class form_acadSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_acad
        fields = '__all__'

class usu_inf_acadSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_acad
        fields = '__all__'

class rl_usu_inf_form_acadSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_usu_inf_form_acad
        fields = '__all__'

class curs_dictSerializer(serializers.ModelSerializer):
    class Meta:
        model = curs_dict
        fields = '__all__'

class rl_usu_inf_contac_curs_dictSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_usu_inf_contac_curs_dict
        fields = '__all__'

class usu_inf_profSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_prof
        fields = '__all__'

class rl_usu_inf_prof_empleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_prof
        fields = '__all__'

class empleosSerializer(serializers.ModelSerializer):
    class Meta:
        model = empleos
        fields = '__all__'

class habilidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = habilidades
        fields = '__all__'

class usu_inf_habSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_inf_hab
        fields = '__all__'

class valid_habSerializer(serializers.ModelSerializer):
    class Meta:
        model = valid_hab
        fields = '__all__'

class app_reg_usuSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_reg_usu
        fields = '__all__'

class etapa_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = etapa_gr
        fields = '__all__'

class usu_nrSerializer(serializers.ModelSerializer):
    class Meta:
        model = usu_nr
        fields = '__all__'

class rel_usugr_ls_etpSerializer(serializers.ModelSerializer):
    class Meta:
        model = rel_usugr_ls_etp
        fields = '__all__'

class rel_usugr_ls_etpSerializer(serializers.ModelSerializer):
    class Meta:
        model = rel_usugr_ls_etp
        fields = '__all__'

class rel_usugr_ls_usuSerializer(serializers.ModelSerializer):
    class Meta:
        model = rel_usugr_ls_usu
        fields = '__all__'

class rel_usugr_ls_usu_nrSerializer(serializers.ModelSerializer):
    class Meta:
        model = rel_usugr_ls_usu_nr
        fields = '__all__'

class usugr_inf_appsSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_apps
        fields = '__all__'

class rl_usugr_inf_rol_ActualSerializer(serializers.ModelSerializer):
    class Meta:
        model = rl_usugr_inf_rol_Actual
        fields = '__all__'

class usugr_inf_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_gr
        fields = '__all__'

class usugr_inf_contacSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_contac
        fields = '__all__'

class usugr_inf_contacSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_contac
        fields = '__all__'

class usugr_inf_red_socialSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_red_social
        fields = '__all__'

class form_acad_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_acad_gr
        fields = '__all__'

class form_acad_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = form_acad_gr
        fields = '__all__'

class usugr_inf_acadSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_inf_acad
        fields = '__all__'

class curs_oferSerializer(serializers.ModelSerializer):
    class Meta:
        model = curs_ofer
        fields = '__all__'

class curs_oferSerializer(serializers.ModelSerializer):
    class Meta:
        model = curs_ofer
        fields = '__all__'

class usugr_form_acad_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_form_acad_gr
        fields = '__all__'

class usugr_curs_oferSerializer(serializers.ModelSerializer):
    class Meta:
        model = usugr_curs_ofer
        fields = '__all__'

class app_reg_grSerializer(serializers.ModelSerializer):
    class Meta:
        model = app_reg_gr
        fields = '__all__'
