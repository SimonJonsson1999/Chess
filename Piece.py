import pygame as p
from Move import Move

##TODO##
# Fix an passant and special cases moves
# Make get_moves functions cleaner for all pieces #


class Piece():

    def __init__(self, color, image):
        self.image = image
        self.color = color

    def __str__(self):
        return self.piece

    # row and col need to be in [0,7]
    def check_if_empty(self, row, col, board):
        return isinstance(board[row][col], Empty)

    # row and col need to be in [0,7]
    def opposite_color(self, row, col, board):
        return self.color != board[row][col].color


class Pawn(Piece):
    def __init__(self, color, image, have_moved=0):
        Piece.__init__(self, color, image)
        self.piece = "P"
        self.have_moved = have_moved
        self.type = 'pawn'

    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]

        if self.color == "white" and white_turn:
            # First move for the pawn
            if not self.have_moved:
                for step in range(1, 3):
                    if self.check_if_empty(row - step, col, board):
                        capturedPiece = board[row-step][col]
                        valid_moves.append(Move(position, (row - step, col), board, capturedPiece))
                    else:
                        break
                # Check for captures
                if col == 0:
                    if not self.check_if_empty(row - 1, col + 1, board) and self.opposite_color(row - 1, col + 1, board):
                        capturedPiece = board[row - 1][col + 1]  # Capture piece here
                        valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
                elif col == 7:
                    if not self.check_if_empty(row - 1, col - 1, board) and self.opposite_color(row - 1, col - 1, board):
                        capturedPiece = board[row - 1][col - 1]
                        valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))
                else:
                    if not self.check_if_empty(row - 1, col + 1, board) and self.opposite_color(row - 1, col + 1, board):
                        capturedPiece = board[row - 1][col + 1]
                        valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
                    if not self.check_if_empty(row - 1, col - 1, board) and self.opposite_color(row - 1, col - 1, board):
                        capturedPiece = board[row - 1][col - 1]
                        valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))

            else:
                # After the first move
                if row > 0:
                    if self.check_if_empty(row - 1, col, board):
                        capturedPiece = board[row - 1][col]
                        valid_moves.append(Move(position, (row - 1, col), board, capturedPiece))
                    if col == 0:
                        if not self.check_if_empty(row - 1, col + 1, board) and self.opposite_color(row - 1, col + 1, board):
                            capturedPiece = board[row - 1][col + 1]
                            valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
                    elif col == 7:
                        if not self.check_if_empty(row - 1, col - 1, board) and self.opposite_color(row - 1, col - 1, board):
                            capturedPiece = board[row - 1][col - 1]
                            valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))
                    else:
                        if not self.check_if_empty(row - 1, col + 1, board) and self.opposite_color(row - 1, col + 1, board):
                            capturedPiece = board[row - 1][col + 1]
                            valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
                        if not self.check_if_empty(row - 1, col - 1, board) and self.opposite_color(row - 1, col - 1, board):
                            capturedPiece = board[row - 1][col - 1]
                            valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))

                if row == 3:
                    # En passant checks
                    if col + 1 < 8:
                        if isinstance(board[row][col + 1], Pawn) and self.opposite_color(row, col + 1, board):
                            capturedPiece = board[row][col + 1]
                            valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece, apassant=True))
                    if col - 1 >= 0:
                        if isinstance(board[row][col - 1], Pawn) and self.opposite_color(row, col - 1, board):
                            capturedPiece = board[row][col - 1]
                            valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece, apassant=True))


        elif self.color == "black" and not white_turn:
            # First move for the black pawn
            if not self.have_moved:
                for step in range(1, 3):
                    if self.check_if_empty(row + step, col, board):
                        capturedPiece = board[row + step][col]
                        valid_moves.append(Move(position, (row + step, col), board, capturedPiece))
                    else:
                        break
                # Check for captures
                if col == 0:
                    if not self.check_if_empty(row + 1, col + 1, board) and self.opposite_color(row + 1, col + 1, board):
                        capturedPiece = board[row + 1][col + 1]  # Capture piece here
                        valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))
                elif col == 7:
                    if not self.check_if_empty(row + 1, col - 1, board) and self.opposite_color(row + 1, col - 1, board):
                        capturedPiece = board[row + 1][col - 1]
                        valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))
                else:
                    if not self.check_if_empty(row + 1, col + 1, board) and self.opposite_color(row + 1, col + 1, board):
                        capturedPiece = board[row + 1][col + 1]
                        valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))
                    if not self.check_if_empty(row + 1, col - 1, board) and self.opposite_color(row + 1, col - 1, board):
                        capturedPiece = board[row + 1][col - 1]
                        valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))

            else:
                # After the first move
                if row < 7:
                    if self.check_if_empty(row + 1, col, board):
                        capturedPiece = board[row + 1][col]
                        valid_moves.append(Move(position, (row + 1, col), board, capturedPiece))
                    # Same capture logic as above
                    if col == 0:
                        if not self.check_if_empty(row + 1, col + 1, board) and self.opposite_color(row + 1, col + 1, board):
                            capturedPiece = board[row + 1][col + 1]
                            valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))
                    elif col == 7:
                        if not self.check_if_empty(row + 1, col - 1, board) and self.opposite_color(row + 1, col - 1, board):
                            capturedPiece = board[row + 1][col - 1]
                            valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))
                    else:
                        if not self.check_if_empty(row + 1, col + 1, board) and self.opposite_color(row + 1, col + 1, board):
                            capturedPiece = board[row + 1][col + 1]
                            valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))
                        if not self.check_if_empty(row + 1, col - 1, board) and self.opposite_color(row + 1, col - 1, board):
                            capturedPiece = board[row + 1][col - 1]
                            valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))

                if row == 4:
                    # En passant checks for black pawn
                    if col + 1 < 8:
                        if isinstance(board[row][col + 1], Pawn) and self.opposite_color(row, col + 1, board):
                            capturedPiece = board[row][col + 1]
                            valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece, apassant=True))
                    if col - 1 >= 0:
                        if isinstance(board[row][col - 1], Pawn) and self.opposite_color(row, col - 1, board):
                            capturedPiece = board[row][col - 1]
                            valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece, apassant=True))

