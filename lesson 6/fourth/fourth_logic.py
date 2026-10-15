import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import QRectF, Qt
from fourth import Ui_Form


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

        size = self.verticalSlider.value()
        painter.drawEllipse(QRectF(0, 0, 10 * size, 10 * size))
        painter.drawEllipse(QRectF(2 * size, 2 * size, 2 * size, 2 * size))
        painter.drawEllipse(QRectF(6 * size, 2 * size, 2 * size, 2 * size))
        painter.drawArc(QRectF(2 * size, 6 * size, 6 * size, 2 * size), -480, -1920)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = GoodMoodRising()
    ex.show()
    sys.exit(app.exec())
