class ProductoControl:
    def __init__(self,registroIca,nombreDeProducto,frecuenciaDeAplicacion,valorDelProducto):
        self.__registroIca=registroIca
        self.__nombreDeProducto=nombreDeProducto
        self.__frecuenciaDeAplicacion=frecuenciaDeAplicacion
        self.__valorDelProducto=valorDelProducto
    
    @property
    def registroIca(self):
        return self.__registroIca

    @registroIca.setter
    def registroIca(self,nuevoRegistro):
        self.__registroIca=nuevoRegistro

    @property
    def nombreDeProducto(self):
        return self.__nombreDeProducto

    @nombreDeProducto.setter
    def nombreDeProducto(self,nuevoNombre):
        self.__nombreDeProducto=nuevoNombre

    @property
    def frecuenciaDeAplicacion(self):
        return self.__frecuenciaDeAplicacion

    @frecuenciaDeAplicacion.setter
    def frecuenciaDeAplicacion(self,nuevaFrecuencia):
        self.__frecuenciaDeAplicacion=nuevaFrecuencia
        
    @property
    def valorDelProducto(self):
        return self.__valorDelProducto

    @valorDelProducto.setter
    def valorDelProducto(self,nuevoValor):
        self.__valorDelProducto=nuevoValor
        