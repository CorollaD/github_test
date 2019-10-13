

class SpeakingMan:

    def __init__(self, name):
        self.name = name

    def say(self, something):
        print(f'{self.name} says: {something}.')