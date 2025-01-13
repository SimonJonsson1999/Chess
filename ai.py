from Piece import *
import random
class AI():
    def __init__(self):
        pass

    def choose_move(self, valid_moves):
        return random.choice(valid_moves)