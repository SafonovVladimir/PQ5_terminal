import sys

from PyQt5.QtWidgets import QApplication

from Controller.terminal_controller import TerminalController
from Model.terminal_model import TerminalModel

if __name__ == '__main__':
    app = QApplication(sys.argv)
    terminal_model = TerminalModel()
    terminal_view = TerminalController()
    sys.exit(app.exec_())
