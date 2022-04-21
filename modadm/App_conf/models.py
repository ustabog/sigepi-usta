#Modelos apra la configuración de la Interfaz de Usuario (IU) para SIGEPI
#creado por: Milton O. Castro Ch.
#fecha: 15-04-2022
#Versión: 0.1.04.22


from django.db import models


class conf_iu(models.Model):
    #clase que almacena la información de los parámetros de configuración de la Interfaz de Usuario
    # conforme a los manuales de imagen corporativa de las Instituciones de investigación o IES
    id_tema = models.AutoField(primary_key=True) # identificado único de programa.

    class Meta:
        verbose_name = 'tema'
        verbose_name_plural = 'temas'
