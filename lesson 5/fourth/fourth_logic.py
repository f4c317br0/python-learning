import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from fourth import Ui_MyNotes


class MyNotes(QMainWindow, Ui_MyNotes):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addContactBtn.clicked.connect(self.run)

    def run(self):
        name = self.contactName.text()
        number = self.contactNumber.text()
        self.contactList.addItem(name + ' ' + number)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyNotes()
    ex.show()
    sys.exit(app.exec())
