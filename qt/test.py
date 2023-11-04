import sys
import PyQt5.QtWidgets as qw
import PyQt5.QtGui as qg
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(qw.QWidget):
    def __init__(self):
        super().__init__()
        # self.setGeometry(500, 300, 400, 200)
        self.setWindowTitle("hello")

        self.setLayout(qw.QVBoxLayout())
        label = qw.QLabel("pick dometing from the list")
        label.setFont(qg.QFont("times", 20))
        self.layout().addWidget(label)

        entry = qw.QLineEdit()
        entry.setObjectName("field")
        entry.setFont(qg.QFont("times", 20))
        # entry.setText("hello")
        self.layout().addWidget(entry)

        combo = qw.QComboBox(editable=True, insertPolicy=qw.QComboBox.InsertAtTop)
        combo.addItem("pepper", 1)
        combo.addItem("egg", 2)
        combo.addItem("mushroom", 3)
        combo.addItem("pepper", 4)
        combo.setFont(qg.QFont("times", 20))
        self.layout().addWidget(combo)

        btn = qw.QPushButton("click", clicked=lambda: press())
        btn.setFont(qg.QFont("times", 20))
        self.layout().addWidget(btn)

        self.show()

        def press():
            label.setText(f"Hello {combo.currentData()}")
            entry.setText("")


app = qw.QApplication(sys.argv)
window = MainWindow()
app.exec_()
