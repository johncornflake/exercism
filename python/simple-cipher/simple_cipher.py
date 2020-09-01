import string
from collections import deque
import math
import secrets

class Cipher:
    def __init__(self, key=None):
        self.key = key
        self.key_list = None

    def encode(self, text):
        pairs = self.getPairs(text)
        return self.rotater(pairs, decode=False)

    def decode(self, text):
        pairs = self.getPairs(text)
        return self.rotater(pairs, decode=True)

    def getCipher(self, text_length):
        alphabet = self.generateAlphabet()
        if self.key_list:
            return self.key_list
        elif self.key:
            multiplier = math.ceil(text_length / len(self.key))
            return [alphabet.index(i) for i in list(self.key)] * multiplier
        else:
            random_cipher = [secrets.choice(alphabet) for i in range(0,len)]
            multiplier = math.ceil(text_length / len(random_cipher))
            return random_ciper * multiplier

    def generateAlphabet(self):
        return deque([letter for letter in string.ascii_lowercase])

    def rotater(self, pairs, decode=False):
        alphabet = self.generateAlphabet()
        res = ''
        print(pairs)
        for pair in pairs:
            alphabet.rotate(alphabet.index(pair[0]) * -1)
            if decode:
                alphabet.rotate(pair[1])
                res += alphabet[0]
            else:
                res += alphabet[pair[1]]

        return res

    def getPairs(self, text):
        key_list = self.getCipher(len(text))
        return list(zip(list(text), key_list))

'''
TO DO:
    - Need to auto-generate cipher. Keylist should probably not be an attribute since it's only used for rotater, just pass it around.
'''
