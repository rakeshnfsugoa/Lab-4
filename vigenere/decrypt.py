def vigenere_decrypt(ciphertext, keyword):
    decrypted_text = []
    keyword = keyword.upper()
    ciphertext = ciphertext.upper()
    
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            decrypted_char = chr((ord(ciphertext[i]) - ord('A') - shift + 26) % 26 + ord('A'))
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(ciphertext[i])
    return ''.join(decrypted_text)

try:
  
    with open('vigenere_ciphertext.txt', 'r') as file:
        lines = file.read().splitlines()

    if len(lines) < 2:
        raise ValueError("File must contain at least two lines: ciphertext and keyword.")

    ciphertext = lines[0]
    keyword = lines[1]

    # Decrypt and write to output file
    plaintext = vigenere_decrypt(ciphertext, keyword)
    with open('vigenere_decrypted.txt', 'w') as file:
        file.write(plaintext)

    print("Decryption successful. Check 'vigenere_decrypted.txt'.")

except FileNotFoundError:
    print("Error: 'vigenere_ciphertext.txt' not found.")
except ValueError as ve:
    print("Error:", ve)
