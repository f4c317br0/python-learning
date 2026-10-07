import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
# from ui_01 import Ui_Form ----------- ui_01 -> filename

class MyWidget(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.label.setText("OK")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())