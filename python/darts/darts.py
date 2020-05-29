def score(x, y):
    # (radius, points)
    circles = [(1,10), (5,5), (10,1)]
    for c in circles:
        if (x**2 + y**2) <= c[0]**2: return c[1]

    # return 0 if none of the points are
    return 0
