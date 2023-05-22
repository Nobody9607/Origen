from PyQt5 import QtWidgets, QtCore
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MyWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Crear una gráfica de Matplotlib y agregarla a la ventana
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.ax = self.canvas.figure.subplots()
        self.ax.plot([0, 1, 2], [0, 1, 0])
        self.canvas.figure.tight_layout()

        # Crear una tabla y agregarla a la ventana
        self.table = QtWidgets.QTableWidget(2, 2)
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("A"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("B"))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("C"))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem("D"))

        # Crear una etiqueta y agregarla a la ventana
        self.label = QtWidgets.QLabel("Texto")

        # Agregar los widgets a un QStackedWidget para poder cambiar entre ellos
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.stacked_widget.addWidget(self.canvas)
        self.stacked_widget.addWidget(self.table)
        self.stacked_widget.addWidget(self.label)

        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)

        # Crear un temporizador y conectar su señal timeout a una función
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.update_content)

        # Establecer el intervalo de tiempo y comenzar el temporizador
        self.timer.setInterval(3000) # 1000 milisegundos = 1 segundo
        self.timer.start()

    def update_content(self):
        # Cambiar el widget actual en el QStackedWidget
        current_index = self.stacked_widget.currentIndex()
        if current_index == 2:
            next_index = 0
        else:
            next_index = current_index + 1
        self.stacked_widget.setCurrentIndex(next_index)

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()