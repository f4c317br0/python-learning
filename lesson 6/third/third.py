from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(493, 374)
        self.alpha = QtWidgets.QSlider(parent=Form)
        self.alpha.setGeometry(QtCore.QRect(10, 30, 31, 291))
        self.alpha.setMinimum(0)
        self.alpha.setMaximum(99)
        self.alpha.setSliderPosition(99)
        self.alpha.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.alpha.setObjectName("alpha")
        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(QtCore.QRect(80, 30, 381, 311))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
