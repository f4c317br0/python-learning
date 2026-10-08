import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
# from seventh import Ui_MainWindow
from PyQt6 import QtCore, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 131, 21))
        self.label.setObjectName("label")
        self.alert_value = QtWidgets.QDoubleSpinBox(parent=self.centralwidget)
        self.alert_value.setGeometry(QtCore.QRect(150, 10, 641, 22))
        self.alert_value.setObjectName("alert_value")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 50, 47, 13))
        self.label_3.setObjectName("label_3")
        self.text1 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.text1.setGeometry(QtCore.QRect(10, 70, 391, 441))
        self.text1.setObjectName("text1")
        self.text2 = QtWidgets.QPlainTextEdit(parent=self.centralwidget)
        self.text2.setGeometry(QtCore.QRect(410, 70, 381, 441))
        self.text2.setObjectName("text2")
        self.checkBtn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.checkBtn.setGeometry(QtCore.QRect(10, 520, 781, 31))
        self.checkBtn.setObjectName("checkBtn")
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
        self.label.setText(_translate("MainWindow", "Порог срабатывания (%)"))
        self.label_2.setText(_translate("MainWindow", "Текст 1"))
        self.label_3.setText(_translate("MainWindow", "Текст 2"))
        self.checkBtn.setText(_translate("MainWindow", "Сравнить"))


class AntiPlagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBtn.clicked.connect(self.run)

    def run(self):
        a = set(self.text1.toPlainText().splitlines() or [''])
        b = set(self.text2.toPlainText().splitlines() or [''])

        result = round(len(a & b) / len(a | b) * 100, 2)

        if result > self.alert_value.value():
            msg = f"Тексты похожи на {result:.2f}%, плагиат"
        else:
            msg = f"Тексты похожи на {result:.2f}%, не плагиат"
        self.statusBar().showMessage(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
