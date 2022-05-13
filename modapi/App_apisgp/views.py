#Librerías del Framework Django
from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from django.template import Template,Context,loader
from django.core import serializers
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy, reverse

#librerías de SIGEPI
from modadm.App_conf.stlapp import *

# Create your views here.

class vst_api():
#Clase que procesa las vistas del API en Vue de SIGEPI-USTA
    def vst_inicio(self,solicitud):
    #función para plantilla de inicio
        stl=estilo()
        ctx=stl.DevolverDict()
        return render(solicitud,"apivue.html",ctx)

    def vst_doc(self, solicitud):
        #función para plantilla de inicio de al documentación del sistema
        respuesta='Documentación del sistema'
        return HttpResponse(respuesta)