from PyQt5.QtWidgets import *
from Ventanas.principal import *
import sys


app = QApplication(sys.argv)



ventana = VentanaPrincipal()
ventana.show()
app.exec_()