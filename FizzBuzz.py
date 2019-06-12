from SoundNumber import SoundNumber


def return_number_or_fizz_buzz(number):
    sound_number = SoundNumber()
    sound_number.add_sound_number('fizz', 3)
    sound_number.add_sound_number('buzz', 5)
    return sound_number.number_or_sound(number)