class Rook(Piece):
    def __init__(self, color, image, have_moved=0):
        Piece.__init__(self, color, image)
        self.piece = "R"
        self.have_moved = have_moved
        self.type = 'rook'

    # position is a tuple, board is an instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]

        if (self.color == "white" and white_turn) or (self.color == "black" and not white_turn):
            # Rook moves down
            for step in range(1, 8):
                if row + step == 8:
                    break
                elif self.check_if_empty(row + step, col, board):
                    capturedPiece = board[row + step][col]
                    valid_moves.append(Move(position, (row + step, col), board, capturedPiece))
                elif self.opposite_color(row + step, col, board):
                    capturedPiece = board[row + step][col]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col), board, capturedPiece))
                    break
                else:
                    break

            # Rook moves up
            for step in range(1, 8):
                if row - step == -1:
                    break
                elif self.check_if_empty(row - step, col, board):
                    capturedPiece = board[row - step][col]
                    valid_moves.append(Move(position, (row - step, col), board, capturedPiece))
                elif self.opposite_color(row - step, col, board):
                    capturedPiece = board[row - step][col]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col), board, capturedPiece))
                    break
                else:
                    break

            # Rook moves right
            for step in range(1, 8):
                if col + step == 8:
                    break
                elif self.check_if_empty(row, col + step, board):
                    capturedPiece = board[row][col + step]
                    valid_moves.append(Move(position, (row, col + step), board, capturedPiece))
                elif self.opposite_color(row, col + step, board):
                    capturedPiece = board[row][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row, col + step), board, capturedPiece))
                    break
                else:
                    break

            # Rook moves left
            for step in range(1, 8):
                if col - step == -1:
                    break
                elif self.check_if_empty(row, col - step, board):
                    capturedPiece = board[row][col - step]
                    valid_moves.append(Move(position, (row, col - step), board, capturedPiece))
                elif self.opposite_color(row, col - step, board):
                    capturedPiece = board[row][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row, col - step), board, capturedPiece))
                    break
                else:
                    break


        
