from PyQt5 import QtCore, QtGui, QtWidgets
from Class.functions import PdfExport


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super(Ui_Dialog, self).__init__()
        self.ListaArgumentos = []
        self.setObjectName("Dialog")
        self.resize(473, 260)
        self.setMinimumSize(QtCore.QSize(473, 260))
        self.setMaximumSize(QtCore.QSize(473, 260))
        self.checkBox = QtWidgets.QCheckBox(self)
        self.checkBox.setGeometry(QtCore.QRect(40, 110, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self)
        self.checkBox_2.stateChanged.connect(lambda state:self.StateChanged(state, "TGTodos"))
        self.checkBox_2.setEnabled(False)
        self.checkBox_2.setGeometry(QtCore.QRect(40, 140, 70, 17))
        self.checkBox_2.setCheckable(True)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self)
        self.checkBox_3.stateChanged.connect(lambda state: self.StateChanged(state, "TGDiarios"))
        self.checkBox_3.setEnabled(False)
        self.checkBox_3.setGeometry(QtCore.QRect(40, 170, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self)
        self.checkBox_4.stateChanged.connect(lambda state: self.StateChanged(state, "TIDiarios"))
        self.checkBox_4.setEnabled(False)
        self.checkBox_4.setGeometry(QtCore.QRect(120, 170, 70, 17))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self)
        self.checkBox_5.stateChanged.connect(lambda state: self.StateChanged(state, "TITodos"))
        self.checkBox_5.setEnabled(False)
        self.checkBox_5.setGeometry(QtCore.QRect(120, 140, 70, 17))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self)
        self.checkBox_6.setGeometry(QtCore.QRect(120, 110, 70, 17))
        self.checkBox_6.setObjectName("checkBox_6")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 10, 471, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(0, 70, 231, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(240, 70, 231, 21))
        self.label_3.setObjectName("label_3")
        self.checkBox_7 = QtWidgets.QCheckBox(self)
        self.checkBox_7.stateChanged.connect(lambda state: self.StateChanged(state, "GIDiarios"))
        self.checkBox_7.setEnabled(False)
        self.checkBox_7.setGeometry(QtCore.QRect(360, 170, 70, 17))
        self.checkBox_7.setObjectName("checkBox_7")
        self.checkBox_8 = QtWidgets.QCheckBox(self)
        self.checkBox_8.stateChanged.connect(lambda state: self.StateChanged(state, "GGTodos"))
        self.checkBox_8.setEnabled(False)
        self.checkBox_8.setGeometry(QtCore.QRect(280, 140, 70, 17))
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(self)
        self.checkBox_9.stateChanged.connect(lambda state: self.StateChanged(state, "GITodos"))
        self.checkBox_9.setEnabled(False)
        self.checkBox_9.setGeometry(QtCore.QRect(360, 140, 70, 17))
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_10 = QtWidgets.QCheckBox(self)
        self.checkBox_10.stateChanged.connect(lambda state: self.StateChanged(state, "GGDiarios"))
        self.checkBox_10.setEnabled(False)
        self.checkBox_10.setGeometry(QtCore.QRect(280, 170, 70, 17))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(self)
        self.checkBox_11.setGeometry(QtCore.QRect(360, 110, 70, 17))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(self)
        self.checkBox_12.setGeometry(QtCore.QRect(280, 110, 70, 17))
        self.checkBox_12.setObjectName("checkBox_12")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.clicked.connect(lambda :PdfExport(self, self.ListaArgumentos))
        self.pushButton.setGeometry(QtCore.QRect(50, 210, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self)
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
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; "
                                                "font-weight:600; font-style:italic;\">Que desea agregar al PDF</span><"
                                                "/p></body></html>"))
        self.label_2.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:12pt; font-weight:600;\">Tablas</span></p></body></html>"))
        self.label_3.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" "
                                                  "font-size:12pt; font-weight:600;\">Graficas</span></p></"
                                                  "body></html>"))
        self.checkBox_7.setText(_translate("Dialog", "Diarios"))
        self.checkBox_8.setText(_translate("Dialog", "Ultimas 30"))
        self.checkBox_9.setText(_translate("Dialog", "Ultimos 30"))
        self.checkBox_10.setText(_translate("Dialog", "Diarias"))
        self.checkBox_11.setText(_translate("Dialog", "Ingresos"))
        self.checkBox_12.setText(_translate("Dialog", "Gastos"))
        self.pushButton.setText(_translate("Dialog", "Aceptar"))
        self.pushButton_2.setText(_translate("Dialog", "Cancelar"))

    def StateChanged(self, state, palabra):
        if state == QtCore.Qt.Checked:
            self.ListaArgumentos.append(palabra)
        else:
            self.ListaArgumentos.remove(palabra)
