import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from Controller.terminal_controller import TerminalController
from Model.terminal_model import TerminalModel
from View.main_window import Ui_MainWindow
from View.terminal_view import TerminalView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # window = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(window)
    # window.show()
    # app.exec_()
    terminal_model = TerminalModel()
    terminal_view = TerminalView()
    terminal_controller = TerminalController(terminal_model, terminal_view)
    # terminal_controller.connect()
    sys.exit(app.exec_())
