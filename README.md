Attribute,Details
Project Description,"This project implements the classic Caesar Cipher, a simple substitution cipher. The tool allows a user to input a plaintext message and an integer key (shift value) to encrypt the message, and can reverse the process to decrypt any cipher text."
Key Security Concept,Symmetric Encryption: Demonstrates the principle where the same key is used for both encryption and decryption.
Key Features,"* Encryption/Decryption Functionality: A single function handles both processes based on the shift direction.  * Looping Alphabet: Handles character wrapping (e.g., 'z' shifted by 1 becomes 'a') using the modulo operator.  * Case Preservation: Maintains the original casing of letters (e.g., 'A' remains capitalized after shifting)."
Technologies Used,Python 3.x (Standard library)
How to Run,Run the script and follow the interactive console prompts:  python task01_caesar_cipher.py
