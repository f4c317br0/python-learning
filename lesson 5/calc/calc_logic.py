import sys
from decimal import Decimal, getcontext
from math import factorial
from PyQt6.QtWidgets import QApplication, QWidget
from calc import Ui_Form

getcontext().prec = 30

MAIN_LIMIT = 11
ERROR_TEXT = 'Error'
FACT_LIMIT = 1000


def to_plain(d):
    if d == 0:
        return '0'
    return format(d.normalize(), 'f')


def to_sci(d):
    return format(d, '.2e')


class Calculator(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.current = '0'
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.error = False

        self.table.setDigitCount(MAIN_LIMIT)

        self.buttonGroup_digits.buttonClicked.connect(self.digit_clicked)
        self.buttonGroup_binary.buttonClicked.connect(self.binary_clicked)
        self.btn_eq.clicked.connect(self.equbc)
        self.btn_dot.clicked.connect(self.fpbc)
        self.btn_clear.clicked.connect(self.reset)
        self.btn_sqrt.clicked.connect(self.sqrt_clicked)
        self.btn_fact.clicked.connect(self.fact_clicked)

        self.update_main()

    def update_main(self):
        text = self.current
        if len(text) > MAIN_LIMIT:
            text = to_sci(Decimal(text))
        self.table.display(text)

    def reset(self):
        self.current = '0'
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.error = False
        self.update_main()

    def show_error(self):
        self.error = True
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.table.display(ERROR_TEXT)

    def calculate(self, a, op, b):
        try:
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
            if op == '^':
                return a ** b
        except ArithmeticError:
            return None
        return None

    def digit_clicked(self, button):
        self.numbers_clicked(int(button.text()))

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

    def binary_clicked(self, button):
        self.operator_clicked(button.text())

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

    def sqrt_clicked(self):
        if self.error:
            self.reset()
            return
        value = Decimal(self.current)
        if value < 0:
            self.show_error()
            return
        self.current = to_plain(value.sqrt())
        self.new_entry = True
        self.update_main()

    def fact_clicked(self):
        if self.error:
            self.reset()
            return
        value = Decimal(self.current)
        if value < 0 or value != value.to_integral_value() or value > FACT_LIMIT:
            self.show_error()
            return
        self.current = to_plain(Decimal(factorial(int(value))))
        self.new_entry = True
        self.update_main()

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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Calculator()
    ex.show()
    sys.exit(app.exec())
