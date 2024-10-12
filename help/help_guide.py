# help_guide.py

class HelpGuide:
    def __init__(self):
        self.guide_content = {
            "Introduction": """
                <h1>Welcome to <span style="color:#2E9CCA;">Cypyr</span></h1>
                <p>
                    Cypyr is a versatile cryptography tool designed for offline security needs. It offers a suite of features to help you protect your data and communications.
                </p>
                <h2>Key Features:</h2>
                <ul>
                    <li><strong>Encryption/Decryption:</strong> Encrypt and decrypt text using various algorithms.</li>
                    <li><strong>Password Vault:</strong> Securely store and manage your passwords.</li>
                    <li><strong>File Shredder:</strong> Permanently delete files to prevent data recovery.</li>
                    <li><strong>Secure Messaging:</strong> Communicate securely using RSA encryption.</li>
                </ul>
                <p>
                    Explore each tab to utilize the full potential of Cypyr and enhance your digital security.
                </p>
            """,
            "Encryption/Decryption": """
                <h1>Encryption/Decryption</h1>
                <p>
                    The <strong>Encryption/Decryption</strong> tab allows you to secure your text data using various algorithms. You can choose between simple ciphers for educational purposes or strong encryption for practical security.
                </p>
                <h2>Available Algorithms:</h2>
                <ul>
                    <li><strong>Caesar Cipher:</strong> A simple substitution cipher where each letter in the plaintext is shifted by a fixed number of positions.</li>
                    <li><strong>Vigenère Cipher:</strong> A method of encrypting text by applying a series of Caesar ciphers based on the letters of a keyword.</li>
                    <li><strong>AES Encryption:</strong> Advanced Encryption Standard is a symmetric encryption algorithm widely used for secure data transmission.</li>
                </ul>
                <h2>How to Use:</h2>
                <ol>
                    <li>Select an encryption algorithm from the dropdown menu.</li>
                    <li>Enter the text you wish to encrypt or decrypt in the 'Text to Encrypt/Decrypt' field.</li>
                    <li>Enter the key if required (for AES, ensure the key length is 16, 24, or 32 bytes).</li>
                    <li>Use the 'Random Key' button to generate a secure key (recommended for AES).</li>
                    <li>Click 'Encrypt' or 'Decrypt' to perform the operation.</li>
                    <li>The result will appear in the 'Output' field, where you can copy it to the clipboard.</li>
                </ol>
                <h2>Tips:</h2>
                <ul>
                    <li>Always use strong, unpredictable keys for encryption.</li>
                    <li>Keep your keys confidential to maintain security.</li>
                </ul>
            """,
            "Password Vault": """
                <h1>Password Vault</h1>
                <p>
                    The <strong>Password Vault</strong> is designed to securely store your passwords using AES encryption. All data is encrypted locally, ensuring that your credentials remain private.
                </p>
                <h2>Getting Started:</h2>
                <ol>
                    <li>Enter a master encryption key in the 'Encryption Key' field. This key will encrypt and decrypt your stored passwords. <strong>Do not forget this key!</strong></li>
                    <li>Click 'Load Vault' to access your saved passwords.</li>
                </ol>
                <h2>Adding a New Password:</h2>
                <ol>
                    <li>Enter the service name (e.g., Gmail) in the 'Service' field.</li>
                    <li>Enter your username or email associated with the service.</li>
                    <li>Enter your password. You can generate a strong password using an external tool.</li>
                    <li>Click 'Add Password' to save the entry.</li>
                </ol>
                <h2>Managing Passwords:</h2>
                <ul>
                    <li>Your passwords will be listed under 'Stored Passwords'.</li>
                    <li>Select a password entry to view details.</li>
                    <li>Click 'Delete Selected Password' to remove an entry from the vault.</li>
                </ul>
                <h2>Security Notice:</h2>
                <ul>
                    <li>Your master encryption key is crucial. If lost, you cannot retrieve your stored passwords.</li>
                    <li>Always use a strong and unique master key.</li>
                </ul>
            """,
            "File Shredder": """
                <h1>File Shredder</h1>
                <p>
                    The <strong>File Shredder</strong> securely deletes files by overwriting them multiple times, reducing the likelihood of data recovery.
                </p>
                <h2>How to Use:</h2>
                <ol>
                    <li>Drag and drop a file into the designated area or click 'Browse File' to select a file.</li>
                    <li>The file path will appear once selected.</li>
                    <li>Click 'Shred File' to permanently delete the file.</li>
                    <li>A confirmation message will appear upon successful shredding.</li>
                </ol>
                <h2>Important Notes:</h2>
                <ul>
                    <li>Secure file deletion on <strong>SSDs</strong> is not guaranteed due to hardware-level data remapping.</li>
                    <li>Even after shredding, remnants of the data may still exist. Consider additional measures for highly sensitive information.</li>
                    <li>Use this feature responsibly and ensure you have backups of important data.</li>
                </ul>
            """,
            "Secure Messaging": """
                <h1>Secure Messaging</h1>
                <p>
                    The <strong>Secure Messaging</strong> feature enables you to encrypt and decrypt messages using RSA encryption, ensuring secure communication.
                </p>
                <h2>Generating RSA Keys:</h2>
                <ol>
                    <li>Click 'Generate RSA Keys' to create a new pair of public and private keys.</li>
                    <li>Save the keys to a secure location when prompted.</li>
                </ol>
                <h2>Encrypting a Message:</h2>
                <ol>
                    <li>Enter your message in the 'Message to Encrypt/Decrypt' field.</li>
                    <li>Paste the recipient's public key into the 'Public Key' field.</li>
                    <li>Click 'Encrypt Message' to generate the encrypted text.</li>
                </ol>
                <h2>Decrypting a Message:</h2>
                <ol>
                    <li>Ensure you have your private key saved and accessible.</li>
                    <li>Paste the encrypted message into the 'Message to Encrypt/Decrypt' field.</li>
                    <li>Click 'Decrypt Message' to reveal the original text.</li>
                </ol>
                <h2>Security Tips:</h2>
                <ul>
                    <li>Never share your private key with anyone.</li>
                    <li>Exchange public keys securely to prevent man-in-the-middle attacks.</li>
                </ul>
            """,
            "FAQ and Troubleshooting": """
                <h1>FAQ and Troubleshooting</h1>
                <h2>Frequently Asked Questions</h2>
                <h3>Q: Why isn't my AES key working?</h3>
                <p>A: Ensure your key length is correct. AES requires keys of 16, 24, or 32 bytes (corresponding to 128, 192, or 256 bits).</p>
                <h3>Q: How can I retrieve a password from the vault?</h3>
                <p>A: Enter your master encryption key and click 'Load Vault' to decrypt and display your stored passwords.</p>
                <h3>Q: What should I do if I forget my encryption key?</h3>
                <p>A: Unfortunately, without your encryption key, you cannot access encrypted data. It's essential to remember or securely store your keys.</p>
                <h3>Q: Is the File Shredder effective on SSDs?</h3>
                <p>A: Due to the way SSDs manage data, secure deletion isn't guaranteed. Consider using full-disk encryption for better security on SSDs.</p>
                <h3>Q: Can I use Cypyr on multiple devices?</h3>
                <p>A: Yes, but ensure that you transfer any necessary keys or data securely between devices.</p>
                <h2>Troubleshooting Tips</h2>
                <ul>
                    <li><strong>Encryption/Decryption Issues:</strong> Double-check that you're using the correct key and algorithm.</li>
                    <li><strong>Password Vault Errors:</strong> Verify that your master key is correct and that the vault file hasn't been corrupted.</li>
                    <li><strong>Application Crashes:</strong> Ensure you have the latest version installed and that your system meets the minimum requirements.</li>
                    <li><strong>Feature Not Working:</strong> Consult the relevant section in this guide and confirm all steps were followed correctly.</li>
                </ul>
                <p>
                    If issues persist, consider reaching out to the developer or checking online resources for additional support.
                </p>
            """,
        }

    def get_content(self, section):
        return self.guide_content.get(
            section,
            """
            <h1>Section Not Found</h1>
            <p>The requested help section does not exist. Please select a valid topic from the list.</p>
            """
        )
