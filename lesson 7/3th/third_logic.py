import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from third import Ui_Form


class HeadersInColor(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.text = []
        self.comboBox.addItems(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6'])
        self.comboBox.setCurrentText('p')
        self.lineEdit_2.setText('#000')
        self.pushButton.clicked.connect(self.write_text)
        self.pushButton_2.clicked.connect(self.clear_text)

    def write_text(self):
        ch = self.comboBox.currentText()
        color = self.lineEdit_2.text()
        line = self.lineEdit.text()
        self.text.append(line)
        html = f'''
        <{ch} style="color: {color};">{line}</{ch}><br>
        '''
        self.textBrowser.insertHtml(html)

    def clear_text(self):
        self.textBrowser.setText('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = HeadersInColor()
    ex.show()
    sys.exit(app.exec())
