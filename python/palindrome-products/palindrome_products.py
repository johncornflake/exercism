from functools import reduce
import operator

def largest(min_factor, max_factor):
    if min_factor > max_factor: raise ValueError('min greater than max.')
    pals = palindromes(min_factor, max_factor)
    if not pals:
        return [None, []]
    else:
        max_pal = pals[-1][0]
        return [max_pal, [p[1] for p in pals if p[0] == max_pal]]

def smallest(min_factor, max_factor):
    if min_factor > max_factor: raise ValueError('min greater than max.')
    pals = palindromes(min_factor, max_factor)
    if not pals:
        return [None, []]
    else:
        min_pal = [] if not pals else pals[0][0]
        return [min_pal, [p[1] for p in pals if p[0] == min_pal]]

def products(min_factor, max_factor):
    l = list(range(min_factor, max_factor+1))
    product_lists = [[[i, x] for x in l] for i in l]
    return tuple([sorted(val) for sublist in product_lists for val in sublist])

def palindromes(min_factor, max_factor):
    prods = products(min_factor, max_factor)
    pals = []
    for p in prods:
        m = multiply_pairs(p)
        if str(m) == str(m)[::-1]: pals.append((m, p))

    return sorted(pals, key=lambda x: x[0])

def multiply_pairs(int_list):
    return reduce(operator.mul, int_list, 1)
