import SoundNumberEvaluator


class SoundNumber:

    def __init__(self):
        self.sound_number = []

    def add_sound_number(self, sound, number):
        self.sound_number.append({'sound': sound, 'number': number})

    def number_or_sound(self, number):
        return ''.join(
            x['sound'] for x in self.sound_number if SoundNumberEvaluator.is_sound_number(number, x['number']))
