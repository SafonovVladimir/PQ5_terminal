import serial

from Utilities.port_reader import SerialPortReader
from View.terminal_view import TerminalView


class TerminalController:
    def __init__(self):
        self.window = TerminalView()
        self.input = self.window.ui.lineEdit
        connect_button = self.window.ui.pushButton
        connect_button.clicked.connect(self.connect_button_clicked)
        self.input.returnPressed.connect(self.send_command)

    def connect_button_clicked(self):
        port = self.window.ui.comboBox.currentText()
        baud_rate = int(self.window.ui.comboBox_2.currentText())

        try:
            self.window.ui.textBrowser.append(f"Connected to {port} at {baud_rate} baud rate.")
            self.serial_port_reader = SerialPortReader(port, baud_rate)
            self.serial_port_reader.new_data_received.connect(self.update_logs)
            self.serial_port_reader.start()
        except serial.SerialException as e:
            self.window.ui.textBrowser.append(f"Error: {str(e)}")

    def update_logs(self, data):
        self.window.ui.textBrowser.append(data)

    def send_command(self):
        command = self.input.text()
        self.serial_port_reader.serial_port.write(command.encode() + b"\r\n")
        self.window.ui.textBrowser.append(f"> {command}")
        self.input.clear()
