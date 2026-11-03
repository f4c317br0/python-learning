import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QApplication, QLabel


class KeyboardTrainer(QWidget):
    """Показывает, какую клавишу вы нажали.
    Полезно для понимания кодов клавиш.
    И для того, чтобы убедиться, что клавиатура работает."""

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 300, 400, 200)
        self.setWindowTitle('Клавиатурный шпион 🕵️')

        self.key_label = QLabel('Нажми любую клавишу!', self)
        self.key_label.move(30, 30)
        self.key_label.resize(340, 40)
        self.key_label.setStyleSheet('font-size: 18px;')

        self.code_label = QLabel('Код: ???', self)
        self.code_label.move(30, 80)
        self.code_label.resize(340, 40)

        self.count_label = QLabel('Нажатий: 0', self)
        self.count_label.move(30, 120)
        self.count_label.resize(340, 40)

        self.press_count = 0

    def keyPressEvent(self, event):
        self.press_count += 1

        # Получаем текстовое представление клавиши
        key_text = event.text() if event.text().strip() else "спецклавиша"
        self.key_label.setText(f'Клавиша: "{key_text}"')
        self.code_label.setText(f'Код: {event.key()}')
        self.count_label.setText(f'Нажатий: {self.press_count}')

        # Реагируем на конкретные клавиши
        if event.key() == Qt.Key.Key_Escape:
            self.close()  # Esc — закрыть окно
        elif event.key() == Qt.Key.Key_Space:
            self.press_count = 0  # Пробел — сбросить счётчик
            self.count_label.setText('Нажатий: 0 (сброс!)')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = KeyboardTrainer()
    ex.show()
    sys.exit(app.exec())