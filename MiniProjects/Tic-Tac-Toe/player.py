import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class RandomCompPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        move = random.choice(game.available_moves())
        return move

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        is_valid = False
        move = None
        while not is_valid:
            square = input(f"{self.letter}'s turn. Enter the square you want to play(1-9): ")
            try:
                move = int(square) - 1
                if move not in game.available_moves():
                    raise ValueError
                is_valid = True
            except ValueError:
                print("Enter a valid square.")
        return move



