'''
from collections import defaultdict seems to be the most commonly used for the
highest rated solutions. why is that?
'''
class School:
    def __init__(self):
        self.students = dict([(g, []) for g in range(1,13)])

    def add_student(self, name, grade):
        self.students[grade].append(name)

    def roster(self):
        return [y for x in self.students.values() for y in sorted(x)]

    def grade(self, grade_number):
        return sorted(self.students[grade_number])
