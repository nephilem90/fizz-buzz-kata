import unittest
from FizzBuzz import FizzBuss
from random import randint


class TestStringMethods(unittest.TestCase):

    def test_tree_return_fizz(self):
        self.assertEqual(FizzBuss(3).return_number_or_fizz_buzz(), 'fizz')

    def test_five_return_buzz(self):
        self.assertEqual(FizzBuss(5).return_number_or_fizz_buzz(), 'buzz')

    def test_fifteen_is_fizzbuzz(self):
        self.assertEqual(FizzBuss(15).return_number_or_fizz_buzz(), 'fizzbuzz')

    def test_all_tree_multiple_are_fizz(self):
        self.assertEqual(FizzBuss(self.rand_multiple(3, 5)).return_number_or_fizz_buzz(), 'fizz')

    def test_all_five_multiple_are_buzz(self):
        self.assertEqual(FizzBuss(self.rand_multiple(5, 3)).return_number_or_fizz_buzz(), 'buzz')

    def test_all_fifteen_multiple_are_fizzbuzz(self):
        self.assertEqual(FizzBuss(randint(1111, 9999) * 15).return_number_or_fizz_buzz(), 'fizzbuzz')

    def rand_multiple(self, multiple_of, not_multiple_of):
        rand_multiple = randint(1111, 9999) * multiple_of
        if (rand_multiple % not_multiple_of) == 0:
            return self.rand_multiple(multiple_of, not_multiple_of)
        return rand_multiple


if __name__ == '__main__':
    unittest.main()
