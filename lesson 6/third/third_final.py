from PyQt6 import QtCore, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPixmap, QImage


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
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><br/></p></body></html>"))


class AlphaManagement(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.orig = QPixmap('orig.jpg')
        self.pixmap = QPixmap(self.orig)
        self.label.setPixmap(self.pixmap)

        self.alpha.setRange(0, 255)
        self.alpha.valueChanged.connect(self.change_opacity)
        self.alpha.setValue(255)

    def change_opacity(self, value):
        img = self.orig.toImage().convertToFormat(QImage.Format.Format_ARGB32)
        for y in range(img.height()):
            for x in range(img.width()):
                c = img.pixelColor(x, y)
                c.setAlpha(value)
                img.setPixelColor(x, y, c)

        img.save('new.png')
        self.pixmap = QPixmap.fromImage(img)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AlphaManagement()
    ex.show()
    sys.exit(app.exec())
