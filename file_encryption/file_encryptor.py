from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

class FileEncryptor:
    def __init__(self, key):
        self.key = key.encode('utf-8')

    def pad(self, data):
        return data + b"\0" * (AES.block_size - len(data) % AES.block_size)

    def encrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                plaintext = f.read()

            padded_plaintext = self.pad(plaintext)
            iv = get_random_bytes(AES.block_size)
            cipher = AES.new(self.key, AES.MODE_CBC, iv)

            encrypted_file_path = f"{file_path}.enc"
            with open(encrypted_file_path, 'wb') as f:
                f.write(iv)
                f.write(cipher.encrypt(padded_plaintext))

            return encrypted_file_path

        except Exception as e:
            print(f"Error encrypting file: {e}")
            return None
