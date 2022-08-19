# funciones de la app modadmin  Gestión de Módulos, Aplicaciones, roles y funciones del SIGEPI
#Autor: creado por Milton O. Castro Ch.
#fecha 10-05-2022

#Creacion de modelos 
#Fecha: 11/08/22
#CoAutor: Brallan Andres Laverde Perez

import sys,ast,os
import logging
from django.db import models
from django.contrib.auth.models import Group
from modadm.app_modadm.models import adm_app, adm_mod
from django.apps import apps


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
    
    #funcion que compara dos versiones devuelve TRUE si v1 > v2 si no FALSE 
    def comp_ver(ver1,ver2):
        ver1 = ver1.split(".")
        ver2 = ver2.split(".")
        if len(ver1)<2:
            ver1.append(0)
        if len(ver2)<2:
            ver2.append(0)
        for i in range(2):
            print("s")
            if ver1[i] < ver2[i]:
                return True
        return False
        


#Clase para modificar como administrador los modulos
class sys_mod():

    #Funcion que registra los diccionarios descritos en los modelos de las aplicaciones base de los modulos
    def reg_mod():
        respuesta=""
        # Ciclo que recorre cada uno de los archivos de SIGEPI
        for dirname, dirnames, filenames in os.walk('.'): 
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)

                #Solo se trabajan con aquellos archivos cuyo fichero terminen en models.py
                if ubicacion[-9:]=='models.py': 
                    inf_mod=sys_utils.ext_var(ubicacion[2:],"INF_MOD")#Busca la lista INF_MOD utilizado el extractor de variables

                    #El fichero contiene una diccionario INF_MOD?
                    if inf_mod!= None:

                        #clase adm_mod con los datos correspondientes a cada campos
                        p=adm_mod(titulo=(inf_mod[0])[1],nom=(inf_mod[1])[1],desc=(inf_mod[2])[1],url_doc=(inf_mod[3])[1],version=(inf_mod[4])[1],activo=(inf_mod[5])[1],instalado=(inf_mod[6])[1],externo=(inf_mod[7])[1],visible=(inf_mod[8])[1],ls_param_cnf=(inf_mod[9])[1])

                        #El aplicativo en el que esta el modulo esta instalada?
                        if sys_app.val_inst_app((inf_mod[1])[1]+"."+"app_"+(inf_mod[1])[1]):

                            #Existe un modulo con mismo titulo y nombre?
                            if sys_mod.val_mod((inf_mod[0])[1],nom=(inf_mod[1])[1]) > 0:

                                #Código que obtiene los datos del modulo con mismos datos en titulo y nombre ordenados por identificador
                                mod_data=(adm_mod.objects.filter(titulo=((inf_mod[0])[1]), nom=((inf_mod[1])[1])).order_by('-id_mod').values())[0]
                                version=mod_data.get('version')
                                # la version del modulo a registrar es igual o menor que el regstrado?
                                if sys_utils.comp_ver(version,(inf_mod[4])[1]):
                                    p.save()
                                    respuesta+=("<p> se ha registrado el "+(inf_mod[0])[1]+" Satisfactoriamente - En la version:"+(inf_mod[4])[1]+"</p>" )
                                    
                                else:
                                    respuesta+=("<p>El "+(inf_mod[0])[1]+" a registrar debe ser de una version superior </p>")
                            else:
                                
                                p.save()

                                respuesta+=("<p> se ha registrado el "+(inf_mod[0])[1]+" Satisfactoriamente </p>" )
                        else:
                            respuesta+=("<p> El "+(inf_mod[0])[1]+"pertenece a una aplicacion no instalada</p>")
        
        return respuesta
                        
                            
    #Validar existencia de Módulo
    def val_mod(titulo,nom):
        id=None
        num_regs=adm_mod.objects.filter(titulo=titulo, nom=nom),
        if num_regs!=0:
            id=adm_mod.objects.filter(titulo=titulo, nom=nom).values().get('id')
        return num_regs,id



#Clase para modificar como administrador las aplicaciones
class sys_app():
    #Instalar Aplicación
    def reg_app():

        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)
                if ubicacion[-9:]=='models.py':
                    nom_mod=ubicacion.split("/")[-3]

                    if(adm_mod.objects.filter(nom=nom_mod).exists()):

                        inf_mod=adm_mod.objects.filter(nom=nom_mod).order_by('-id_mod').values()[0]

                        inf_app = sys_utils.ext_var(ubicacion[2:],"INF_APP")

                        if inf_app != None:

                            id_mod=inf_mod.get('id_mod')
                            
                            for i in range(len(inf_app)):

                               nom_var=str(inf_app[i][0])
                               globals()[nom_var]=inf_app[i][1]
                               
                    else:
                        print("modulo que contiene a la aplicacion no esta instalado")
                    
                   
                            
    #desistalar Aplicación
    def val_inst_app(nom):
        return apps.is_installed(nom)

        

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



#sys_mod.val_mod("Módulo de Administración SIGEPI","modadm")
#sys_mod.reg_mod()
sys_app.reg_app()



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
