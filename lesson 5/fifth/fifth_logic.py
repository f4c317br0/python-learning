import sys
from PyQt6.QtWidgets import QApplication, QWidget, QGridLayout, QPushButton
from fifth import Ui_Form


class WidgetArt(QWidget, Ui_Form):
    def __init__(self, matrix):
        super().__init__()
        self.setupUi(self)
        self.matrix = matrix
        self.widgetArt = QGridLayout()
        self.setLayout(self.widgetArt)
        self.run()

    def run(self):
        for i, row in enumerate(self.matrix):
            for j, value in enumerate(row):
                button = QPushButton('*' if value == 1 else '')
                self.widgetArt.addWidget(button, i, j)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    matrix = [
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    ]
    ex = WidgetArt(matrix)
    ex.show()
    sys.exit(app.exec())
