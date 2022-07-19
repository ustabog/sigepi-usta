# App de consultas genéricas funciones para SIGEPI
#Autor: Milton O. Castro Ch.
# Coautor(a): Laura Sofía Rodríguez
#fecha 06-07-2022

DIAS =[
    (0, 'Lunes'),
    (1, 'Martes'),
    (2, 'Miércoles'),
    (3, 'Jueves'),
    (4, 'Viernes'),
    (5, 'Sábado')
]

HORARIO = [
    (0,'8am-12m'),
    (1,'2pm-6pm'),
    (1,'8am-10am'),
    (1,'10am-12m'),
    (1,'2pm-4pm'),
    (1,'4pm-6pm'),
    (1,'2pm-6pm'),
    (1,'6pm-8pm'),
    (2,'8am-12pm;2pm-6pm')
    ]

UNIDAD_MED_TIEM = [
    (0, 'Seg'),
    (1, 'Min'),
    (2, 'Horas'),
    (3, 'Meses'),
    (4, 'Años')
    ]

class ubicacion():
    #Clase que agrupa las funciones de ubicación, dirección , seleeción de unidades geográficas
    def direccion(self):
        #Funcion para devolver una dirección seleccionando unidades geográficas de mayor a menor
        direccion1= 'Colombia'
        return direccion1