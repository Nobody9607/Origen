from Ventanas.operacion import *
from Objetos.Operaciones import *
from Ventanas.info import *
from PyQt5 import QtWidgets
import json


def LeerTotalGastado():
    try:
        with open("TotalGastado.json", "r") as archivo:
            TotalGastado = json.load(archivo)
    except:
        TotalGastado = 0
        
    return  TotalGastado

def LeerTotalIngresado():
    try:
        with open("TotalIngresado.json", "r") as archivo:
            TotalIngresado = json.load(archivo)
    except:
        TotalIngresado = 0

    return TotalIngresado

def LeerGastos():
    try:
        with open("gastos.json", "r") as archivo:
            ListadoGastos = json.load(archivo)
    except:
        ListadoGastos = []
    
    return ListadoGastos

def CalcularUtilidades():
    TotalGastado = LeerTotalGastado()
    TotalIngresado = LeerTotalIngresado()
    Utilidades = TotalIngresado - TotalGastado
    return Utilidades

def LeerIngresos():
    try:
        with open("Ingresos.json", "r") as archivo:
            ListadoIngresos = json.load(archivo)
    except:
        ListadoIngresos = []

    return ListadoIngresos

def VentanaOperacion():
    ventana = VentanasDeEntrada()
    ventana.exec()
    
def ActualizarLabel(label, label2, label3):
    TotalGastado = LeerTotalGastado()
    TotalIngresado = LeerTotalIngresado()
    Utilidades = CalcularUtilidades()
    label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{TotalGastado}</span></p></body></html>")
    label2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{TotalIngresado}</span></p></body></html>")
    label3.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{Utilidades}</span></p></body></html>")

def error(ventana, titulo, texto):
    QtWidgets.QMessageBox.warning(ventana, titulo, texto)

def GuardarOperacion(ventana, monto, concepto, tipo):
    if not monto and not concepto:
        error(ventana, "Error", "Los campos concepto y monto estan vacios")
        return
    elif not monto and concepto:
        error(ventana, "Error", "Indique un monto")
        return
    elif monto and not concepto:
        error(ventana, "Error", "Indique un concepto")
        return
    NuevaOperacion = operacion("21/05/2023", monto, concepto, tipo)
    NuevaOperacion = NuevaOperacion.__dict__
    if tipo == "Gasto":
        ListadoGastos = LeerGastos()
        ListadoGastos.append(NuevaOperacion)
        with open("gastos.json", "w") as archivo:
            json.dump(ListadoGastos, archivo)
        TotalGastado = LeerTotalGastado()
        TotalGastado = TotalGastado + int(NuevaOperacion.get("monto"))
        with open("TotalGastado.json", "w") as archivo:
            json.dump(TotalGastado, archivo)
    else:
        ListadoIngresos = LeerIngresos()
        ListadoIngresos.append(NuevaOperacion)
        with open("ingresos.json", "w") as archivo:
            json.dump(ListadoIngresos, archivo)
        TotalIngresado = LeerTotalIngresado()
        TotalIngresado = TotalIngresado + int(NuevaOperacion.get("monto"))
        with open("TotalIngresado.json", "w") as archivo:
            json.dump(TotalIngresado, archivo)

    ventana.close()

def info():
    a =VentanaInfo()
    a.exec_()