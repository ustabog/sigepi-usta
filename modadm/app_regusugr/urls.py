from django.urls import path, include
from modadm.app_regusugr.views import *
from .views import *

urlpatterns = [
    #url para crear registro de igrupo

    path('crearusugr/', vts_reg_usugr.as_view(), name = 'crear_usugr'),
    path('conusugrmod/', vts_ls_usugr.cons_gen, name = 'cons_usugr'),
    path('edit_usugr/<int:pk>/', vts_modf_usugr.as_view(), name = 'editar_usugr'),

    # ----------- CRUD CONTACTO USUARIO GRUPO DE INVERSTIGACIÓN ------------------------
    path('nvo_contact', NuevoContacto.as_view(), name = 'nvo_contact'),
    path('cons_contact', ConsultarContacto.as_view(), name = 'cons_contact'),
    path('cons_esp_contact/<int:pk>', ConsultarContacto.as_view(), name = 'cons_esp_contact'),
    path('edt_contact/<int:pk>', ModificarContacto.as_view(), name = 'edt_contact'),
    path('eli_contact', EliminarContacto.as_view(), name = 'eli_contact'),
    
    #----------- CRUD ETAPAS DEL GRUPO DE INVESTIGACION ---------------
    path('nvo_etapa', NuevaEtapa.as_view(), name = 'nvo_etapa'),
    path('cons_etapa', ConsultarEtapas.as_view(), name = 'cons_etapa'),
    path('cons_esp_etapa/<int:pk>', ConsultaEspEtapa.as_view(), name = 'cons_esp_etapa'),
    path('edt_etapa/<int:pk>', ModificarEtapa.as_view(), name = 'edt_etapa'),
    path('eli_etapa', EliminarEtapa.as_view(), name = 'eli_etapa'),

    # ----------- CRUD CURSOS DE FORMACION REALIZADOS POR EL USUARIO ------------------------
    path('nvo_curso', NuevoCurso.as_view(), name = 'nvo_curso'),
    path('cons_curso', ConsultarCurso.as_view(), name = 'cons_curso'),
    path('cons_esp_curso/<int:pk>', ConsultaEspCurso.as_view(), name = 'cons_esp_curso'),
    path('edt_curso/<int:pk>', ModificarCurso.as_view(), name = 'edt_curso'),
    path('eli_curso', EliminarCurso.as_view(), name = 'eli_curso'),

    #----------- CRUD REDES PUBLICAS DEL GRUPO ---------------
    path('nvo_redes', NuevaRed.as_view(), name = 'nvo_redes'),
    path('cons_redes', ConsultarRedes.as_view(), name ='cons_redes'),
    path('cons_esp_redes/<int:pk>', ConsultarEspRed.as_view(), name = 'cons_esp_redes'),
    path('edt_redes/<int:pk>', ModificarRed.as_view(), name = 'edt_redes'),
    path('eli_redes', EliminarRed.as_view(), name = 'eli_redes'),

    #----------- CRUD PARA USUARIOS NO REGISTRADOS EN LA PLATAFORMA --------------------------------
    path('nvo_usunr', NuevoUsuarionr.as_view(), name = 'nvo_usunr'),
    path('cons_usunr', ConsultarUsuarionr.as_view(), name ='cons_usunr'),
    path('cons_esp_usunr/<int:pk>', ConsultaEspUsuarionr.as_view(), name = 'cons_esp_usunr'),
    path('edt_usunr/<int:pk>', ModificarUsuarionr.as_view(), name = 'edt_usunr'),
    path('eli_usunr', EliminarUsuarionr.as_view(), name = 'eli_usunr'),
]