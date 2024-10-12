from Crypto.Cipher import AES
import base64

def aes_encrypt(text, key):
    # Create a new AES cipher object using the key, padded to 32 bytes
    cipher = AES.new(key.encode('utf-8').ljust(32)[:32], AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(text.encode('utf-8'))
    return base64.b64encode(nonce + ciphertext).decode('utf-8')

def aes_decrypt(text, key):
    try:
        # Decode the base64 encoded string and extract the nonce and ciphertext
        raw = base64.b64decode(text)
        nonce = raw[:16]
        ciphertext = raw[16:]
        
        # Create a new AES cipher object with the same nonce and key, and decrypt the message
        cipher = AES.new(key.encode('utf-8').ljust(32)[:32], AES.MODE_EAX, nonce=nonce)
        decrypted = cipher.decrypt(ciphertext)
        return decrypted.decode('utf-8')
    except Exception as e:
        return f"Decryption failed: {str(e)}"
