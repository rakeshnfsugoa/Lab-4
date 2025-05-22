# Program 2: Caesar Cipher
def caesar_encrypt(text, shift=3):
    encrypted = ''
    for char in text:
        if char.isupper():
            encrypted += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.islower():
            encrypted += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
        else:
            encrypted += char
    return encrypted

# Read names from file
with open('caesar_input.txt', 'r') as file:
    lines = file.read().splitlines()
    firstname = lines[0]
    lastname = lines[1]

plaintext = firstname + " " + lastname
ciphertext = caesar_encrypt(plaintext, shift=3)

# Write encrypted text to output file
with open('caesar_output.txt', 'w') as file:
    file.write(ciphertext)
