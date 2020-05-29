def checkNum(number):
    if number not in range(1,65):
        raise ValueError("Number not between 1 and 64")

def square(number):
    checkNum(number)
    return 2 ** (number - 1)

def total(number, total=0):
    checkNum(number)
    for n in range(number):
        total += square(n+1)
    return total
