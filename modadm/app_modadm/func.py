# funciones de la app modadmin  Gestión de Módulos, Aplicaciones, roles y funciones del SIGEPI
#Autor: creado por Milton O. Castro Ch.
#fecha 10-05-2022

#Creacion de permisos y grupos por defecto
#Fecha: 26/04/22
#Autor: Juan Sebastian Cely Caro

import logging
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.db import migrations
from django.db import connection

ROLES = [
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
    'mod', 'app_mod', 'listado_aplicativo', 'mod_ext', 'app_ext', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf'
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
    'mod', 'app_mod', 'listado_aplicativo', 'mod_ext', 'app_ext', 'rol', 'func_app', 'usu', 'mod_adm', 'log_acc_mod', 'log_acc_pltf',
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


#clase de instalación de módulos, aplicaciones y extensiones
class instal():
    #Instalar Módulo
    def instal_mod():
        pass
    
    #desistalar Módulo
    def desinstal_mod():
        pass

    #Instalar Aplicación
    def instal_app():
        pass

    #desistalar Aplicación
    def desinstal_app():
        pass

    #Instalar Aplicación externa
    def instal_app_ext():
        pass

    #desistalar Aplicación externa
    def desinstal_app_ext():
        pass

    #Instalar Módulo externo
    def instal_mod_ext():
        pass
    
    #desistalar Módulo externo
    def desinstal_mod_ext():
        pass

# clase para facilitar la migración automática según las dependencias del modelo base


# Funciones pendientes
#registrar funciones de aplicación
#modificar funciones de aplicación
#Eliminar funciones de aplicación
#Activar o desactivar funciones
#desinstalar Aplicación
#Instalar Extensión
#desinstalar Extensión
#registrar usuarios individuales
#registrar usuarios grupales
#registrar usuarios institucionales
#modificar usuarios individuales
#modificar usuarios grupales
#modificar usuarios institucionales
#eliminar usuarios individuales
#eliminar usuarios grupales
#eliminar usuarios institucionales
#Consultar usuarios individuales
#Consultar usuarios grupales
#Consultar usuarios institucionales
#crear roles
#Modificar permisos de roles
#Asignar permisos de roles
#Asignar roles a usuarios
#Eliminar roles de aplicación
#Respaldar datos de usuarios
#Respaldar datos de proyectos
#Respaldar datos de productos
#Repsladar datos de programas
#Vincular usuarios a grupo
#Vincular Usuarios a Instituciones
#Vincular Usuarios a Proyectos
#Vincular Proyectos a Programas
#vincular Usuarios a Productos
#Vincular Productos a Proyectos
#archivar usuarios individuales
#archivar usuarios grupales
#archivar usuarios institucionales

#ejecución
roles().crear_roles()