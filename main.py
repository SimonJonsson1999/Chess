import pygame as p
from Piece import Piece
from Board import Board
from Move import Move
from ChessEngine import ChessEngine


WIDTH = HEIGHT = 640
DIMENSION = 8 #8 by 8 board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15

def main():
    p.init()
    p.font.init()
    screen = p.display.set_mode((WIDTH, HEIGHT)) #create the screen
    screen.fill(p.Color("Black"))
    clock = p.time.Clock() #create a clock
    chess_engine = ChessEngine(screen, clock, SQ_SIZE, DIMENSION, MAX_FPS)
    chess_engine.create_game()
    chess_engine.play(AI=False, ai_vs_ai=True)

if __name__ == "__main__":
    main()
