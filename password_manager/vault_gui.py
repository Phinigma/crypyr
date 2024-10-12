from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QLineEdit,
    QListWidget, QHBoxLayout, QMessageBox, QSizePolicy
)
from password_manager.password_vault import PasswordVault


class VaultGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.vault = PasswordVault()
        self.encryption_key = None  # User-defined key for encrypting/decrypting passwords
        self.init_ui()

    def init_ui(self):
        # Removed self.setWindowTitle and self.setGeometry

        layout = QVBoxLayout()

        # Key input for encryption/decryption
        key_layout = QHBoxLayout()
        key_layout.addWidget(QLabel("Encryption Key:"))
        self.key_input = QLineEdit()
        self.key_input.setPlaceholderText("Enter encryption key")
        self.key_input.setEchoMode(QLineEdit.Password)  # Hide input by default
        key_layout.addWidget(self.key_input)
        layout.addLayout(key_layout)

        # Buttons to interact with vault
        self.load_button = QPushButton("Load Vault")
        self.load_button.clicked.connect(self.load_vault)
        layout.addWidget(self.load_button)

        self.service_input = QLineEdit()
        self.service_input.setPlaceholderText("Service (e.g., Gmail)")
        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username (e.g., user@gmail.com)")
        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)  # Mask the password input

        layout.addWidget(QLabel("Add New Password:"))
        layout.addWidget(self.service_input)
        layout.addWidget(self.username_input)
        layout.addWidget(self.password_input)

        self.add_button = QPushButton("Add Password")
        self.add_button.clicked.connect(self.add_password)
        layout.addWidget(self.add_button)

        # Password list
        self.password_list = QListWidget()
        self.password_list.setSelectionMode(QListWidget.SingleSelection)
        layout.addWidget(QLabel("Stored Passwords:"))
        layout.addWidget(self.password_list)

        # Delete password button
        self.delete_button = QPushButton("Delete Selected Password")
        self.delete_button.clicked.connect(self.delete_password)
        layout.addWidget(self.delete_button)

        # Set size policies
        self.password_list.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.setLayout(layout)

    def load_vault(self):
        self.encryption_key = self.key_input.text()
        if not self.encryption_key:
            self.show_error_message("Please enter an encryption key.")
            return
        passwords = self.vault.get_passwords(self.encryption_key)
        self.password_list.clear()
        for pwd in passwords:
            self.password_list.addItem(f"ID: {pwd[0]}, Service: {pwd[1]}, Username: {pwd[2]}, Password: {pwd[3]}")

    def add_password(self):
        service = self.service_input.text()
        username = self.username_input.text()
        password = self.password_input.text()
        self.encryption_key = self.key_input.text()

        if not (service and username and password):
            self.show_error_message("Please fill in all fields.")
            return

        if not self.encryption_key:
            self.show_error_message("Please enter an encryption key.")
            return

        self.vault.add_password(service, username, password, self.encryption_key)
        QMessageBox.information(self, "Password Added", "Password successfully added to vault.")
        self.service_input.clear()
        self.username_input.clear()
        self.password_input.clear()
        self.load_vault()

    def delete_password(self):
        selected_item = self.password_list.currentItem()
        if selected_item:
            item_text = selected_item.text()
            password_id = item_text.split(",")[0].split(":")[1].strip()
            self.vault.delete_password(int(password_id))
            QMessageBox.information(self, "Password Deleted", "Password successfully deleted.")
            self.load_vault()
        else:
            self.show_error_message("Please select a password to delete.")

    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()
