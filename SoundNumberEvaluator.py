def contain(number, must_contains):
    if number == must_contains or unit(number) == must_contains:
        return True
    elif number > 10:
        return contain(decimal(number), must_contains)
    return False


def unit(number):
    return number % 10


def decimal(number):
    return (number - unit(number)) / 10


def is_multiple(number, multiple_of):
    return (number % multiple_of) == 0


def is_sound_number(number, sound_number):
    return is_multiple(number, sound_number) or contain(number, sound_number)
