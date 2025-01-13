import pygame as p
from Piece import Piece
from Board import Board
from Move import Move
import random
from ai import AI

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
        self.AI = AI()

        

    def create_game(self, SQ_SIZE = 80, DIMENSION = 8 ):
        self.board = Board(SQ_SIZE, DIMENSION)


    def play(self, AI = False, ai_vs_ai=False):
        moves = []
        valid_moves = []
        
        while self.run:
            self.handle_events(moves, valid_moves, AI)

            if ai_vs_ai:  
                if self.board.white_to_move:
                    self.ai_move()
                else:  
                    self.ai_move()

            
            elif AI and not self.board.white_to_move:
                self.ai_move()
            
            self.clock.tick(self.MAX_FPS)
            
            self.update_highlighting()
            self.board.draw(self.screen)
            self.board.draw_moves(self.screen)
            p.display.flip()
            self.check_for_winner()

    def handle_events(self, moves, valid_moves, AI):
        """Handles events such as quit, mouse clicks, and key presses."""
        for event in p.event.get():
            if event.type == p.QUIT:
                self.run = False
            elif event.type == p.MOUSEBUTTONDOWN:
                self.handle_mouse_click(moves, valid_moves)
            elif event.type == p.KEYDOWN:
                self.handle_keypress(event)

    def handle_mouse_click(self, moves, valid_moves):
        """Handles mouse click events to select and move pieces."""
        location = p.mouse.get_pos()  #(x, y) location of mouse
        col, row = location[0] // self.SQ_SIZE, location[1] // self.SQ_SIZE
        
        if self.sq_selected == (row, col):  # Same square clicked again
            self.deselect_square()
        else:
            self.select_square(row, col)
        
        if len(self.player_clicks) == 2:
            self.process_player_move(moves, valid_moves)

    def process_player_move(self, moves, valid_moves):
        """Processes the player's move after two clicks."""
        move = Move(self.player_clicks[0], self.player_clicks[1], self.board.board)
        
        if not moves:
            moves = self.board.get_all_moves()
        if not valid_moves:
            valid_moves = self.board.get_valid_moves(moves)
        
        for valid_move in valid_moves:
            if valid_move == move:
                self.board.make_move(valid_move)
                self.board.movelog.append(valid_move)
                self.moveMade = True
                moves = []
                valid_moves = []
                break
                
        if self.moveMade:
            self.reset_for_next_turn()
        else:
            self.player_clicks = [self.sq_selected]

    def reset_for_next_turn(self):
        """Resets the game state for the next player's turn."""
        self.board.get_all_moves()
        self.moveMade = False
        self.deselect_square()

    def deselect_square(self):
        """Deselects the square and clears the player clicks."""
        self.sq_selected = ()
        self.player_clicks = []

    def select_square(self, row, col):
        """Selects a square and appends it to player clicks."""
        self.sq_selected = (row, col)
        self.player_clicks.append(self.sq_selected)

    def handle_keypress(self, event):
        """Handles key press events (e.g., undo move)."""
        if event.key == p.K_z:
            self.board.undo_move()

    def update_highlighting(self):
        """Updates the board highlighting for selected square and possible moves."""
        if self.sq_selected:
            self.board.highlight(self.sq_selected)
            self.board.highlight_move(self.sq_selected)

    def ai_move(self):
        moves = self.board.get_all_moves()
        valid_moves = self.board.get_valid_moves(moves)

        if valid_moves:
            move = self.AI.choose_move(valid_moves)
            self.board.make_move(move)
            self.board.movelog.append(move)
            self.moveMade = True

            self.board.get_all_moves()
            self.moveMade = False

    def check_for_winner(self):
        """Checks if the current player is out of moves or if the opponent wins/draws."""
        # Check for insufficient material
        if self.check_insufficient_material():
            print("Draw due to insufficient material!")
            self.run = False
            return

        # Get all moves for the current player
        moves = self.board.get_all_moves()
        valid_moves = self.board.get_valid_moves(moves)

        # If no valid moves, the opponent wins
        if not valid_moves:
            winner = "White" if not self.board.white_to_move else "Black"
            print(f"{winner} wins because the opponent has no valid moves!")
            self.run = False


    def check_insufficient_material(self):
        """
        Checks for insufficient material to determine if a draw should be declared.
        """
        pieces = self.board.get_all_pieces()
        piece_count = {}
        bishops = []

        for piece, position in pieces:
            piece_type = type(piece).__name__
            piece_count[piece_type] = piece_count.get(piece_type, 0) + 1
            if piece_type == "Bishop":
                square_color = (position[0] + position[1]) % 2
                bishops.append((piece.color, square_color))

        if len(pieces) == 2:
            return True

        if len(pieces) == 3 and ("Bishop" in piece_count or "Knight" in piece_count):
            return True
        
        if self.board.no_capture_or_pawn_move_count >= 50*2:
            return True

        if len(pieces) == 4 and piece_count.get("Bishop", 0) == 2:
            bishop_colors = set(bishop[1] for bishop in bishops)
            if len(bishop_colors) == 1:
                return True

        return False









    