# addmitedly, I came up with an awful solution initially before googling and finding
# a more elegant solution here: https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
def primes(limit):
    s = datetime.now()
    prime = [True for i in range(limit+1)]
    p = 2
    while (p*p <= limit):
        if prime[p] == True:
            for i in range(p*2, limit+1, p):
                prime[i] = False
        p+=1

    res = [p for p in range(2, limit+1) if prime[p] == True]

    return res
