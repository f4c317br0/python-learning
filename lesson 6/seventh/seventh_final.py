import sys
import math
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QColorDialog


class NoTSquare(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color = None
        self.start_point = [350.0, 250.0]

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(500, 500)

        self.label = QtWidgets.QLabel("K =", parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.label_2 = QtWidgets.QLabel("N =", parent=Form)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 51, 41))
        self.label_3 = QtWidgets.QLabel("M =", parent=Form)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 51, 41))

        self.k = QtWidgets.QLineEdit(parent=Form)
        self.k.setGeometry(QtCore.QRect(60, 20, 61, 20))
        self.k.setObjectName("k")
        self.n = QtWidgets.QLineEdit(parent=Form)
        self.n.setGeometry(QtCore.QRect(170, 20, 61, 20))
        self.n.setObjectName("n")
        self.m = QtWidgets.QLineEdit(parent=Form)
        self.m.setGeometry(QtCore.QRect(290, 20, 61, 20))
        self.m.setObjectName("m")

        self.draw = QtWidgets.QPushButton("Рисовать", parent=Form)
        self.draw.setGeometry(QtCore.QRect(370, 20, 111, 23))
        self.draw.setObjectName("draw")
        self.draw.clicked.connect(self.draw_clicked)

    def paintEvent(self, event):
        if self.color is None:
            return
        try:
            k = float(self.k.text())
            n = int(self.n.text())
            m = int(self.m.text())
        except ValueError:
            return
        if n < 3 or m <= 0:
            return

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self.color))

        cx, cy, radius = 250.0, 250.0, 100.0
        points = [
            (cx + radius * math.cos(2.0 * math.pi * i / n),
             cy + radius * math.sin(2.0 * math.pi * i / n))
            for i in range(n)
        ]

        for _ in range(m):
            polygon = QtGui.QPolygonF()
            for x, y in points:
                polygon.append(QtCore.QPointF(x, y))
            painter.drawPolygon(polygon)

            new_points = []
            for i in range(n):
                x1, y1 = points[i]
                x2, y2 = points[(i + 1) % n]
                new_points.append((x1 + k * (x2 - x1), y1 + k * (y2 - y1)))
            points = new_points

        painter.end()

    def draw_clicked(self):
        color_dialog = QColorDialog()
        color = color_dialog.getColor()
        if color.isValid():
            self.color = color
            self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = NoTSquare()
    window.show()
    sys.exit(app.exec())
