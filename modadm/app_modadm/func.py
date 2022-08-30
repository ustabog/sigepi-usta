# funciones de la app modadmin  Gestión de Módulos, Aplicaciones, roles y funciones del SIGEPI
#Autor: creado por Milton O. Castro Ch.
#fecha 10-05-2022

#Creacion de funciones de registro - MODULOS OK, APPS OK, ROLES en_proceso
#Fecha: 19/08/22
#CoAutor: Brallan Andres Laverde Perez ORCID:0000-0002-6173-0301

from operator import iconcat
from sqlite3 import IntegrityError
import sys,ast,os
import logging
from urllib import request
from django.db import models, utils
from django.contrib.auth.models import Group, User
from modadm.app_modadm.models import adm_app, adm_func, adm_mod, adm_rol
from django.apps import apps


INF_FUNC=[
    {"nom_func":'reg_mod',"desc_func":'Aplicacion que registra en el modelo mod_adm los modulos descritos en Sigepi',"url_loc":'#',"com_exc":'sys_mod.reg_mod()',"context":'Registrar modulos',"ico":'Source'},

    {"nom_func":'ext_var',"desc_func":'Función que devuelve un variable de un archivo de python sin ejecutarlo',"url_loc":'#',"com_exc":'sys_utils.ext_var()',"context":'Extraer variable',"ico":'DataArray'},

    {"nom_func":'comp_ver',"desc_func":'Función que compara dos versiones devuelve TRUE si v1 > v2 si no FALSE ',"url_loc":'#',"com_exc":'sys_utils.comp_ver()',"context":'Comparar versiones',"ico":'Balance'},

    {"nom_func":'val_mod',"desc_func":'Función que devuelve el número de modulos registrados en el modelo adm_mod',"url_loc":'#',"com_exc":'sys_mod.val_mod()',"context":'Validar existencia del modulo',"ico":'Pageview'},

    {"nom_func":'reg_app',"desc_func":'Función que extrae la informacion de INF_APP y la registra en los modelos ',"url_loc":'#',"com_exc":'sys_app.reg_app()',"context":'Registrar aplicaciones',"ico":'AppShortcut'},

    {"nom_func":'val_inst_app',"desc_func":'Funcion que devuelve un True si se han hecho las migraciones de la aplicacion dada como parametro de entrada',"url_loc":'#',"com_exc":'sys_app.val_inst_app()',"context":'Registrar aplicaciones',"ico":'AppShortcut'},

    {"nom_func":'val_app',"desc_func":'Funcion que devuelve un True si existe una aplicación con el nombre dado como parametro de entrada',"url_loc":'#',"com_exc":'sys_app.val_app(nom)',"context":'Validar aplicación',"ico":'SystemSecurityUpdateGood'},
    
    {"nom_func":'reg_roles',"desc_func":'Funcion que extrae los roles definidos en la listas ROL_APP y los almacena en el modelo modadm_rol',"url_loc":'#',"com_exc":'sys_rol.reg_roles()',"context":'Registrar Roles',"ico":'PersonSearch'}

]


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
            if ver1[i] < ver2[i]:
                return True
        return False
        


#Clase para modificar como administrador los modulos
class sys_mod():

    #Funcion que registra los diccionarios descritos en los modelos de las aplicaciones base de los modulos
    def reg_mod():
        respuesta="<h5> Resumen de Modulos</h5>"
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
        num_regs=adm_mod.objects.filter(titulo=titulo, nom=nom).count()
        return num_regs



