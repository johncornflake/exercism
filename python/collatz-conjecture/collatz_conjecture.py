def steps(number, count=0):
    if number < 1: raise ValueError('You must use a positive integer')

    if number == 1:
        return count
    else:
        number =  number / 2 if number % 2 == 0 else (3 * number) + 1
        return steps(number, count+1)
