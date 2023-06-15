from PyQt5 import QtWidgets, QtGui, QtCore


class texto_borde(QtWidgets.QLabel):
    def __init__(self, texto, texto1=QtGui.QColor, borde=QtGui.QColor, tamaño_borde=0, *args, **kwargs):
        super().__init__(texto, *args, **kwargs)
        self.texto1 = texto1
        self.borde = borde
        self.tamaño_borde = tamaño_borde

    def paintEvent(self, event):
        pintor = QtGui.QPainter(self)
        pintor.setRenderHint(QtGui.QPainter.Antialiasing)

        texto = QtGui.QPainterPath()
        texto.addText(0, 0, self.font(), self.text())

        texto_rect = texto.boundingRect()
        x = (self.width() - texto_rect.width()) / 2 - texto_rect.x()
        y = (self.height() - texto_rect.height()) / 2 - texto_rect.y()
        texto.translate(x, y)

        pintor.setPen(QtGui.QPen(self.borde, self.tamaño_borde))
        pintor.setBrush(QtCore.Qt.NoBrush)
        pintor.drawPath(texto)

        pintor.setPen(QtCore.Qt.NoPen)
        pintor.setBrush(self.texto1)
        pintor.drawPath(texto)


class boton_animado(QtWidgets.QPushButton):
    def __init__(self, icon, font, width, height, texto, parent=None):
        super().__init__("", parent)
        self.width = int(width * 0.7)
        self.height = int(height / 3)

        self.textWidth = int(width / 2)
        self.textHeight = int(height / 2)

        self.textPosition = int(width / 3)
        self.textFinalPosition = int(width / 8)

        self.label = QtWidgets.QLabel(texto, self)
        self.label.setFont(font)
        self.label.setGeometry(self.textPosition, self.height, self.textWidth, self.textHeight)
        self.label.setStyleSheet("background: transparent")

        self.animation = QtCore.QPropertyAnimation(self.label, b'geometry')
        self.animation.setDuration(700)
        self.animation.setStartValue(QtCore.QRect(self.textPosition, self.height, self.textWidth, self.textHeight))
        self.animation.setEndValue(QtCore.QRect(self.textFinalPosition, self.height, self.textWidth, self.textHeight))

        self.animation1 = QtCore.QPropertyAnimation(self.label, b'geometry')
        self.animation1.setDuration(700)
        self.animation1.setStartValue(
            QtCore.QRect(self.textFinalPosition, self.height, self.textWidth, self.textHeight))
        self.animation1.setEndValue(QtCore.QRect(self.textPosition, self.height, self.textWidth, self.textHeight))

        self.icon_label = QtWidgets.QLabel(self)
        self.icon_label.setGeometry(width + 10, 5, 20, 20)
        self.icon_label.setPixmap(QtGui.QIcon(icon).pixmap(20, 20))
        self.icon_label.setStyleSheet("background: transparent")

        self.animation2 = QtCore.QPropertyAnimation(self.icon_label, b"geometry")
        self.animation2.setDuration(1400)
        self.animation2.setStartValue(QtCore.QRect(width + 10, self.height, 20, 20))
        self.animation2.setEndValue(QtCore.QRect(self.width, self.height, 20, 20))
        self.animation2.setEasingCurve(QtCore.QEasingCurve.Type.OutBounce)

        self.animation3 = QtCore.QPropertyAnimation(self.icon_label, b"geometry")
        self.animation3.setDuration(700)
        self.animation3.setStartValue(QtCore.QRect(self.width, self.height, 20, 20))
        self.animation3.setEndValue(QtCore.QRect(width + 10, self.height, 20, 20))

    def enterEvent(self, event):
        self.animation.start()
        self.animation2.start()

    def leaveEvent(self, event):
        self.animation1.start()
        self.animation3.start()
