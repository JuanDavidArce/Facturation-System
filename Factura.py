class Factura:
    def __init__(self,fecha,valorTotal):
        self.__fecha=fecha
        self.__valorTotal=valorTotal

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