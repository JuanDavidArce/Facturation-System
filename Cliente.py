from Factura import *

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

    @property
    def facturas(self):
        return self.__facturas

    def compraRealizada(self,factura):
        self.__facturas.append(factura)
    
    def __eq__(self, another):
        return self.__cedula==another   

    