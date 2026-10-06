import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QLabel


class Arifmometr(QWidget):
    def __init__(self):
        super().__init__()
        self.second_value = None
        self.multiply_button = None
        self.substract_button = None
        self.add_button = None
        self.first_value = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Прятки для виджетов')

        self.first_value = QLineEdit('0', self)
        self.first_value.move(10, 35)
        self.first_value.resize(50, 20)

        self.add_button = QPushButton('+', self)
        self.add_button.move(60, 35)
        self.add_button.resize(30, 20)

        self.substract_button = QPushButton('-', self)
        self.substract_button.move(90, 35)
        self.substract_button.resize(30, 20)

        self.multiply_button = QPushButton('*', self)
        self.multiply_button.move(120, 35)
        self.multiply_button.resize(30, 20)

        self.second_value = QLineEdit('0', self)
        self.second_value.move(150, 35)
        self.second_value.resize(50, 20)

        self.res = QLabel('=', self)
        self.res.move(201, 35)
        self.res.resize(30, 20)

        self.result = QLineEdit('0', self)
        self.result.move(210, 35)
        self.result.resize(50, 20)
        self.result.setReadOnly(True)

        self.add_button.clicked.connect(self.add)
        self.substract_button.clicked.connect(self.sub)
        self.multiply_button.clicked.connect(self.multiply)

    def add(self):
        try:
            self.result.setText(str((int(self.first_value.text())) + int(self.second_value.text())))
        except Exception as er:
            print(er)

    def sub(self):
        try:
            self.result.setText(str((int(self.first_value.text())) - int(self.second_value.text())))
        except Exception as er:
            print(er)

    def multiply(self):
        try:
            self.result.setText(str((int(self.first_value.text())) * int(self.second_value.text())))
        except Exception as er:
            print(er)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Arifmometr()
    ex.show()
    sys.exit(app.exec())
