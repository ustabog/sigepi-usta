# App Registro de usuarios institucionales - Funciones para SIGEPI
#Autor: Laura Sofía Rodríguez Castillo - ORCID: 0000-0001-7873-8716
# Coautor(a): Milton O. Castro Ch.
#fecha 08-07-2022

# Funciones de la aplicación

import random
from modadm.app_regusui.models import usui
from django.contrib.auth.models import User
# Funciones de la aplicación
def reg_usu(datos):
    pass

def gen_nom_usui(nombre,apellido,institucion):
    nombre = nombre.split(" ")
    apellido = apellido.split(" ")
    numero = random.randint(0,99)

    #Caso 1 Nombre + Apellido
    usuario = nombre[0]+apellido[0]+"."+institucion

    if esta_usui_reg(usuario) is not True:
        return usuario

    #Caso 2 Nombre + Apellido + Inicial Segundo Apellido
    if len(apellido) > 1:
        apellido_ini = apellido[1][0]
        usuario = nombre[0]+apellido[0]+apellido_ini+"."+institucion
        
        if esta_usui_reg(usuario) is not True:
            return usuario
    
    #Caso 3 Nombre + Apellido + Num Aleatorio
    usuario = nombre[0]+apellido[0]+str(numero)+"."+institucion
    return usuario
       
    
def esta_usui_reg(usuario):
   return User.objects.filter(username=usuario).exists()

#Agregar inf. de acceso al sistema de Usuario institucional
#Modificar inf. de acceso al sistema de Usuario institucional
#Archivar inf. de acceso al sistema de Usuario institucional
#Eliminar inf. de acceso al sistema de Usuario institucional
#Consultar inf. de acceso al sistema de Usuario institucional
#Listar inf. de acceso al sistema de Usuario institucional
#Agregar inf. del rol por aplicación del Usuario institucional
#Modificar inf. del rol por aplicación del Usuario institucional
#Archivar inf. del rol por aplicación del Usuario institucional
#Eliminar inf. del rol por aplicación del Usuario institucional
#Consultar inf. del rol por aplicación del Usuario institucional
#Listar inf. del rol por aplicación del Usuario institucional
#Agregar inf. de Usuario institucional
#Modificar inf. de Usuario institucional
#Archivar inf. de Usuario institucional
#Eliminar inf. de Usuario institucional
#Consultar inf. de Usuario institucional
#Listar inf. de Usuario institucional
#Agregar inf. de contacto de Usuario institucional
#Modificar inf. de contacto de Usuario institucional
#Archivar inf. de contacto de Usuario institucional
#Eliminar inf. de contacto de Usuario institucional
#Consultar inf. de contacto de Usuario institucional
#Listar inf. de contacto de Usuario institucional
#Agregar inf. de programas ofertados por el Usuario institucional
#Modificar inf. de programas ofertados por el Usuario institucional
#Archivar inf. de programas ofertados por el Usuario institucional
#Eliminar inf. de programas ofertados por el Usuario institucional
#Consultar inf. de programas ofertados por el Usuario institucional
#Clonar inf. de programas ofertados por el Usuario institucional
#Listar inf. de programas ofertados por el Usuario institucional
#Agregar inf. de convocatorias de investigación
#Modificar inf. de convocatorias de investigación
#Archivar inf. de convocatorias de investigación
#Eliminar inf. de convocatorias de investigación
#Consultar inf. de convocatorias de investigación
#Clonar inf. de convocatorias de investigación
#Listar inf. de convocatorias de investigación
#Listar los Usuarios institucionales registrados en el sistema
#importar inf. de usuario institucional csv
