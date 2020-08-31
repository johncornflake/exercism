import string
from collections import deque
import math

class Cipher:
    def __init__(self, key=None):
        self.alphabet = deque([letter for letter in string.ascii_lowercase])

    def encode(self, text):
        pass

    def decode(self, text):
        pass

alphabet = deque([letter for letter in string.ascii_lowercase])
key = 'abcdefghij' #1,2, [1,2,1,2,1]
input = 'zzzzzzzzzz'
expected_output = 'zabcdefghi'

input_list = list(input)
print(input_list)


alphabet = deque([letter for letter in string.ascii_lowercase])
key_adj = [alphabet.index(c) for c in key] * math.ceil(len(input) / len(key))
input_list = list(input)
pairs = list(zip(input_list, key_adj))


print(pairs)

# encode
res = ''
for p in pairs:
    alphabet.rotate(alphabet.index(p[0]) * -1)
    res += alphabet[p[1]]

print(res)

x = Cipher()
print(x.alphabet)