class Knight(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "K"
        self.type = 'knight'

    # position is a tuple, board is an instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]

        if (self.color == "white" and white_turn) or (self.color == "black" and not white_turn):
            # Knight move 2 down and 1 left or right
            if row + 2 < 8:
                if col + 1 < 8:
                    if self.check_if_empty(row + 2, col + 1, board):
                        capturedPiece = board[row + 2][col + 1]
                        valid_moves.append(Move(position, (row + 2, col + 1), board, capturedPiece))
                    elif self.opposite_color(row + 2, col + 1, board):
                        capturedPiece = board[row + 2][col + 1]  # Capture piece here
                        valid_moves.append(Move(position, (row + 2, col + 1), board, capturedPiece))

                if col - 1 >= 0:
                    if self.check_if_empty(row + 2, col - 1, board):
                        capturedPiece = board[row + 2][col - 1]
                        valid_moves.append(Move(position, (row + 2, col - 1), board, capturedPiece))
                    elif self.opposite_color(row + 2, col - 1, board):
                        capturedPiece = board[row + 2][col - 1]  # Capture piece here
                        valid_moves.append(Move(position, (row + 2, col - 1), board, capturedPiece))

            # Knight move 2 up and 1 left or right
            if row - 2 >= 0:
                if col + 1 < 8:
                    if self.check_if_empty(row - 2, col + 1, board):
                        capturedPiece = board[row - 2][col + 1]
                        valid_moves.append(Move(position, (row - 2, col + 1), board, capturedPiece))
                    elif self.opposite_color(row - 2, col + 1, board):
                        capturedPiece = board[row - 2][col + 1]  # Capture piece here
                        valid_moves.append(Move(position, (row - 2, col + 1), board, capturedPiece))

                if col - 1 >= 0:
                    if self.check_if_empty(row - 2, col - 1, board):
                        capturedPiece = board[row - 2][col - 1]
                        valid_moves.append(Move(position, (row - 2, col - 1), board, capturedPiece))
                    elif self.opposite_color(row - 2, col - 1, board):
                        capturedPiece = board[row - 2][col - 1]  # Capture piece here
                        valid_moves.append(Move(position, (row - 2, col - 1), board, capturedPiece))

            # Knight move 2 left and 1 up or down
            if col - 2 >= 0:
                if row + 1 < 8:
                    if self.check_if_empty(row + 1, col - 2, board):
                        capturedPiece = board[row + 1][col - 2]
                        valid_moves.append(Move(position, (row + 1, col - 2), board, capturedPiece))
                    elif self.opposite_color(row + 1, col - 2, board):
                        capturedPiece = board[row + 1][col - 2]  # Capture piece here
                        valid_moves.append(Move(position, (row + 1, col - 2), board, capturedPiece))

                if row - 1 >= 0:
                    if self.check_if_empty(row - 1, col - 2, board):
                        capturedPiece = board[row - 1][col - 2]
                        valid_moves.append(Move(position, (row - 1, col - 2), board, capturedPiece))
                    elif self.opposite_color(row - 1, col - 2, board):
                        capturedPiece = board[row - 1][col - 2]  # Capture piece here
                        valid_moves.append(Move(position, (row - 1, col - 2), board, capturedPiece))

            # Knight move 2 right and 1 up or down
            if col + 2 < 8:
                if row + 1 < 8:
                    if self.check_if_empty(row + 1, col + 2, board):
                        capturedPiece = board[row + 1][col + 2] 
                        valid_moves.append(Move(position, (row + 1, col + 2), board, capturedPiece))
                    elif self.opposite_color(row + 1, col + 2, board):
                        capturedPiece = board[row + 1][col + 2]  # Capture piece here
                        valid_moves.append(Move(position, (row + 1, col + 2), board, capturedPiece))

                if row - 1 >= 0:
                    if self.check_if_empty(row - 1, col + 2, board):
                        capturedPiece = board[row - 1][col + 2]
                        valid_moves.append(Move(position, (row - 1, col + 2), board, capturedPiece))
                    elif self.opposite_color(row - 1, col + 2, board):
                        capturedPiece = board[row - 1][col + 2]  # Capture piece here
                        valid_moves.append(Move(position, (row - 1, col + 2), board, capturedPiece))




class Bishop(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "B"
        self.type = 'bishop'

    # position is a tuple, board is an instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        
        if (self.color == "white" and white_turn) or (self.color == "black" and not white_turn):
            # Bishop moves up and right
            for step in range(1, 8):
                if col + step == 8 or row + step == 8:
                    break           
                if self.check_if_empty(row + step, col + step, board):
                    capturedPiece = board[row + step][col + step]
                    valid_moves.append(Move(position, (row + step, col + step), board, capturedPiece))
                elif self.opposite_color(row + step, col + step, board):
                    capturedPiece = board[row + step][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col + step), board, capturedPiece))
                    break 
                else:
                    break

            # Bishop moves down and right
            for step in range(1, 8):
                if col + step == 8 or row - step == -1:
                    break           
                if self.check_if_empty(row - step, col + step, board):
                    capturedPiece = board[row - step][col + step]
                    valid_moves.append(Move(position, (row - step, col + step), board, capturedPiece))
                elif self.opposite_color(row - step, col + step, board):
                    capturedPiece = board[row - step][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col + step), board, capturedPiece))
                    break 
                else:
                    break

            # Bishop moves up and left
            for step in range(1, 8):
                if col - step == -1 or row + step == 8:
                    break           
                if self.check_if_empty(row + step, col - step, board):
                    capturedPiece = board[row + step][col - step]
                    valid_moves.append(Move(position, (row + step, col - step), board, capturedPiece))
                elif self.opposite_color(row + step, col - step, board):
                    capturedPiece = board[row + step][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col - step), board, capturedPiece))
                    break 
                else:
                    break

            # Bishop moves down and left
            for step in range(1, 8):
                if col - step == -1 or row - step == -1:
                    break           
                if self.check_if_empty(row - step, col - step, board):
                    capturedPiece = board[row - step][col - step]
                    valid_moves.append(Move(position, (row - step, col - step), board, capturedPiece))
                elif self.opposite_color(row - step, col - step, board):
                    capturedPiece = board[row - step][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col - step), board, capturedPiece))
                    break 
                else:
                    break


