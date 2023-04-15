import sys
from model import *

from PyQt5.QtWidgets import QMainWindow, QApplication, QVBoxLayout, QTableWidgetItem
from PyQt5.QtCore import QSize


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.model = TestModel(saves_data)
        self.view = TestView()
        self.view.setModel(self.model)

        self.checkboxes = []
        for row in range(self.model.rowCount(0)):
            checkbox = TestCheckBox(self.model, row)
            checkbox.stateChanged.connect(checkbox.checkbox_clicked)
            self.checkboxes.append(checkbox)

            layout = QVBoxLayout()
            layout.setAlignment(Qt.AlignHCenter)
            layout.addWidget(checkbox)

            pane = QWidget()
            pane.setLayout(layout)
            # pane.
            # checkbox.setAutoFillBackground(True)
            self.view.setIndexWidget(self.model.index(row, 0), pane)

        self.view.resizeColumnsToContents()
        self.view.resizeRowsToContents()
        self.setCentralWidget(self.view)

    def sizeHint(self):
        return QSize(400, 300)




app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()


