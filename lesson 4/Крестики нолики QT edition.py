import sys
from PyQt6.QtWidgets import QApplication, QWidget, QRadioButton, QLabel, QPushButton


class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.o_radio = None
        self.x_radio = None
        self.new_game_button = None
        self.result = None
        self.button_grid = []
        self.current_player = 'X'
        self.game_over = False
        self.initUI()

    def initUI(self):
        x = 450
        self.setGeometry(500, 500, x, x)
        self.setWindowTitle('Крестики-нолики')

        self.x_radio = QRadioButton('X', self)
        self.x_radio.move(185, 40)
        self.x_radio.resize(self.x_radio.sizeHint())
        self.x_radio.setChecked(True)

        self.o_radio = QRadioButton('O', self)
        self.o_radio.move(235, 40)
        self.o_radio.resize(self.o_radio.sizeHint())

        self.x_radio.toggled.connect(self.new_game)

        self.result = QLabel('', self)
        self.result.move(200, 70)
        self.result.resize(150, 20)

        for row in range(3):
            row_buttons = []
            for col in range(3):
                btn = QPushButton(self)
                btn.move(150 + col * 50, 100 + row * 50)
                btn.resize(50, 50)
                btn.clicked.connect(lambda checked, r=row, c=col: self.make_move(r, c))
                row_buttons.append(btn)
            self.button_grid.append(row_buttons)

        self.new_game_button = QPushButton('Новая игра', self)
        self.new_game_button.move(150, 260)
        self.new_game_button.resize(150, 30)
        self.new_game_button.clicked.connect(self.new_game)

        self.new_game()

    def make_move(self, row, col):
        if self.game_over:
            return
        btn = self.button_grid[row][col]
        if btn.text() != '':
            return

        btn.setText(self.current_player)

        winner = self.check_winner()
        if winner:
            self.result.setText(f'Выиграл {winner}!')
            self.game_over = True
            self.set_board_enabled(False)
            return

        if self.check_draw():
            self.result.setText('Ничья!')
            self.game_over = True
            return

        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
        grid = self.button_grid
        lines = []

        for i in range(3):
            lines.append([grid[i][0], grid[i][1], grid[i][2]])
            lines.append([grid[0][i], grid[1][i], grid[2][i]])

        lines.append([grid[0][0], grid[1][1], grid[2][2]])
        lines.append([grid[0][2], grid[1][1], grid[2][0]])

        for line in lines:
            texts = [btn.text() for btn in line]
            if texts[0] != '' and texts[0] == texts[1] == texts[2]:
                return texts[0]
        return None

    def check_draw(self):
        return all(
            self.button_grid[row][col].text() != ''
            for row in range(3) for col in range(3)
        )

    def set_board_enabled(self, enabled):
        for row in self.button_grid:
            for btn in row:
                btn.setEnabled(enabled)

    def new_game(self):
        self.game_over = False
        self.result.setText('')
        self.current_player = 'X' if self.x_radio.isChecked() else 'O'
        self.set_board_enabled(True)
        for row in self.button_grid:
            for btn in row:
                btn.setText('')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TicTacToe()
    ex.show()
    sys.exit(app.exec())
