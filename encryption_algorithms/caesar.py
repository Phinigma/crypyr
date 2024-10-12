def caesar_encrypt(text, shift):
    encrypted = ''.join(
        chr((ord(char) - 65 + shift) % 26 + 65) if char.isalpha() else char
        for char in text.upper()
    )
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ''.join(
        chr((ord(char) - 65 - shift) % 26 + 65) if char.isalpha() else char
        for char in text.upper()
    )
    return decrypted
