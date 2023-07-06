import serial
from PyQt5.QtWidgets import QMainWindow

from Utilities.port_reader import SerialPortReader
from View.main_window import Ui_MainWindow


class TerminalView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.window = QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.window)
        self.window.show()

        self.input = self.ui.textEdit_3
        connect_button = self.ui.pushButton
        connect_button.clicked.connect(self.connect_button_clicked)
        self.input.returnPressed.connect(self.send_command)

    def connect_button_clicked(self):
        port = self.ui.comboBox.currentText()
        baud_rate = int(self.ui.comboBox_2.currentText())

        try:
            self.ui.textBrowser.append(f"Connected to {port} at {baud_rate} baud rate.")
            self.serial_port_reader = SerialPortReader(port, baud_rate)
            self.serial_port_reader.new_data_received.connect(self.update_logs)
            self.serial_port_reader.start()
        except serial.SerialException as e:
            self.ui.textBrowser.append(f"Error: {str(e)}")

    def update_logs(self, data):
        self.ui.textBrowser.append(data)

    def send_command(self):
        command = self.input.text()
        self.serial_port_reader.serial_port.write(command.encode() + b"\r\n")
        self.ui.textBrowser.append(f"> {command}")
        self.input.clear()
