class Matrix(object):

    def __init__(self, matrix_string):
        split_lines = matrix_string.splitlines()
        self.__matrix_row = [[int(i) for i in row.split()] for row in split_lines]
        self.__matrix_column = [list(column) for column in zip(*self.__matrix_row)]

    def row(self, index):
        return self.__matrix_row[index-1].copy()

    def column(self, index):
        return self.__matrix_column[index-1].copy()
