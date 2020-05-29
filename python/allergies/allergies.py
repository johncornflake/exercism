class Allergies:
    allergens = {
        "eggs": 1,
        "peanuts": 2,
        "shellfish": 4,
        "strawberries": 8,
        "tomatoes": 16,
        "chocolate": 32,
        "pollen": 64,
        "cats": 128,
    }

    def __init__(self, score):
        self.score = score
        self.allergens = [i for i in self.allergens if score & self.allergens[i]]

    def allergic_to(self, item):
        return item in self.allergens

    @property
    def lst(self):
        return self.allergens

allergens = {
    "eggs": 1,
    "peanuts": 2,
    "shellfish": 4,
    "strawberries": 8,
    "tomatoes": 16,
    "chocolate": 32,
    "pollen": 64,
    "cats": 128,
}

x = [i for i in allergens if 3 & allergens[i]]

score = 255
for i in allergens:
    #print(i, ':', allergens[i])
    print(i, '-', '128', '&', allergens[i], ': ', score & allergens[i])

print('\nbitshift right\n')

for i in range(0,8):
    print(score>>i, ' ||| ', bin(score>>i))

# print('\nbitshift left\n')
#
# x = 3
# for i in range(0,16):
#     print(x<<i, ' ||| ', bin(x<<i))
