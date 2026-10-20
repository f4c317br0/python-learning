from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(641, 519)
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 621, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox = QtWidgets.QComboBox(parent=Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 60, 161, 41))
        self.comboBox.setObjectName("comboBox")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(180, 60, 151, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 60, 141, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Form)
        self.pushButton_2.setGeometry(QtCore.QRect(490, 60, 141, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textBrowser = QtWidgets.QTextBrowser(parent=Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 110, 621, 401))
        self.textBrowser.setObjectName("textBrowser")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Вывести"))
        self.pushButton_2.setText(_translate("Form", "Очистить"))


class HeadersInColor(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = []
        self.comboBox.addItems(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        self.comboBox.setCurrentText('p')
        self.lineEdit_2.setText('#000')
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)

    def write_text(self):
        ch = self.comboBox.currentText()
        color = self.lineEdit_2.text()
        line = self.lineEdit.text()
        self.text.append(line)
        html = f'''
        <{ch} style="color: {color};">{line}</{ch}><br>
        '''
        self.textBrowser.insertHtml(html)

    def clear_text(self):
        self.textBrowser.setText('')
        self.text = []


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = HeadersInColor()
    ex.show()
    sys.exit(app.exec())
