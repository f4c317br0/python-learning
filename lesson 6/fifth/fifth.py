from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 400)
        self.button = QtWidgets.QPushButton(parent=Form)
        self.button.setGeometry(QtCore.QRect(30, 30, 241, 51))
        self.button.setObjectName("button")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.button.setText(_translate("Form", "Введите количество цветов флага"))
