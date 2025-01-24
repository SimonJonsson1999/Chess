import pygame as p
from Piece import Piece
from Board import Board
from Move import Move
from ChessEngine import ChessEngine
WIDTH = HEIGHT = 640
DIMENSION = 8 
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

class ChessGame():
    def __init__(self):
        self.screen = p.display.set_mode((WIDTH, HEIGHT)) 
        self.screen.fill(p.Color("Black"))
        self.clock = clock = p.time.Clock()
        self.chess_engine = ChessEngine(self.screen, clock, SQ_SIZE, DIMENSION, MAX_FPS)

    def play(self):
        self.chess_engine.create_game()
        self.chess_engine.play(AI=False, ai_vs_ai=False, online=True)  




def main():

    game = ChessGame()
    game.play()
    


if __name__ == "__main__":
    main()
