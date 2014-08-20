"""
Testing the Vigener cipher.
"""

import math

def encrypt(message, key):
    new_letters = []
    if len(key) < len(message):
        key = key * int(math.ceil(len(message) / float(len(key))))
    for message_letter, key_letter in zip(message, key):
        new_num = (to_num(message_letter) + to_num(key_letter)) % 26
        new_letter = to_letter(new_num)
        new_letters.append(new_letter)
    return ''.join(new_letters)

def to_num(letter):
    return ord(letter.capitalize()) - ord('A')

def to_letter(num):
    return chr(num + ord('A') + 1)

if __name__ == "__main__":    
    print(encrypt("WHATANICEDAYTODAY", "CRYPTO"))
