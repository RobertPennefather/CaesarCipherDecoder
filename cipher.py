import argparse
import random


def encrypt(plainText, shift=-1):

    #Allow zero to test base case
    if shift < 0 or 26 < shift:
        shift = random.randint(1, 26)
    print(shift)
    plainText = plainText.upper()
    plainTextArray = list(plainText)
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    for i in range(0, len(plainTextArray)):
        char = plainTextArray[i]
        index = alphabet.find(char)
        index = (index + shift) % len(alphabet)
        plainTextArray[i] = alphabet[index]

    cipherText = "".join(plainTextArray)
    return cipherText

if __name__ == "__main__":

    #Arguments
    parser = argparse.ArgumentParser(description='Encrypts or Decrypts text')
    parser.add_argument('plainText', help='text to encrypt')
    parser.add_argument('-s', '--shift', help='shift')
    args = parser.parse_args()
    
    cipherText = encrypt(args.plainText)
    print(cipherText)