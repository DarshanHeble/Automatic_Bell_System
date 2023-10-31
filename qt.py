from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont


def main():
    app = QApplication([])
    Window = QWidget()
    Window.setWindowTitle("heo")
    Window.setGeometry(500, 100, 200, 300)

    layout = QVBoxLayout()

    l = QLabel("press")
    textbox = QTextEdit()
    b = QPushButton("press btn")
    b.clicked.connect(click)

    layout.addWidget(l)
    layout.addWidget(b)

    Window.setLayout(layout)

    Window.show()
    app.exec_()


def click():
    message = QMessageBox()
    message.setText("hello w")
    message.exec_()
    print("click")


if __name__ == "__main__":
    main()
