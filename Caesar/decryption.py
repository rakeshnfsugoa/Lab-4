def caesar_decrypt(ciphertext, shift=3):
    decrypted = ''
    for char in ciphertext:
        if char.isupper():
            decrypted += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        elif char.islower():
            decrypted += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
        else:
            decrypted += char
    return decrypted

try:
    # Read ciphertext from file
    with open('todecrypt.txt', 'r') as file:
        lines = file.read().splitlines()

    # Decrypt each line
    decrypted_lines = [caesar_decrypt(line, shift=3) for line in lines]

    # Write decrypted text to output file
    with open('caesar_decrypted.txt', 'w') as file:
        for line in decrypted_lines:
            file.write(line + '\n')

    print("Decryption successful. Check 'caesar_decrypted.txt'.")

except FileNotFoundError:
    print("Error: 'caesar_ciphertext.txt' not found.")
