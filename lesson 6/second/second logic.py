import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen, QBrush
from second import Ui_Form
from PyQt6.QtCore import QRectF, Qt


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
