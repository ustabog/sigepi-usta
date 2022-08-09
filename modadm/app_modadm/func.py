# funciones de la app modadmin  Gestión de Módulos, Aplicaciones, roles y funciones del SIGEPI
#Autor: creado por Milton O. Castro Ch.
#fecha 10-05-2022

#Creacion de permisos y grupos por defecto
#Fecha: 26/04/22
#Autor: Juan Sebastian Cely Caro

from cmath import nan
import logging
from logging.config import valid_ident
from typing_extensions import Self
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.apps import
from django.db import migrations
from django.db import connection


#Clase para modificar como administrador los modulos
class sys_mod():
    #Instalar Módulo
    def reg_mod(self):
        pass
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
        

class sys_rol():
    #crear roles
    def crear_rol(nom):
        grupo, creado =Group.objects.get_or_create(name=nom)
        if creado:
            return True
        else:
            return False
        
    #verificar roles
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
    
    def bus_rol():
        pass
        

class sys_perm():
    #Asignar permisos de roles
    def dar_perm(nom_rol,modelo,permiso):
        pass
    #"Modificar" permisos de roles
    def quitar_perm(nombre):
        pass



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
