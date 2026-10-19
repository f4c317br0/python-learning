import sys
import math
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QApplication, QFileDialog
from eith import Ui_Form


class LSystem(QtWidgets.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.color = QtGui.QColor(0, 0, 0)

        self.parts = 1
        self.rules = {}
        self.cache = []

        self.load_file()
        self.slider.valueChanged.connect(self.update)

    def load_file(self):
        res = QtWidgets.QFileDialog.getOpenFileName(
            self, "Открыть файл L-системы", "", "All files (*)")
        if isinstance(res, (tuple, list)):
            path = res[0]
        else:
            path = res
        if not path:
            self.cache = [""]
            return
        with open(path, encoding="utf-8") as f:
            lines = [s.strip() for s in f.read().splitlines()]
        lines = [s for s in lines if s]

        self.setWindowTitle(lines[0])
        self.parts = int(lines[1])
        for s in lines[3:]:
            p = s.split(None, 1)
            self.rules[p[0]] = p[1].replace(" ", "") if len(p) > 1 else ""
        self.cache = [lines[2]]

    def evolve(self, n):
        while len(self.cache) <= n:
            self.cache.append("".join(self.rules.get(c, c) for c in self.cache[-1]))
        return self.cache[n]

    def paintEvent(self, event):
        if not self.cache or not self.cache[0]:
            return
        prog = self.evolve(self.slider.value())

        painter = QtGui.QPainter(self)
        painter.setPen(QtGui.QPen(self.color))

        turn = 2.0 * math.pi / self.parts
        x, y = 250.0, 400.0
        a = 0.0
        stack = []

        for c in prog:
            if c == "F":
                nx = x + 20.0 * math.cos(a)
                ny = y + 20.0 * math.sin(a)
                painter.drawLine(QtCore.QPointF(x, y), QtCore.QPointF(nx, ny))
                x, y = nx, ny
            elif c == "f":
                x += 20.0 * math.cos(a)
                y += 20.0 * math.sin(a)
            elif c == "+":
                a += turn
            elif c == "-":
                a -= turn
            elif c == "[":
                stack.append((x, y, a))
            elif c == "]":
                if stack:
                    x, y, a = stack.pop()

        painter.end()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LSystem()
    ex.show()
    sys.exit(app.exec())
