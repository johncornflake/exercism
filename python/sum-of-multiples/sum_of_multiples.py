def sum_of_multiples(limit, multiples):
    multiples = [m for m in multiples if m > 0]
    res = [n for n in range(1,limit) if len([i for i in multiples if n % i == 0])]

    return sum(res)
