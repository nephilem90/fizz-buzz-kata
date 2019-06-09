class FizzBuss:

    def return_number_or_fizz_buzz(self, number):
        return_value = number
        if self.is_fizz(number) and self.is_buzz(number):
            return_value = 'fizzbuzz'
        elif self.is_fizz(number):
            return_value = 'fizz'
        elif self.is_buzz(number):
            return_value = 'buzz'
        return return_value

    def is_fizz(self, number):
        return self.contain(number, 3) or self.is_multiple(number, 3)

    def is_buzz(self, number):
        return self.is_multiple(number, 5) or self.contain(number, 5)

    def contain(self, number, must_contains):
        unit = number % 10
        if number == must_contains or unit == must_contains:
            return True
        elif number > 10:
            return self.contain((number - unit) / 10, must_contains)
        return False

    @staticmethod
    def is_multiple(number, multiple_of):
        return (number % multiple_of) == 0
