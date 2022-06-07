

class Banker:
    def __init__(self, balance=0, shelved=0):
        self.balance = balance
        self.shelved = shelved
    def shelf(self, points):
        self.shelved = points
    def bank(self):
        self.balance = self.shelved
        self.clear_shelf()
    def clear_shelf(self):
        self.shelved = 0