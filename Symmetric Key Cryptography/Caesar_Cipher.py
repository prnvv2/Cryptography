# Function to encrypt text using the Caesar cipher
def caesar_cipher(text, shift):
    result = ""  # Initialize an empty string to store the encrypted text
    
    for char in text:  # Iterate over each character in the input text
        if char.isalpha():  # Check if the character is a letter (ignores spaces, numbers, etc.)
            # Determine the ASCII base for the shift (uppercase 'A' or lowercase 'a')
            if char.isupper(): # Check if the character is Uppercase
                shift_base = ord('A')
            else:  # check if the character is lowercase 
                shift_base = ord('a')

            
            # Apply the Caesar cipher formula:
            # - Convert the character to its ASCII number using ord()
            # - Shift it by the given amount
            # - Ensure it wraps around within the alphabet using modulo 26
            # - Convert it back to a character using chr()
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Keep non-alphabet characters unchanged (e.g., spaces, punctuation)

    return result  # Return the encrypted (or decrypted) text

# Function to decrypt text by reversing the shift
def decrypt_caesar_cipher(text, shift):
    return caesar_cipher(text, -shift)  # Call the encryption function with a negative shift

# Usage
text = {Enter the text you want to encrypt in string format}  # Original message eg: "HELLO WORLD"
shift = {Enter the numeric shift value}   # Shift value for encryption eg: 3

# Encrypt the text
encrypted = caesar_cipher(text, shift)

# Decrypt the text
decrypted = decrypt_caesar_cipher(encrypted, shift)

# Display the results
print("Encrypted:", encrypted)  # Output: KHOOR ZRUOG
print("Decrypted:", decrypted)  # Output: HELLO WORLD
