import os
import sqlite3
from encryption_algorithms.aes import aes_encrypt, aes_decrypt


class PasswordVault:
    def __init__(self, db_path='vault.db'):
        self.db_path = db_path
        if not os.path.exists(self.db_path):
            self.initialize_vault()

    def initialize_vault(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE vault (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    service TEXT NOT NULL,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            """)
            conn.commit()

    def add_password(self, service, username, password, key):
        encrypted_password = aes_encrypt(password, key)
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO vault (service, username, password) VALUES (?, ?, ?)
            """, (service, username, encrypted_password))
            conn.commit()

    def get_passwords(self, key):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM vault")
            passwords = cursor.fetchall()

        decrypted_passwords = []
        for pwd in passwords:
            try:
                decrypted_password = aes_decrypt(pwd[3], key)
                decrypted_passwords.append((pwd[0], pwd[1], pwd[2], decrypted_password))
            except Exception:
                continue  # Skip entries that can't be decrypted (wrong key)

        return decrypted_passwords

    def delete_password(self, password_id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM vault WHERE id = ?", (password_id,))
            conn.commit()
