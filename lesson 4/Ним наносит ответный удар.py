import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout


class NimStrikesBack(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nim Strikes Back")

        self.X = 0
        self.Y = 0
        self.Z = 0
        self.moves = 10

        self.x_label = QLabel()
        self.moves_label = QLabel()
        self.result_label = QLabel("")

        self.btnp = QPushButton()
        self.btnm = QPushButton()
        self.btnp.clicked.connect(self.increase)
        self.btnm.clicked.connect(self.decrease)

        buttons = QHBoxLayout()
        buttons.addWidget(self.btnm)
        buttons.addWidget(self.btnp)

        layout = QVBoxLayout()
        layout.addWidget(self.x_label)
        layout.addWidget(self.moves_label)
        layout.addLayout(buttons)
        layout.addWidget(self.result_label)
        self.setLayout(layout)

        self.new_game()

    def new_game(self):
        self.X = random.randint(1, 100)
        self.Y = random.randint(1, 20)
        self.Z = random.randint(1, 20)
        self.moves = 10
        self.btnp.setText(f"+{self.Y}")
        self.btnm.setText(f"-{self.Z}")
        self.btnp.setEnabled(True)
        self.btnm.setEnabled(True)
        self.update_labels()

    def update_labels(self):
        self.x_label.setText(f"X = {self.X}")
        self.moves_label.setText(f"Осталось ходов: {self.moves}")

    def increase(self):
        self.X += self.Y
        self.after_move()

    def decrease(self):
        self.X -= self.Z
        self.after_move()

    def after_move(self):
        self.moves -= 1
        self.update_labels()
        self.result_label.setText("")

        if self.X == 0:
            self.result_label.setText("Поздравляем! Вы выиграли!")
            self.btnp.setEnabled(False)
            self.btnm.setEnabled(False)
        elif self.moves == 0:
            self.new_game()
            self.result_label.setText("Вы проиграли. Игра началась заново!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NimStrikesBack()
    window.show()
    sys.exit(app.exec())
