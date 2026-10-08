import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from seventh import Ui_MainWindow


class AntiPlagiarism(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.checkBtn.clicked.connect(self.run)

    def run(self):
        a = set(self.text1.toPlainText().splitlines() or [''])
        b = set(self.text2.toPlainText().splitlines() or [''])

        result = round(len(a & b) / len(a | b) * 100, 2)

        if result > self.alert_value.value():
            msg = f"Тексты похожи на {result:.2f}%, плагиат"
        else:
            msg = f"Тексты похожи на {result:.2f}%, не плагиат"
        self.statusBar().showMessage(msg)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AntiPlagiarism()
    ex.show()
    sys.exit(app.exec())
