import functools
import operator
from money import Money


class Portfolio():
    def __init__(self, *moneys):
        self.moneys = []

    def add(self, *moneys):
        self.moneys.extend(moneys)

    def evaluate(self, currency):
        total = functools.reduce(operator.add, map(lambda m: m.amount, self.moneys))
        return Money(total, currency)