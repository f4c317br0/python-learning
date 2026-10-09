import sys  #
from decimal import Decimal, getcontext  # импорт для вывода экспоненты
from math import factorial  # для кнопки факториала
from PyQt6.QtWidgets import QApplication, QWidget  # основа виджета
# from calc import Ui_Form


from PyQt6 import QtCore, QtGui, QtWidgets


# создание оболочки
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(371, 565)
        self.layoutWidget = QtWidgets.QWidget(parent=Form)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 20, 345, 481))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table = QtWidgets.QLCDNumber(parent=self.layoutWidget)
        self.table.setObjectName("table")
        self.verticalLayout.addWidget(self.table)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn8 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn8.setMinimumSize(QtCore.QSize(80, 80))
        self.btn8.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn8.setFont(font)
        self.btn8.setObjectName("btn8")
        self.buttonGroup_digits = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_digits.setObjectName("buttonGroup_digits")
        self.buttonGroup_digits.addButton(self.btn8)
        self.gridLayout.addWidget(self.btn8, 2, 1, 1, 1)
        self.btn2 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn2.setMinimumSize(QtCore.QSize(80, 80))
        self.btn2.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn2.setFont(font)
        self.btn2.setObjectName("btn2")
        self.buttonGroup_digits.addButton(self.btn2)
        self.gridLayout.addWidget(self.btn2, 0, 1, 1, 1)
        self.btn_plus = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_plus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_plus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_plus.setFont(font)
        self.btn_plus.setObjectName("btn_plus")
        self.buttonGroup_binary = QtWidgets.QButtonGroup(Form)
        self.buttonGroup_binary.setObjectName("buttonGroup_binary")
        self.buttonGroup_binary.addButton(self.btn_plus)
        self.gridLayout.addWidget(self.btn_plus, 0, 3, 1, 1)
        self.btn_eq = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_eq.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_eq.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_eq.setFont(font)
        self.btn_eq.setObjectName("btn_eq")
        self.gridLayout.addWidget(self.btn_eq, 3, 2, 1, 1)
        self.btn0 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn0.setMinimumSize(QtCore.QSize(80, 80))
        self.btn0.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn0.setFont(font)
        self.btn0.setObjectName("btn0")
        self.buttonGroup_digits.addButton(self.btn0)
        self.gridLayout.addWidget(self.btn0, 3, 0, 1, 1)
        self.btn_div = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_div.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_div.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_div.setFont(font)
        self.btn_div.setObjectName("btn_div")
        self.buttonGroup_binary.addButton(self.btn_div)
        self.gridLayout.addWidget(self.btn_div, 3, 3, 1, 1)
        self.btn1 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn1.setMinimumSize(QtCore.QSize(80, 80))
        self.btn1.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn1.setFont(font)
        self.btn1.setObjectName("btn1")
        self.buttonGroup_digits.addButton(self.btn1)
        self.gridLayout.addWidget(self.btn1, 0, 0, 1, 1)
        self.btn9 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn9.setMinimumSize(QtCore.QSize(80, 80))
        self.btn9.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn9.setFont(font)
        self.btn9.setObjectName("btn9")
        self.buttonGroup_digits.addButton(self.btn9)
        self.gridLayout.addWidget(self.btn9, 2, 2, 1, 1)
        self.btn_dot = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_dot.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_dot.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_dot.setFont(font)
        self.btn_dot.setObjectName("btn_dot")
        self.gridLayout.addWidget(self.btn_dot, 3, 1, 1, 1)
        self.btn3 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn3.setMinimumSize(QtCore.QSize(80, 80))
        self.btn3.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn3.setFont(font)
        self.btn3.setObjectName("btn3")
        self.buttonGroup_digits.addButton(self.btn3)
        self.gridLayout.addWidget(self.btn3, 0, 2, 1, 1)
        self.btn4 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn4.setMinimumSize(QtCore.QSize(80, 80))
        self.btn4.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn4.setFont(font)
        self.btn4.setObjectName("btn4")
        self.buttonGroup_digits.addButton(self.btn4)
        self.gridLayout.addWidget(self.btn4, 1, 0, 1, 1)
        self.btn5 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn5.setMinimumSize(QtCore.QSize(80, 80))
        self.btn5.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn5.setFont(font)
        self.btn5.setObjectName("btn5")
        self.buttonGroup_digits.addButton(self.btn5)
        self.gridLayout.addWidget(self.btn5, 1, 1, 1, 1)
        self.btn7 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn7.setMinimumSize(QtCore.QSize(80, 80))
        self.btn7.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn7.setFont(font)
        self.btn7.setObjectName("btn7")
        self.buttonGroup_digits.addButton(self.btn7)
        self.gridLayout.addWidget(self.btn7, 2, 0, 1, 1)
        self.btn6 = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn6.setMinimumSize(QtCore.QSize(80, 80))
        self.btn6.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn6.setFont(font)
        self.btn6.setObjectName("btn6")
        self.buttonGroup_digits.addButton(self.btn6)
        self.gridLayout.addWidget(self.btn6, 1, 2, 1, 1)
        self.btn_minus = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_minus.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_minus.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_minus.setFont(font)
        self.btn_minus.setObjectName("btn_minus")
        self.buttonGroup_binary.addButton(self.btn_minus)
        self.gridLayout.addWidget(self.btn_minus, 1, 3, 1, 1)
        self.btn_mult = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_mult.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_mult.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_mult.setFont(font)
        self.btn_mult.setObjectName("btn_mult")
        self.buttonGroup_binary.addButton(self.btn_mult)
        self.gridLayout.addWidget(self.btn_mult, 2, 3, 1, 1)
        self.btn_pow = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_pow.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_pow.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_pow.setFont(font)
        self.btn_pow.setObjectName("btn_pow")
        self.buttonGroup_binary.addButton(self.btn_pow)
        self.gridLayout.addWidget(self.btn_pow, 4, 0, 1, 1)
        self.btn_sqrt = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_sqrt.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_sqrt.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_sqrt.setFont(font)
        self.btn_sqrt.setObjectName("btn_sqrt")
        self.gridLayout.addWidget(self.btn_sqrt, 4, 1, 1, 1)
        self.btn_fact = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_fact.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_fact.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_fact.setFont(font)
        self.btn_fact.setObjectName("btn_fact")
        self.gridLayout.addWidget(self.btn_fact, 4, 2, 1, 1)
        self.btn_clear = QtWidgets.QPushButton(parent=self.layoutWidget)
        self.btn_clear.setMinimumSize(QtCore.QSize(80, 80))
        self.btn_clear.setMaximumSize(QtCore.QSize(80, 80))
        font = QtGui.QFont()
        font.setFamily("Helvetica")
        font.setPointSize(36)
        self.btn_clear.setFont(font)
        self.btn_clear.setStyleSheet("background-color: rgb(254, 166, 43);")
        self.btn_clear.setObjectName("btn_clear")
        self.gridLayout.addWidget(self.btn_clear, 4, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Красивый калькулятор"))
        self.btn8.setText(_translate("Form", "8"))
        self.btn2.setText(_translate("Form", "2"))
        self.btn_plus.setText(_translate("Form", "+"))
        self.btn_eq.setText(_translate("Form", "="))
        self.btn0.setText(_translate("Form", "0"))
        self.btn_div.setText(_translate("Form", "/"))
        self.btn1.setText(_translate("Form", "1"))
        self.btn9.setText(_translate("Form", "9"))
        self.btn_dot.setText(_translate("Form", "."))
        self.btn3.setText(_translate("Form", "3"))
        self.btn4.setText(_translate("Form", "4"))
        self.btn5.setText(_translate("Form", "5"))
        self.btn7.setText(_translate("Form", "7"))
        self.btn6.setText(_translate("Form", "6"))
        self.btn_minus.setText(_translate("Form", "-"))
        self.btn_mult.setText(_translate("Form", "*"))
        self.btn_pow.setText(_translate("Form", "^"))
        self.btn_sqrt.setText(_translate("Form", "√"))
        self.btn_fact.setText(_translate("Form", "!"))
        self.btn_clear.setText(_translate("Form", "C"))


getcontext().prec = 30


def to_plain(d): # из документации работы с decimal : Используется для создания канонических значений класса эквивалентности в текущем или указанном контексте.
    if d == 0:
        return '0'
    return format(d.normalize(), 'f')


class Calculator(QWidget, Ui_Form): # логика
    def __init__(self): # инициализация
        super().__init__()
        self.setupUi(self) # окно

        self.current = '0' # текущее значение по умолчанию 0
        self.operand = None # текущий операнд
        self.operator = None # текущий оператор
        self.new_entry = False # второе число, по умолчанию нет еще
        self.error = False # наличие ошибки по умолчанию нет

        self.table.setDigitCount(11) # длина лейбла

        # подключение кнопок к их функциям
        self.buttonGroup_digits.buttonClicked.connect(self.digit_clicked)
        self.buttonGroup_binary.buttonClicked.connect(self.binary_clicked)
        self.btn_eq.clicked.connect(self.equbc)
        self.btn_dot.clicked.connect(self.fpbc)
        self.btn_clear.clicked.connect(self.reset)
        self.btn_sqrt.clicked.connect(self.sqrt_clicked)
        self.btn_fact.clicked.connect(self.fact_clicked)

        self.update_main() # проверка длины

    def update_main(self): # проверка длины лейбла чтобы не более 11
        text = self.current # текст лейбла
        if len(text) > 11: # если более, то преобразование по децималу в формат .2е
            text = format(Decimal(text), '.2e')
        self.table.display(text)

    def reset(self): # кнопка с нажата то все очищается, все сбрасывается
        self.current = '0'
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.error = False
        self.update_main()

    def show_error(self): # если ошибка, то также очистка + вывод ошибки
        self.error = True
        self.operand = None
        self.operator = None
        self.new_entry = False
        self.table.display('Error')

    def calculate(self, a, op, b): # основной подсчет, передается кнопка, возвращается результат
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
        except ArithmeticError: # Основной класс для ошибок типа деления на ноль и т.д. т.к. ошибка проверяется не здесь, нужен только результат
            return None
        return None

    def digit_clicked(self, button):
        self.numbers_clicked(int(button.text()))

    def numbers_clicked(self, digit):  # запись числа в память
        if self.error: # если ошибка, то полный сброс
            self.error = False
            self.current = '0'
            self.new_entry = True
        if self.new_entry or self.current == '0': # если текущее или новое число равно нулю, то текущее = переданному числу, нового еще нет
            self.current = str(digit)
            self.new_entry = False
        else: # в противном случае, текущее число просто обновляется
            self.current += str(digit)
        self.update_main() # проверка лейбла в любом случае

    def binary_clicked(self, button): # при нажатии на точку отправляет с кнопкой к след функции
        self.operator_clicked(button.text())

    def operator_clicked(self, op): # вызван оператор
        if self.error: # всегда проверяем наличие ошибки
            self.reset() # сброс при ошибке
            return
        if self.operator is not None and not self.new_entry: # ВАЖНОЕ если например 6 + 6 + 6 вводится, то сначала считается 6 + 6 сразу вывод и дальше + 6 идет
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

    def sqrt_clicked(self): # логика при нажатии квадрата
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

    def fact_clicked(self): # факториал
        if self.error:
            self.reset()
            return
        value = Decimal(self.current) # число переводим в децимал
        if value < 0 or value != value.to_integral_value() or value > 1000:
            self.show_error()
            return
        self.current = to_plain(Decimal(factorial(int(value))))
        self.new_entry = True
        self.update_main()

    def fpbc(self): # осталось от прошлого кода
        if self.error:
            self.reset()
            return
        if self.new_entry:
            self.current = '0.'
            self.new_entry = False
        elif '.' not in self.current:
            self.current += '.'
        self.update_main()

    def equbc(self): # логика степени
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
