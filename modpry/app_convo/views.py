from django.shortcuts import render

# Create your views here.

class vst_convo():
    #Clase que procesa las vistas del IU del inicio de la aplicación de convocatorias de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_convo_iu.html")