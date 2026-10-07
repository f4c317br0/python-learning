import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from first import Ui_Form

class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 300)
        self.setupUi(self)
        self.make_flag.clicked.connect(self.run)

    def run(self):
        res = []
        for el in self.color_group_1.buttons():
            if el.isChecked():
                res.append(el.text())
        for el in self.color_group_2.buttons():
            if el.isChecked():
                res.append(el.text())
        for el in self.color_group_3.buttons():
            if el.isChecked():
                res.append('и ' + el.text())

        self.result.setText(f'Цвета: {', '.join(res)}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
