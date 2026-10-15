import random
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QInputDialog
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRectF
from fifth import Ui_Form


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        self.button = QtWidgets.QPushButton(parent=Form)
        self.button.setGeometry(QtCore.QRect(30, 30, 241, 51))
        self.button.setObjectName("button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button.setText(_translate("Form", "Введите количество цветов флага"))


class RandomFlag(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(300, 400)
        self.base = [50, 90, 200, 30]
        self.n = 0
        self.button.clicked.connect(self.run)

    def run(self):
        n, ok = QInputDialog.getInt(self, 'Количество цветов', 'Введите количество цветов флага', 3, 1, 10, 1)
        if ok:
            self.n = n
            self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QColor(0, 0, 0))
        if not self.n:
            return
        x, y, w, h = self.base
        for i in range(self.n):
            painter.setBrush(QColor(random.randrange(256), random.randrange(256), random.randrange(256)))
            painter.drawRect(QRectF(x, y + i * h, w, h))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = RandomFlag()
    ex.show()
    sys.exit(app.exec())
