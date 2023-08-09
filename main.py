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
        key = msvcrt.getch()
        if key == b'\x00' or key == b'\xe0':  # Special keys
            key = msvcrt.getch()
        key = key.decode('utf-8')

        if key == 'q':  # If q is pressed, quit
            break
        print(str(ChordGenerator.generate_string().value) + ' ' + ChordGenerator.generate_note())
