import unittest
from models import quotes
Quotes = quotes.Quotes

class QuoteTest(unittest.TestCase):
    def setUp(self):
        self.new_quote = Quotes('Manasseh','Life is a journey')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_quote,Quotes))

if __name__ == '__main':
    unittest.main()