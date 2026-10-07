import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
# from second import Ui_Form
from PyQt6 import QtCore, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(615, 454)
        self.timeEdit = QtWidgets.QTimeEdit(parent=Form)
        self.timeEdit.setGeometry(QtCore.QRect(0, 0, 311, 41))
        self.timeEdit.setObjectName("timeEdit")
        self.calendarWidget = QtWidgets.QCalendarWidget(parent=Form)
        self.calendarWidget.setGeometry(QtCore.QRect(0, 40, 311, 321))
        self.calendarWidget.setObjectName("calendarWidget")
        self.lineEdit = QtWidgets.QLineEdit(parent=Form)
        self.lineEdit.setGeometry(QtCore.QRect(0, 370, 311, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.addEventBtn = QtWidgets.QPushButton(parent=Form)
        self.addEventBtn.setGeometry(QtCore.QRect(0, 410, 311, 41))
        self.addEventBtn.setObjectName("addEventBtn")
        self.eventList = QtWidgets.QListWidget(parent=Form)
        self.eventList.setGeometry(QtCore.QRect(310, 0, 301, 451))
        self.eventList.setObjectName("eventList")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.addEventBtn.setText(_translate("Form", "Добавить событие"))


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
