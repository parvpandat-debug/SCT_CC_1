# 📜 Caesar Cipher Program

## 🌟 Overview

This program is a simple implementation of the **Caesar Cipher** algorithm. It allows a user to perform both **encryption** and **deception** on a given text message by applying a specified **shift value**. The Caesar Cipher is one of the earliest and simplest encryption techniques.

## 🔑 Features

* **Encryption:** Converts plaintext into ciphertext using a specified shift key.
* **Decryption:** Converts ciphertext back into plaintext using the same shift key.
* **User Input:** Prompts the user for the text message and the integer shift value required for the operation.

## 🛠️ Requirements

* **Python 3** (or the programming language used for the implementation).

## 🚀 How to Run

1.  **Save the Code:** Save the program code (e.g., `caesar_cipher.py`).
2.  **Execute:** Run the program from your terminal:

    ```bash
    python caesar_cipher.py
    ```

3.  **Follow Prompts:** The program will guide you through the process:
    * **Select Operation:** Choose 'E' for Encryption or 'D' for Decryption.
    * **Enter Message:** Type the text you want to process.
    * **Enter Shift Value:** Provide the integer number for the shift (e.g., 3).

## 💻 Example Usage

### Encryption

* **Input Message:** `HELLO`
* **Input Shift Value:** `3`
* **Output Ciphertext:** `KHOOR`

### Decryption

* **Input Message:** `KHOOR`
* **Input Shift Value:** `3`
* **Output Plaintext:** `HELLO`

## ⚙️ Algorithm Details

The program handles the cipher operation by shifting each letter in the input message forward (for encryption) or backward (for decryption) by the specified shift value $k$.

* **Encryption Formula:** $E_k(x) = (x + k) \pmod{26}$
* **Decryption Formula:** $D_k(y) = (y - k) \pmod{26}$

Non-alphabetic characters (e.g., spaces, punctuation) are left unchanged.

## 📝 Future Enhancements

* [ ] Implement a Brute-Force option for decryption.
* [ ] Support more complex character sets.
* [ ] Add a graphical user interface (GUI).
* [ ] Improve error handling for invalid inputs.