#Clase para modificar como administrador las aplicaciones
class sys_app():
    #Instalar Aplicación
    def reg_app():

        respuesta="<h5> Resumen de Aplicaciones</h5>"

        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)
                if ubicacion[-9:]=='models.py':
                    nom_mod=ubicacion.split("/")[-3]
                    nom_app=ubicacion.split("/")[-2]

                    if(adm_mod.objects.filter(nom=nom_mod).exists()):

                        inf_mod=adm_mod.objects.filter(nom=nom_mod).order_by('-id_mod').values()[0]

                        inf_app = sys_utils.ext_var(ubicacion[2:],"INF_APP")

                        if inf_app != None:
                            
                            campos=[f.name for f in adm_app._meta.get_fields()]
                            dic=sys_utils.ext_var("./modadm/app_modadm/dic.py","TIPO_APP")
                            
                            dict_val = {}

                            for i in range(len(campos)):
                                for j in range(len(inf_app)):
                                    if(campos[i]==inf_app[j][0]):
                                        dict_val[campos[i]]=inf_app[j][1]
                                        break
                                    else:
                                        dict_val[campos[i]]=None
                                        
                                        
                            for i in range(len(dic)):
                                if dict_val["tipo_app"] == (dic[i])[1]:
                                    dict_val["tipo_app"] = (dic[i])[0]
                                    


                            id_mod=inf_mod.get('id_mod')   
                               
                            p=adm_app(nom=dict_val["nom"],titulo=dict_val["titulo"],desc=dict_val["desc"],url_doc=dict_val["url_doc"],url_instal=dict_val["url_instal"],url_pl=dict_val["url_pl"],nom_url=dict_val["nom_url"],version=dict_val["version"],ver_mod=dict_val["ver_mod"],activo=dict_val["activo"],instalada=dict_val["instalada"],visible=dict_val["visible"],externa=dict_val["externa"],tipo_app=dict_val["tipo_app"],ico=dict_val["ico"],id_mod_id=id_mod)
                            
                            if(sys_app.val_app(dict_val["nom"])):
                                act_ver = (adm_app.objects.filter(nom=dict_val["nom"]).values().order_by("-id_app"))[0].get('version')
                                if sys_utils.comp_ver(act_ver,dict_val["version"]):
                                    try:
                                        p.save()
                                        respuesta+="<p>El aplicativo ["+dict_val["nom"]+"] ha sido registrado con version "+dict_val["version"]+" version anterior "+act_ver+"</p>"
                                    except utils.IntegrityError:
                                        respuesta+="<p>Faltan datos o son erroneos para el registro del modulo, ERROR DE INTEGRIDAD, el aplicativo ["+dict_val["nom"]+"] NO se registro</p>"

                                else:
                                    respuesta+="<p>Ya se encuentra registrada["+dict_val["nom"]+"] con una version igual o superior,el aplicativo ["+dict_val["nom"]+"] NO se registro</p>"
                            else:
                                try:
                                    p.save()
                                    respuesta+="<p>El aplicativo ["+dict_val["nom"]+"] ha sido registrado</p>"
                                except utils.IntegrityError:
                                    respuesta+="<p>Faltan datos o son erroneos para el registro del modulo, ERROR DE INTEGRIDAD, el aplicativo ["+dict_val["nom"]+"] NO se registro</p>"

                             
                    else:
                        respuesta+="<p>se encontraron datos en los modelos de aplicacion ["+nom_app+"] pero el el modulo no ha sido instalado</p>"


        return respuesta           
                            
    #validar migracion
    def val_inst_app(nom):
        return apps.is_installed(nom)

    #validar existencia de Aplicación
    def val_app(nom):
        return adm_app.objects.filter(nom=nom).exists()

        

