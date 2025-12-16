def caesar_cipher(text, shift, mode):
    """
    Encrypts or decrypts text using the Caesar Cipher algorithm.
    :param text: The message string.
    :param shift: The integer shift value (key).
    :param mode: 'encrypt' or 'decrypt'.
    """
    result = ""
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift

    for char in text:
        if char.isalpha():
            # Determine starting point (A for uppercase, a for lowercase)
            start = ord('A') if char.isupper() else ord('a')
            
            # 1. Convert character to 0-25 index (e.g., A=0, B=1)
            index = ord(char) - start
            
            # 2. Apply shift and use modulo 26 to wrap around
            new_index = (index + shift) % 26
            
            # 3. Convert back to character
            new_char = chr(start + new_index)
            result += new_char
        else:
            # Keep non-alphabetic characters unchanged
            result += char
    return result

# --- User Interface ---
if __name__ == "__main__":
    print("--- Caesar Cipher Tool ---")
    
    # Get user inputs
    while True:
        choice = input("Do you want to (E)ncrypt or (D)ecrypt? ").lower()
        if choice in ['e', 'd']:
            mode = 'encrypt' if choice == 'e' else 'decrypt'
            break
        print("Invalid choice. Please enter 'E' or 'D'.")

    message = input("Enter the message: ")
    
    while True:
        try:
            key = int(input("Enter the shift key (an integer): "))
            break
        except ValueError:
            print("Invalid key. Please enter a whole number.")

    # Perform the operation
    final_output = caesar_cipher(message, key, mode)
    
    # Print result
    print(f"\nMode: {mode.capitalize()}")
    print(f"Shift Key: {key}")
    print(f"Original: {message}")
    print(f"Result: {final_output}")