class FizzBuss:

    def __init__(self, number):
        self.number = number

    def return_number_or_fizz_buzz(self):
        return_value = self.number
        if self.is_fizz() and self.is_buzz():
            return_value = 'fizzbuzz'
        elif self.is_fizz():
            return_value = 'fizz'
        elif self.is_buzz():
            return_value = 'buzz'
        return return_value

    def is_fizz(self):
        if (self.number % 3) == 0:
            return True
        return False

    def is_buzz(self):
        if (self.number % 5) == 0:
            return True
        return False
