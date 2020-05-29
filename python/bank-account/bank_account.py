from multiprocessing import Pool

class BankAccount(object):
    def __init__(self):
        self.is_open = False
        self.balance = 0

    def get_balance(self):
        self.test_open()
        return self.balance

    def open(self):
        if self.is_open == True:
            raise ValueError('Account is already open')
        else:
            self.is_open = True

    def deposit(self, amount):
        self.test_open()
        self.positive_int_test(amount)
        self.balance += amount

    def withdraw(self, amount):
        self.test_open()
        self.positive_int_test(amount)
        if amount > self.balance:
            raise ValueError('Not enough in balance to withdraw.')
        else:
            self.balance -= amount

    def close(self):
        if self.is_open == False:
            raise ValueError('Account is already closed.')
        else:
            self.is_open = False
            self.balance = 0

    def test_open(self):
        message = 'Account is closed and no actions can be made to it.'
        if self.is_open == False: raise ValueError(message)

    def positive_int_test(self, amount):
        if amount < 0: raise ValueError('Value must be positive')
