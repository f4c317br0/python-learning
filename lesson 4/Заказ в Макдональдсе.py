import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QPlainTextEdit, QPushButton


class MacOrder(QWidget):
    def __init__(self):
        super().__init__()
        self.result = None
        self.order_btn = None
        self.checkbox1 = None
        self.menu = ["Чизбургер", "Гамбургер", "Кока-кола", "Наггетсы"]
        self.menu_checkboxes = []
        self.menu_toggled = []
        self.initUI()

    def initUI(self):
        self.setGeometry(710, 300, 500, 600)
        self.setWindowTitle('')

        for i in range(4):
            checkbox = QCheckBox(self.menu[i], self)
            checkbox.move(10, 10 + i * 20)
            checkbox.resize(checkbox.sizeHint())

            checkbox.toggled.connect(lambda checked, index=i: self.if_toggled(index, checked))

            self.menu_checkboxes.append(checkbox)

        self.order_btn = QPushButton('Заказать', self)
        self.order_btn.move(10, 110)

        self.result = QPlainTextEdit(self)
        self.result.setPlainText('Ваш заказ:\n')
        self.result.move(10, 150)
        self.result.resize(300, 400)
        self.result.setReadOnly(True)

        self.order_btn.clicked.connect(self.run)

    def if_toggled(self, index, checked):
        if checked:
            try:
                self.menu_toggled.append(self.menu_checkboxes[index].text())
                self.menu_toggled.sort(key=self.menu.index)
            except Exception as er:
                print(er)
        else:
            try:
                self.menu_toggled.remove(self.menu_checkboxes[index].text())
            except Exception as er:
                print(er)

    def run(self):
        try:
            self.result.setPlainText('Ваш заказ:\n')
            for el in self.menu_toggled:
                self.result.appendPlainText(el)
        except Exception as er:
            print(er)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MacOrder()
    ex.show()
    sys.exit(app.exec())
