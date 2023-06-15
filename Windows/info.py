from PyQt5 import QtCore, QtWidgets, QtGui


class InfoWindow(QtWidgets.QDialog):
   def __init__(self):
        super().__init__()
        self.setWindowTitle("Información")
        self.setFixedSize(250, 200)
        self.setStyleSheet("background: rgb(88, 93, 104)")
        self.setWindowIcon(QtGui.QIcon("dependencias/info.ico"))

        label = QtWidgets.QLabel(self)
        label.setFixedSize(250, 200)
        pixmap = QtGui.QPixmap("dependencias/fondo.jpg")
        pixmap = pixmap.scaled(label.size())
        label.setPixmap(pixmap)
        opacity_effect = QtWidgets.QGraphicsBlurEffect()
        opacity_effect.setBlurRadius(2.5)
        label.setGraphicsEffect(opacity_effect)

        self.label = QtWidgets.QLabel(self)
        self.label.setFont(QtGui.QFont("Arial", 15))
        self.label.setText("Leandro Rojas Rodriguez \n \nlrr1907@gmail.com \n \n51446763 \n \n2023")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setStyleSheet("color: white;font-weight: bold; background: transparent")
        self.label.move(6, 14)