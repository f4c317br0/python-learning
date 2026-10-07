import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from second import Ui_Form


class SimplePlanner(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.addEventBtn.clicked.connect(self.run)

    def run(self):
        timeoclock = self.timeEdit.time().toString("HH:mm:ss")
        data = self.calendarWidget.selectedDate().toString("yyyy-MM-dd")
        todo = self.lineEdit.text()
        try:
            self.eventList.addItem(data + ' ' + timeoclock + ' - ' + todo)
            self.eventList.sortItems()
        except Exception as er:
            print(er)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimplePlanner()
    ex.show()
    sys.exit(app.exec())
