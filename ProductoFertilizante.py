from ProductoControl import *
class ControlDeFertilizantes(ProductoControl):
    def __init__(self, registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto, fechaUltimaAplicacion):
        self.__fechaUltimaAplicacion=fechaUltimaAplicacion
        super().__init__(registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto)
    
    @property
    def fechaUltimaAplicacion(self):
        return self.__fechaUltimaAplicacion

    @fechaUltimaAplicacion.setter
    def frecuenciaDeAplicacion(self,nuevaFecha):
        self.__fechaUltimaAplicacion=nuevaFecha