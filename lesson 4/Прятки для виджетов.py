import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCheckBox, QLineEdit


class WidgetsHideNSeek(QWidget):
    def __init__(self):
        super().__init__()
        self.edit4 = None
        self.edit3 = None
        self.edit2 = None
        self.edit1 = None
        self.checkbox4 = None
        self.checkbox3 = None
        self.checkbox2 = None
        self.checkbox1 = None
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 300, 100)
        self.setWindowTitle('Прятки для виджетов')

        self.checkbox1 = QCheckBox('edit1', self)
        self.checkbox1.move(10, 10)
        self.checkbox1.resize(self.checkbox1.sizeHint())

        self.checkbox2 = QCheckBox('edit2', self)
        self.checkbox2.move(10, 30)
        self.checkbox2.resize(self.checkbox1.sizeHint())

        self.checkbox3 = QCheckBox('edit3', self)
        self.checkbox3.move(10, 50)
        self.checkbox3.resize(self.checkbox1.sizeHint())

        self.checkbox4 = QCheckBox('edit4', self)
        self.checkbox4.move(10, 70)
        self.checkbox4.resize(self.checkbox1.sizeHint())

        self.edit1 = QLineEdit(self)
        self.edit2 = QLineEdit(self)
        self.edit3 = QLineEdit(self)
        self.edit4 = QLineEdit(self)

        self.edit1.resize(self.edit1.sizeHint())
        self.edit2.resize(self.edit2.sizeHint())
        self.edit3.resize(self.edit3.sizeHint())
        self.edit4.resize(self.edit4.sizeHint())

        self.edit1.setText('Поле edit1')
        self.edit2.setText('Поле edit2')
        self.edit3.setText('Поле edit3')
        self.edit4.setText('Поле edit4')

        self.edit1.move(70, 10)
        self.edit2.move(70, 30)
        self.edit3.move(70, 50)
        self.edit4.move(70, 70)

        self.edit1.hide()
        self.edit2.hide()
        self.edit3.hide()
        self.edit4.hide()

        self.checkbox1.stateChanged.connect(self.run1)
        self.checkbox2.stateChanged.connect(self.run2)
        self.checkbox3.stateChanged.connect(self.run3)
        self.checkbox4.stateChanged.connect(self.run4)

    def run1(self):
        if self.checkbox1.isChecked():
            self.edit1.show()
        else:
            self.edit1.hide()

    def run2(self):
        if self.checkbox2.isChecked():
            self.edit2.show()
        else:
            self.edit2.hide()

    def run3(self):
        if self.checkbox3.isChecked():
            self.edit3.show()
        else:
            self.edit3.hide()

    def run4(self):
        if self.checkbox4.isChecked():
            self.edit4.show()
        else:
            self.edit4.hide()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WidgetsHideNSeek()
    ex.show()
    sys.exit(app.exec())
