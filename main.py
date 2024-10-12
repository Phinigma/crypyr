from PyQt5.QtWidgets import QApplication
from gui import CryptoApp
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")  # Apply the Fusion style to your application
    window = CryptoApp()
    window.show()
    sys.exit(app.exec_())
