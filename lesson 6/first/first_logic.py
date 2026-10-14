import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt6.QtGui import QImage, QPixmap, QTransform
from PyQt6.QtCore import Qt
from first import Ui_Form


class MyPillow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.curr_image = QImage()
        self.source_image = QImage()
        self.current_ch = None

        self.rbtn.clicked.connect(lambda: self.logic("R"))
        self.gbtn.clicked.connect(lambda: self.logic("G"))
        self.bbtn.clicked.connect(lambda: self.logic("B"))
        self.allbtn.clicked.connect(self.returned)

        self.againbtn.clicked.connect(lambda: self.rotated("Left"))
        self.forbtn.clicked.connect(lambda: self.rotated("Right"))

        self.open_image()

    def open_image(self):
        result = QFileDialog.getOpenFileName(
            self,
            "Выбрать изображение",
            "",
            "Изображения (*.png *.jpg *.jpeg *.bmp)"
        )

        if isinstance(result, (tuple, list)):
            file_name = result[0] if result else ""
        else:
            file_name = result

        if not file_name:
            return

        self.source_image = QImage(str(file_name))

        if self.source_image.isNull():
            raise ValueError("Не удалось загрузить изображение")

        self.curr_image = self.source_image.copy()
        self.show_image()

    def show_image(self):
        self.label.setPixmap(QPixmap.fromImage(self.curr_image))

    def inverting(self, image, ch):
        result = image.convertToFormat(
            QImage.Format.Format_ARGB32
        ).copy()

        for y in range(result.height()):
            for x in range(result.width()):
                color = result.pixelColor(x, y)

                if ch == "R":
                    color.setGreen(0)
                    color.setBlue(0)
                elif ch == "G":
                    color.setRed(0)
                    color.setBlue(0)
                elif ch == "B":
                    color.setRed(0)
                    color.setGreen(0)

                result.setPixelColor(x, y, color)

        return result

    def logic(self, ch):
        self.current_ch = ch
        self.curr_image = self.inverting(self.source_image, ch)
        self.show_image()

    def returned(self):
        self.current_ch = None
        self.curr_image = self.source_image.copy()
        self.show_image()

    def rotated(self, direction):
        transform = QTransform()
        transform.rotate(-90 if direction == "Left" else 90)

        self.source_image = self.source_image.transformed(
            transform,
            Qt.TransformationMode.SmoothTransformation
        )

        if self.current_ch is not None:
            self.curr_image = self.inverting(
                self.source_image, self.current_ch
            )
        else:
            self.curr_image = self.source_image.copy()

        self.show_image()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec())
