from PyQt5 import QtCore, QtGui, QtWidgets


class InfoWindow(QtWidgets.QDialog):
    def __init__(self):
        super(InfoWindow, self).__init__()
        self.setObjectName("Dialog")
        self.resize(331, 397)
        self.setMinimumSize(QtCore.QSize(331, 397))
        self.setMaximumSize(QtCore.QSize(331, 397))
        self.setStyleSheet("background-color: rgb(166, 166, 166);")
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(10, 20, 311, 361))
        self.label.setObjectName("label")

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Dialog", "Informacion"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Leandro Rojas Rodriguez</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">lrr1907@gmail.com</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">51446763</span></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">2023</span></p></body></html>"))