#Clase para realizar acciones de creacion consulta y actualizacion de grupos en el administrador de DJANGO
class sys_rol():

    #crea roles en el administrador de DJANGO a partir de un nombre tipo String
    #verificar la existencia de un rol en el administrador de DJANGO por su nombre
    #Actualiza los roles en el administrador de DJANGO sean nuevos, editados o removidos por una accion con la aplicación 
   
                

    #extrae listados de nombres de roles contenidos en los archivos models.py de las apps incluidas en SIGEPI
    def reg_roles():

        respuesta = "<h5>Registro de roles</h5>"

        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)
                if ubicacion[-9:]=='models.py':
                  
                    lista_roles = sys_utils.ext_var(ubicacion[2:],'ROL_APP')
                                
                    if lista_roles != None:
                        nom_mod=ubicacion.split("/")[-3]
                        nom_app=ubicacion.split("/")[-2]
                        
                        id_mod=(adm_mod.objects.filter(nom=nom_mod).order_by("-id_mod").values()[0]).get('id_mod')
                        id_app=(adm_app.objects.filter(nom=nom_app).order_by("-id_app").values()[0]).get('id_app')
                        
                        for i in range(len(lista_roles)):
                            
                            print((lista_roles[i])[1])
                            grupo = Group(name=(lista_roles[i])[1])
                            p=adm_rol(id_gru=grupo,etq_rol=(lista_roles[i])[0],desc=(lista_roles[i])[1],req_reg=(lista_roles[i])[2],id_app_id=id_app,id_mod_id=id_mod,tipo=(lista_roles[i])[3])  

                            if Group.objects.filter(name=(lista_roles[i])[1]).count()>0:
                                respuesta +=("<p>ERROR: El Rol ["+str((lista_roles[i])[1])+"] de la aplicación ["+nom_app+"] tiene conflictos con un rol del mismo nombre, ATRIBUTO UNICO!</p>")
                            else:
                                try:
                                    grupo.save()
                                    p.save()
                                    respuesta +=("<p> El Rol ["+str((lista_roles[i])[1])+"] de la aplicación ["+nom_app+"] ha sido registrado</p>")
                                except utils.IntegrityError:
                                    respuesta +=("<p>ERROR: El Rol ["+str((lista_roles[i])[1])+"] de la aplicación ["+nom_app+"] presento errores de integridad</p>") 
                        
        return respuesta



def rutina_prueba():
    a=''
    a+=sys_mod.reg_mod()
    a+=sys_app.reg_app()
    a+=sys_rol.reg_roles()
    print(a)
    return a
    

#Clase para gestionar permisos en el administrador de DJANGO
class sys_perm():
    #Asignar permisos de roles
    def dar_perm(nom_rol,modelo,permiso):
        pass
    #"Modificar" permisos de roles
    def quitar_perm(nombre):
        pass



#sys_mod.val_mod("Módulo de Administración SIGEPI","modadm")



#clase de instalación de módulos, aplicaciones y extensiones
#Instalar Aplicación externa
#desistalar Aplicación externa
#Instalar Módulo externo
#desistalar Módulo externo

# clase para facilitar la migración automática según las dependencias del modelo base
class sys_func():
    def reg_func():
        for dirname, dirnames, filenames in os.walk('.'): 
            for filename in filenames:
                ubicacion = os.path.join(dirname,filename)

                #Solo se trabajan con aquellos archivos cuyo fichero terminen en func.py  
                if ubicacion[-7:]=='func.py': 
                    inf_func=sys_utils.ext_var(ubicacion[2:],"INF_FUNC")#Busca la lista INF_FUNC utilizado el extractor de variables

                    #El fichero contiene una diccionario INF_FUNC?
                    if inf_func!= None:

                        #Recorrer INF_FUNC donde cada elemento es una función
                        for i in range(len(inf_func)):

                            func=inf_func[i]

                            #Obtencion de la ruta de la función
                            lib_func=ubicacion
                            nom_app=ubicacion.split("/")[-2]

                            #Información suministrada por el usuario
                            nom_func=func['nom_func']
                            url_loc=func['url_loc']
                            com_exc=func['com_exc']
                            context=func['context']
                            ico=func['ico']
                            desc_func=func['desc_func']
                            id_app=(adm_app.objects.filter(nom=nom_app).order_by("-id_app").values()[0]).get('id_app')

                            if adm_func.objects.filter(nom_func=nom_func,lib_func=lib_func).exists():
                                print("LA FUNCION YA ESTA REGISTRADA")
                            else:
                                p=adm_func(nom_func=nom_func,url_loc=url_loc,com_exc=com_exc,context=context,ico=ico,lib_func=lib_func,id_app_id=id_app,desc_func=desc_func)
                                p.save()
                  
        return 

rutina_prueba()
sys_func.reg_func()

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
