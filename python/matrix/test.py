from matrix import Matrix

m = Matrix('1 2\n3 4')
print(m.row(1))
r = m.row(1)
print(m.row(1))
r[0] = 9
print(m.row(1))
