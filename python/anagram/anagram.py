def find_anagrams(word, candidates):
    matches = []
    for c in candidates:
        if word.lower() != c.lower() and sorted(c.lower()) == sorted(word.lower()):
            matches.append(c)

    return matches
