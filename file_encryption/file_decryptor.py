from Crypto.Cipher import AES

class FileDecryptor:
    def __init__(self, key):
        self.key = key.encode('utf-8')

    def decrypt_file(self, file_path):
        try:
            with open(file_path, 'rb') as f:
                iv = f.read(AES.block_size)
                ciphertext = f.read()

            cipher = AES.new(self.key, AES.MODE_CBC, iv)
            decrypted_data = cipher.decrypt(ciphertext).rstrip(b"\0")

            decrypted_file_path = f"{file_path}.dec"
            with open(decrypted_file_path, 'wb') as f:
                f.write(decrypted_data)

            return decrypted_file_path

        except Exception as e:
            print(f"Error decrypting file: {e}")
            return None
