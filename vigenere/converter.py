
def vigenere_encrypt(plaintext, keyword):
    cipher_text = []
    keyword = keyword.upper()
    plaintext = plaintext.upper()
    
    for i in range(len(plaintext)):
        if plaintext[i].isalpha():
            shift = ord(keyword[i % len(keyword)]) - ord('A')
            encrypted_char = chr((ord(plaintext[i]) - ord('A') + shift) % 26 + ord('A'))
            cipher_text.append(encrypted_char)
        else:
            cipher_text.append(plaintext[i])
    return ''.join(cipher_text)

with open('vigenere_input.txt', 'r') as file:
    lines = file.read().splitlines()
    plaintext = lines[0]
    keyword = lines[1]

ciphertext = vigenere_encrypt(plaintext, keyword)
with open('vigenere_output.txt', 'w') as file:
    file.write(ciphertext)
