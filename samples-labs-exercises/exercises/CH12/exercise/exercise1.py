import unittest
from dvdlib2 import Customer, Movie, Rental

class CustomerTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = Customer('test')
        movies = [Movie('ABC', Movie.NEW_RELEASE), Movie('XYZ', Movie.REGULAR), Movie('123', Movie.CHILDRENS)]
        for movie in movies:
            self.customer.add_rental(Rental(movie, 7))

    def test_statement(self):
        statement = self.customer.statement()
        self.assertTrue(
            'ABC	21' in statement and
            'XYZ	9.5' in statement and
            '123	7.5' in statement and
            'Amount owed is 38.0' in statement and
            'You earned 4 frequent renter points' in statement
        )
