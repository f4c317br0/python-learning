from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QRectF, Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 580)
        self.slider = QtWidgets.QSlider(parent=Form)
        self.slider.setGeometry(QtCore.QRect(970, 40, 20, 500))
        self.slider.setMaximum(100)
        self.slider.setProperty("value", 50)
        self.slider.setOrientation(QtCore.Qt.Orientation.Vertical)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


class GoodMoodRising(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.setFixedSize(1000, 1000)

        self.color = QColor(250, 0, 0)

        self.slider.valueChanged.connect(self.update)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.color))
        painter.setBrush(Qt.BrushStyle.NoBrush)

        size = self.slider.value()
        painter.drawEllipse(QRectF(0, 0, 10 * size, 10 * size))
        painter.drawEllipse(QRectF(2 * size, 2 * size, 2 * size, 2 * size))
        painter.drawEllipse(QRectF(6 * size, 2 * size, 2 * size, 2 * size))
        painter.drawArc(QRectF(2 * size, 6 * size, 6 * size, 2 * size), -480, -1920)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())
