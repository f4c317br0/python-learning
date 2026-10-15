from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 580)
        self.slider = QtWidgets.QSlider(parent=Form)
        self.slider.setGeometry(QtCore.QRect(970, 40, 20, 500))
        self.slider.setMaximum(100)
        self.slider.setProperty("value", 50)
        self.slider.setOrientation(QtCore.Qt.Orientation.Vertical)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
