import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from sixth import Ui_Form


class Pseudonym(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.startButton.clicked.connect(self.run)
        self.takeButton.clicked.connect(self.run2)
        self.count = 0
        self.playing = False

    def run(self):
        self.count = self.stones.value()
        self.remainLcd.display(self.count)
        self.listWidget.clear()
        self.resultLabel.setText('')
        self.playing = self.count > 0

    def run2(self):
        if not self.playing:
            return
        try:
            take = int(self.takeInput.text())
        except ValueError:
            return
        if not 1 <= take <= min(3, self.count):
            return

        self.count -= take
        self.listWidget.addItem(f'Игрок взял - {take}')
        self.remainLcd.display(self.count)
        if self.count == 0:
            self.resultLabel.setText('Победа пользователя!')
            self.playing = False
            return

        limit = min(3, self.count)
        move = self.count % 4 or random.randint(1, limit)
        move = min(move, limit)
        self.count -= move
        self.listWidget.addItem(f'Компьютер взял - {move}')
        self.remainLcd.display(self.count)
        if self.count == 0:
            self.resultLabel.setText('Победа компьютера!')
            self.playing = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Pseudonym()
    ex.show()
    sys.exit(app.exec())
