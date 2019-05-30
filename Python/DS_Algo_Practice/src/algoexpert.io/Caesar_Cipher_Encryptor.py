# https://www.algoexpert.io/questions/Caesar%20Cipher%20Encryptor

# Solution 1

def caesar_cipher_encryptor(string, key):
    new_letters = []
    new_key = key % 26
    for letters in string:
        new_letters.append(get_new_letter(letters, string))
    return "".join(new_letters)

def get_new_letter(letter, key):
    newLetterCode = ord(letter) + key
    return chr(newLetterCode) if newLetterCode <= 122 else chr(96 + newLetterCode % 122)