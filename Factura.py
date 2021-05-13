from ProductoFertilizante import *
from ProductoPlaga import *
from Antibiotico import *

class Factura:
    def __init__(self,fecha,valorTotal,producto):
        self.__fecha=fecha
        self.__valorTotal=valorTotal
        self.__producto=producto

    @property
    def fecha(self):
        return self.__fecha

    @fecha.setter
    def fecha(self,nuevaFecha):
        self.__fecha=nuevaFecha
    
    @property
    def valorTotal(self):
        return self.__valorTotal

    @valorTotal.setter
    def valorTotal(self,nuevoValor):
        self.__valorTotal=nuevoValor

    @property
    def producto(self):
        return self.__producto

    @producto.setter
    def producto(self,nuevoProducto):
        self.__producto=nuevoProducto

    def mostrarCaracteristicas(self):
        print("Fecha :",self.__fecha )
        print("Valor total", self.__valorTotal)
        print("Producto: ",self.__producto.nombreDeProducto)
        