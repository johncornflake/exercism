import random
import string

class Robot(object):
    def __init__(self):
        self.name = self.reset()
        self.reset()

    def reset(self):
        self.name = self.generate_name()

    def generate_name(self):
        letters = random.choices(string.ascii_uppercase, k=2)
        numbers = random.choices(string.digits, k=3)
        return ''.join(letters + numbers)
