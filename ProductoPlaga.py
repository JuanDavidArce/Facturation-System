from ProductoControl import *
class ControlDePlagas(ProductoControl):
    def __init__(self, registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto, periodoDeCarencia):
        self.__periodoDeCarencia=periodoDeCarencia
        super().__init__(registroIca, nombreDeProducto, frecuenciaDeAplicacion, valorDelProducto)
    
    @property
    def periodoDeCarencia(self):
        return self.__periodoDeCarencia
        
    @periodoDeCarencia.setter
    def periodoDeCarencia(self,nuevoPeriodo):
        self.__periodoDeCarencia=nuevoPeriodo