from django.urls import path, include
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter
from modadm.moduloAdm.views import *
from modadm.moduloAdm.class_view import *

#from administr.views import inicio, inicio2, inicioapp, crearrol, crearmod, editarRol, crearapp, editarMod,editarApp, eliminarMod,eliminarApp
#inicio nombre de la funcion importada e viw de adminityr
"""
router = DefaultRouter()
router.register(r'permisosj', permisoViewSet)
router.register(r'modelosj', moduloViewSet)
router.register(r'rolesj', rolViewSet)
router.register(r'appsj', appViewSet)
router.register(r'funcionesj', funcionViewSet)

urlpatterns = router.urls

urlpatterns += [
"""
#    path('admin/', admin.site.urls),
#    path('',inicio,name = 'index'),
#    path('home/',Home, name = 'index'),

    # path('',home, name = 'index'),
    # path('usuarios/',UsuList.as_view(), name = 'usu'),
    #path('registro/', LoginView.as_view(template_name='registration/login.html'), name="login"),

urlpatterns = [
    path('regis/', acceder, name="regis"),

    path('inicioadmin', modadm, name="inicioadmin"),
    path('cerrar', salir, name = 'salir'),
    path('role/', iniciorol, name = 'role'),


    #usuario
    path('crearusu/',RegistroUsuario.as_view(), name = 'crear_usu'),
    path('usuarios/',UsuList.as_view(), name = 'usuarios'),
    path('editar_usu/<int:pk>/',UsuUpdate.as_view(), name='editarusu'),
    path('eliminar_usu/<int:pk>/',UsuDelete.as_view(), name='eliminarusu'),

    #infousuario
    path('crearinfo/',infopersCreate.as_view(), name = 'crearinfo'),
    path('infopers/',infoperslList.as_view(), name = 'infopers'),
    path('editarinfopers/<int:pk>/',infopersUpdate.as_view(), name='editarinfopers'),
    path('eliminarinfopers/<int:pk>/',infopersDelete.as_view(), name='eliminarinfopers'),

    #infociontacto usuario
    path('crearinfocont/',usuinfcontacCreate.as_view(), name = 'crearinfocont'),
    path('infocont/',usuinfcontacList.as_view(), name = 'infocont'),
    path('editarinfocont/<int:pk>/',usuinfcontacUpdate.as_view(), name='editarinfocont'),
    path('eliminarinfocont/<int:pk>/',usuinfcontacDelete.as_view(), name='eliminarinfocont'),

    #info academico usurio
    path('crearinfacad/',usuinfacaCreate.as_view(), name = 'crearinfacad'),
    path('infoacad/',usuinfacaList.as_view(), name = 'infoacad'),
    path('editarinfoacad/<int:pk>/',usuinfacaUpdate.as_view(), name='editarinfoacad'),
    path('eliminarinfoacad/<int:pk>/',usuinfacaDelete.as_view(), name='eliminarinfoacad'),

    #cursos dictados por el usuario
    path('crearcurs_dict/',curs_dictCreate.as_view(), name = 'crearcurs_dict'),
    path('curs_dict/',curs_dictList.as_view(), name = 'curs_dict'),
    path('editarcurs_dict/<int:pk>/',curs_dictUpdate.as_view(), name='editarcurs_dict'),
    path('eliminarcursdict/<int:pk>/',curs_dictDelete.as_view(), name='eliminarcursdict'),

    #empleos
    path('crearempleos/',empleosCreate.as_view(), name = 'crearempleos'),
    path('empleos/',empleosList.as_view(), name = 'empleos'),
    path('editarempleos/<int:pk>/',empleosUpdate.as_view(), name='editarempleos'),
    path('eliminarempleos/<int:pk>/',empleosDelete.as_view(), name='eliminarempleos'),

    #grupo
    path('crearusugr/',usugrCreate.as_view(), name = 'crearusugr'),
    path('usugr/',usugrList.as_view(), name = 'usugr'),
    path('editarusugr/<int:pk>/',usugrUpdate.as_view(), name='editarusugr'),
    path('eliminarusugr/<int:pk>/',usugrDelete.as_view(), name='eliminarusugr'),

    #ETAPAS DE GRUPO
    path('crearetapa_gr/',etapa_grCreate.as_view(), name = 'crearetapa_gr'),
    path('etapa_gr/',etapa_grList.as_view(), name = 'etapa_gr'),
    path('editaretapa_gr/<int:pk>/',etapa_grUpdate.as_view(), name='editaretapa_gr'),
    path('eliminaretapagr/<int:pk>/',etapa_grDelete.as_view(), name='eliminaretapagr'),

    #informacion grupo
    path('crearusugr_inf_gr/',usugr_inf_grCreate.as_view(), name = 'crearusugr_inf_gr'),
    path('usugr_inf_gr/',usugr_inf_grList.as_view(), name = 'usugr_inf_gr'),
    path('editarusugr_inf_gr/<int:pk>/',usugr_inf_grUpdate.as_view(), name='editarusugr_inf_gr'),
    path('eliminarusugr_inf_gr/<int:pk>/',usugr_inf_grDelete.as_view(), name='eliminarusugr_inf_gr'),

    #informacion grupo contacto
    path('crearusugr_inf_contac/',usugr_inf_contacCreate.as_view(), name = 'crearusugr_inf_contac'),
    path('usugr_inf_contac/',usugr_inf_contacList.as_view(), name = 'usugr_inf_contac'),
    path('editarusugr_inf_contac/<int:pk>/',usugr_inf_contacCreate.as_view(), name='editarusugr_inf_contac'),
    path('eliminarusugr_inf_contac/<int:pk>/',usugr_inf_contacDelete.as_view(), name='eliminarusugr_inf_contac'),



    path('aplicativo/',AplicativoList.as_view(), name = 'aplicativo'),
    path('crear_aplicativo/',AplicativoCreate.as_view(), name = 'crearaplicativo'),
    path('editar_aplicativo/<int:pk>/',AplicativoUpdate.as_view(), name='editaraplicativo'),
    path('eliminar_aplicativo/<int:pk>/',AplicativoDelete.as_view(), name='eliminaraplicativo'),

    path('permisos/',PermisoList.as_view(), name = 'permisos'),
    path('crear_permiso/',PermisosCreate.as_view(), name = 'crearpermiso'),
    path('editar_permiso/<int:pk>/',PermisosUpdate.as_view(), name='editarpermiso'),
    path('eliminar_permiso/<int:pk>/',PermisosDelete.as_view(), name='eliminarpermiso'),

    path('app/',AppList.as_view(), name = 'app'),
    path('crear_app/',AppCreate.as_view(), name = 'crearapp'),
    path('editar_app/<int:pk>/',AppUpdate.as_view(), name='editarapp'),
    path('eliminar_app/<int:pk>/',AppDelete.as_view(), name='eliminarapp'),

    path('roles/', RolList.as_view(), name = 'roles'),
    path('crear_rol/', RolCreate.as_view(), name = 'crearrol'),
    path('editar_rol/<int:pk>/', RolUpdate.as_view(), name='editarRol'),
    path('eliminar_rol/<int:pk>/',RolDelete.as_view(), name='eliminarrol'),

    #path('usuarios/',UsuList.as_view(), name = 'usu'),
#    path('crear_usu/',UsuCreate.as_view(), name = 'crearusu'),
#    path('editar_usu/<in   path('fuentes/',iniciofuentes, name = 'fuentes'),t:pk>/',UsuUpdate.as_view(), name='editarusu'),
#    path('eliminar_usu/<int:pk>/',UsuDelete.as_view(), name='eliminarusu'),

    path('modulos/',modList.as_view(), name = 'mod'),
    path('crear_mod/',modCreate.as_view(), name = 'crearmod'),
    path('editar_mod/<int:pk>/',modUpdate.as_view(), name='editarmod'),
    path('eliminar_mod/<int:pk>/',modDelete.as_view(), name='eliminarmod'),

    path('rlmodulorol/',modrolList.as_view(), name = 'modrol'),
    path('crear_modrol/',modrolCreate.as_view(), name = 'crearmodrol'),
    path('editar_modrol/<int:pk>/',modrolUpdate.as_view(), name='editarmodrol'),
    path('eliminar_modrol/<int:pk>/',modrolDelete.as_view(), name='eliminarmodrol')


#    path('fuentes/',iniciofuentes, name = 'fuentes'),
#    path('crear_fuente/',crearfuente, name = 'crearfuente'),
#    path('editar_fuente/<int:id>/',editarfuente, name='editarfuente'),
#    path('eliminar_fuente/<int:id>/',eliminarfuente, name='eliminarfuente'),

#    path('eliminar_rol/<int:id>/',eliminarRol, name='eliminarrol'),
#    path('<int:user_id>/', account_view, name="view"),

]
