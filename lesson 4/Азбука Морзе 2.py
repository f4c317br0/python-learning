import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton


class MorseCode(QWidget):
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..'
    }

    def __init__(self):
        super().__init__()
        self.result = None
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.alphabet_buttons = dict()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 410, 120)
        self.setWindowTitle('Азбука Морзе 2')

        for i, letter in enumerate(self.alphabet):
            row, col = divmod(i, 13)
            btn = QPushButton(letter, self)
            btn.move(10 + col * 30, 10 + row * 30)
            btn.resize(30, 30)
            btn.clicked.connect(lambda checked, letter=letter: self.translate(letter))

            self.alphabet_buttons[letter] = btn

        self.result = QLineEdit(self)
        self.result.move(10, 70)
        self.result.resize(390, 30)

    def translate(self, letter):
        code = MorseCode.MORSE_CODE[letter.upper()]
        self.result.setText(self.result.text() + code)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MorseCode()
    ex.show()
    sys.exit(app.exec())
