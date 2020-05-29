import re

def abbreviate(words):
    split_words = re.split(r'[^a-zA-Z\']', words)
    return ''.join([w[0].upper() for w in split_words if w])
