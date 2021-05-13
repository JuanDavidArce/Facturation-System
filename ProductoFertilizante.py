from ProductoControl import *
class ControlDeFertilizantes(ProductoControl):
    def __init__(self, registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto, fechaUltimaAplicacion):
        self.__fechaUltimaAplicacion=fechaUltimaAplicacion
        super().__init__(registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto)
    
    @property
    def frecuenciaDeAplicacion(self):
        return self.__frecuenciaDeAplicacion
        
    @frecuenciaDeAplicacion.setter
    def frecuenciaDeAplicacion(self,nuevaFrecuencia):
        self.__frecuenciaDeAplicacion=nuevaFrecuencia