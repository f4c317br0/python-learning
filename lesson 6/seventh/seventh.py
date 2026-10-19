from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 51, 41))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(120, 10, 51, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(parent=Form)
        self.label_3.setGeometry(QtCore.QRect(240, 10, 51, 41))
        self.label_3.setObjectName("label_3")
        self.k = QtWidgets.QLineEdit(parent=Form)
        self.k.setGeometry(QtCore.QRect(60, 20, 61, 20))
        self.k.setObjectName("k")
        self.n = QtWidgets.QLineEdit(parent=Form)
        self.n.setGeometry(QtCore.QRect(170, 20, 61, 20))
        self.n.setObjectName("n")
        self.m = QtWidgets.QLineEdit(parent=Form)
        self.m.setGeometry(QtCore.QRect(290, 20, 61, 20))
        self.m.setObjectName("m")
        self.draw = QtWidgets.QPushButton(parent=Form)
        self.draw.setGeometry(QtCore.QRect(370, 20, 111, 23))
        self.draw.setObjectName("draw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">K</span></p></body></html>"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">N</span></p></body></html>"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">M</span></p></body></html>"))
        self.draw.setText(_translate("Form", "Рисовать"))
