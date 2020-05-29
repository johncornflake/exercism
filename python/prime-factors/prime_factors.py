from math import sqrt

def factors(value):
    prime_factors = []
    current = value
    while current % 2 == 0:
        prime_factors.append(2),
        current /= 2

    for i in range(3, int(sqrt(current))+1, 2):
        while current % i == 0:
            prime_factors.append(int(i)),
            current /= i

    if current > 2: prime_factors.append(int(current))

    return prime_factors
