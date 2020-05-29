class Phone(object):
    def __init__(self, phone_number):
        self.raw_nums = ''.join(c for c in str(phone_number) if c.isdigit())

        # logic check to make sure number is valid
        if len(self.raw_nums) not in (10,11): self.invalid()
        if self.raw_nums[-10:][0] in ('1', '0'): self.invalid()
        if self.raw_nums[-10:][3] in ('1', '0'): self.invalid()
        if len(self.raw_nums) == 11:
            if self.raw_nums[0] != '1': self.invalid()

        self.number = self.raw_nums[-10:]
        self.area_code = self.get_area_code(self.number)

    def pretty(self):
        ac = '(' + self.number[0:3] + ') '
        num = self.number[3:6] + '-' + self.number[-4:]
        return ac + num

    def get_area_code(self, number):
        return number[0:3]

    def invalid(self):
        raise ValueError('Invalid phone number supplied.')
