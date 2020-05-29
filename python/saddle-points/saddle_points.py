def saddle_points(matrix):
    if len(set([len(i) for i in matrix])) != 1 and len(matrix) != 0:
        raise ValueError('Irregular matrix given')
    cols = [i for i in zip(*matrix)]
    saddles = []
    for row_num, row in enumerate(matrix):
        for col_num, val in enumerate(row):
            row_check = all(val >= x for x in row)
            col_check = all(val <= x for x in cols[col_num])
            if row_check == col_check == True:
                saddles.append({'row': row_num+1, 'column': col_num+1})

    return [{}] if len(saddles) == 0 else saddles
