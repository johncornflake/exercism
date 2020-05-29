def test_if_triangle(sides):
    if 0 in sides: return False
    side_sums = [sum(sides) - i for i in sides]
    for s in sides:
        for summed in side_sums:
            if s >= summed: return False

@test_if_triangle
def equilateral(sides):
    #if test_if_triangle(sides) == False: return False
    return len(set(sides)) == 1

@test_if_triangle
def isosceles(sides):
    #if test_if_triangle(sides) == False: return False
    return len(set(sides)) <= 2

@test_if_triangle
def scalene(sides):
    #if test_if_triangle(sides) == False: return False
    return len(set(sides)) == 3
