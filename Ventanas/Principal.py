from PyQt5 import QtWidgets,QtGui,QtCore
from Objetos.cambio import *


class ventana(QtWidgets.QMainWindow):
    def __init__(ven):
        super(ventana, ven).__init__()
        ven.setFixedSize(800, 600)
        ven.setWindowTitle("Ventana Principal")

        ven.aceptar = QtWidgets.QPushButton(ven)
        ven.aceptar.setText("Aceptar")
        ven.aceptar.move(680, 550)
        ven.aceptar.clicked.connect(lambda: ca(ven.aceptar))