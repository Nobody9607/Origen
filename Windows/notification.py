from PyQt5 import QtWidgets, QtGui, QtCore
from playsound import playsound


screen = QtWidgets.QDesktopWidget().screenGeometry()
available_screen = QtWidgets.QDesktopWidget().availableGeometry()


class dialog_animado(QtWidgets.QDialog):
    def __init__(self, texto, parent=None):
        super().__init__(parent)

        start_x = screen.width() - 50
        start_y = available_screen.height() - 180 //1
        end = screen.width() - 340

        self.setGeometry(1920, 900, 335, 150)
        self.setWindowFlags(self.windowFlags() | QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("QDialog{background: rgb(57, 88, 138)}")

        self.label = QtWidgets.QLabel(self)
        self.label.move(20, 70)
        self.label.setText(texto)
        self.label.setFont(QtGui.QFont("Arial", 13))

        self.label1 = QtWidgets.QLabel(self)
        self.label1.setText("           Contable")
        self.label1.move(0, 0)
        self.label1.setFixedSize(335, 30)
        self.label1.setFont(QtGui.QFont("Arial", 10))
        self.label1.setStyleSheet("background: rgb(53, 91, 153)")

        self.label2 = QtWidgets.QLabel(self)
        icono = QtGui.QPixmap("dependencias/app.ico")
        self.label2.setScaledContents(True)
        self.label2.setPixmap(icono)
        self.label2.setFixedSize(25, 25)
        self.label2.move(8, 2)

        self.animacion = QtCore.QPropertyAnimation(self, b"geometry")
        self.animacion.setDuration(1200)
        self.animacion.setStartValue(QtCore.QRect(start_x, start_y, 335, 150))
        self.animacion.setEndValue(QtCore.QRect(end, start_y, 335, 150))

        self.animacion1 = QtCore.QPropertyAnimation(self, b"geometry")
        self.animacion1.setDuration(1200)
        self.animacion1.setStartValue(QtCore.QRect(end, start_y, 335, 150))
        self.animacion1.setEndValue(QtCore.QRect(start_x, start_y, 335, 150))
        self.animacion1.finished.connect(self.close)

        self.timer = QtCore.QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.timeout.connect(self.animacion1.start)

        self.boton = QtWidgets.QPushButton(self)
        self.boton.setText("→")
        self.boton.setFixedSize(40, 20)
        self.boton.move(290, 6)
        self.boton.setStyleSheet("background: rgb(53, 91, 153); border: transparent")
        self.boton.clicked.connect(self.animacion1.start)

    def paintEvent(self, event):
        super().paintEvent(event)
        path = QtGui.QPainterPath()
        path.addRoundedRect(QtCore.QRectF(self.rect()), 10, 10)
        mask = QtGui.QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def repro(self):
       playsound("dependencias/Notification-Sandy-Beach.mp3",  block=False)
       self.show()
       self.animacion.start()
       self.timer.start(3000)