import pygame as p
from Piece import Piece
from Board import Board
from Move import Move

class ChessEngine():
    def __init__(self, screen, clock, SQ_SIZE, DIMENSION, MAX_FPS):
        self.screen = screen
        self.clock = clock
        self.SQ_SIZE = SQ_SIZE
        self.DIMENSION = DIMENSION
        self.MAX_FPS = MAX_FPS
        self.board = None
        self.player_clicks = []
        self.sq_selected = ()
        self.moveMade = False
        self.run = True
        

    def create_game(self, SQ_SIZE = 80, DIMENSION = 8 ):
        self.board = Board(SQ_SIZE, DIMENSION)


    def play(self, AI = False):
        moves = []
        valid_moves = []
        if not(AI):
            while self.run:
                    for event in p.event.get():
                        if event.type == p.QUIT:
                            self.run = False
                        elif event.type == p.MOUSEBUTTONDOWN:
                            location = p.mouse.get_pos() #(x,y) location of mouse
                            col = location[0]//self.SQ_SIZE
                            row = location[1]//self.SQ_SIZE
                            if self.sq_selected == (row, col): # check if user click the same square twice
                                self.sq_selected = () # deselct the squares
                                self.player_clicks = [] # clear playerClicks
                            else:
                                self.sq_selected = (row, col)
                                self.player_clicks.append(self.sq_selected) # append for both and second clicks
                            if len(self.player_clicks) == 2: # after second clicks
                                move = Move(self.player_clicks[0],self.player_clicks[1],self.board.board)
                                if not moves:
                                    moves = self.board.get_all_moves()
                                if not valid_moves:
                                    valid_moves = self.board.get_valid_moves( moves )
                                for valid_move in valid_moves:
                                    if valid_move == move:
                                        self.board.make_move(move)
                                        self.board.movelog.append(move)
                                        self.moveMade = True
                                        moves = []
                                        valid_moves = []
                                        break
                                if self.moveMade:
                                    self.board.get_all_moves()
                                    self.moveMade = False
                                    self.sq_selected = () # reset user clicks
                                    self.player_clicks = []
                                else:
                                    self.player_clicks = [self.sq_selected]
                        elif event.type == p.KEYDOWN:
                            if event.key == p.K_z:
                                self.board.undo_move()
                    self.clock.tick(self.MAX_FPS)
                    if self.sq_selected:
                        self.board.highlight(self.sq_selected)
                        self.board.highlight_move(self.sq_selected)
                    self.board.draw(self.screen)
                    self.board.draw_moves(self.screen)
                    p.display.flip()









    