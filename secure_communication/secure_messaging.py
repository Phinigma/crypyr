import rsa

def generate_rsa_keys():
    """Generate RSA public and private keys"""
    (public_key, private_key) = rsa.newkeys(2048)
    return private_key, public_key

def save_keys(private_key, public_key, private_key_file='private.pem', public_key_file='public.pem'):
    """Save the keys to .pem files"""
    with open(private_key_file, 'wb') as priv_file:
        priv_file.write(private_key.save_pkcs1())
    with open(public_key_file, 'wb') as pub_file:
        pub_file.write(public_key.save_pkcs1())

def encrypt_message(message, public_key):
    """Encrypt a message using the RSA public key"""
    return rsa.encrypt(message.encode(), public_key)

def decrypt_message(encrypted_message, private_key):
    """Decrypt a message using the RSA private key"""
    return rsa.decrypt(encrypted_message, private_key).decode()
