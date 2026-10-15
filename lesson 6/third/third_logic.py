import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QImage
from third import Ui_Form


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
