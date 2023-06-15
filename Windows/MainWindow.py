from PyQt5 import QtCore, QtGui, QtWidgets
from Class.Interfaz import texto_borde
from Class.functions import *


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Contable")
        self.setFixedSize(800, 618)
        self.setWindowIcon(QtGui.QIcon("dependencias/app.ico"))

        label = QtWidgets.QLabel(self)
        label.setFixedSize(800, 620)
        pixmap = QtGui.QPixmap("dependencias/fondo.jpg")
        pixmap = pixmap.scaled(label.size())
        label.setPixmap(pixmap)
        effect = QtWidgets.QGraphicsBlurEffect()
        effect.setBlurRadius(1.7)
        label.setGraphicsEffect(effect)

        barraMenu = self.menuBar()
        barraMenu.setStyleSheet(
            "QMenuBar{background-color: rgb(146, 153, 172)}"
            "QMenuBar::item:selected{background: rgb(122, 135, 153)}")

        operaciones = barraMenu.addMenu("Operaciones")
        operaciones.setStyleSheet(
            "QMenu{background-color: rgb(146, 153, 172)}""QMenu::item:selected{background: "
            "rgb(122, 135, 153); color: black}")

        tablas = barraMenu.addMenu("Tablas")
        tablas.setStyleSheet(
            "QMenu{background-color: rgb(146, 153, 172)}""QMenu::item:selected{background: "
            "rgb(122, 135, 153); color: black}")
        all = tablas.addMenu("Todas las operaciones")
        actionGasto3 = all.addAction("Gastos")
        actionGasto3.triggered.connect(lambda: TablesWindows("gastos", "Todas"))
        actionIngreso3 = all.addAction("Ingresos")
        actionIngreso3.triggered.connect(lambda: TablesWindows("ingresos", "Todas"))
        actionAmbos = all.addAction("Ambos")
        actionAmbos.triggered.connect(lambda: TablesWindows("ambos", "Todas"))
        daily = tablas.addMenu("Valores por dia")
        ActionGasto4 = daily.addAction("Gastos")
        ActionGasto4.triggered.connect(lambda: TablesWindows("gastos", "Diario"))
        ActionIngreso4 = daily.addAction("Ingresos")
        ActionIngreso4.triggered.connect(lambda: TablesWindows("ingresos", "Diario"))
        ActionAmbos2 = daily.addAction("Ambos")
        ActionAmbos2.triggered.connect(lambda: TablesWindows("ambos", "Diario"))

        graficas = barraMenu.addMenu("Gráficas")
        graficas.setStyleSheet(
            "QMenu{background-color: rgb(146, 153, 172)}""QMenu::item:selected{background: "
            "rgb(122, 135, 153); color: black}")
        GAll = graficas.addMenu("Todas las operaciones")
        actionGasto = GAll.addAction("Gastos")
        actionGasto.triggered.connect(lambda: OpenGraphicsWindow("gastos", "Todos"))
        actionIngreso = GAll.addAction("Ingresos")
        actionIngreso.triggered.connect(lambda: OpenGraphicsWindow("ingresos", "Todos"))
        GDaily = graficas.addMenu("Valores por dia")
        actionGasto2 = GDaily.addAction("Gastos")
        actionGasto2.triggered.connect(lambda: OpenGraphicsWindow("gastos", "Diario"))
        actionIngreso2 = GDaily.addAction("Ingresos")
        actionIngreso2.triggered.connect(lambda: OpenGraphicsWindow("ingresos", "Diario"))

        pdf = barraMenu.addMenu("Exportar")
        pdf.setStyleSheet(
            "QMenu{background-color: rgb(146, 153, 172)}""QMenu::item:selected{background: "
            "rgb(122, 135, 153); color: black}")
        PdfAction = pdf.addAction("Exportar a PDF")
        PdfAction.triggered.connect(lambda: PdfWindow())

        info1 = barraMenu.addMenu("Ayuda")
        info1.setStyleSheet("QMenu{background-color: rgb(146, 153, 172)}""QMenu::item:selected{background: "
                           "rgb(122, 135, 153); color: black}")
        infoAction = info1.addAction("Información")
        infoAction.triggered.connect(info)

        Operation = operaciones.addAction("Agregar operación")
        Operation.triggered.connect(OperationWindow)

        bienvenida = texto_borde("Bienvenido(a)", QtGui.QColor(146, 153, 172), QtGui.QColor("solid black"), 2.5)
        bienvenida.setParent(self)
        bienvenida.setFixedSize(300, 50)
        bienvenida.setFont(QtGui.QFont("Arial", 22, QtGui.QFont.Bold))
        bienvenida.move(10, 25)

        label = QtWidgets.QLabel(self)
        label.setFixedSize(500, 80)
        label.move(60, 530)
        label.setStyleSheet("border: 1.5px solid black;background: rgb(146, 153, 172);border-radius: 6px")

        label1 = QtWidgets.QLabel(self)
        label1.setFixedSize(2, 80)
        label1.move(220, 530)
        label1.setStyleSheet("border: 1.5px solid black;")

        label2 = QtWidgets.QLabel(self)
        label2.setFixedSize(2, 80)
        label2.move(390, 530)
        label2.setStyleSheet("border: 1.5px solid black;")

        labelTG = QtWidgets.QLabel(self)
        labelTG.setText("Total Gasto")
        labelTG.setStyleSheet("background: rgb(146, 153, 172); text-decoration: underline")
        labelTG.move(95, 540)
        labelTG.setFont(QtGui.QFont("Arial", 12))

        labelTI = QtWidgets.QLabel(self)
        labelTI.setText("Total ingreso")
        labelTI.setStyleSheet("background: rgb(146, 153, 172); text-decoration: underline")
        labelTI.move(255, 540)
        labelTI.setFont(QtGui.QFont("Arial", 12))

        labelU = QtWidgets.QLabel(self)
        labelU.setText("Utilidades")
        labelU.setStyleSheet("background: rgb(146, 153, 172); text-decoration: underline")
        labelU.move(440, 540)
        labelU.setFont(QtGui.QFont("Arial", 12))

        self.label = QtWidgets.QLabel(self)
        self.label.setText("Cargando...")
        self.label.setStyleSheet("background: transparent")
        self.label.move(90, 570)
        self.label.setFont(QtGui.QFont("Arial", 12))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("Cargando...")
        self.label1.setStyleSheet("background: transparent")
        self.label1.move(255, 570)
        self.label1.setFont(QtGui.QFont("Arial", 12))

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setText("Cargando...")
        self.label2.setStyleSheet("background: transparent")
        self.label2.move(425, 570)
        self.label2.setFont(QtGui.QFont("Arial", 12))

        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(4000)
        self.timer.timeout.connect(lambda: (LabelUpdate(self.label, self.label1, self.label2)))
        self.timer.start()