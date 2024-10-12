Security Proof Documentation for Cypyr

1. AES Encryption

Algorithm Strength: AES (Advanced Encryption Standard) is widely regarded as one of the most secure symmetric encryption algorithms available. It is used by the U.S. government and many organizations worldwide for protecting sensitive information.

Key Size: AES supports key sizes of 128, 192, or 256 bits, with each providing a higher level of security. Cypyr requires keys of 16, 24, or 32 characters, which correspond to the 128, 192, and 256-bit key sizes, respectively.

Mathematical Security: AES relies on a series of complex transformations involving substitution, permutation, and mixing. This makes it resistant to common attacks, such as brute force and differential cryptanalysis.

Industry Standards: AES is approved by the National Institute of Standards and Technology (NIST) and is the de facto standard for data encryption.

2. Vigenère Cipher

Historical Context: The Vigenère Cipher is a polyalphabetic substitution cipher that was considered secure for centuries until more advanced techniques like frequency analysis were developed.

Key Security: In Cypyr, the key is used to determine a unique Caesar shift for each character of the message, making it more resistant to frequency analysis compared to simple substitution ciphers.

Limitations: The Vigenère Cipher is not suitable for protecting highly sensitive data due to its susceptibility to modern cryptographic attacks, such as the Kasiski examination. However, for basic use cases, such as obfuscating messages, it provides a reasonable level of security.

3. Caesar Cipher

Algorithm Simplicity: The Caesar Cipher is one of the oldest encryption methods, which involves shifting each letter in the plaintext by a fixed number of positions.

Security Concerns: The Caesar Cipher is not secure by modern standards since it can be easily broken using frequency analysis or brute force (only 25 possible shifts). It is included in Cypyr for educational purposes and simple use cases where strong security is not required.

4. Hashing for Integrity

Hashing Algorithms: While not implemented as an encryption mechanism in Cypyr, hashing (such as SHA-256) can be used to ensure data integrity. Hashing is a one-way process that creates a unique fixed-size hash for any input, which is useful for verifying data integrity.

Mathematical Security: SHA-256, part of the SHA-2 family, is designed to be collision-resistant, meaning that finding two different inputs that produce the same hash is computationally infeasible.

5. Proof of Security

AES: The strength of AES lies in its key size and complex structure, which make it resistant to all known practical attacks when used with a sufficiently long key (e.g., 256 bits). Brute-forcing a 256-bit AES key would require 2^256 operations, which is computationally impossible with current technology.

Vigenère and Caesar: These ciphers are included for educational purposes and do not offer strong security by today’s standards. Their purpose in Cypyr is to provide insight into the evolution of cryptographic techniques and to demonstrate the importance of strong keys and algorithms.

6. Recommendations for Users

Use AES for Sensitive Data: When encrypting sensitive information, always choose AES with a strong key (e.g., 256-bit) to ensure your data is secure.

Key Management: Ensure that your encryption keys are stored securely and not shared with unauthorized parties. Key management is critical for maintaining the confidentiality of encrypted data.

Educational Awareness: Understanding the strengths and weaknesses of each algorithm is essential. While AES is suitable for securing sensitive information, the Vigenère and Caesar ciphers should only be used in low-risk scenarios.

This documentation provides an overview of the security features and standards used in Cypyr, highlighting the strengths of AES and explaining the educational value of the other ciphers included in the tool.

