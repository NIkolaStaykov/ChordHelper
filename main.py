import random
import msvcrt
from enum import Enum


class Strings(Enum):
    E = 1
    A = 2
    D = 3
    G = 4
    B = 5
    e = 6


notes = ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']


class ChordGenerator:
    def __init__(self):
        pass

    @staticmethod
    def generate_note():
        return random.choice(notes)

    @staticmethod
    def generate_string():
        return random.choice(list(Strings))


if __name__ == '__main__':
    while True:
        # Wait for user to press a button
        key = msvcrt.getch().decode('ASCII')
        if key == 'q':  # ESC
            break
        print(str(ChordGenerator.generate_string().value) + ' ' + ChordGenerator.generate_note())
