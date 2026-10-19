import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from second import Ui_MainWindow


class Distributor(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.source_text = None

    def load_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Открыть текст", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            with open(file_name, 'r', encoding='utf-8') as file:
                self.source_text = file.read()
            self.text_browser.setPlainText(self.source_text)

    def save_file(self):
        file_name, _ = QFileDialog.getSaveFileName(self, "Сохранить текст", "", "Text Files (*.txt);;All Files (*)")
        if file_name:
            text = self.text_browser.toPlainText()
            with open(file_name, 'w', encoding='utf-8') as file:
                file.write(text)

    @staticmethod
    def ext(name):
        return name.rsplit('.', 1)[1] if '.' in name else ''

    def spread(self, q):
        if self.source_text is None:
            return
        names = [line.strip() for line in self.source_text.splitlines() if line.strip()]
        if q:
            selected = [n for n in names if self.ext(n) == q]
        else:
            selected = [n for n in names if self.ext(n) not in ['txt', 'csv', 'png', 'py']]
        self.text_browser.setPlainText('\n'.join(sorted(selected)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Distributor()
    ex.show()
    sys.exit(app.exec())
