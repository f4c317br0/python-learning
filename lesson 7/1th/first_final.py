from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 41))
        self.label.setObjectName("label")
        self.filenameEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.filenameEdit.setGeometry(QtCore.QRect(140, 20, 401, 41))
        self.filenameEdit.setObjectName("filenameEdit")
        self.button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.button.setGeometry(QtCore.QRect(550, 20, 231, 41))
        self.button.setObjectName("button")
        self.textBrowser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 70, 781, 471))
        self.textBrowser.setObjectName("textBrowser")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; "
                                      "font-weight:600;\">Имя файла</span></p></body></html>"))
        self.button.setText(_translate("MainWindow", "Рассчитать"))


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
