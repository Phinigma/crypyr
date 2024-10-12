from Crypto.Cipher import AES
import base64

def aes_encrypt(text, key):
    cipher = AES.new(key.encode('utf-8').ljust(32)[:32], AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def aes_decrypt(text, key):
    try:
        raw = base64.b64decode(text)
        nonce = raw[:16]
        ciphertext = raw[16:]
        cipher = AES.new(key.encode('utf-8').ljust(32)[:32], AES.MODE_EAX, nonce=nonce)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {str(e)}"
