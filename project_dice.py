from random import randint

class Dice:
    def __init__(self, name):
        self.name = name

    def roll(self):
        print(f'{self.name} rolled ({randint(1, 6)}, {randint(1, 6)})')

player1 = Dice("Player1")
player1.roll()

player2 = Dice("Player2")
player2.roll()