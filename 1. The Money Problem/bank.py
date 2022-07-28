from money import Money


class Bank():
    def __init__(self):
        self.exchange_rates = {}

    def addExchangeRate(self, currency_from, currency_to, rate):
        key = f'{currency_from}->{currency_to}'
        self.exchange_rates[key] = rate

    def convert(self, aMoney, aCurrency):
        if aMoney.currency == aCurrency:
            return Money(aMoney.amount, aCurrency)

        key = f'{aMoney.currency}->{aCurrency}'
        if key in self.exchange_rates:
            return Money(aMoney.amount * self.exchange_rates[key], aCurrency)

        raise Exception(key)
