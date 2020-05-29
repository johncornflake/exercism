from random import randint

class Character:

    def __init__(self):
        self.abilities = ('strength', 'dexterity', 'constitution',
                         'intelligence', 'wisdom', 'charisma')

        for a in self.abilities:
            self.__setattr__(a, self.ability())

        self.hitpoints = 10 + modifier(self.constitution)

    def ability(self):
        rolls = sorted([randint(1,6) for i in range(4)], reverse=True)
        ability_points = sum(rolls[:3])

        return ability_points

def modifier(constitution):
    return int((constitution - 10) // 2)
