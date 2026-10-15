from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QPolygonF
from PyQt6.QtCore import Qt, QPointF


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.k = QtWidgets.QLineEdit(parent=Form)
        self.k.setGeometry(QtCore.QRect(40, 20, 121, 31))
        self.k.setObjectName("k")
        self.n = QtWidgets.QLineEdit(parent=Form)
        self.n.setGeometry(QtCore.QRect(200, 20, 121, 31))
        self.n.setObjectName("n")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 21, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 21, 31))
        self.label_2.setObjectName("label_2")
        self.draw = QtWidgets.QPushButton(parent=Form)
        self.draw.setGeometry(QtCore.QRect(330, 20, 161, 31))
        self.draw.setObjectName("draw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "K ="))
        self.label_2.setText(_translate("Form", "N ="))
        self.draw.setText(_translate("Form", "Рисовать"))


class Square2(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(500, 500)
        self.color = QColor(250, 0, 0)
        self.squares = [self.make_polygon(150.0, 150.0, 200.0)]

        self.draw.clicked.connect(self.drawing)
        self.k.textChanged.connect(self.drawing)
        self.n.textChanged.connect(self.drawing)

    @staticmethod
    def make_polygon(x, y, side):
        poly = QPolygonF()
        poly.append(QPointF(x, y))
        poly.append(QPointF(x + side, y))
        poly.append(QPointF(x + side, y + side))
        poly.append(QPointF(x, y + side))
        return poly

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(self.color))
        painter.setBrush(Qt.BrushStyle.NoBrush)

        for poly in self.squares:
            painter.drawPolygon(poly)

    def drawing(self):
        try:
            k = float(self.k.text())
            n = int(self.n.text())

            if not 0 < k < 1 or n < 1:
                return
        except ValueError:
            return

        v = [
            QPointF(150.0, 150.0),
            QPointF(350.0, 150.0),
            QPointF(350.0, 350.0),
            QPointF(150.0, 350.0)
        ]

        squares = []

        for _ in range(n):
            poly = QPolygonF()
            for p in v:
                poly.append(QPointF(p))
            squares.append(poly)

            new_v = []
            for i in range(4):
                p = v[i]
                next_p = v[(i + 1) % 4]

                new_v.append(QPointF(
                    p.x() + (next_p.x() - p.x()) * (1 - k),
                    p.y() + (next_p.y() - p.y()) * (1 - k)
                ))

            v = new_v

        self.squares = squares
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec())
