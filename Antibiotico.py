class Antibiotico:
    def __init__(self, nombreDeProducto,dosis,tipoDeAnimal,precio):
        self.__nombreDeProducto=nombreDeProducto
        self.__dosis=dosis
        self.__tipoDeAnimal=tipoDeAnimal
        self.__precio=precio

    @property
    def nombreDeProducto(self):
        return self.__nombreDeProducto

    @nombreDeProducto.setter
    def nombreDeProducto(self,nuevoNombre):
        self.__nombreDeProducto=nuevoNombre

    @property
    def dosis(self):
        return self.__dosis

    @dosis.setter
    def dosis(self,nuevaDosis):
        self.__dosis=nuevaDosis

    @property
    def tipoDeAnimal(self):
        return self.__tipoDeAnimal

    @tipoDeAnimal.setter
    def tipoDeAnimal(self,nuevoTipo):
        self.__tipoDeAnimal=nuevoTipo
    
    @property 
    def precio(self):
        return self.__precio
    @precio.setter
    def precio(self,nuevoPrecio):
        self.__precio=nuevoPrecio
        