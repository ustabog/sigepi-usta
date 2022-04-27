
"""
Creacion de permisos y grupos po defecto
Fecha: 26/04/22
Auto: Juan Sebastian Cely Caro
"""

import logging
from django.contrib.auth.models import Group, Permission

GRUPOS = [
    'Sistema',
    'Admin Modulo Administracion',
    'Admin Aplicacion Modulo Administracion',
    'Admin Aplicacion Usuarios',
    'Admin Aplicacion Grupos',
    'Admin Aplicacion Instituciones',
    'Admin Aplicacion Configuracion',
    'Admin Aplicacion Modulo Consultas',
    'Admin Aplicacion Consultas',
]

MODELOS_ADM = [
    'mod', 'app_mod', 'listado_aplicativo', 'ext_mod', 'ext_app', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf'
]

MODELOS_USU = [
    'usu_inf_apps', 'discapacidad', 'usu_inf_pers', 'usu_inf_contac', 'red_soc', 'form_acad', 'usu_inf_acad', 'curs_dict', 'usu_inf_prof', 'empleos', 'habilidades', 'valid_hab', 'app_reg_usu'
]

MODELOS_USUGR = [
    'etapa_gr', 'usugr', 'usu_nr', 'usugr_inf_apps', 'usugr_inf_gr', 'usugr_inf_contac', 'form_acad_gr', 'curs_ofer', 'app_reg_gr'
]

MODELOS_USUI = [
    'usui', 'usui_inf_apps', 'usui_inf_inst', 'usui_inf_contac', 'prog_ofer', 'conv_inv', 'app_reg_ins' 
]

MODELOS = [
    'conf_iu',
    MODELOS_ADM,
    MODELOS_USU,
    MODELOS_USUGR,
    MODELOS_USUI
]

PERMISOS = ['view', 'add', 'change', 'delete']

PERMISOS_VA = ['view', 'add']

class roles ():

    def __init__(self) -> None:
        pass

    def crear_roles():
        for group in GRUPOS:
            new_group, created = Group.objects.get_or_create(name=group)
            for model in MODELOS:
                for permission in PERMISOS:
                    name = 'Can {} {}'.format(permission, model)
                    #print("Creating {}".format(name))
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("Permission not found with name '{}'.".format(name))
                        continue

                    new_group.permissions.add(model_add_perm)

        #print("Se crearon los grupos y permisso por defecto")

