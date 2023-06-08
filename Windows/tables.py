from PyQt5 import QtWidgets
from Class.functions import *
import json


class tables(QtWidgets.QDialog):
    def __init__(self, Type, Frequency):
        super().__init__()
        self.Type = Type
        self.Frequency = Frequency
        self.setFixedSize(423, 600)
        self.setWindowTitle("Tabla")
        self.label = QtWidgets.QLabel(self)

        # Crea un layout para la ventana
        layout = QtWidgets.QVBoxLayout(self)

        # Crea un widget QTableWidget y agrégalo al layout
        self.table = QtWidgets.QTableWidget()
        layout.addWidget(self.table)

        # Lee los datos del archivo correspondiente
        if self.Type == "gastos":
            self.data = LeerGastos()
        elif self.Type == "ingresos":
            self.data = LeerIngresos()


        if self.Frequency == "Diario" and not Type == "ambos":
            self.DailyOperations()
        elif self.Frequency == "Todas" and not Type == "ambos":
            self.AllOperations()
        elif self.Type == "ambos" and Frequency == "Diario":
            from Class.functions import DatosAmbosDaily
            self.data = DatosAmbosDaily()
            self.AmbosDialy()
        elif self.Type == "ambos" and Frequency == "Todas":
            self.gastos = LeerGastos()
            for dic in self.gastos:
                dic["operation"] = "gasto"
            self.ingresos = LeerIngresos()
            for dic in self.ingresos:
                dic["operation"] = "ingreso"
            self.data = self.gastos + self.ingresos
            self.AmbosAll()


    def DailyOperations(self):
        ListaDiario = []
        diccionario = {}
        for dic in self.data:
            Fecha = dic["fecha"]
            Operacion = int(dic["monto"])
            if Fecha in diccionario:
                diccionario[Fecha] += Operacion
            else:
                diccionario[Fecha] = Operacion
        for clave in diccionario.keys():
            Fecha = clave
            Monto = diccionario[clave]
            ListaDiario.append({"fecha": Fecha, "monto": Monto})


        # Muestra los datos en la tabla
        headers = ["Fecha", "Monto"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(["Fecha", "Monto"])

        for row, item in enumerate(ListaDiario):
            self.table.insertRow(row)
            for column, key in enumerate(headers):
                value = item.get(key.lower(), "")
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row, column, cell)


    def AllOperations(self):
        headers = ["Fecha", "Monto", "Concept"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(["Fecha", "Monto", "Concepto"])
        self.table.setColumnWidth(2, 200)

        for row, item in enumerate(self.data):
            self.table.insertRow(row)
            for column, key in enumerate(headers):
                value = item.get(key.lower(), "")
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row, column, cell)


    def AmbosAll(self):
        headers = ["fecha", "monto", "concept", "operation"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(["Fecha", "Monto", "Concepto", "Operación"])
        self.table.setColumnWidth(2, 190)
        self.table.setColumnWidth(1, 50)
        self.table.setColumnWidth(0, 80)
        self.table.setColumnWidth(3, 70)

        for row, item in enumerate(self.data):
            self.table.insertRow(row)
            for column, key in enumerate(headers):
                value = item.get(key.lower(), "")
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row, column, cell)


    def AmbosDialy(self):
        headers = ["fecha", "monto", "type"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(["Fecha", "Monto", "Operación"])


        for row, item in enumerate(self.data):
            self.table.insertRow(row)
            for column, key in enumerate(headers):
                value = item.get(key.lower(), "")
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row, column, cell)



