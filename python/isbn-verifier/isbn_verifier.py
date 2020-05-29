def is_valid(isbn):
    isbn_splitter = lambda x: [i for i in x if (i.isdigit() or i == 'X')]
    split_isbn = isbn_splitter(isbn)
    multiplier = [len(split_isbn) - i for i in range(len(split_isbn))]
    sum_isbn = [(10 if a == 'X' else int(a))*b for a,b in zip(split_isbn, multiplier)]

    valid = ('X' not in split_isbn[:-1] \
                and len(split_isbn) in (10, 13) \
                and sum(sum_isbn) % 11 == 0)

    return valid
