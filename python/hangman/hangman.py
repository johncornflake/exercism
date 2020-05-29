# Game status categories
# Change the values as you see fit
STATUS_WIN = "Winner!"
STATUS_LOSE = "Loser!"
STATUS_ONGOING = "You have 9 guesses left."

class Hangman:
    def __init__(self, word):
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = '_' * len(word)
        self.secret_word = word
        self.guesses = []

    def guess(self, char):
        if self.status != STATUS_ONGOING: raise ValueError('The game is over.')
        hits = [p for p, c in enumerate(self.secret_word) if c == char]
        hit = len(hits) > 0 and char not in self.guesses
        res = [self.secret_word[i] if i in hits else e for i, e in enumerate(self.masked_word)]
        self.masked_word = ''.join(res)
        self.register_turn(char, hit)

    def get_masked_word(self):
        return self.masked_word

    def get_status(self):
        return self.status

        return self.status

    def register_turn(self, char, hit):
        if hit != True: self.remaining_guesses -= 1
        self.guesses.append(char)
        STATUS_ONGOING = f'You have {self.remaining_guesses} guesses left.'
        if '_' not in self.masked_word: self.status = STATUS_WIN
        if self.remaining_guesses < 0: self.status = STATUS_LOSE
