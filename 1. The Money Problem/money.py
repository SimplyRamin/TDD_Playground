class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def __str__(self):
        return f'{self.currency} {self.amount:.2f}'

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, denominator):
        if denominator != 0:
            return Money(self.amount / denominator, self.currency)
        else:
            print('Division by Zero')
