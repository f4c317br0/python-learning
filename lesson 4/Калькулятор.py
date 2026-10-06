import sys
from decimal import Decimal, getcontext

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QLabel, QPushButton, QWidget

getcontext().prec = 30

MAIN_LIMIT = 11
SECONDARY_LIMIT = 30
ERROR_TEXT = 'ОШИБКА'

def to_plain(d):
    if d == 0:
        return '0'
    return format(d.normalize(), 'f')


def to_sci(d, limit):
    s = format(d, 'E')
    for p in range(limit, -1, -1):
        s = format(d, f'.{p}E')
        if len(s) <= limit:
            break
    mantissa, exp = s.split('E')
    if '.' in mantissa:
        mantissa = mantissa.rstrip('0').rstrip('.')
    return f'{mantissa}E{exp}'

class Calculator(QWidget):
    def __init__(self):
        super().__init__()
        self.equals_button = None
        self.plus_minus_button = None
        self.float_point_button = None
        self.add_button = None
        self.substract_button = None
        self.multiply_button = None
        self.divide_button = None
        self.clear_entry_button = None
        self.clear_button = None
        self.zero = None
        self.secondary_label = None
        self.main_label = None
        self.number_buttons = []
        self.numbers = ['789', '456', '123']
        self.initUI()

    def initUI(self):
        self.setGeometry(710, 300, 300, 400)
        self.setWindowTitle('Калькулятор')

        self.main_label = QLabel('0', self)
        self.main_label.move(120, 20)
        self.main_label.resize(176, 50)
        self.main_label.setStyleSheet("font-size: 20pt;font-weight: bold;")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.secondary_label = QLabel('123456789123456789123456789123', self)
        self.secondary_label.move(120, 0)
        self.secondary_label.resize(180, 80)
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignTop)

        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton(self.numbers[row][col], self)
                btn.move(10 + 70 * col, 70 + 65 * row)
                btn.resize(70, 65)
                btn.clicked.connect(lambda checked, r=row, c=col: self.numbers_clicked(r, c))
                row_buttons.append(btn)
            self.number_buttons.append(row_buttons)

        self.zero = QPushButton('0', self)
        self.zero.resize(70, 65)
        self.zero.move(80, 265)
        self.number_buttons.append([self.zero])
        self.zero.clicked.connect(lambda checked, r=-1, c=-1: self.numbers_clicked(r, c))

        self.clear_button = QPushButton('C', self)
        self.clear_button.resize(70, 65)
        self.clear_button.move(10, 265)
        self.clear_button.clicked.connect(self.c_button)

        self.clear_entry_button = QPushButton('CE', self)
        self.clear_entry_button.resize(70, 65)
        self.clear_entry_button.move(150, 265)
        self.clear_entry_button.clicked.connect(self.ce_button)

        self.divide_button = QPushButton('/', self)
        self.divide_button.resize(70, 65)
        self.divide_button.move(220, 70)
        self.divide_button.clicked.connect(self.divbc)

        self.multiply_button = QPushButton('*', self)
        self.multiply_button.resize(70, 65)
        self.multiply_button.move(220, 70 + 65)
        self.multiply_button.clicked.connect(self.mulbc)

        self.substract_button = QPushButton('-', self)
        self.substract_button.resize(70, 65)
        self.substract_button.move(220, 70 + 65 * 2)
        self.substract_button.clicked.connect(self.subbc)

        self.add_button = QPushButton('+', self)
        self.add_button.resize(70, 65)
        self.add_button.move(220, 70 + 65 * 3)
        self.add_button.clicked.connect(self.addbc)

        self.float_point_button = QPushButton('.', self)
        self.float_point_button.resize(70, 65)
        self.float_point_button.move(10, 70 + 65 * 4)
        self.float_point_button.clicked.connect(self.fpbc)

        self.plus_minus_button = QPushButton('±', self)
        self.plus_minus_button.resize(70, 65)
        self.plus_minus_button.move(10 + 70, 70 + 65 * 4)
        self.plus_minus_button.clicked.connect(self.pmbc)
        
        self.equals_button = QPushButton('=', self)
        self.equals_button.resize(140, 65)
        self.equals_button.move(150, 70 + 65 * 4)
        self.equals_button.clicked.connect(self.equbc)

    def numbers_clicked(self, r, c):
        num = self.number_buttons[r][c].text()
        if self.main_label.text() == '0':
            self.main_label.setText(num)
        else:
            self.main_label.setText(self.main_label.text() + num)

    def c_button(self):
        self.main_label.setText('0')
        self.secondary_label.setText('')

    def ce_button(self):
        self.main_label.setText('0')

    def divbc(self):
        pass

    def mulbc(self):
        pass

    def subbc(self):
        pass

    def addbc(self):
        pass

    def fpbc(self):
        if '.' not in self.main_label.text():
            self.main_label.setText(self.main_label.text() + '.')
        else:
            pass

    def pmbc(self):
        self.main_label.setText(str(int(self.main_label.text()) * -1))

    def equbc(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
