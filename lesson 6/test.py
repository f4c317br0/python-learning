from math import cos, pi, sin
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPen
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QRadioButton, QCheckBox, QPlainTextEdit, QLineEdit
import sys



class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.main_label = None
        self.initUI()
        self.label = None

    def initUI(self):
        self.setGeometry(710, 300, 300, 400)
        self.setWindowTitle('Example')
        self.SIDE_LENGTH = 10
        self.SIDES_COUNT = 10

    def draw_star(self, qp):
        nodes = [(self.SIDE_LENGTH * cos(i * 2 * pi / self.SIDES_COUNT),
                  self.SIDE_LENGTH * sin(i * 2 * pi / self.SIDES_COUNT))
                 for i in range(self.SIDES_COUNT)]
        nodes2 = [(int(self.xs(node[0])), int(self.ys(node[1]))) for node in nodes]

        # Пятиугольник
        for i in range(-1, len(nodes2) - 1):
            qp.drawLine(*nodes2[i], *nodes2[i + 1])

        # Звезда (красным цветом)
        pen = QPen(Qt.GlobalColor.red, 2)
        qp.setPen(pen)
        for i in range(-2, len(nodes2) - 2):
            qp.drawLine(*nodes2[i], *nodes2[i + 2])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())
