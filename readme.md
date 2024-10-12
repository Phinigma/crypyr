# Cypyr - Cryptography Tool

## Overview

Cypyr is a versatile, offline cryptography tool designed for both educational purposes and practical data security. It provides multiple encryption algorithms, including the Caesar Cipher, Vigenère Cipher, and AES (Advanced Encryption Standard), to help users learn about cryptographic techniques and securely encrypt/decrypt their data. Additionally, Cypyr includes features like a Password Vault, File Shredder, and Secure Messaging to enhance your digital security toolkit.

## Features

- **Multiple Encryption Methods:**
  - **Caesar Cipher:** Simple substitution cipher for educational purposes.
  - **Vigenère Cipher:** Polyalphabetic cipher offering more complexity than Caesar.
  - **AES Encryption:** Industry-standard encryption for secure data protection.
- **Password Vault:** Securely store and manage your passwords using AES encryption.
- **File Shredder:** Permanently delete files to prevent data recovery.
- **Secure Messaging:** Communicate securely using RSA encryption.
- **User-friendly Interface:** Modern, easy-to-use graphical interface using PyQt5.
- **Offline Functionality:** All operations occur locally on your machine, ensuring your data remains private.

## Installation

### Prerequisites

- **Python 3.7** or higher
- Required packages:
  - `PyQt5`
  - `cryptography`
  - `pycryptodome`

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Phinigma/cypyr.git
   cd cypyr
