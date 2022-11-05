from ui_form import *
import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5 import QtCore


class Login(QWidget):
    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.retry.clicked.connect(self.retry)  # type: ignore
        self.ui.entry.clicked.connect(self.entry)  # type: ignore

    def entry(self):
        cookie = self.ui.cookie_info.toPlainText()

    def retry(self):
        self.ui.cookie_info.clear()


if __name__ == "__main__":
    myapp = QApplication(sys.argv)
    login = Login()
    login.show()
    sys.exit(myapp.exec_())
