from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDateEdit
from PyQt5.QtCore import QDate

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()

        # Create a QDateEdit widget and set its date to the current date
        self.date_edit = QDateEdit(self)
        self.date_edit.setDate(QDate.currentDate())
        self.date_edit.setCalendarPopup(True)  # Enable the popup calendar

        layout.addWidget(self.date_edit)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication([])
    widget = MyWidget()
    widget.show()
    app.exec_()
