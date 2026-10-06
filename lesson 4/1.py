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


def to_sci(d, limit=None):
    return format(d, '.2e')


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

        self.current = '0'
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.error = False

        self.initUI()

    def initUI(self):
        self.setGeometry(710, 300, 300, 400)
        self.setWindowTitle('Калькулятор')

        self.main_label = QLabel('0', self)
        self.main_label.move(10, 25)
        self.main_label.resize(280, 45)
        self.main_label.setStyleSheet("font-size: 20pt;font-weight: bold;")
        self.main_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.secondary_label = QLabel('', self)
        self.secondary_label.move(10, 0)
        self.secondary_label.resize(280, 25)
        self.secondary_label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        self.number_buttons = [None] * 10
        for digit in range(1, 10):
            row = (9 - digit) // 3
            col = (digit - 1) % 3
            btn = QPushButton(str(digit), self)
            btn.move(10 + 70 * col, 70 + 65 * row)
            btn.resize(70, 65)
            btn.clicked.connect(lambda checked, d=digit: self.numbers_clicked(d))
            self.number_buttons[digit] = btn

        self.zero = QPushButton('0', self)
        self.zero.resize(70, 65)
        self.zero.move(80, 265)
        self.zero.clicked.connect(lambda checked: self.numbers_clicked(0))
        self.number_buttons[0] = self.zero

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

    def update_main(self):
        text = self.current
        if len(text) > MAIN_LIMIT:
            text = to_sci(Decimal(text), MAIN_LIMIT)
        self.main_label.setText(text)

    def update_secondary(self):
        if self.operand is None or self.operator is None:
            self.secondary_label.setText('')
            return
        text = to_plain(self.operand)
        if len(text.lstrip('-').replace('.', '')) > SECONDARY_LIMIT:
            text = to_sci(self.operand, SECONDARY_LIMIT)
        self.secondary_label.setText(f'{text} {self.operator}')

    def reset(self):
        self.current = '0'
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.error = False
        self.update_main()
        self.update_secondary()

    def show_error(self):
        self.error = True
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.main_label.setText(ERROR_TEXT)
        self.secondary_label.setText('')

    def calculate(self, a, op, b):
        if op == '+':
            return a + b
        if op == '-':
            return a - b
        if op == '*':
            return a * b
        if op == '/':
            if b == 0:
                return None
            return a / b
        return None

    def numbers_clicked(self, digit):
        if self.error:
            self.error = False
            self.current = '0'
            self.new_entry = True
        if self.new_entry or self.current == '0':
            self.current = str(digit)
            self.new_entry = False
        else:
            self.current += str(digit)
        self.update_main()

    def c_button(self):
        self.reset()

    def ce_button(self):
        if self.error:
            self.reset()
            return
        self.current = '0'
        self.new_entry = False
        self.update_main()

    def operator_clicked(self, op):
        if self.error:
            self.reset()
            return
        if self.operator is not None and not self.new_entry:
            result = self.calculate(self.operand, self.operator, Decimal(self.current))
            if result is None:
                self.show_error()
                return
            self.operand = result
            self.current = to_plain(result)
            self.update_main()
        elif self.operator is None:
            self.operand = Decimal(self.current)
        self.operator = op
        self.new_entry = True
        self.update_secondary()

    def divbc(self):
        self.operator_clicked('/')

    def mulbc(self):
        self.operator_clicked('*')

    def subbc(self):
        self.operator_clicked('-')

    def addbc(self):
        self.operator_clicked('+')

    def fpbc(self):
        if self.error:
            self.reset()
            return
        if self.new_entry:
            self.current = '0.'
            self.new_entry = False
        elif '.' not in self.current:
            self.current += '.'
        self.update_main()

    def pmbc(self):
        if self.error:
            self.reset()
            return
        if Decimal(self.current) == 0:
            return
        if self.current.startswith('-'):
            self.current = self.current[1:]
        else:
            self.current = '-' + self.current
        self.update_main()

    def equbc(self):
        if self.error:
            self.reset()
            return
        if self.operator is None or self.operand is None:
            return
        result = self.calculate(self.operand, self.operator, Decimal(self.current))
        if result is None:
            self.show_error()
            return
        self.current = to_plain(result)
        self.operand = None
        self.operator = None
        self.new_entry = True
        self.update_main()
        self.update_secondary()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
