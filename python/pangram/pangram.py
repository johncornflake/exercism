

def is_pangram(sentence):
    lower_sentence = sentence.lower()
    alpha_list = [c for c in lower_sentence if c.isalpha()]
    character_count = len(set(alpha_list))
    return True if character_count == 26 else False
