from PyQt5 import QtWidgets
from Class.functions import *
import json


class tables(QtWidgets.QDialog):
    def __init__(self, Type):
        super().__init__()
        self.Type = Type
        self.setFixedSize(423,600)
        self.setWindowTitle("Tabla")
        self.label = QtWidgets.QLabel(self)

        # Crea un layout para la ventana
        layout = QtWidgets.QVBoxLayout(self)

        # Crea un widget QTableWidget y agrégalo al layout
        self.table = QtWidgets.QTableWidget()
        layout.addWidget(self.table)

        # Lee los datos del archivo correspondiente
        if self.Type == "gastos":
                data = LeerGastos()
        elif self.Type == "ingresos":
                data = LeerIngresos()

        # Muestra los datos en la tabla
        headers = ["Fecha", "Monto", "Concept"]
        self.table.setColumnCount(len(headers))
        self.table.setHorizontalHeaderLabels(["Fecha", "Monto", "Concepto"])
        self.table.setColumnWidth(2, 200)

        for row, item in enumerate(data):
            self.table.insertRow(row)
            for column, key in enumerate(headers):
                value = item.get(key.lower(), "")
                cell = QtWidgets.QTableWidgetItem(str(value))
                self.table.setItem(row, column, cell)

