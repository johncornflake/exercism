import math
def triplets_with_sum(number):
    res = []
    for b in range(number):
        for a in range(1, b):
            c = math.sqrt(a**2 + b**2)
            if c % 1 == 0 and sum([a,b,c]) == number:
                res.append([a, b, int(c)])

    return res
