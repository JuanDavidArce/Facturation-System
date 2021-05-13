from UI import *
from Cliente import *
from Factura import *

def main():
    registroClientes=[]
    mensajeDeBienvenida()
    while True:
        menuDeOpciones()
        elecccion=int(input())

        if elecccion==1:
            datosAIngresarDelCliente()
            datosCliente=input().split(",")
            datosAIngresarControlFertilizantes()
            datosFertilizante=input().split(",")
            datosAIngresarFactura()
            fecha=input()
            facturaGenerada=Factura(fecha,datosFertilizante[3],ControlDeFertilizantes(datosFertilizante[0],
            datosFertilizante[1],datosFertilizante[2],datosFertilizante[3],datosFertilizante[4]))

            try:
                registroClientes.index(datosCliente[1])
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)
            except:
                registroClientes.append(Cliente(datosCliente[0],datosCliente[1]))
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)

        elif elecccion==2:
            datosAIngresarDelCliente()
            datosCliente=input().split(",")
            datosAIngresarControlDePlagas()
            datosPLagas=input().split(",")
            datosAIngresarFactura()
            fecha=input()
            facturaGenerada=Factura(fecha,datosPLagas[3],ControlDePlagas(datosPLagas[0],datosPLagas[1],
            datosPLagas[2],datosPLagas[3],datosPLagas[4]))
            try:
                registroClientes.index(datosCliente[1])
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)
            except:
                registroClientes.append(Cliente(datosCliente[0],datosCliente[1]))
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)

        elif elecccion==3:
            datosAIngresarDelCliente()
            datosCliente=input().split(",")
            datosAIngresarAntibioticos()
            datosAntibioticos=input().split(",")
            datosAIngresarFactura()
            fecha=input()
            facturaGenerada=Factura(fecha,datosAntibioticos[3],Antibiotico(datosAntibioticos[0],
            datosAntibioticos[1],datosAntibioticos[2],datosAntibioticos[3]))
            try:
                registroClientes.index(datosCliente[1])
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)
            except:
                registroClientes.append(Cliente(datosCliente[0],datosCliente[1]))
                registroClientes[registroClientes.index(datosCliente[1])].compraRealizada(facturaGenerada)

        elif elecccion ==4:
            for clienteIterador in registroClientes:
                print("Nombre de cliente: ", clienteIterador.nombre)
                for facturaIterador in clienteIterador.facturas:
                    facturaIterador.mostrarCaracteristicas()

        elif elecccion==0:
            break
        input("Presione enter para otra seleccionar opcion")





main()