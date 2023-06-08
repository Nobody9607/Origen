from PyQt5 import QtWidgets
from datetime import *
import pyqtgraph as pg
import json


today = date.today()
today = today.strftime("%d/%m/%Y")

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
    from Windows.operation import EnterWindow
    ventana = EnterWindow()
    ventana.exec()
    
def ActualizarLabel(label, label2, label3):
    TotalGastado = LeerTotalGastado()
    TotalIngresado = LeerTotalIngresado()
    Utilidades = CalcularUtilidades()
    label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{TotalGastado}</span></p></body></html>")
    label2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{TotalIngresado}</span></p></body></html>")
    label3.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#828296;\">{Utilidades}</span></p></body></html>")

def error(parent, title, text):
    QtWidgets.QMessageBox.warning(parent, title, text)

def GuardarOperacion(window, monto, concept, type):
    from Class.Operations import operation
    if not monto and not concept:
        error(window, "Error", "Los campos concepto y monto estan vacios")
        return
    elif not monto and concept:
        error(window, "Error", "Indique un monto")
        return
    elif monto and not concept:
        error(window, "Error", "Indique un concepto")
        return
    NuevaOperacion = operation(today, monto, concept, type)
    NuevaOperacion = NuevaOperacion.__dict__
    if type == "Gasto":
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

    window.close()

def info():
    from Windows.info import InfoWindow
    a =InfoWindow()
    a.exec_()


def TablesWindows(Type, Frequency):
    from Windows.tables import tables
    asd = tables(Type, Frequency)
    asd.exec_()


def DatosDaily(datos):
    datos.sort(key=lambda x: x['fecha'])
    resultado = []
    NuevaTransaccion = {}

    for transaccion in datos:
        fecha = transaccion["fecha"]
        monto = int(transaccion["monto"])
        Type = transaccion["type"]
        try:
            if fecha in NuevaTransaccion["fecha"] and Type in NuevaTransaccion["type"]:
                NuevaTransaccion["monto"] += monto
            else:
                NuevaTransaccion = {"fecha": fecha, "monto": monto, "type": Type}
        except:
            NuevaTransaccion = {"fecha": fecha, "monto": monto, "type": Type}
        finally:
            if not NuevaTransaccion in resultado:
                resultado.append(NuevaTransaccion)

    return resultado


def OpenGraphicsWindow(Type, Frequency):
    if Type == "gastos" and Frequency == "Diario":
        lista =  DatosDaily(LeerGastos())
    if Type == "ingresos" and Frequency == "Diario":
        lista = DatosDaily(LeerIngresos())
    if Type == "gastos" and  Frequency == "Todos":
        lista = LeerGastos()
    if Type == "ingresos" and Frequency == "Todos":
        lista = LeerIngresos()

    window = pg.plot()
    window.setGeometry(100, 100, 600, 500)
    title = "Gráfico de barras con PyQtGraph"
    window.setWindowTitle(title)

    valores = []
    for dic in lista:
        valor = int(dic["monto"])
        valores.append(valor)
    x = range(1, len(valores) + 1)

    bargraph = pg.BarGraphItem(x=x, height=valores, width=0.8, brush='w')
    window.addItem(bargraph)
    viewbox = window.getViewBox()
    viewbox.setMouseEnabled(y=False)
    viewbox.setLimits(xMin=0)
