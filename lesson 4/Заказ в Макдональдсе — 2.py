import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QCheckBox, QPlainTextEdit,
                             QPushButton, QLineEdit)


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.menu = {
            "Чизбургер": 10,
            "Гамбургер": 20,
            "Кока-кола": 15,
            "Наггетсы": 30,
        }
        self.checkboxes = []
        self.inputs = []
        self.initUI()

    def initUI(self):
        self.setGeometry(710, 300, 500, 600)
        self.setWindowTitle('Заказ в Макдональдсе')

        for i, name in enumerate(self.menu):
            checkbox = QCheckBox(name, self)
            checkbox.move(10, 10 + i * 30)
            checkbox.resize(checkbox.sizeHint())
            checkbox.toggled.connect(lambda checked, index=i: self.on_toggled(index, checked))
            self.checkboxes.append(checkbox)

            line = QLineEdit(self)
            line.move(130, 8 + i * 30)
            line.resize(60, 22)
            self.inputs.append(line)

        self.orderButton = QPushButton('Заказать', self)
        self.orderButton.move(10, 140)
        self.orderButton.clicked.connect(self.make_order)

        self.order = QPlainTextEdit(self)
        self.order.setPlainText('Ваш заказ\n')
        self.order.move(10, 180)
        self.order.resize(300, 400)
        self.order.setReadOnly(True)

    def on_toggled(self, index, checked):
        line = self.inputs[index]
        if checked:
            if not line.text().strip():
                line.setText('1')
        else:
            line.setText('')

    def get_count(self, line):
        text = line.text().strip()
        try:
            return int(text)
        except ValueError:
            return 1

    def make_order(self):
        self.order.setPlainText('Ваш заказ\n')
        total = 0
        for checkbox, line in zip(self.checkboxes, self.inputs):
            if not checkbox.isChecked():
                continue
            count = self.get_count(line)
            if count <= 0:
                continue
            name = checkbox.text()
            cost = self.menu[name] * count
            total += cost
            self.order.appendPlainText(f'{name}-----{count}-----{cost}')
        self.order.appendPlainText(f'\nИтого: {total}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
