from PyQt5 import QtCore, QtGui, QtWidgets
from Objetos import funciones



class VentanasDeEntrada(QtWidgets.QDialog):
    def __init__(self):
        super(VentanasDeEntrada, self).__init__()
        self.setObjectName("VentanasDeEntrada")
        self.resize(600, 300)
        self.setMinimumSize(QtCore.QSize(600, 300))
        self.setMaximumSize(QtCore.QSize(600, 300))
        self.setStyleSheet("background-color: rgb(99, 99, 118);")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.clicked.connect(lambda: (funciones.GuardarOperacion(self.lineEdit.text(), self.lineEdit_2.text(), self.comboBox.currentText())))
        self.pushButton.clicked.connect(self.close)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("QPushButton{background-color:  rgb(132, 134, 150);border-radius: 6px }\n"
"QPushButton:hover{background-color:rgb(158, 161, 180)}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.clicked.connect(self.close)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 230, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("QPushButton{background-color:  rgb(132, 134, 150);border-radius: 6px }\n"
"QPushButton:hover{background-color:rgb(158, 161, 180)}")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 20, 601, 41))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
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
        self.comboBox.setStyleSheet("background: rgb(132, 134, 150);  selection-background-color:rgb(145, 147, 165); selection-color: black\n"
"")
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

    def retranslateUi(self, VentanasDeEntrada):
        _translate = QtCore.QCoreApplication.translate
        VentanasDeEntrada.setWindowTitle(_translate("VentanasDeEntrada", "Operación"))
        self.pushButton.setText(_translate("VentanasDeEntrada", "Aceptar"))
        self.pushButton_2.setText(_translate("VentanasDeEntrada", "Cancelar"))
        self.label.setText(_translate("VentanasDeEntrada", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600; font-style:italic; color:#848696;\">Indique Operación</span></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("VentanasDeEntrada", "MONTO"))
        self.comboBox.setItemText(0, _translate("VentanasDeEntrada", "Gasto"))
        self.comboBox.setItemText(1, _translate("VentanasDeEntrada", "Ingreso"))
        self.lineEdit_2.setPlaceholderText(_translate("VentanasDeEntrada", "CONCEPTO"))
