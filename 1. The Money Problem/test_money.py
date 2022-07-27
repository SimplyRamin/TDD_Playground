import unittest
from portfolio import Portfolio
from money import Money


class Test_Money(unittest.TestCase):
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
        self.assertEqual(fifteen_dollars, portfolio.evaluate('USD'))

    def test_AdditionOfDollarAndEuro(self):
        five_dollars = Money(5, 'USD')
        ten_euros = Money(10, 'EUR')
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, 'USD')
        actual_value = portfolio.evaluate('USD')
        self.assertEqual(expected_value, actual_value, f'{expected_value} != {actual_value}')

    def test_AdditionDollarsWons(self):
        one_dollar = Money(1, 'USD')
        eleven_hundered_won = Money(1100, 'KRW')
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundered_won)
        expected_value = Money(2200, 'KRW')
        actual_value = portfolio.evaluate('KRW')
        self.assertEqual(expected_value, actual_value, f'{expected_value} != {actual_value}')

    def test_MissingExchangeRate(self):
        one_dollar = Money(1, 'USD')
        one_euro = Money(1, 'EUR')
        one_won = Money(1, 'KRW')
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(Exception,
                                    r'Missing exchange rate\(s\):\[USD\->Kalganid,EUR->Kalganid,KRW->Kalganid]',):
            portfolio.evaluate('Kalganid')


if __name__ == '__main__':
    unittest.main()
