from django.shortcuts import render

# Create your views here.

class vst_recur():
    #Clase que procesa las vistas del IU del incio de la aplicación de recursos de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        #stl=estilo()
        #ctx=stl.DevolverDict()
        return render(solicitud,"app_recur_iu.html")