import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import QtCore, QtWidgets


class Ui_MyNotes(object):
    def setupUi(self, MyNotes):
        MyNotes.setObjectName("MyNotes")
        MyNotes.resize(298, 288)
        self.contactName = QtWidgets.QLineEdit(parent=MyNotes)
        self.contactName.setGeometry(QtCore.QRect(70, 20, 113, 20))
        self.contactName.setObjectName("contactName")
        self.contactNumber = QtWidgets.QLineEdit(parent=MyNotes)
        self.contactNumber.setGeometry(QtCore.QRect(70, 50, 113, 20))
        self.contactNumber.setObjectName("contactNumber")
        self.label = QtWidgets.QLabel(parent=MyNotes)
        self.label.setGeometry(QtCore.QRect(30, 20, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=MyNotes)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 47, 13))
        self.label_2.setObjectName("label_2")
        self.addContactBtn = QtWidgets.QPushButton(parent=MyNotes)
        self.addContactBtn.setGeometry(QtCore.QRect(200, 30, 75, 23))
        self.addContactBtn.setObjectName("addContactBtn")
        self.contactList = QtWidgets.QListWidget(parent=MyNotes)
        self.contactList.setGeometry(QtCore.QRect(10, 80, 281, 201))
        self.contactList.setObjectName("contactList")

        self.retranslateUi(MyNotes)
        QtCore.QMetaObject.connectSlotsByName(MyNotes)

    def retranslateUi(self, MyNotes):
        _translate = QtCore.QCoreApplication.translate
        MyNotes.setWindowTitle(_translate("MyNotes", "Form"))
        self.label.setText(_translate("MyNotes", "<html><head/><body><p>Имя</p></body></html>"))
        self.label_2.setText(_translate("MyNotes", "Телефон"))
        self.addContactBtn.setText(_translate("MyNotes", "Добавить"))


class MyNotes(QMainWindow, Ui_MyNotes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addContactBtn.clicked.connect(self.run)

    def run(self):
        name = self.contactName.text()
        number = self.contactNumber.text()
        self.contactList.addItem(name + ' ' + number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
