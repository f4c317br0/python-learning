import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QTransform, QColor
from PyQt6.QtCore import Qt


class Ui_Form(object):
    def setupUi(self, Form):
        Form.resize(454, 384)

        self.rbtn = QtWidgets.QPushButton(parent=Form)
        self.rbtn.setGeometry(10, 20, 131, 41)
        self.rbtn.setText("R")

        self.gbtn = QtWidgets.QPushButton(parent=Form)
        self.gbtn.setGeometry(10, 80, 131, 41)
        self.gbtn.setText("G")

        self.bbtn = QtWidgets.QPushButton(parent=Form)
        self.bbtn.setGeometry(10, 140, 131, 41)
        self.bbtn.setText("B")

        self.allbtn = QtWidgets.QPushButton(parent=Form)
        self.allbtn.setGeometry(10, 200, 131, 41)
        self.allbtn.setText("ALL")

        self.channelButtons = QtWidgets.QButtonGroup(Form)
        self.channelButtons.setObjectName("channelButtons")
        for button in (self.rbtn, self.gbtn, self.bbtn, self.allbtn):
            self.channelButtons.addButton(button)

        self.againbtn = QtWidgets.QPushButton(parent=Form)
        self.againbtn.setGeometry(10, 260, 201, 111)
        self.againbtn.setText("Против часовой стрелки")

        self.forbtn = QtWidgets.QPushButton(parent=Form)
        self.forbtn.setGeometry(240, 260, 201, 111)
        self.forbtn.setText("По часовой стрелке")

        self.rotateButtons = QtWidgets.QButtonGroup(Form)
        self.rotateButtons.setObjectName("rotateButtons")
        self.rotateButtons.addButton(self.againbtn)
        self.rotateButtons.addButton(self.forbtn)

        self.label = QtWidgets.QLabel(parent=Form)
        self.label.setGeometry(160, 20, 281, 221)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)


class MyPillow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.curr_image = QImage()
        self.source_image = QImage()
        self.current_ch = "ALL"

        self.rbtn.clicked.connect(lambda: self.logic("R"))
        self.gbtn.clicked.connect(lambda: self.logic("G"))
        self.bbtn.clicked.connect(lambda: self.logic("B"))
        self.allbtn.clicked.connect(lambda: self.logic("ALL"))

        self.againbtn.clicked.connect(lambda: self.rotated(-90))
        self.forbtn.clicked.connect(lambda: self.rotated(90))

        self.open_image()

    def open_image(self):
        result = QFileDialog.getOpenFileName(
            self, "Выбрать изображение", "",
            "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )
        file_name = result[0] if isinstance(result, (tuple, list)) else result

        if not file_name:
            return

        self.source_image = QImage(file_name)
        if self.source_image.isNull():
            return

        self.curr_image = self.source_image.copy()
        self.show_image()

    def show_image(self):
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def logic(self, ch):
        self.current_ch = ch

        if ch == "ALL":
            self.curr_image = self.source_image.copy()
        else:
            image = self.source_image.convertToFormat(
                QImage.Format.Format_RGB32
            )
            result = QImage(
                image.size(), QImage.Format.Format_RGB32
            )

            for y in range(image.height()):
                for x in range(image.width()):
                    color = image.pixelColor(x, y)

                    if ch == "R":
                        result.setPixelColor(
                            x, y, QColor(color.red(), 0, 0)
                        )
                    elif ch == "G":
                        result.setPixelColor(
                            x, y, QColor(0, color.green(), 0)
                        )
                    else:
                        result.setPixelColor(
                            x, y, QColor(0, 0, color.blue())
                        )

            self.curr_image = result

        self.show_image()

    def rotated(self, angle):
        transform = QTransform().rotate(angle)
        self.source_image = self.source_image.transformed(
            transform, Qt.TransformationMode.FastTransformation
        )
        self.logic(self.current_ch)


if __name__ == "__main__":
    from PyQt6 import QtGui

    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
