from PyQt5 import QtWidgets, QtGui
from datetime import *
import pyqtgraph as pg
import pyqtgraph.exporters
from pyqtgraph import GraphicsLayoutWidget
from reportlab.platypus import Spacer, Paragraph, SimpleDocTemplate, Table, Image, KeepTogether
from reportlab.lib.styles import  ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
import json


today = date.today()
todayFormat = today.strftime("%d/%m/%Y")
months = {
        1: 'enero',
        2: 'febrero',
        3: 'marzo',
        4: 'abril',
        5: 'mayo',
        6: 'junio',
        7: 'julio',
        8: 'agosto',
        9: 'septiembre',
        10: 'octubre',
        11: 'noviembre',
        12: 'diciembre'
    }


def LeerTotalGastado():
    try:
        with open("TotalGastado.json", "r") as archivo:
            TotalGastado = json.load(archivo)
    except:
        TotalGastado = 0
        
    return TotalGastado


def notification(TEXTO):
    from Windows.notification import dialog_animado
    a = dialog_animado(TEXTO)
    a.repro()



def LeerTotalIngresado():
    try:
        with open("TotalIngresado.json", "r") as archivo:
            TotalIngresado = json.load(archivo)
    except:
        TotalIngresado = 0

    return TotalIngresado


def ReadExpenses():
    try:
        with open("gastos.json", "r") as archivo:
            ExpenseList = json.load(archivo)
    except:
        ExpenseList = []
    
    return ExpenseList


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


def OperationWindow():
    from Windows.operation import EnterWindow
    ventana = EnterWindow()
    ventana.exec()


def LabelUpdate(label, label2, label3):
    TotalGastado = LeerTotalGastado()
    TotalIngresado = LeerTotalIngresado()
    Utilidades = CalcularUtilidades()
    label.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#626276;\">{TotalGastado}</span></p></body></html>")
    label2.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#626276;\">{TotalIngresado}</span></p></body></html>")
    label3.setText(f"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600; color:#626276;\">{Utilidades}</span></p></body></html>")


def error(parent, title, text):
    QtWidgets.QMessageBox.warning(parent, title, text)


def SaveOperation(window, amount, concept, type):
    from Class.Operations import operation
    if not amount and not concept:
        error(window, "Error", "Los campos concepto y monto estan vacios")
        return
    elif not amount and concept:
        error(window, "Error", "Indique un monto")
        return
    elif amount and not concept:
        error(window, "Error", "Indique un concepto")
        return
    NewOperation = operation(todayFormat, amount, concept, type)
    NewOperation = NewOperation.__dict__
    if type == "Gasto":
        ExpenseList = ReadExpenses()
        ExpenseList.append(NewOperation)
        with open("gastos.json", "w") as archivo:
            json.dump(ExpenseList, archivo)

        TotalGastado = LeerTotalGastado()
        TotalGastado = TotalGastado + int(NewOperation.get("monto"))
        with open("TotalGastado.json", "w") as archivo:
            json.dump(TotalGastado, archivo)
    else:
        ListadoIngresos = LeerIngresos()
        ListadoIngresos.append(NewOperation)
        with open("ingresos.json", "w") as archivo:
            json.dump(ListadoIngresos, archivo)
        TotalIngresado = LeerTotalIngresado()
        TotalIngresado = TotalIngresado + int(NewOperation.get("monto"))
        with open("TotalIngresado.json", "w") as archivo:
            json.dump(TotalIngresado, archivo)

    window.close()


def info():
    from Windows.info import InfoWindow
    a = InfoWindow()
    a.exec_()


def TablesWindows(Type, Frequency):
    from Windows.tables import tables
    asd = tables(Type, Frequency)
    asd.exec_()


def DatosDaily(data):
    data.sort(key=lambda x: x['fecha'])
    resultado = []
    NuevaTransaccion = {}

    for transaccion in data:
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
        lista =  DatosDaily(ReadExpenses())
    if Type == "ingresos" and Frequency == "Diario":
        lista = DatosDaily(LeerIngresos())
    if Type == "gastos" and  Frequency == "Todos":
        lista = ReadExpenses()
    if Type == "ingresos" and Frequency == "Todos":
        lista = LeerIngresos()

    window = pg.plot()
    window.setGeometry(100, 100, 600, 500)
    title = "Gráfico de barras"
    window.setWindowTitle(title)
    window.setWindowIcon(QtGui.QIcon("dependencias/agua2.png"))

    bargraph = CreateGraph(lista)

    window.addItem(bargraph)
    viewbox = window.getViewBox()
    viewbox.setMouseEnabled(y=False)
    viewbox.setLimits(xMin=0)


