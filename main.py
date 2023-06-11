from PyQt5.QtWidgets import *
from Windows.MainWindow import MainWindow
import sys


app = QApplication(sys.argv)

window = MainWindow()
window.show()
app.exec_()