def is_paired(input_string):
    open = ['(', '[', '{']
    closed = [')', ']', '}']
    brackets = [c for c in list(input_string) if c in '(){}[]']
    if len(brackets) % 2 != 0: return False
    stack = []
    for b in brackets:
        if b in open:
            stack.append(b)
        elif len(stack) == 0:
            return False
        elif b == closed[open.index(stack[-1])]:
            stack.pop(-1)

    return len(stack) == 0
