def value(colors):
    codes =  'black brown red orange yellow green blue violet grey white'.split()
    return int(''.join([str(codes.index(c)) for c in colors[:2]]))
