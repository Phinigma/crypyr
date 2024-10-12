# gui.py

import os
import secrets
import string
from PyQt5.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QPushButton, QTextEdit, QLabel,
    QComboBox, QLineEdit, QMessageBox, QGridLayout, QHBoxLayout,
    QTabWidget, QScrollArea, QFileDialog, QWidget, QMenuBar, QSizePolicy,
    QTextBrowser
)

from PyQt5.QtGui import QDragEnterEvent, QIcon
from PyQt5.QtCore import Qt

from encryption_algorithms.caesar import caesar_encrypt, caesar_decrypt
from encryption_algorithms.vigenere import vigenere_encrypt, vigenere_decrypt
from encryption_algorithms.aes import aes_encrypt, aes_decrypt
from secure_communication.secure_messaging import (
    generate_rsa_keys, encrypt_message as rsa_encrypt_message,
    decrypt_message as rsa_decrypt_message, save_keys
)
from help.help_guide import HelpGuide
from password_manager.vault_gui import VaultGUI
from file_shredder.shredder import FileShredder


class CryptoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_stylesheet()
        self.setFixedSize(1000, 700)  # Adjust window size to ensure all elements fit well

    def load_stylesheet(self):
        with open('styles.qss', 'r') as f:
            stylesheet = f.read()
            self.setStyleSheet(stylesheet)

    def init_ui(self):
        self.setWindowTitle("Cypyr - Cryptography Tool")
        self.setGeometry(100, 100, 1000, 700)

        # Create Menu Bar
        menu_bar = self.menuBar()

        # Create Menus
        file_menu = menu_bar.addMenu("File")
        tools_menu = menu_bar.addMenu("Tools")
        help_menu = menu_bar.addMenu("Help")

        # Add actions to menus
        exit_action = file_menu.addAction("Exit")
        exit_action.triggered.connect(self.close)
        # You can add more actions to the File menu here if desired

        tools_menu.addAction("Encryption/Decryption", self.switch_to_encryption_tab)
        tools_menu.addAction("Password Vault", self.switch_to_password_vault_tab)
        tools_menu.addAction("File Shredder", self.switch_to_shredder_tab)
        tools_menu.addAction("Secure Messaging", self.switch_to_secure_messaging_tab)

        # Help Menu Actions
        help_menu.addAction("User Guide", self.switch_to_help_tab)
        about_action = help_menu.addAction("About")
        about_action.triggered.connect(self.show_about_dialog)
        license_action = help_menu.addAction("License")
        license_action.triggered.connect(self.show_license_dialog)
        disclaimer_action = help_menu.addAction("Disclaimer")
        disclaimer_action.triggered.connect(self.show_disclaimer_dialog)

        # Initialize the QTabWidget
        self.tabs = QTabWidget()

        # Create individual tabs
        self.encryption_tab = QWidget()
        self.password_vault_tab = QWidget()
        self.shredder_tab = QWidget()
        self.secure_messaging_tab = QWidget()
        self.help_tab = QWidget()

        # Initialize tabs
        self.init_encryption_tab()
        self.init_password_vault_tab()
        self.init_shredder_tab()
        self.init_secure_messaging_tab()
        self.init_help_tab()

        # Add tabs to the QTabWidget
        self.tabs.addTab(self.encryption_tab, "Encryption")
        self.tabs.addTab(self.password_vault_tab, "Password Vault")
        self.tabs.addTab(self.shredder_tab, "File Shredder")
        self.tabs.addTab(self.secure_messaging_tab, "Secure Messaging")
        self.tabs.addTab(self.help_tab, "Help")

        # Set the central widget of the QMainWindow
        self.setCentralWidget(self.tabs)

    # Switch between tabs
    def switch_to_encryption_tab(self):
        self.tabs.setCurrentWidget(self.encryption_tab)

    def switch_to_password_vault_tab(self):
        self.tabs.setCurrentWidget(self.password_vault_tab)

    def switch_to_shredder_tab(self):
        self.tabs.setCurrentWidget(self.shredder_tab)

    def switch_to_secure_messaging_tab(self):
        self.tabs.setCurrentWidget(self.secure_messaging_tab)

    def switch_to_help_tab(self):
        self.tabs.setCurrentWidget(self.help_tab)

    # Toggle key visibility
    def toggle_key_visibility(self, checked):
        if checked:
            self.key_input.setEchoMode(QLineEdit.Normal)  # Show text
            self.show_key_button.setText("Hide Key")
        else:
            self.key_input.setEchoMode(QLineEdit.Password)  # Hide text
            self.show_key_button.setText("Show Key")

    # Copy key to clipboard functionality
    def copy_key_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.key_input.text())
        QMessageBox.information(self, "Copied", "Encryption key copied to clipboard.")

    # Copy output to clipboard functionality
    def copy_output_to_clipboard(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.output.toPlainText())
        QMessageBox.information(self, "Copied", "Output text copied to clipboard.")

    # Encryption Tab Initialization
    def init_encryption_tab(self):
        self.encryption_tab.layout = QGridLayout()
        self.algorithm_dropdown = QComboBox()
        self.algorithm_dropdown.addItems(["Caesar", "Vigenère", "AES"])
        self.encryption_tab.layout.addWidget(QLabel("Select Encryption Algorithm"), 0, 0)
        self.encryption_tab.layout.addWidget(self.algorithm_dropdown, 0, 1)
        self.encryption_tab.layout.setContentsMargins(10, 10, 10, 10)  # Add margins to the layout
        self.encryption_tab.layout.setSpacing(10)  # Add spacing between widgets

        # Key Input and Key Controls
        self.key_layout = QHBoxLayout()
        self.key_input = QLineEdit()
        self.key_input.setEchoMode(QLineEdit.Password)  # Hide key input by default
        self.key_layout.addWidget(self.key_input)

        self.random_key_button = QPushButton("Random Key")
        self.random_key_button.setObjectName("topButton")  # Set object name for styling
        self.random_key_button.clicked.connect(self.generate_random_key)
        self.key_layout.addWidget(self.random_key_button)

        self.show_key_button = QPushButton("Show Key")
        self.show_key_button.setObjectName("topButton")  # Set object name for styling
        self.show_key_button.setCheckable(True)
        self.show_key_button.toggled.connect(self.toggle_key_visibility)
        self.key_layout.addWidget(self.show_key_button)

        self.copy_key_button = QPushButton("Copy Key")
        self.copy_key_button.setObjectName("topButton")  # Set object name for styling
        self.copy_key_button.clicked.connect(self.copy_key_to_clipboard)
        self.key_layout.addWidget(self.copy_key_button)

        self.encryption_tab.layout.addWidget(QLabel("Key (if applicable)"), 1, 0)
        self.encryption_tab.layout.addLayout(self.key_layout, 1, 1)

        # Text Input for Encryption/Decryption
        self.text_input = QTextEdit()
        self.encryption_tab.layout.addWidget(QLabel("Text to Encrypt/Decrypt"), 2, 0)
        self.encryption_tab.layout.addWidget(self.text_input, 2, 1)

        # Encrypt/Decrypt Buttons
        self.encrypt_button = QPushButton("Encrypt")
        self.encrypt_button.setObjectName("topButton")  # Set object name for styling
        self.encrypt_button.clicked.connect(self.encrypt_text)
        self.decrypt_button = QPushButton("Decrypt")
        self.decrypt_button.setObjectName("topButton")  # Set object name for styling
        self.decrypt_button.clicked.connect(self.decrypt_text)

        button_layout = QHBoxLayout()
        button_layout.addWidget(self.encrypt_button)
        button_layout.addWidget(self.decrypt_button)

        self.encryption_tab.layout.addLayout(button_layout, 3, 1)

        # Output Display
        self.output = QTextEdit()
        self.output.setReadOnly(True)
        self.encryption_tab.layout.addWidget(QLabel("Output"), 4, 0)

        output_layout = QHBoxLayout()
        output_layout.addWidget(self.output)

        self.copy_output_button = QPushButton("Copy Output")
        self.copy_output_button.setObjectName("topButton")  # Set object name for styling
        self.copy_output_button.clicked.connect(self.copy_output_to_clipboard)
        output_layout.addWidget(self.copy_output_button)

        self.encryption_tab.layout.addLayout(output_layout, 4, 1)

        self.encryption_tab.setLayout(self.encryption_tab.layout)

    # Random Key Generation
    def generate_random_key(self):
        algorithm = self.algorithm_dropdown.currentText()
        if algorithm == "Caesar":
            self.key_input.setText(str(secrets.randbelow(26)))
        elif algorithm == "Vigenère":
            self.key_input.setText(''.join(secrets.choice(string.ascii_uppercase) for _ in range(8)))
        elif algorithm == "AES":
            self.key_input.setText(secrets.token_hex(16))  # 256-bit key (32 hex characters)

    # Text Encrypt
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
            if len(key) not in [32, 48, 64]:
                self.show_error_message("AES key must be 16, 24, or 32 bytes (32, 48, or 64 hex characters).")
            else:
                encrypted_text = aes_encrypt(text, key)
                self.output.setPlainText(encrypted_text)

    # Text Decrypt
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
            if len(key) not in [32, 48, 64]:
                self.show_error_message("AES key must be 16, 24, or 32 bytes (32, 48, or 64 hex characters).")
            else:
                decrypted_text = aes_decrypt(text, key)
                self.output.setPlainText(decrypted_text)

    # File Shredder Tab Initialization
    def init_shredder_tab(self):
        self.shredder_tab.layout = QVBoxLayout()

        # Drag-and-drop area for selecting files to shred
        self.drag_drop_label = QLabel("Drag and drop a file here to shred it")
        self.drag_drop_label.setAlignment(Qt.AlignCenter)
        self.drag_drop_label.setStyleSheet("border: 2px dashed #00FF00; padding: 20px;")
        self.drag_drop_label.setAcceptDrops(True)
        self.drag_drop_label.dragEnterEvent = self.drag_enter_event
        self.drag_drop_label.dropEvent = self.drop_event

        self.shredder_tab.layout.addWidget(self.drag_drop_label)

        # File browser button for selecting files
        self.browse_file_button = QPushButton("Browse File")
        self.browse_file_button.setObjectName("topButton")  # Set object name for styling
        self.browse_file_button.clicked.connect(self.browse_file)
        self.shredder_tab.layout.addWidget(self.browse_file_button)

        # Shred file button to delete the selected file
        self.shred_file_button = QPushButton("Shred File")
        self.shred_file_button.setObjectName("topButton")  # Set object name for styling
        self.shred_file_button.clicked.connect(self.shred_file)
        self.shredder_tab.layout.addWidget(self.shred_file_button)

        self.shredder_tab.setLayout(self.shredder_tab.layout)
        self.file_to_shred = None

    # Browse Files
    def browse_file(self):
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Select File to Shred", "", "All Files (*)", options=options
        )
        if file_path:
            self.file_to_shred = file_path
            self.drag_drop_label.setText(f"File to shred: {os.path.basename(self.file_to_shred)}")

    # Drag & Drop Events
    def drag_enter_event(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def drop_event(self, event):
        urls = event.mimeData().urls()
        if urls:
            self.file_to_shred = urls[0].toLocalFile()
            self.drag_drop_label.setText(f"File to shred: {os.path.basename(self.file_to_shred)}")

    # Shredder Function
    def shred_file(self):
        if self.file_to_shred:
            shredder = FileShredder()
            success = shredder.shred_file(self.file_to_shred)
            if success:
                QMessageBox.information(self, "File Shredded", "The file has been securely shredded.")
                self.drag_drop_label.setText("Drag and drop a file here to shred it")
                self.file_to_shred = None
            else:
                self.show_error_message("Failed to shred the file.")
        else:
            self.show_error_message("No file selected for shredding.")

    # Secure Messaging Tab Initialization
    def init_secure_messaging_tab(self):
        self.secure_messaging_tab.layout = QVBoxLayout()
        self.generate_keys_button = QPushButton("Generate RSA Keys")
        self.generate_keys_button.setObjectName("topButton")  # Set object name for styling
        self.generate_keys_button.clicked.connect(self.generate_keys)
        self.secure_messaging_tab.layout.addWidget(self.generate_keys_button)

        self.message_input = QTextEdit()
        self.secure_messaging_tab.layout.addWidget(QLabel("Message to Encrypt/Decrypt"))
        self.secure_messaging_tab.layout.addWidget(self.message_input)

        self.public_key_input = QLineEdit()
        self.public_key_input.setPlaceholderText("Enter recipient's public key")
        self.secure_messaging_tab.layout.addWidget(QLabel("Public Key (for encryption)"))
        self.secure_messaging_tab.layout.addWidget(self.public_key_input)

        self.encrypt_message_button = QPushButton("Encrypt Message")
        self.encrypt_message_button.setObjectName("topButton")  # Set object name for styling
        self.encrypt_message_button.clicked.connect(self.encrypt_message)
        self.secure_messaging_tab.layout.addWidget(self.encrypt_message_button)

        self.decrypt_message_button = QPushButton("Decrypt Message")
        self.decrypt_message_button.setObjectName("topButton")  # Set object name for styling
        self.decrypt_message_button.clicked.connect(self.decrypt_message)
        self.secure_messaging_tab.layout.addWidget(self.decrypt_message_button)

        self.encrypted_message_output = QTextEdit()
        self.encrypted_message_output.setReadOnly(True)
        self.secure_messaging_tab.layout.addWidget(QLabel("Encrypted/Decrypted Message"))
        self.secure_messaging_tab.layout.addWidget(self.encrypted_message_output)

        self.secure_messaging_tab.setLayout(self.secure_messaging_tab.layout)

    # RSA Key Generation
    def generate_keys(self):
        private_key, public_key = generate_rsa_keys()

        # Prompt the user to select a location to save the keys
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save RSA Keys", "", "Key Files (*.pem);;All Files (*)", options=options
        )
        if file_path:
            save_keys(private_key, public_key, file_path)
            QMessageBox.information(
                self, "Keys Generated", f"RSA keys have been generated and saved to: {file_path}"
            )

    # Secure Messaging Encryption
    def encrypt_message(self):
        public_key = self.public_key_input.text()
        message = self.message_input.toPlainText()
        if not public_key or not message:
            self.show_error_message("Please enter both a public key and a message to encrypt.")
            return

        try:
            encrypted_message = rsa_encrypt_message(public_key, message)
            self.encrypted_message_output.setPlainText(encrypted_message)
        except Exception as e:
            self.show_error_message(f"Failed to encrypt the message: {str(e)}")

    # Secure Messaging Decryption
    def decrypt_message(self):
        message = self.message_input.toPlainText()
        if not message:
            self.show_error_message("Please enter a message to decrypt.")
            return

        try:
            decrypted_message = rsa_decrypt_message(message)
            self.encrypted_message_output.setPlainText(decrypted_message)
        except Exception as e:
            self.show_error_message(f"Failed to decrypt the message: {str(e)}")

    # Help Tab Initialization
    def init_help_tab(self):
        self.help_guide = HelpGuide()
        self.help_tab.layout = QVBoxLayout()

        # Layout for selecting the help topic
        help_layout = QHBoxLayout()
        self.section_dropdown = QComboBox()
        self.section_dropdown.addItems(list(self.help_guide.guide_content.keys()))
        self.section_dropdown.currentTextChanged.connect(self.update_help_content)
        help_layout.addWidget(QLabel("Select Topic:"))
        help_layout.addWidget(self.section_dropdown)
        self.help_tab.layout.addLayout(help_layout)

        # Text area to display the help content
        self.help_text = QTextBrowser()
        self.help_text.setOpenExternalLinks(True)
        self.help_text.setReadOnly(True)
        self.help_text.setHtml(self.help_guide.get_content("Introduction"))

        # Adding Scroll Area for Compactness
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_widget = QWidget()
        scroll_widget_layout = QVBoxLayout()
        scroll_widget_layout.addWidget(self.help_text)
        scroll_widget.setLayout(scroll_widget_layout)
        scroll_area.setWidget(scroll_widget)

        self.help_tab.layout.addWidget(scroll_area)
        self.help_tab.setLayout(self.help_tab.layout)

    # Update Help Content
    def update_help_content(self, section):
        content = self.help_guide.get_content(section)
        self.help_text.setHtml(content)

    # Error Handling
    def show_error_message(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(message)
        msg.setWindowTitle("Error")
        msg.exec()

    # Show About Dialog
    def show_about_dialog(self):
        QMessageBox.about(
            self,
            "About Cypyr",
            "Cypyr - Cryptography Tool\nVersion 1.0\n\nDeveloped by Phinigma\n"
            "GitHub Repository: https://github.com/Phinigma/cypyr",
        )

    # Show License Dialog
    def show_license_dialog(self):
        # MIT License Text
        license_text = """
        MIT License

        Copyright (c) 2024 Phi

        Permission is hereby granted, free of charge, to any person obtaining a copy
        of this software and associated documentation files (the "Software"), to deal
        in the Software without restriction, including without limitation the rights
        to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
        copies of the Software, and to permit persons to whom the Software is
        furnished to do so, subject to the following conditions:

        The above copyright notice and this permission notice shall be included in all
        copies or substantial portions of the Software.

        THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
        IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
        FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
        AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
        LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
        OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
        SOFTWARE.
        """
        QMessageBox.information(self, "License", license_text)

    # Show Disclaimer Dialog
    def show_disclaimer_dialog(self):
        disclaimer_text = """
        <h2>Disclaimer</h2>
        <p>
            The Cypyr application is provided "as is" without any guarantees or warranty. In association with the product, the developer makes no warranties of any kind, either express or implied, including but not limited to warranties of merchantability, fitness for a particular purpose, of title, or of noninfringement of third-party rights. Use of the software by a user is at the user's risk.

            The developer shall not be liable for any damages, including but not limited to direct, indirect, special, incidental, or consequential damages or other losses arising out of the use of or inability to use the software.

            By using this application, you agree that you understand the risks involved with cryptographic software, including but not limited to potential data loss, security vulnerabilities, or legal implications. You are responsible for ensuring that your use of this software complies with all applicable laws and regulations.

            The developer is not responsible for any damage to your system, loss of data, or any other harm resulting from the use of this software. Always backup your data before using tools that modify or delete data.

            If you do not agree with these terms, you should not use this software.
        </p>
        """
        QMessageBox.information(self, "Disclaimer", disclaimer_text)

    # Password Vault Tab Initialization
    def init_password_vault_tab(self):
        # Integrate the VaultGUI
        self.vault_gui = VaultGUI()
        vault_layout = QVBoxLayout()
        vault_layout.addWidget(self.vault_gui)
        self.password_vault_tab.setLayout(vault_layout)