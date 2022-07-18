from django.shortcuts import render

# Create your views here.

class vst_gespry():
    #Clase que procesa las vistas del IU del inicio de la aplicación de gestión de proyectos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_gespry_iu.html")