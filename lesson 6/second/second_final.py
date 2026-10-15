from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QRectF, Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 900)
        self.btn = QtWidgets.QPushButton(parent=Form)
        self.btn.setGeometry(QtCore.QRect(60, 30, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(510, 30, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 101, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(600, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 90, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Показать"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" "
                                      "font-size:14pt;\">side</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" "
                                        "font-size:14pt;\">coeff</span></p></body></html>"))
        self.label_3.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" "
                                        "font-size:14pt;\">n</span></p></body></html>"))


class Square1(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(800, 900)
        self.rects = []
        self.color = QColor(250, 0, 0)
        self.lineEdit.setText("300")
        self.lineEdit_2.setText("0.9")
        self.lineEdit_3.setText("10")
        self.btn.clicked.connect(self.drawing)
        self.lineEdit.textChanged.connect(self.drawing)
        self.lineEdit_2.textChanged.connect(self.drawing)
        self.lineEdit_3.textChanged.connect(self.drawing)

        self.drawing()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.color))
        painter.setBrush(Qt.BrushStyle.NoBrush)

        for x, y, size in self.rects:
            painter.drawRect(QRectF(x, y, size, size))

    def drawing(self):
        try:
            a = float(self.lineEdit.text())
            k = float(self.lineEdit_2.text())
            n = int(float(self.lineEdit_3.text()))
        except ValueError:
            return

        self.rects = []

        x, y = 50.0, 130.0
        center_x = x + a / 2
        center_y = y + a / 2

        for _ in range(n):
            self.rects.append((x, y, a))
            a *= k
            x = center_x - a / 2
            y = center_y - a / 2

        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec())
