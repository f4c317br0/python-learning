from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.text_browser = QtWidgets.QTextBrowser(parent=self.centralwidget)
        self.text_browser.setGeometry(QtCore.QRect(10, 30, 781, 521))
        self.text_browser.setObjectName("text_browser")
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


class Distributor(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.source_text = None
        menubar = self.menuBar()
        filemenu = menubar.addMenu('Файл')
        openact = filemenu.addAction('Открыть')
        saveact = filemenu.addAction('Сохранить')
        raspr = menubar.addMenu('Распределить')
        txtact = raspr.addAction('TXT')
        csvact = raspr.addAction('CSV')
        pngact = raspr.addAction('PNG')
        pyact = raspr.addAction('PY')
        otheract = raspr.addAction('Другие')

        openact.triggered.connect(self.load_file)
        saveact.triggered.connect(self.save_file)
        txtact.triggered.connect(lambda checked: self.spread('txt'))
        csvact.triggered.connect(lambda checked: self.spread('csv'))
        pngact.triggered.connect(lambda checked: self.spread('png'))
        pyact.triggered.connect(lambda checked: self.spread('py'))
        otheract.triggered.connect(lambda checked: self.spread(''))

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
            selected = [n for n in names if self.ext(n.lower()) == q]
        else:
            selected = [n for n in names if self.ext(n.lower()) not in ['txt', 'csv', 'png', 'py']]
        self.text_browser.setPlainText('\n'.join(sorted(selected)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Distributor()
    ex.show()
    sys.exit(app.exec())
