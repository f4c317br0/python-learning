import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QCheckBox, QPlainTextEdit, QLineEdit


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = None
        self.initUI()

    def initUI(self):
        self.setGeometry(710, 300, 300, 400)
        self.setWindowTitle('Example')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
