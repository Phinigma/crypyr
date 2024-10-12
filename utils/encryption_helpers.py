import secrets
import string

class EncryptionHelpers:
    @staticmethod
    def generate_random_key(algorithm):
        if algorithm == "Caesar":
            return str(secrets.randbelow(26))
        elif algorithm == "Vigenère":
            return ''.join(secrets.choice(string.ascii_uppercase) for _ in range(8))
        elif algorithm == "AES":
            return secrets.token_hex(16)  # 256-bit key (32 hex characters)
        return None