class Queen(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "Q"
        self.type = 'queen'
    
    # position is a tuple, board is an instance of Board, valid_moves is a list with moves, and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        
        if (self.color == "white" and white_turn) or (self.color == "black" and not white_turn):
            # Queen moves down
            for step in range(1, 8):
                if row + step == 8:
                    break
                if self.check_if_empty(row + step, col, board):
                    capturedPiece = board[row + step][col]
                    valid_moves.append(Move(position, (row + step, col), board, capturedPiece))
                elif self.opposite_color(row + step, col, board):
                    capturedPiece = board[row + step][col]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves up
            for step in range(1, 8):
                if row - step == -1:
                    break
                if self.check_if_empty(row - step, col, board):
                    capturedPiece = board[row - step][col]
                    valid_moves.append(Move(position, (row - step, col), board, capturedPiece))
                elif self.opposite_color(row - step, col, board):
                    capturedPiece = board[row - step][col]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves right
            for step in range(1, 8):
                if col + step == 8:
                    break
                if self.check_if_empty(row, col + step, board):
                    capturedPiece = board[row][col + step]
                    valid_moves.append(Move(position, (row, col + step), board, capturedPiece))
                elif self.opposite_color(row, col + step, board):
                    capturedPiece = board[row][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row, col + step), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves left
            for step in range(1, 8):
                if col - step == -1:
                    break
                if self.check_if_empty(row, col - step, board):
                    capturedPiece = board[row][col - step]
                    valid_moves.append(Move(position, (row, col - step), board, capturedPiece))
                elif self.opposite_color(row, col - step, board):
                    capturedPiece = board[row][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row, col - step), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves down and right
            for step in range(1, 8):
                if col + step == 8 or row + step == 8:
                    break
                if self.check_if_empty(row + step, col + step, board):
                    capturedPiece = board[row + step][col + step]
                    valid_moves.append(Move(position, (row + step, col + step), board, capturedPiece))
                elif self.opposite_color(row + step, col + step, board):
                    capturedPiece = board[row + step][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col + step), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves up and right
            for step in range(1, 8):
                if col + step == 8 or row - step == -1:
                    break
                if self.check_if_empty(row - step, col + step, board):
                    capturedPiece = board[row - step][col + step]
                    valid_moves.append(Move(position, (row - step, col + step), board, capturedPiece))
                elif self.opposite_color(row - step, col + step, board):
                    capturedPiece = board[row - step][col + step]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col + step), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves down and left
            for step in range(1, 8):
                if col - step == -1 or row + step == 8:
                    break
                if self.check_if_empty(row + step, col - step, board):
                    capturedPiece = board[row + step][col - step]
                    valid_moves.append(Move(position, (row + step, col - step), board, capturedPiece))
                elif self.opposite_color(row + step, col - step, board):
                    capturedPiece = board[row + step][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row + step, col - step), board, capturedPiece))
                    break
                else:
                    break

            # Queen moves up and left
            for step in range(1, 8):
                if col - step == -1 or row - step == -1:
                    break
                if self.check_if_empty(row - step, col - step, board):
                    capturedPiece = board[row - step][col - step]
                    valid_moves.append(Move(position, (row - step, col - step), board, capturedPiece))
                elif self.opposite_color(row - step, col - step, board):
                    capturedPiece = board[row - step][col - step]  # Capture piece here
                    valid_moves.append(Move(position, (row - step, col - step), board, capturedPiece))
                    break
                else:
                    break



