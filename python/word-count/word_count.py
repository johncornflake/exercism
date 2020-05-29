import re

def count_words(sentence):
    res = {}
    words = [w.lower() for w in re.findall(r"[a-zA-Z0-9]+(?:'\w)?", sentence) if w]
    [res.update({word: words.count(word)}) for word in words]

    return res
