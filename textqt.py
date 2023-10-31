import sys
from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QPushButton,
    QFrame,
    QScrollArea,
    QWidget,
)
from PyQt5.QtGui import QFont

app = QApplication(sys.argv)


def open_window():
    # Your open_window function logic here
    pass


main_window = QMainWindow()
main_window.setWindowTitle("PyQt GUI Example")

mainframe = QWidget(main_window)
main_window.setCentralWidget(mainframe)

scroll_area = QScrollArea(mainframe)
scroll_area.setWidgetResizable(True)
mainframe_layout = QVBoxLayout()
mainframe_layout.addWidget(scroll_area)
mainframe.setLayout(mainframe_layout)

scroll_frame = QWidget()
scroll_area.setWidget(scroll_frame)
scroll_frame_layout = QVBoxLayout()
scroll_frame.setLayout(scroll_frame_layout)

buttonframe = QFrame(mainframe)
mainframe_layout.addWidget(buttonframe)

btn = QPushButton("+", buttonframe)
btn.setMaximumWidth(50)
btn.setMaximumHeight(50)
btn.setFont(QFont("Arial", 40))

btn.clicked.connect(open_window)

main_window.show()
sys.exit(app.exec_())
