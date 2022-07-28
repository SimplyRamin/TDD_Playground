import unittest
from portfolio import Portfolio
from money import Money
from bank import Bank


class Test_Money(unittest.TestCase):
    def setUp(self):
        self.bank = Bank()
        self.bank.addExchangeRate('EUR', 'USD', 1.2)
        self.bank.addExchangeRate('USD', 'KRW', 1100)

    def test_Multiplication(self):
        ten_euros = Money(10, 'EUR')
        twenty_euros = Money(20, 'EUR')
        self.assertEqual(twenty_euros, ten_euros.times(2))
        self.assertEqual('EUR', twenty_euros.currency)

    def test_DivideMoney(self):
        korean_money = Money(4002, 'KRW')
        korean_money = korean_money.divide(4)
        expected_money = Money(1000.5, 'KRW')
        self.assertEqual(korean_money.amount, expected_money.amount)
        self.assertEqual(korean_money.currency, expected_money.currency)

    def test_Addition(self):
        five_dollars = Money(5, 'USD')
        ten_dollars = Money(10, 'USD')
        fifteen_dollars = Money(15, 'USD')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteen_dollars, portfolio.evaluate(self.bank, 'USD'))

    def test_AdditionOfDollarAndEuro(self):
        five_dollars = Money(5, 'USD')
        ten_euros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, 'USD')
        actual_value = portfolio.evaluate(self.bank, 'USD')
        self.assertEqual(expected_value, actual_value, f'{expected_value} != {actual_value}')

    def test_AdditionDollarsWons(self):
        one_dollar = Money(1, 'USD')
        eleven_hundered_won = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundered_won)
        expected_value = Money(2200, 'KRW')
        actual_value = portfolio.evaluate(self.bank, 'KRW')
        self.assertEqual(expected_value, actual_value, f'{expected_value} != {actual_value}')

    def test_MissingExchangeRate(self):
        one_dollar = Money(1, 'USD')
        one_euro = Money(1, 'EUR')
        one_won = Money(1, 'KRW')
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(Exception,
                                    r'Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]',):
            portfolio.evaluate(self.bank, 'Kalganid')

    def test_ConversionWithDifferentRatesBetweenTwoCurrencies(self):
        bank = Bank()
        bank.addExchangeRate('EUR', 'USD', 1.2)
        ten_euros = Money(10, 'EUR')
        self.assertEqual(bank.convert(ten_euros, 'USD'), Money(12, 'USD'))

        self.bank.addExchangeRate('EUR', 'USD', 1.3)
        self.assertEqual(self.bank.convert(ten_euros, 'USD'), Money(13, 'USD'))

    def test_ConversionWithMissingExchangeRate(self):
        bank = Bank()
        ten_euros = Money(10, 'EUR')
        with self.assertRaisesRegex(Exception, 'EUR->Kalganid'):
            bank.convert(ten_euros, 'Kalganid')

    def test_WhatIsTheConversionRateFromEURToUSD(self):
        ten_euros = Money(10, 'EUR')
        self.assertEqual(self.bank.convert(ten_euros, 'USD'), Money(12, 'USD'))


if __name__ == '__main__':
    unittest.main()
