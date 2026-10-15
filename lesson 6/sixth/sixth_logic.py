from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QPolygonF
from PyQt6.QtCore import Qt, QPointF
from sixth import Ui_Form


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
            n = int(float(self.n.text()))
        except ValueError:
            return
        v = [QPointF(150.0, 150.0), QPointF(350.0, 150.0),
             QPointF(350.0, 350.0), QPointF(150.0, 350.0)]

        squares = []
        for _ in range(max(n, 1)):
            poly = QPolygonF()
            for p in v:
                poly.append(QPointF(p))
            squares.append(poly)
            v = [QPointF(v[i].x() + (v[(i + 1) % 4].x() - v[i].x()) * k,
                         v[i].y() + (v[(i + 1) % 4].y() - v[i].y()) * k)
                 for i in range(4)]

        self.squares = squares
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square2()
    ex.show()
    sys.exit(app.exec())
