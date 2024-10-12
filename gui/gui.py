from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QComboBox, QLineEdit, QMessageBox, QGridLayout
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import Qt
from encryption_algorithms.caesar import caesar_encrypt, caesar_decrypt
from encryption_algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from encryption_algorithms.aes import aes_encrypt, aes_decrypt

class CryptoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Cypyr - Cryptography Tool")
        self.setGeometry(100, 100, 700, 500)

        # Overall layout and style
        layout = QGridLayout()
        self.setStyleSheet("""
            QWidget {
                background-color: #1e1e1e;
                color: #00ff00;
            }
            QTextEdit, QLineEdit {
                background-color: #2e2e2e;
                color: #00ff00;
                border: 2px solid #00ff00;
                padding: 8px;
                border-radius: 5px;
            }
            QPushButton {
                background-color: #3e3e3e;
                color: #00ff00;
                border-radius: 10px;
                padding: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #00ff00;
                color: #1e1e1e;
            }
            QComboBox {
                background-color: #2e2e2e;
                color: #00ff00;
                border: 2px solid #00ff00;
                padding: 5px;
                border-radius: 5px;
            }
        """)

        # Header
        header_label = QLabel("Cypyr")
        header_label.setFont(QFont("Arial", 20, QFont.Bold))
        header_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(header_label, 0, 0, 1, 2)

        # Dropdown to select algorithm
        self.algorithm_dropdown = QComboBox()
        self.algorithm_dropdown.addItems(["Caesar", "Vigenère", "AES"])
        layout.addWidget(QLabel("Select Encryption Algorithm"), 1, 0)
        layout.addWidget(self.algorithm_dropdown, 1, 1)

        # Input fields
        self.text_input = QTextEdit()
        self.key_input = QLineEdit()
        layout.addWidget(QLabel("Text to Encrypt/Decrypt"), 2, 0)
        layout.addWidget(self.text_input, 2, 1)
        layout.addWidget(QLabel("Key (if applicable)"), 3, 0)
        layout.addWidget(self.key_input, 3, 1)

        # Buttons
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        layout.addWidget(self.encrypt_button, 4, 0)
        layout.addWidget(self.decrypt_button, 4, 1)

        self.output = QTextEdit()
        self.output.setReadOnly(True)
        layout.addWidget(QLabel("Output"), 5, 0)
        layout.addWidget(self.output, 5, 1)

        # Set layout and signals
        self.setLayout(layout)
        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button.clicked.connect(self.decrypt_text)

    def encrypt_text(self):
        algorithm = self.algorithm_dropdown.currentText()
        text = self.text_input.toPlainText()
        key = self.key_input.text()

        if algorithm == "Caesar":
            try:
                shift = int(key)
                encrypted_text = caesar_encrypt(text, shift)
                self.output.setPlainText(encrypted_text)
            except ValueError:
                self.show_error_message("Invalid key for Caesar Cipher. Please enter an integer.")
        elif algorithm == "Vigenère":
            if not key:
                self.show_error_message("Please provide a key for Vigenère Cipher.")
            else:
                encrypted_text = vigenere_encrypt(text, key)
                self.output.setPlainText(encrypted_text)
        elif algorithm == "AES":
            if len(key) not in [16, 24, 32]:
                self.show_error_message("AES key must be 16, 24, or 32 characters long.")
            else:
                encrypted_text = aes_encrypt(text, key)
                self.output.setPlainText(encrypted_text)

    def decrypt_text(self):
        algorithm = self.algorithm_dropdown.currentText()
        text = self.text_input.toPlainText()
        key = self.key_input.text()

        if algorithm == "Caesar":
            try:
                shift = int(key)
                decrypted_text = caesar_decrypt(text, shift)
                self.output.setPlainText(decrypted_text)
            except ValueError:
                self.show_error_message("Invalid key for Caesar Cipher. Please enter an integer.")
        elif algorithm == "Vigenère":
            if not key:
                self.show_error_message("Please provide a key for Vigenère Cipher.")
            else:
                decrypted_text = vigenere_decrypt(text, key)
                self.output.setPlainText(decrypted_text)
        elif algorithm == "AES":
            if len(key) not in [16, 24, 32]:
                self.show_error_message("AES key must be 16, 24, or 32 characters long.")
            else:
                decrypted_text = aes_decrypt(text, key)
                self.output.setPlainText(decrypted_text)

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec_()
