# caesar_cipher.py
"""
Task 1 - Caesar Cipher
Author: [Your Name]
Description: This program allows users to encrypt and decrypt messages using the Caesar Cipher technique.
"""

def caesar_encrypt(text, shift):
    """Encrypt the text by shifting letters by 'shift' positions."""
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def caesar_decrypt(text, shift):
    """Decrypt the text by reversing the shift."""
    return caesar_encrypt(text, -shift)

def main():
    print("=== Caesar Cipher Program ===")
    choice = input("Type 'e' to Encrypt or 'd' to Decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Please select 'e' or 'd'.")
        return

    message = input("Enter your message: ")
    try:
        shift = int(input("Enter the shift value (e.g., 3): "))
    except ValueError:
        print("Invalid shift value. Must be an integer.")
        return

    if choice == 'e':
        encrypted = caesar_encrypt(message, shift)
        print(f"Encrypted Message: {encrypted}")
    else:
        decrypted = caesar_decrypt(message, shift)
        print(f"Decrypted Message: {decrypted}")

if __name__ == "__main__":
    main()
