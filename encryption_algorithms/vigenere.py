def vigenere_encrypt(text, key):
    key = key.upper()
    encrypted = ''.join(
        chr((ord(text[i]) + ord(key[i % len(key)]) - 2 * 65) % 26 + 65) if text[i].isalpha() else text[i]
        for i in range(len(text))
    )
    return encrypted

def vigenere_decrypt(text, key):
    key = key.upper()
    decrypted = ''.join(
        chr((ord(text[i]) - ord(key[i % len(key)]) + 26) % 26 + 65) if text[i].isalpha() else text[i]
        for i in range(len(text))
    )
    return decrypted
