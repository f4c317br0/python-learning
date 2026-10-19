import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from first import Ui_MainWindow


class FileStat(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.button.clicked.connect(self.min_med_max)

    def min_med_max(self):
        line = self.filenameEdit.text()
        try:
            with open(line, 'r', encoding='utf-8') as f:
                x = [int(num) for row in f for num in row.split()]
            if any('.' in str(el) for el in x):
                self.statusbar.showMessage('Указанный файл не существует')
                self.textBrowser.setText('')
                return
        except FileNotFoundError:
            self.statusbar.showMessage('Указанный файл не существует')
            self.textBrowser.setText('')
            return
        except ValueError:
            self.statusbar.showMessage('Файл содержит некорректные данные')
            self.textBrowser.setText('')
            return

        if x:
            maxx = f'Максимальное значение = {max(x)}'
            minn = f'Минимальное значение = {min(x)}'
            sr = sum(x) / len(x)
            sred = f'Среднее значение = {sr:.2f}'
            self.textBrowser.setText(maxx + '\n' + minn + '\n' + sred)
            self.statusbar.clearMessage()
            with open('out.txt', 'w', encoding='utf-8') as f:
                f.write(maxx + '\n' + minn + '\n' + sred)
        else:
            self.statusbar.showMessage('Указанный файл пуст')
            self.textBrowser.setText('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = FileStat()
    ex.show()
    sys.exit(app.exec())