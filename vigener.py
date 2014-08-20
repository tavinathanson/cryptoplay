"""
Testing the Vigener cipher.
"""

import math

def encrypt(message, key):
    new_letters = []
    key = expand_key(key, len(message))
    for message_letter, key_letter in zip(message, key):
        new_num = (to_num(message_letter) + to_num(key_letter)) % 26
        new_letter = to_letter(new_num)
        new_letters.append(new_letter)
    return ''.join(new_letters)

def decrypt(cipher, key):
    new_letters = []
    key = expand_key(key, len(cipher))
    for cipher_letter, key_letter in zip(cipher, key):
        new_num = (to_num(cipher_letter) - to_num(key_letter)) % 26
        new_letter = to_letter(new_num)
        new_letters.append(new_letter)
    return ''.join(new_letters)

def expand_key(key, length):
    if len(key) < length:
        return key * int(math.ceil(length / float(len(key))))
    return key

def to_num(letter):
    return ord(letter.capitalize()) - (ord('A') - 1)

def to_letter(num):
    # TODO Fix this hack
    if num == 0:
        return 'Z'
    return chr(num + ord('A') - 1)

if __name__ == "__main__":
    cipher = encrypt("WHATANICEDAYTODAY", "CRYPTO")
    print("Cipher: %s" % cipher)
    decrypted = decrypt(cipher, "CRYPTO")
    print("Decrypted: %s" % decrypted)
