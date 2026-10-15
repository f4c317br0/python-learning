from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.k = QtWidgets.QLineEdit(parent=Form)
        self.k.setGeometry(QtCore.QRect(40, 20, 121, 31))
        self.k.setObjectName("k")
        self.n = QtWidgets.QLineEdit(parent=Form)
        self.n.setGeometry(QtCore.QRect(200, 20, 121, 31))
        self.n.setObjectName("n")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(10, 20, 21, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Form)
        self.label_2.setGeometry(QtCore.QRect(170, 20, 21, 31))
        self.label_2.setObjectName("label_2")
        self.draw = QtWidgets.QPushButton(parent=Form)
        self.draw.setGeometry(QtCore.QRect(330, 20, 161, 31))
        self.draw.setObjectName("draw")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "K ="))
        self.label_2.setText(_translate("Form", "N ="))
        self.draw.setText(_translate("Form", "Рисовать"))
