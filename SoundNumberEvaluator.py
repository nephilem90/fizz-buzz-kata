def contain(number, must_contains):
    unit = number % 10
    if number == must_contains or unit == must_contains:
        return True
    elif number > 10:
        return contain((number - unit) / 10, must_contains)
    return False

def is_multiple(number, multiple_of):
    return (number % multiple_of) == 0

def is_sound_number(number, sound_number):
        return is_multiple(number, sound_number) or contain(number, sound_number)
