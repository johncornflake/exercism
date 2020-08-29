import re
def response(hey_bob):
    is_question = hey_bob.strip().endswith('?')
    is_caps = hey_bob.isupper()
    if is_caps and is_question:
        return "Calm down, I know what I'm doing!"
    if is_question and not is_caps:
        return "Sure."
    elif is_caps:
        return "Whoa, chill out!"
    elif not hey_bob.strip():
        return 'Fine. Be that way!'
    else:
        return 'Whatever.'
