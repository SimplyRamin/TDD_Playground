import unittest
import functools
import operator


class Money():
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, denominator):
        if denominator != 0:
            return Money(self.amount / denominator, self.currency)
        else:
            print('Division by Zero')


class Portfolio():
    def __init__(self, *moneys):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(operator.add, map(lambda m: m.amount, self.moneys))
        return Money(total, currency)


class TestMoney(unittest.TestCase):
    def testMultiplicationInDollars(self):
        ten_dollars = Money(10, 'USD')
        twenty_dollars = Money(20, 'USD')
        self.assertEqual(twenty_dollars, ten_dollars.times(2))
        self.assertEqual('USD', twenty_dollars.currency)

    def testMultiplicationInEuros(self):
        ten_euros = Money(10, 'EUR')
        twenty_euros = Money(20, 'EUR')
        self.assertEqual(twenty_euros, ten_euros.times(2))
        self.assertEqual('EUR', twenty_euros.currency)

    def testDivideMoney(self):
        korean_money = Money(4002, 'KRW')
        korean_money = korean_money.divide(4)
        expected_money = Money(1000.5, 'KRW')
        self.assertEqual(korean_money.amount, expected_money.amount)
        self.assertEqual(korean_money.currency, expected_money.currency)

    def testAddition(self):
        five_dollars = Money(5, 'USD')
        ten_dollars = Money(10, 'USD')
        fifteen_dollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteen_dollars, portfolio.evaluate('USD'))


if __name__ == '__main__':
    unittest.main()
