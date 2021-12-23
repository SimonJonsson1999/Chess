import pygame as p
from Move import Move
class Piece():

    def __init__(self, color, image):
        self.image = image
        self.color = color

    def __str__(self):
        return self.piece

    def check_if_empty(self, row, col, board):
        return isinstance(board[row][col], Empty)
    def opposite_color(self, row, col, board):
        return self.color != board[row][col].color


class Pawn(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "P"

    def get_moves(self, position, board, valid_moves, white_turn):
        ## maybe can be done a little nicer
        ## still need to fix an psaant and promoting
        row = position[0]
        col =  position[1]
        if self.color == "white" and white_turn:
            if row == 6:
                for step in range(1,3):
                    if self.check_if_empty(row - step, col, board):
                        valid_moves.append( Move( position, (row - step, col), board ))
                if col == 0:
                    ## fix indixeds here
                    if not( self.check_if_empty(row - 1, col + 1, board) ) and self.opposite_color( row - 1, col + 1, board):
                        valid_moves.append( Move( position, (row - 1, col + 1), board ) )
                elif col == 7:
                    if not( self.check_if_empty(row - 1, col - 1, board) ) and self.opposite_color( row - 1, col - 1, board):
                        valid_moves.append( Move( position, (row - 1, col - 1), board ) )
                else:
                    if not( self.check_if_empty(row - 1, col + 1, board) ) and self.opposite_color( row - 1, col + 1, board):
                        valid_moves.append( Move( position, (row - 1, col + 1), board ) )
                    if not( self.check_if_empty(row - 1, col - 1, board) ) and self.opposite_color( row - 1, col - 1, board):
                        valid_moves.append( Move( position, (row - 1, col - 1), board ) )

            elif 0 < row < 6:
                if self.check_if_empty( row - 1, col, board):
                    valid_moves.append( Move( position, (row - 1, col), board ) )
                if col == 0:
                    if not( self.check_if_empty(row - 1, col + 1, board) ) and self.opposite_color( row - 1, col + 1, board):
                        valid_moves.append( Move( position, (row - 1, col + 1), board ) )
                elif col == 7:
                    if not( self.check_if_empty(row - 1, col - 1, board) ) and self.opposite_color( row - 1, col - 1, board):
                        valid_moves.append( Move( position, (row - 1, col - 1), board ) )
                else:
                    if not( self.check_if_empty(row - 1, col + 1, board) ) and self.opposite_color( row - 1, col + 1, board):
                        valid_moves.append( Move( position, (row - 1, col + 1), board ) )
                    if not( self.check_if_empty(row - 1, col - 1, board) ) and self.opposite_color( row - 1, col - 1, board):
                        valid_moves.append( Move( position, (row - 1, col - 1), board ) )

        elif self.color == "black" and not(white_turn):
                if row == 1:
                    for step in range(1,3):
                        if self.check_if_empty(row + step, col, board):
                            valid_moves.append( Move( position, (row + step, col), board ))
                    if col == 0:
                        if not( self.check_if_empty(row + 1, col + 1, board) ) and self.opposite_color( row + 1, col + 1, board):
                            valid_moves.append( Move( position, (row + 1, col + 1), board ) )
                    elif col == 7:
                        if not( self.check_if_empty(row + 1, col - 1, board) ) and self.opposite_color( row + 1, col - 1, board):
                            valid_moves.append( Move( position, (row + 1, col - 1), board ) )
                    else:
                        if not( self.check_if_empty(row + 1, col + 1, board) ) and self.opposite_color( row + 1, col + 1, board):
                            valid_moves.append( Move( position, (row + 1, col + 1), board ) )
                        if not( self.check_if_empty(row + 1, col - 1, board) ) and self.opposite_color( row + 1, col - 1, board):
                            valid_moves.append( Move( position, (row + 1, col - 1), board ) )

                elif 0 < row < 6:
                    if self.check_if_empty( row + 1, col, board):
                        valid_moves.append( Move( position, (row + 1, col), board ) )
                    if col == 0:
                        if not( self.check_if_empty(row + 1, col + 1, board) ) and self.opposite_color( row + 1, col + 1, board):
                            valid_moves.append( Move( position, (row + 1, col + 1), board ) )
                    elif col == 7:
                        if not( self.check_if_empty(row + 1, col - 1, board) ) and self.opposite_color( row + 1, col - 1, board):
                            valid_moves.append( Move( position, (row + 1, col - 1), board ) )
                    else:
                        if not( self.check_if_empty(row + 1, col + 1, board) ) and self.opposite_color( row + 1, col + 1, board):
                            valid_moves.append( Move( position, (row + 1, col + 1), board ) )
                        if not( self.check_if_empty(row + 1, col - 1, board) ) and self.opposite_color( row + 1, col - 1, board):
                            valid_moves.append( Move( position, (row + 1, col - 1), board ) )

class Rook(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
       # self.piece = "R"
        pass

    def get_moves(self, position, board, valid_moves, white_turn):
        #row = position[0]
        #col = positon[1]
        pass

class Knight(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "K"

    def get_moves(self, position, board, valid_moves, white_turn):
        if self.color == "white" and white_turn:
            pass
        elif self.color == "black" and not(white_turn):
            pass


class Bishop(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "B"

    def get_moves(self, position, board, valid_moves, white_turn):
        if self.color == "white" and white_turn:
            pass
        elif self.color == "black" and not(white_turn):
            pass

class Queen(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "Q"

    def get_moves(self, position, board, valid_moves, white_turn):
        if self.color == "white" and white_turn:
            pass
        elif self.color == "black" and not(white_turn):
            pass


class King(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "K"

    def get_moves(self, position, board, valid_moves, white_turn):
        if self.color == "white" and white_turn:
            pass
        elif self.color == "black" and not(white_turn):
            pass


class Empty(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "E"

    def get_moves(self, position, board, valid_moves, white_turn):
        if self.color == "white" and white_turn:
            pass
        elif self.color == "black" and not(white_turn):
            pass
