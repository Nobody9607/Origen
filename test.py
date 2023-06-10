import sys
from PyQt5 import QtWidgets
from PyQt5.QtPrintSupport import QPrinter
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import reportlab.lib.pagesizes as pagesizes
from reportlab.pdfgen.canvas import Canvas

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # Create a layout
        layout = QtWidgets.QVBoxLayout()

        # Create a table widget and add some data
        self.table = QtWidgets.QTableWidget()
        self.table.setRowCount(3)
        self.table.setColumnCount(2)
        self.table.setItem(0, 0, QtWidgets.QTableWidgetItem("A"))
        self.table.setItem(0, 1, QtWidgets.QTableWidgetItem("1"))
        self.table.setItem(1, 0, QtWidgets.QTableWidgetItem("B"))
        self.table.setItem(1, 1, QtWidgets.QTableWidgetItem("2"))
        self.table.setItem(2, 0, QtWidgets.QTableWidgetItem("C"))
        self.table.setItem(2, 1, QtWidgets.QTableWidgetItem("3"))

        # Add the table to the layout
        layout.addWidget(self.table)

        # Create a plot widget and add some data
        self.graphWidget = pg.PlotWidget()
        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35]
        self.graphWidget.plot(hour, temperature)

        # Add the plot to the layout
        layout.addWidget(self.graphWidget)

        # Create a button to export the content to PDF
        btn = QtWidgets.QPushButton("Export to PDF")
        btn.clicked.connect(self.export_to_pdf)
        layout.addWidget(btn)

        # Set the layout on the window
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def export_to_pdf(self):
        # Create a QPrinter object and set its output format to PDF
        printer = QPrinter()
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName("output.pdf")

        # Create a reportlab canvas and set its page size
        canvas = Canvas(printer.outputFileName(), pagesize=pagesizes.A4)

        # Export the table to the PDF
        for row in range(self.table.rowCount()):
            for col in range(self.table.columnCount()):
                item = self.table.item(row, col)
                if item is not None:
                    text = item.text()
                    canvas.drawString(50 + col * 100, 800 - row * 20, text)

        # Export the plot to the PDF
        pixmap = self.graphWidget.grab()
        pixmap.save("plot.png")
        canvas.drawImage("plot.png", 50, 400)

        # Save the PDF file and show a message
        canvas.save()
        QtWidgets.QMessageBox.information(self, "Exported", "PDF file exported successfully")

# Run the application
app = QtWidgets.QApplication(sys.argv)
w = MainWindow()
w.show()
sys.exit(app.exec_())