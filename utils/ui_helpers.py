from PyQt5.QtWidgets import QMessageBox

class UIHelpers:
    @staticmethod
    def show_error_message(parent, message):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()

    @staticmethod
    def show_info_message(parent, message, title="Information"):
        msg = QMessageBox(parent)
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.exec_()
