import unittest
from main import currency_rates


class TestStringMethods(unittest.TestCase):

    def test_right_args(self):
        self.assertEqual(currency_rates('USD', '2021-10-08'), 'USD (Доллар США): 72,2854')

    def test_bad_date_format(self):
        self.assertEqual(currency_rates('USD', '2021-10-089'), 'Введите дату в формате YYYY-MM-DD')

    def test_not_found_date_record(self):
        self.assertEqual(currency_rates('USD', '2025-10-08'), 'На введенную дату нет информации')

    def test_bad_currency_name(self):
        self.assertEqual(currency_rates('USDddddd', '2021-10-08'), 'Невозможно найти введенную валюту')


if __name__ == '__main__':
    unittest.main()
