import unittest
import FizzBuzz
from SoundNumber import SoundNumber
from random import randint
import SoundNumberEvaluator


class TestStringMethods(unittest.TestCase):

    def test_three_return_fizz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(3), 'fizz')

    def test_five_return_buzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(5), 'buzz')

    def test_fifteen_is_fizzbuzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(15), 'fizzbuzz')

    def test_all_three_multiple_are_fizz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(
            self.rand_multiple(3, 'buzz')), 'fizz')

    def test_all_five_multiple_are_buzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(
            self.rand_multiple(5, 'fizz')), 'buzz')

    def test_all_fifteen_multiple_are_fizzbuzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(
            randint(1111, 9999) * 15), 'fizzbuzz')

    def test_onehundredthree_is_fizz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(103), 'fizz')

    def test_onehundredthirtyfour_is_fizz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(134), 'fizz')

    def test_thirteen_is_fizz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(13), 'fizz')

    def test_onehundredfiftyfour_is_buzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(154), 'buzz')

    def test_eleven_not_fizz_not_buzz(self):
        self.assertEqual(FizzBuzz.return_number_or_fizz_buzz(11), 11)

    def rand_multiple(self, number, no_type):
        rand_multiple = randint(1111, 9999) * number
        if (no_type == 'fizz' and SoundNumberEvaluator.is_sound_number(rand_multiple, 3)) or (
                no_type == 'buzz' and SoundNumberEvaluator.is_sound_number(rand_multiple, 5)):
            return self.rand_multiple(number, no_type)
        return rand_multiple


if __name__ == '__main__':
    unittest.main()
