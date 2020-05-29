# Score categories.
# Change the values as you see fit.
YACHT = lambda x: 50 if len(set(x)) == 1 else 0
ONES = lambda x: sum([i for i in x if i == 1])
TWOS = lambda x: sum([i for i in x if i == 2])
THREES = lambda x: sum([i for i in x if i == 3])
FOURS = lambda x: sum([i for i in x if i == 4])
FIVES = lambda x: sum([i for i in x if i == 5])
SIXES = lambda x: sum([i for i in x if i == 6])
FULL_HOUSE = lambda x: sum(x) if len(set(x)) == 2 \
                       and x.count(x[0]) in (3,2) else 0
FOUR_OF_A_KIND = lambda x: 4 * x[0] if x.count(x[0]) >= 4 \
                           else (4 * x[1] if x.count(x[1]) >= 4 else 0)
LITTLE_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and sorted(x)[-1] == 5 else 0
BIG_STRAIGHT = lambda x: 30 if len(set(x)) == 5 and sorted(x)[-1] == 6 \
                         and 1 not in x else 0
CHOICE = lambda x: sum(x)


def score(dice, category):
    return category(dice)
