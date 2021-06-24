import unittest
from cheque.model import tokenize
from cheque.model import translate_three_digits
from cheque.model import translate_full_amount


class TestTokenizeAmount(unittest.TestCase):
    def test_tokenize(self):
        self.assertEqual(
            tokenize('0'),
            {
                'Dollars': '0',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('4'),
            {
                'Dollars': '4',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('16'),
            {
                'Dollars': '16',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('247'),
            {
                'Dollars': '247',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('1024'),
            {
                'Thousand': '1',
                'Dollars': '024',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('12345'),
            {
                'Thousand': '12',
                'Dollars': '345',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('123456'),
            {
                'Thousand': '123',
                'Dollars': '456',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('1000001'),
            {
                'Million': '1',
                'Thousand': '000',
                'Dollars': '001',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('12312312'),
            {
                'Million': '12',
                'Thousand': '312',
                'Dollars': '312',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('123456789'),
            {
                'Million': '123',
                'Thousand': '456',
                'Dollars': '789',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('1234567890'),
            {
                'Billion': '1',
                'Million': '234',
                'Thousand': '567',
                'Dollars': '890',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('23232323232'),
            {
                'Billion': '23',
                'Million': '232',
                'Thousand': '323',
                'Dollars': '232',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('111222333444'),
            {
                'Billion': '111',
                'Million': '222',
                'Thousand': '333',
                'Dollars': '444',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('1222333444555'),
            {
                'Trillion': '1',
                'Billion': '222',
                'Million': '333',
                'Thousand': '444',
                'Dollars': '555',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('11222333444555'),
            {
                'Trillion': '11',
                'Billion': '222',
                'Million': '333',
                'Thousand': '444',
                'Dollars': '555',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('111222333444555'),
            {
                'Trillion': '111',
                'Billion': '222',
                'Million': '333',
                'Thousand': '444',
                'Dollars': '555',
                'Cents': '00'
            }
        )
        self.assertEqual(
            tokenize('1234567.89'),
            {
                'Million': '1',
                'Thousand': '234',
                'Dollars': '567',
                'Cents': '89'
            }
        )

# TODO: Replace translate_three_digits with translate_full_amount


class TestTranslateThreeDigits(unittest.TestCase):
    def test_translate_three_digits(self):
        self.assertEqual(
            translate_three_digits('123'),
            'One Hundred And Twenty Three'
        )
        self.assertEqual(
            translate_three_digits('404'),
            'Four Hundred And Four'
        )
        self.assertEqual(
            translate_three_digits('520'),
            'Five Hundred And Twenty'
        )
        self.assertEqual(
            translate_three_digits('300'),
            'Three Hundred'
        )


class TestTranslateFullAmount(unittest.TestCase):
    def test_translate_full_amount(self):
        self.assertEqual(
            translate_full_amount('1234567.89'),
            'One Million Two Hundred And Thirty Four Thousand Five Hundred '
            'And Sixty Seven Dollars And Eighty Nine Cents Only'
        )
        self.assertEqual(
            translate_full_amount('1000001'),
            'One Million One Dollars Only'
        )
        self.assertEqual(
            translate_full_amount('0.99'),
            'Ninety Nine Cents Only'
        )


if __name__ == '__main__':
    unittest.main()
