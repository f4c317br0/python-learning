import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(522, 449)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.label.setObjectName("label")
        self.stones = QtWidgets.QSpinBox(parent=Form)
        self.stones.setGeometry(QtCore.QRect(160, 20, 141, 21))
        self.stones.setObjectName("stones")
        self.startButton = QtWidgets.QPushButton(parent=Form)
        self.startButton.setGeometry(QtCore.QRect(320, 20, 191, 23))
        self.startButton.setObjectName("startButton")
        self.remainLcd = QtWidgets.QLCDNumber(parent=Form)
        self.remainLcd.setGeometry(QtCore.QRect(10, 50, 501, 23))
        self.remainLcd.setObjectName("remainLcd")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 121, 16))
        self.label_2.setObjectName("label_2")
        self.takeInput = QtWidgets.QLineEdit(parent=Form)
        self.takeInput.setGeometry(QtCore.QRect(140, 80, 371, 20))
        self.takeInput.setObjectName("takeInput")
        self.takeButton = QtWidgets.QPushButton(parent=Form)
        self.takeButton.setGeometry(QtCore.QRect(10, 110, 501, 23))
        self.takeButton.setObjectName("takeButton")
        self.listWidget = QtWidgets.QListWidget(parent=Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 140, 501, 261))
        self.listWidget.setObjectName("listWidget")
        self.resultLabel = QtWidgets.QLabel(parent=Form)
        self.resultLabel.setGeometry(QtCore.QRect(70, 410, 331, 31))
        self.resultLabel.setObjectName("resultLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Задать количество камней"))
        self.startButton.setText(_translate("Form", "Задать"))
        self.label_2.setText(_translate("Form", "Сколько камней взять?"))
        self.takeButton.setText(_translate("Form", "Взять"))
        self.resultLabel.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


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
