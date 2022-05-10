#Estilos automatizados y preestablecidos de IU para SIGEPI
#creado por Milton O. Castro Ch.
#fecha 12-04-2022

ESTRUC_BASE_EST=[
    ['estilo_cuerpo',''],# cadena de instrucciones de estilo CSS de la etiqueta body
    ['estilo_cabecera',''],# cadena de instrucciones de estilo CSS de la etiqueta head
    ['estilo_menu_ppal',''],# cadena de instrucciones de estilo CSS de la etiqueta menu_ppal
    ['estilo_app',''],# cadena de instrucciones de estilo CSS de la etiqueta app app
    ['estilo_menu_app',''],# cadena de instrucciones de estilo CSS de la etiqueta menu_app
    ['estilo_panel_der',''],# cadena de instrucciones de estilo CSS de la etiqueta panel_der
    ['estilo_panel_ppal',''],# cadena de instrucciones de estilo CSS de la etiqueta panel_ppal
    ['estilo_articulo',''],# cadena de instrucciones de estilo CSS de la etiqueta articulo
    ['estilo_panel_iz',''],# cadena de instrucciones de estilo CSS de la etiqueta panel_iz
    ['estilo_pie_app',''],# cadena de instrucciones de estilo CSS de la etiqueta footer
    ['estilo_pie',''],# cadena de instrucciones de estilo CSS de la etiqueta pie
    ['estilo_pie_extra','']# cadena de instrucciones de estilo CSS de la etiqueta pie_extra
    ];

ESTRUC_BASE_CLASES=[
    ['clase_cuerpo',''],
    ['clase_cabecera',''],
    ['clase_menu_ppal',''],
    ['clase_app',''],
    ['clase_menu_app',''],
    ['clase_panel_der',''],
    ['clase_panel_ppal',''],
    ['clase_articulo',''],
    ['clase_panel_iz',''],
    ['clase_pie_app',''],
    ['clase_pie','pie-pag'],
    ['clase_pie_extra','']
    ];

class estilo():
    """Crea un objeto del tipo estilo que permite pasar los parámetros
    de una interfaz de usuario acorde con al estructura de SIGEPI"""

    def __init__(self):
        #inicializa la instancia de clase con los valores inciales
        self.ebe=ESTRUC_BASE_EST;
        self.ebc=ESTRUC_BASE_CLASES;
        self.clase_cuerpo='';
        self.clase_cabecera='';
        self.clase_menu_ppal='';
        self.clase_app='';
        self.clase_menu_app='';
        self.clase_panel_der='';
        self.clase_panel_ppal='';
        self.clase_articulo='';
        self.clase_panel_iz='';
        self.clase_pie_app='';
        self.clase_pie='';
        self.clase_pie_extr='';
        self.estilo_cuerpo='';
        self.estilo_cabecera='';
        self.estilo_menu_ppal='';
        self.estilo_app='';
        self.estilo_menu_app='';
        self.estilo_panel_der='';
        self.estilo_panel_ppal='';
        self.estilo_articulo='';
        self.estilo_panel_iz='';
        self.estilo_pie_app='';
        self.estilo_pie='';
        self.estilo_pie_extr='';
        self.estilo_base();

    def DevolverTxt(self):
        #devuelve los valores de estilo y clase de los componentes como un contexto para la plantilla de django.
        contexto_lista=self.ebc+self.ebe;
        texto='';
        num_filas=len(contexto_lista);
        contador=0;
        for fila in contexto_lista:
            contador += 1;
            #if contador == 1:
            #    texto='<script type="text/javascript"> var ';
            if contador!= num_filas:
                linea= "{{\'"+fila[0]+"'"+':'+"\'"+fila[1]+"\'}}";
            else:
                linea= "{{\'"+fila[0]+"\'"+':'+"\'"+fila[1]+"\'}}";
            texto=texto+linea
        #texto= texto +'</script>'
        #print(texto)
        return (texto)

    def DevolverDict(self):
        #devuelve los valores de estilo y clase de los componentes como un contexto para la plantilla de django.
        contexto_lista=self.ebc+self.ebe;
        num_filas=len(contexto_lista);
        contador=0;
        dicc={}
        for fila in contexto_lista:
            dicc[fila[0]]=fila[1]
            contador=+ 1
        #print(dicc)
        return (dicc)

    def DevolverProp(self):
        #devuelve los valores de estilo y clase de los componentes como un contexto para la plantilla de django.
        contexto_lista=self.ebc+self.ebe;
        #print(contexto_lista)
        return (contexto_lista)

    def estilo_base(self):
        #devuelve un contexto con el estilo base tomando la configuración de clases css de sigepi.css
        #contexto_lista=self.ebc+self.ebe
        self.ebe[0][1]=self.estilo_cuerpo='';
        self.ebe[1][1]=self.estilo_cabecera='';
        self.ebe[2][1]=self.estilo_menu_ppal='';
        self.ebe[3][1]=self.estilo_app='';
        self.ebe[4][1]=self.estilo_menu_app='';
        self.ebe[5][1]=self.estilo_panel_der='';
        self.ebe[6][1]=self.estilo_panel_ppal='';
        self.ebe[7][1]=self.estilo_articulo='';
        self.ebe[8][1]=self.estilo_panel_iz='';
        self.ebe[9][1]=self.estilo_pie_app='';
        self.ebe[10][1]=self.estilo_pie='';
        self.ebe[11][1]=self.estilo_pie_extr='';
        self.ebc[0][1]=self.clase_cuerpo='cuerpo';
        self.ebc[1][1]=self.clase_cabecera='cabecera';
        self.ebc[2][1]=self.clase_menu_ppal='menu_ppal';
        self.ebc[3][1]=self.clase_app='app';
        self.ebc[4][1]=self.clase_menu_app='menu_app';
        self.ebc[5][1]=self.clase_panel_der='panel_der';
        self.ebc[6][1]=self.clase_panel_ppal='panel_ppal';
        self.ebc[7][1]=self.clase_articulo='articulo';
        self.ebc[8][1]=self.clase_panel_iz='panel_iz';
        self.ebc[9][1]=self.clase_pie_app='pie_app';
        self.ebc[10][1]=self.clase_pie='pie';
        self.ebc[11][1]=self.clase_pie_extr='pie_extr';
        #return(self)

    def prueba_estl(self):
        #función para probar las funcionalidades de la función
        est=estilo()
        est.DevolverTxt()
        est.DevolverDict()

#estilo().prueba_estl()
