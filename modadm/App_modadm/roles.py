
"""
Creacion de permisos y grupos po defecto
Fecha: 26/04/22
Auto: Juan Sebastian Cely Caro
"""

import logging
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import migrations
from django.db import connection



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
    'usu', 'usu_inf_apps', 'discapacidad', 'usu_inf_pers', 'usu_inf_contac', 'red_soc', 'form_acad', 'usu_inf_acad', 'curs_dict', 'usu_inf_prof', 'empleos', 'habilidades', 'valid_hab', 'app_reg_usu'
]

MODELOS_USUGR = [
    'etapa_gr', 'usugr', 'usu_nr', 'usugr_inf_apps', 'usugr_inf_gr', 'usugr_inf_contac', 'form_acad_gr', 'curs_ofer', 'app_reg_gr'
]

MODELOS_USUI = [
    'usui', 'usui_inf_apps', 'usui_inf_inst', 'usui_inf_contac', 'prog_ofer', 'conv_inv', 'app_reg_ins' 
]

MODELOS = [
    'mod', 'app_mod', 'listado_aplicativo', 'ext_mod', 'ext_app', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf',
    'usu_inf_apps', 'discapacidad', 'usu_inf_pers', 'usu_inf_contac', 'red_soc', 'form_acad', 'usu_inf_acad', 'curs_dict', 'usu_inf_prof', 'empleos', 'habilidades', 'valid_hab', 'app_reg_usu',
    'etapa_gr', 'usugr', 'usu_nr', 'usugr_inf_apps', 'usugr_inf_gr', 'usugr_inf_contac', 'form_acad_gr', 'curs_ofer', 'app_reg_gr',
    'usui', 'usui_inf_apps', 'usui_inf_inst', 'usui_inf_contac', 'prog_ofer', 'conv_inv', 'app_reg_ins' 

]


PERMISOS = ['view', 'add', 'change', 'delete']

PERMISOS_VA = ['view', 'add']

class roles ():
#Clase que permite registrar roles por defeco y sus respectivos permisos
    def __init__(self) -> None:
        pass

    def crear_roles(self):

        def db_table_exists(table):
            return table in connection.introspection.table_names()

        var = db_table_exists(table='auth_group')
        # print(var)

        if var == True:
            for group in GRUPOS:
                new_group, created = Group.objects.get_or_create(name=group)
                for model in MODELOS:
                    for permission in PERMISOS_VA:
                        name = 'Can {} {}'.format(permission, model)    
                        #print("Creating {}".format(name))
                        try:
                            model_add_perm = Permission.objects.get(name=name)
                        except Permission.DoesNotExist:
                            logging.warning("No se crearon los permisos '{}'.".format(name))
                            continue
                        new_group.permissions.add(model_add_perm)

            g_sis = Group.objects.get(name='Sistema')
            g_modadm = Group.objects.get(name='Admin Modulo Administracion')
            g_appmodadm = Group.objects.get(name='Admin Aplicacion Modulo Administracion')
            g_usu = Group.objects.get(name='Admin Aplicacion Usuarios')
            g_usugr = Group.objects.get(name='Admin Aplicacion Grupos')
            g_usui = Group.objects.get(name='Admin Aplicacion Instituciones')
            g_inv, create = Group.objects.get_or_create(name='Invitado')

            for model in MODELOS:
                for permission in PERMISOS:
                    name = 'Can {} {}'.format(permission, model)
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("No se crearon los permisos '{}'.".format(name))
                        continue
                    g_sis.permissions.add(model_add_perm)
                    g_modadm.permissions.add(model_add_perm)
                    g_appmodadm.permissions.add(model_add_perm)

            for model in MODELOS_USU:
                for permission in PERMISOS:
                    name = 'Can {} {}'.format(permission, model)
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("No se crearon los permisos '{}'.".format(name))
                        continue

                    g_usu.permissions.add(model_add_perm)

            for model in MODELOS_USUGR:
                for permission in PERMISOS:
                    name = 'Can {} {}'.format(permission, model)
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("No se crearon los permisos '{}'.".format(name))
                        continue

                    g_usugr.permissions.add(model_add_perm)

            for model in MODELOS_USUI:
                for permission in PERMISOS:
                    name = 'Can {} {}'.format(permission, model)
                    try:
                        model_add_perm = Permission.objects.get(name=name)
                    except Permission.DoesNotExist:
                        logging.warning("No se crearon los permisos '{}'.".format(name))
                        continue

                    g_usui.permissions.add(model_add_perm)
            
            resultado = "Se crearon los grupos y permisos por defecto"
            return resultado
        
        else:
            print('Debes realizar las migraciones')
            pass
        

roles().crear_roles()