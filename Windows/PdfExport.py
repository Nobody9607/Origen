from PyQt5 import QtCore, QtWidgets, QtGui
from Class.functions import PdfExport
from Class.Interfaz import boton_animado, texto_borde


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.setWindowIcon(QtGui.QIcon("dependencias/lista.ico"))

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        label = QtWidgets.QLabel(self)
        label.setFixedSize(800, 620)
        pixmap = QtGui.QPixmap("dependencias/fondo.jpg")
        pixmap = pixmap.scaled(label.size())
        label.setPixmap(pixmap)
        effect = QtWidgets.QGraphicsBlurEffect()
        effect.setBlurRadius(0.6)
        label.setGraphicsEffect(effect)

        self.ListaArgumentos = []
        self.setObjectName("Dialog")
        self.resize(473, 260)
        self.setMinimumSize(QtCore.QSize(473, 260))
        self.setMaximumSize(QtCore.QSize(473, 260))

        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox.setGeometry(QtCore.QRect(40, 110, 90, 17))
        self.checkBox.setObjectName("checkBox")

        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_2.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_2.stateChanged.connect(lambda state: self.StateChanged(state, "TGTodos"))
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 140, 90, 17))
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)

        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_3.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_3.stateChanged.connect(lambda state: self.StateChanged(state, "TGDiarios"))
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 170, 90, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_4.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_4.stateChanged.connect(lambda state: self.StateChanged(state, "TIDiarios"))
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(130, 170, 90, 17))

        self.checkBox_5 = QtWidgets.QCheckBox(self)
        self.checkBox_5.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_5.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_5.stateChanged.connect(lambda state: self.StateChanged(state, "TITodos"))
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setGeometry(QtCore.QRect(130, 140, 90, 17))

        self.checkBox_6 = QtWidgets.QCheckBox(self)
        self.checkBox_6.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_6.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_6.setGeometry(QtCore.QRect(130, 110, 90, 17))

        self.label = texto_borde("Que desea agregar al PDF", QtGui.QColor(146, 153, 172), QtGui.QColor("solid black"), 2.5, self)
        self.label.setFont(QtGui.QFont("Arial", 19, QtGui.QFont.Bold))
        self.label.setGeometry(QtCore.QRect(0, 10, 471, 41))

        self.label_2 = texto_borde("Tablas", QtGui.QColor(146, 153, 172), QtGui.QColor("solid black"), 2.5, self)
        self.label_2.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label_2.setGeometry(QtCore.QRect(0, 70, 231, 21))

        self.label_3 = texto_borde("Graficas", QtGui.QColor(146, 153, 172), QtGui.QColor("solid black"), 2.5, self)
        self.label_3.setFont(QtGui.QFont("Arial", 14, QtGui.QFont.Bold))
        self.label_3.setGeometry(QtCore.QRect(240, 70, 231, 21))
        self.label_3.setObjectName("label_3")

        self.checkBox_7 = QtWidgets.QCheckBox(self)
        self.checkBox_7.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_7.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_7.stateChanged.connect(lambda state: self.StateChanged(state, "GIDiarios"))
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setGeometry(QtCore.QRect(370, 170, 90, 17))
        self.checkBox_7.setObjectName("checkBox_7")

        self.checkBox_8 = QtWidgets.QCheckBox(self)
        self.checkBox_8.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_8.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_8.stateChanged.connect(lambda state: self.StateChanged(state, "GGTodos"))
        self.checkBox_8.setEnabled(False)
        self.checkBox_8.setGeometry(QtCore.QRect(280, 140, 90, 17))
        self.checkBox_8.setObjectName("checkBox_8")

        self.checkBox_9 = QtWidgets.QCheckBox(self)
        self.checkBox_9.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_9.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_9.stateChanged.connect(lambda state: self.StateChanged(state, "GITodos"))
        self.checkBox_9.setEnabled(False)
        self.checkBox_9.setGeometry(QtCore.QRect(370, 140, 90, 17))
        self.checkBox_9.setObjectName("checkBox_9")

        self.checkBox_10 = QtWidgets.QCheckBox(self)
        self.checkBox_10.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_10.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_10.stateChanged.connect(lambda state: self.StateChanged(state, "GGDiarios"))
        self.checkBox_10.setEnabled(False)
        self.checkBox_10.setGeometry(QtCore.QRect(280, 170, 90, 17))
        self.checkBox_10.setObjectName("checkBox_10")

        self.checkBox_11 = QtWidgets.QCheckBox(self)
        self.checkBox_11.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_11.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_11.setGeometry(QtCore.QRect(370, 110, 90, 17))
        self.checkBox_11.setObjectName("checkBox_11")

        self.checkBox_12 = QtWidgets.QCheckBox(self)
        self.checkBox_12.setStyleSheet("color: rgb(146, 153, 172)")
        self.checkBox_12.setFont(QtGui.QFont("Arial", 10, QtGui.QFont.Bold))
        self.checkBox_12.setGeometry(QtCore.QRect(280, 110, 80, 17))
        self.checkBox_12.setObjectName("checkBox_12")

        self.pushButton = boton_animado("dependencias/lista.ico", font, 121, 25, "Aceptar", self)
        self.pushButton.clicked.connect(lambda :PdfExport(self, self.ListaArgumentos))
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 121, 31))
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = boton_animado("dependencias/cancelar.ico", font, 121, 25, "Cancelar", self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 210, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi()
        self.checkBox.toggled['bool'].connect(self.checkBox_2.setEnabled) # type: ignore
        self.checkBox.toggled['bool'].connect(self.checkBox_3.setEnabled) # type: ignore
        self.checkBox_6.toggled['bool'].connect(self.checkBox_5.setEnabled) # type: ignore
        self.checkBox_6.toggled['bool'].connect(self.checkBox_4.setEnabled) # type: ignore
        self.checkBox_12.toggled['bool'].connect(self.checkBox_8.setEnabled) # type: ignore
        self.checkBox_12.toggled['bool'].connect(self.checkBox_10.setEnabled) # type: ignore
        self.checkBox_11.toggled['bool'].connect(self.checkBox_9.setEnabled) # type: ignore
        self.checkBox_11.toggled['bool'].connect(self.checkBox_7.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Exportar PDF"))
        self.checkBox.setText(_translate("Dialog", "Gastos"))
        self.checkBox_2.setText(_translate("Dialog", "Ultimas 30"))
        self.checkBox_3.setText(_translate("Dialog", "Diarias"))
        self.checkBox_4.setText(_translate("Dialog", "Diarios"))
        self.checkBox_5.setText(_translate("Dialog", "Ultimos 30"))
        self.checkBox_6.setText(_translate("Dialog", "Ingresos"))
        self.checkBox_7.setText(_translate("Dialog", "Diarios"))
        self.checkBox_8.setText(_translate("Dialog", "Ultimas 30"))
        self.checkBox_9.setText(_translate("Dialog", "Ultimos 30"))
        self.checkBox_10.setText(_translate("Dialog", "Diarias"))
        self.checkBox_11.setText(_translate("Dialog", "Ingresos"))
        self.checkBox_12.setText(_translate("Dialog", "Gastos"))

    def StateChanged(self, state, palabra):
        if state == QtCore.Qt.Checked:
            self.ListaArgumentos.append(palabra)
        else:
            self.ListaArgumentos.remove(palabra)
