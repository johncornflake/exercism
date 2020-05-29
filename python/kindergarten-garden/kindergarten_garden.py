'''
I noticed every solution used a default students list, but I tried to do something
a little different and still satisfy the criteria, so I used string.ascii_lowercase.index
instead.
'''

import string

class Garden:
    def __init__(self, diagram, students=[]):
        self.students = sorted(students)
        self.plant_map = {'R': 'Radishes',
                          'G': 'Grass',
                          'C': 'Clover',
                          'V': 'Violets'}

        self.student_plants = self.parse_plants(diagram)

    def plants(self, student):
        if student in self.students:
            i = self.students.index(student)
        else:
            i = string.ascii_lowercase.index(student[0].lower())

        return self.student_plants[i]

    def parse_plants(self, diagram):
        diagram = diagram.split('\n')
        split_plants = [''.join([row[i:i+2] for row in diagram])
                        for i in range(0, len(diagram[0]), 2)]

        return [[self.plant_map.get(k) for k in p] for p in split_plants]
