import string
from collections import deque
import math
import secrets

class Cipher:
    def __init__(self, key=None):
        self.key = key or self.generateCipher()

    def encode(self, text):
        pairs = self.getPairs(text)
        return self.rotater(pairs, decode=False)

    def decode(self, text):
        pairs = self.getPairs(text)
        return self.rotater(pairs, decode=True)

    def generateCipher(self):
        alphabet = self.generateAlphabet()
        return ''.join([secrets.choice(alphabet) for i in range(0, 10)])

    def generateAlphabet(self):
        return deque([letter for letter in string.ascii_lowercase])

    def rotater(self, pairs, decode=False):
        alphabet = self.generateAlphabet()
        res = ''
        for pair in pairs:
            alphabet.rotate(alphabet.index(pair[0]) * -1)
            if decode:
                alphabet.rotate(pair[1])
                res += alphabet[0]
            else:
                res += alphabet[pair[1]]

        return res

    def cipherList(self, text_length):
        alphabet = self.generateAlphabet()
        multiplier = math.ceil(text_length / len(self.key))
        return [alphabet.index(i) for i in list(self.key)] * multiplier

    def getPairs(self, text):
        key_list = self.cipherList(len(text))
        return list(zip(list(text), key_list))
