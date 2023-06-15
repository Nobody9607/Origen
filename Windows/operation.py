from Class import functions
from Windows.MainWindow import *
from Class.Interfaz import texto_borde, boton_animado


class EnterWindow(QtWidgets.QDialog):
    def __init__(self):
        super(EnterWindow, self).__init__()
        self.setObjectName("VentanasDeEntrada")
        self.setWindowIcon(QtGui.QIcon("dependencias/Gasto.ico"))
        self.setFixedSize(600, 300)
        self.setStyleSheet("background-color: rgb(99, 99, 118);")

        label = QtWidgets.QLabel(self)
        label.setFixedSize(self.size())
        pixmap = QtGui.QPixmap("dependencias/fondo.jpg")
        pixmap = pixmap.scaled(label.size())
        label.setPixmap(pixmap)
        opacity_effect = QtWidgets.QGraphicsOpacityEffect()
        opacity_effect.setOpacity(0.7)
        label.setGraphicsEffect(opacity_effect)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)

        self.pushButton = boton_animado("dependencias/Gasto.ico", font, 161, 41, "Aceptar", self)
        self.pushButton.clicked.connect(lambda: (functions.SaveOperation(self, self.lineEdit.text(),
                                                                         self.lineEdit_2.text(),
                                                                         self.comboBox.currentText())))
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 161, 41))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:  rgb(132, 134, 150);border-radius: 6px }\n"
                                      "QPushButton:hover{background-color:rgb(158, 161, 180)}")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = boton_animado("dependencias/Cancelar.ico", font, 161, 41, "Cancelar", self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 230, 161, 41))
        self.pushButton_2.setStyleSheet("QPushButton{background-color:  rgb(132, 134, 150);border-radius: 6px }\n"
                                        "QPushButton:hover{background-color:rgb(158, 161, 180)}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.label = texto_borde("Indique monto", QtGui.QColor(146, 153, 172), QtGui.QColor("solid black"), 5)
        self.label.setParent(self)
        self.label.setStyleSheet("background: transparent")
        self.label.setFont(QtGui.QFont("Arial", 25, QtGui.QFont.Bold))
        self.label.setGeometry(QtCore.QRect(0, 20, 601, 41))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 113, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("QLineEdit{border:transparent; background-color: rgb(132, 134, 150);}")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(480, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("background: rgb(132, 134, 150);  selection-background-color:rgb(145, 147, 165); "
                                    "selection-color: black\n""")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.lineEdit_2 = QtWidgets.QLineEdit(self)
        self.lineEdit_2.setGeometry(QtCore.QRect(160, 130, 301, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("QLineEdit{border:transparent; background-color: rgb(132, 134, 150);}")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, EnterWindow):
        _translate = QtCore.QCoreApplication.translate
        EnterWindow.setWindowTitle(_translate("VentanasDeEntrada", "Operación"))
        self.lineEdit.setPlaceholderText(_translate("VentanasDeEntrada", "MONTO"))
        self.comboBox.setItemText(0, _translate("VentanasDeEntrada", "Gasto"))
        self.comboBox.setItemText(1, _translate("VentanasDeEntrada", "Ingreso"))
        self.lineEdit_2.setPlaceholderText(_translate("VentanasDeEntrada", "CONCEPTO"))
