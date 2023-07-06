import sys

from PyQt5.QtWidgets import QApplication

from Controller.terminal_controller import TerminalController
from Model.terminal_model import TerminalModel
from View.terminal_view import TerminalView

if __name__ == '__main__':
    app = QApplication(sys.argv)
    terminal_model = TerminalModel()
    terminal_view = TerminalView()
    terminal_controller = TerminalController(terminal_model, terminal_view)
    sys.exit(app.exec_())
