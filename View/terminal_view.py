import serial
from PyQt5.QtWidgets import QMainWindow

from View.main_window import Ui_MainWindow


class TerminalView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()