def CreateGraph(lista):
    valores = []
    for dic in lista:
        valor = int(dic["monto"])
        valores.append(valor)
    x = range(1, len(valores) + 1)

    bargraph = pg.BarGraphItem(x=x, height=valores, width=0.8, brush='w')

    return bargraph


def PdfWindow():
    from Windows.PdfExport import Ui_Dialog
    window = Ui_Dialog()
    window.exec_()


def GenerateImage(bargraph, name):
    widget = GraphicsLayoutWidget()
    plotItem = widget.addPlot()
    plotItem.addItem(bargraph)
    exporter = pyqtgraph.exporters.ImageExporter(plotItem)
    exporter.export(name)


def PdfExport(ventana, lista):
    style = ParagraphStyle(name="normal")
    spacer = Spacer(0, 10)
    styleCenter = ParagraphStyle(name="normal", alignment=1)
    styleRight = ParagraphStyle(name="normal", alignment=2, fontSize=6)
    InitialText = Paragraph(f"Holguin, {today.day} de {months[today.month]} del {today.year}", style)
    PdfElements = [InitialText]
    doc = SimpleDocTemplate(f"Operaciones de {months[today.month]} .pdf", pagesize = letter)

    def DailyTableCreate(data, palabra):
        if not data:
            return
        TableData = [["Fecha", "Monto"]]
        Text = Paragraph(f"{palabra} por dia", styleCenter)

        for operation in data[-30:]:
            NewList = []
            NewList.append(operation["fecha"])
            NewList.append(operation["monto"])
            TableData.append(NewList)

        table = Table(TableData)
        table.setStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ])
        table.setStyle([('BACKGROUND', (0, 0), (-1, 0), colors.beige), ])
        table.setStyle([('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke), ])
        table.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])

        group = KeepTogether([Text, spacer, table])
        PdfElements.append(spacer)
        PdfElements.append(group)
        PdfElements.append(spacer)

    def TableCreate(data, palabra):
        if not data:
            return
        TableData = [["Fecha", "Monto", "Concepto"]]
        Text = Paragraph(f"Ultimos 30 {palabra}", styleCenter)
        for expense in data[-30:]:
            NewList = []
            NewList.append(expense["fecha"])
            NewList.append(expense["monto"])
            NewList.append(expense["concept"])
            TableData.append(NewList)

        table = Table(TableData)
        table.setStyle([('GRID', (0, 0), (-1, -1), 1, colors.black), ])
        table.setStyle([('BACKGROUND', (0, 0), (-1, 0), colors.beige), ])
        table.setStyle([('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke), ])
        table.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])
        table._argW[-1] = 150

        group = KeepTogether([Text, spacer, table])
        PdfElements.append(spacer)
        PdfElements.append(group)
        PdfElements.append(spacer)

    def GenerateGraph(data, Text, name):
        Text = Paragraph(f"{Text}", styleCenter)
        bargraph = CreateGraph(data)
        GenerateImage(bargraph, name)
        img = Image(name, height=180, width=350)

        group = KeepTogether([Text, spacer, img])
        PdfElements.append(group)
        PdfElements.append(spacer)

    def GGDiarios():
        ExpensesList = ReadExpenses()
        Operations = DatosDaily(ExpensesList)
        Text = "Gastos por dia"
        GenerateGraph(Operations, Text, "DailyExpensesGraph.png")

    def GIDiarios():
        Ingresos = LeerIngresos()
        Operations = DatosDaily(Ingresos)
        Text = "Ingresos por dia"
        GenerateGraph(Operations, Text, "DailyIngresosGraph.png")

    def GGTodos():
        ExpensesList = ReadExpenses()
        Text = "Ultimos 30 gastos"
        GenerateGraph(ExpensesList, Text, "expensesGraph.png")

    def GITodos():
        Ingresos = LeerIngresos()
        Text = "Ultimos 30 ingresos"
        GenerateGraph(Ingresos, Text, "graficaIngresos.png")

    def TGTodos():
        ExpensesList = ReadExpenses()
        TableCreate(ExpensesList, "gastos")

    def TITodos():
        IngresosList = LeerIngresos()
        TableCreate(IngresosList, "ingresos")

    def TGDiarios():
        Expenses = ReadExpenses()
        data = DatosDaily(Expenses)
        DailyTableCreate(data, "gastos")

    def TIDiarios():
        Operations = LeerIngresos()
        data = DatosDaily(Operations)
        DailyTableCreate(data, "ingresos")

    for element in lista:
        try:
            locals()[element]()
        except:
            pass

    PdfElements.append(spacer)
    FinalText = Paragraph("Este PDF ha sido generado por la aplicacion CONTABLE", styleRight)
    PdfElements.append(FinalText)

    try:
        doc.build(PdfElements)
        notification("El PDF se ha creado correctamente")
    except Exception as ex:
        error(ventana, "Ha ocurrido un error", f"{ex}")