class King(Piece):
    def __init__(self, color, image, have_moved=0):
        Piece.__init__(self, color, image)
        self.piece = "K"
        self.have_moved = have_moved
        self.type = 'king'
    
    # position is a tuple, board is an instance of Board, valid_moves is a list with moves, and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        
        if (self.color == "white" and white_turn) or (self.color == "black" and not white_turn):
            # King moves down
            if row + 1 != 8:
                if self.check_if_empty(row + 1, col, board):
                    capturedPiece = board[row + 1][col] 
                    valid_moves.append(Move(position, (row + 1, col), board, capturedPiece))
                elif self.opposite_color(row + 1, col, board):
                    capturedPiece = board[row + 1][col]  # Capture piece here
                    valid_moves.append(Move(position, (row + 1, col), board, capturedPiece))

            # King moves up
            if row - 1 != -1:
                if self.check_if_empty(row - 1, col, board):
                    capturedPiece = board[row - 1][col]
                    valid_moves.append(Move(position, (row - 1, col), board, capturedPiece))
                elif self.opposite_color(row - 1, col, board):
                    capturedPiece = board[row - 1][col]  # Capture piece here
                    valid_moves.append(Move(position, (row - 1, col), board, capturedPiece))

            # King moves right
            if col + 1 != 8:
                if self.check_if_empty(row, col + 1, board):
                    capturedPiece = board[row][col + 1]
                    valid_moves.append(Move(position, (row, col + 1), board, capturedPiece))
                elif self.opposite_color(row, col + 1, board):
                    capturedPiece = board[row][col + 1]  # Capture piece here
                    valid_moves.append(Move(position, (row, col + 1), board, capturedPiece))

            # King moves left
            if col - 1 != -1:
                if self.check_if_empty(row, col - 1, board):
                    capturedPiece = board[row][col - 1]
                    valid_moves.append(Move(position, (row, col - 1), board, capturedPiece))
                elif self.opposite_color(row, col - 1, board):
                    capturedPiece = board[row][col - 1]  # Capture piece here
                    valid_moves.append(Move(position, (row, col - 1), board, capturedPiece))

            # King moves down and right
            if col + 1 != 8 and row + 1 != 8:
                if self.check_if_empty(row + 1, col + 1, board):
                    capturedPiece = board[row + 1][col + 1]
                    valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))
                elif self.opposite_color(row + 1, col + 1, board):
                    capturedPiece = board[row + 1][col + 1]  # Capture piece here
                    valid_moves.append(Move(position, (row + 1, col + 1), board, capturedPiece))

            # King moves down and left
            if col - 1 != -1 and row + 1 != 8:
                if self.check_if_empty(row + 1, col - 1, board):
                    capturedPiece = board[row + 1][col - 1]
                    valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))
                elif self.opposite_color(row + 1, col - 1, board):
                    capturedPiece = board[row + 1][col - 1]  # Capture piece here
                    valid_moves.append(Move(position, (row + 1, col - 1), board, capturedPiece))

            # King moves up and left
            if col - 1 != -1 and row - 1 != -1:
                if self.check_if_empty(row - 1, col - 1, board):
                    capturedPiece = board[row - 1][col - 1]
                    valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))
                elif self.opposite_color(row - 1, col - 1, board):
                    capturedPiece = board[row - 1][col - 1]  # Capture piece here
                    valid_moves.append(Move(position, (row - 1, col - 1), board, capturedPiece))

            # King moves up and right
            if col + 1 != 8 and row - 1 != -1:
                if self.check_if_empty(row - 1, col + 1, board):
                    capturedPiece = board[row - 1][col + 1]
                    valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
                elif self.opposite_color(row - 1, col + 1, board):
                    capturedPiece = board[row - 1][col + 1]  # Capture piece here
                    valid_moves.append(Move(position, (row - 1, col + 1), board, capturedPiece))
        ### Add Castling
        if self.color == "white" and not(self.have_moved):
            if isinstance(board[row][7], Rook) and not board[row][7].have_moved:  # Rook hasn't moved
                if isinstance(board[row][5], Empty) and isinstance(board[row][6], Empty):  # No pieces between
                    capturedPiece = board[row][6]
                    valid_moves.append(Move(position, (row, 6), board, capturedPiece, castle=True))

            if isinstance(board[row][0], Rook) and not board[row][0].have_moved:  # Rook hasn't moved
                if isinstance(board[row][1], Empty) and isinstance(board[row][2], Empty) and isinstance(board[row][3], Empty):  # No pieces between
                    capturedPiece = board[row][2]
                    valid_moves.append(Move(position, (row, 2), board, capturedPiece, castle=True))  # Castling queenside
        if self.color == "black" and not(self.have_moved):
            # Kingside Castling (Short Castling)
            if isinstance(board[row][7], Rook) and not board[row][7].have_moved:  # Rook hasn't moved
                if isinstance(board[row][5], Empty) and isinstance(board[row][6], Empty):  # No pieces between
                    capturedPiece = board[row][6]
                    valid_moves.append(Move(position, (row, 6), board, capturedPiece, castle=True))  # Castling kingside

            # Queenside Castling (Long Castling)
            if isinstance(board[row][0], Rook) and not board[row][0].have_moved: 
                if isinstance(board[row][1], Empty) and isinstance(board, Empty) and isinstance(board[row][3], Empty):  
                    capturedPiece = board[row][2]
                    valid_moves.append(Move(position, (row, 2), board, capturedPiece, castle=True))


class Empty(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "E"
        self.type = 'empty'

    def get_moves(self, position, board, valid_moves, white_turn):
        pass
    
