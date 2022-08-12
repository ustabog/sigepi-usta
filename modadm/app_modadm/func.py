# funciones de la app modadmin  Gestión de Módulos, Aplicaciones, roles y funciones del SIGEPI
#Autor: creado por Milton O. Castro Ch.
#fecha 10-05-2022

#Creacion de permisos y grupos por defecto
#Fecha: 11/08/22
#CoAutor: Brallan Andres Laverde Perez

import sys,ast,os
import logging
from django.contrib.auth.models import Group
from modadm.app_modadm.models import adm_mod


#Clase con algoritmos utiles para el funcionamiento de func.py
class sys_utils():

    # extraer variables de python sin ejecutar el script, requiere la ubicacion del archivo y nombre de variable
    def ext_var(mod_path, variable, default=None, *, raise_exception=False):
        ModuleType = type(ast)
        with open(mod_path, "r", encoding='UTF-8') as file_mod:
            data = file_mod.read()

        ast_data = ast.parse(data, filename=mod_path)
        
        if ast_data:
            for body in ast_data.body:
                if body.__class__ == ast.Assign:
                    if len(body.targets) == 1:
                        if getattr(body.targets[0], "id", "") == variable:
                            return ast.literal_eval(body.value)
        return default
            


#Clase para modificar como administrador los modulos
class sys_mod():
    #Instalar Módulo
    def reg_mod():
        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)
                if ubicacion[-9:]=='models.py': 
                    inf_mod=sys_utils.ext_var(ubicacion[2:],"INF_MOD")
                    if inf_mod!= None:
                        p=adm_mod(titulo=(inf_mod[0])[1],desc=(inf_mod[1])[1],url_doc=(inf_mod[2])[1],version=(inf_mod[3])[1],activo=(inf_mod[4])[1],instalado=(inf_mod[5])[1],externo=(inf_mod[6])[1],visible=(inf_mod[7])[1],ls_param_cnf=(inf_mod[8])[1]) 
                        p.save()
                        respuesta ='Módulos registrados correctamente'
                        return respuesta
             
            
            
    #Desinstalar Módulo
    def val_mod(self):
        pass


#Clase para modificar como administrador las aplicaciones
class sys_app():
    #Instalar Aplicación
    def reg_app(self):
        pass
    #desistalar Aplicación
    def val_app(self):
        pass
        

#Clase para realizar acciones de creacion consulta y actualizacion de grupos en el administrador de DJANGO
class sys_rol():

    #crea roles en el administrador de DJANGO a partir de un nombre tipo String
    def crear_rol(nom):
        creado =Group.objects.get_or_create(name=nom)
        if creado:
            return True
        else:
            return False
        
    #verificar la existencia de un rol en el administrador de DJANGO por su nombre
    def val_rol(nom):
        x =Group.objects.filter(name=nom).count()
        if x == 1:
            return True
        else:
            return False

    #Eliminar roles de aplicación
    def quitar_rol(nom):
        if Self.val_rol(nom):
            print("Ya existe el rol "+nom+" registrado en el administrador")
        else:
            Group.objects.filter(name=nom).delete()
    
    #Actualiza los roles en el administrador de DJANGO sean nuevos, editados o removidos por una accion con la aplicación 
    def act_rol():

        roles_registrados=[] #roles que ya estan en el administrador de DJANGO
        roles_encontrados=sys_rol.ext_roles() #roles encontrados en archivos de modelos
        
        #asignacion de valores a la variable roles_registrados
        for nom_rol in Group.objects.all():
            roles_registrados.append(nom_rol.name)

        for rol in range(len(roles_encontrados)):
            if sys_rol.val_rol(roles_encontrados[rol]):
                print("Encontrado en el administrador ["+roles_encontrados[rol]+ "] no se guardara de nuevo.. \n")
            else:
                sys_rol.crear_rol(roles_encontrados[rol])
                

    #extrae listados de nombres de roles contenidos en los archivos models.py de las apps incluidas en SIGEPI
    def ext_roles():
        roles=[]
        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)
                if ubicacion[-9:]=='models.py':
                    lista_roles=sys_utils.ext_var(ubicacion[2:],"ROL_APP")
                    if lista_roles==None:
                        lista_roles=sys_utils.ext_var(ubicacion[2:],"ROL_BASE")        
                    
                    if type(lista_roles)==list:
                        for rol in lista_roles:
                            roles.append(rol[1])
        return roles


        

#Clase para gestionar permisos en el administrador de DJANGO
class sys_perm():
    #Asignar permisos de roles
    def dar_perm(nom_rol,modelo,permiso):
        pass
    #"Modificar" permisos de roles
    def quitar_perm(nombre):
        pass

sys_mod.reg_mod()

#clase de instalación de módulos, aplicaciones y extensiones
#Instalar Aplicación externa
#desistalar Aplicación externa
#Instalar Módulo externo
#desistalar Módulo externo

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
#Modificar permisos de roles
#Asignar roles a usuarios
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
