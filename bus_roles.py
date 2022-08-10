import os,ast

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
            

def ext_roles():
    roles=[]
    for dirname, dirnames, filenames in os.walk('.'):
        for filename in filenames:
            ubicacion = os.path.join(dirname,filename)
            if ubicacion[-9:]=='models.py':
                lista_roles=ext_var(ubicacion[2:],"ROL_APP")
                if lista_roles==None:
                   lista_roles=ext_var(ubicacion[2:],"ROL_BASE")        
                
                if type(lista_roles)==list:
                    for rol in lista_roles:
                        roles.append(rol[1])
    return roles

print(ext_roles())