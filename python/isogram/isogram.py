def is_isogram(string):
    clean_string = [l for l in string.lower() if l.isalpha() == True]

    return len(set(clean_string)) == len(clean_string)
