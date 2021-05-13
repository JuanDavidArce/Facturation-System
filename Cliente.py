class Cliente:
    def __init__(self,nombre,cedula):
        self.__nombre=nombre
        self.__cedula=cedula
        self.__facturas=[]


    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevoNombre):
        self.__nombre=nuevoNombre

    @property
    def cedula(self):
        return self.__cedula

    @cedula.setter
    def cedula(self,nuevaCedula):
        self.__cedula=nuevaCedula
    
    

    