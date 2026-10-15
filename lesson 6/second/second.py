from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 900)
        self.btn = QtWidgets.QPushButton(parent=Form)
        self.btn.setGeometry(QtCore.QRect(60, 30, 161, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.btn.setFont(font)
        self.btn.setObjectName("btn")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(510, 30, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(510, 60, 101, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 101, 21))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(600, 30, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(600, 60, 113, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(600, 90, 113, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn.setText(_translate("Form", "Показать"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">side</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">coeff</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">n</span></p></body></html>"))


