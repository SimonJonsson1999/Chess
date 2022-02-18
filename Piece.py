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
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "P"
        self.have_moved = 0

    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col =  position[1]
        if self.color == "white" and white_turn:
            #First move for the pawn
            if not(self.have_moved):
                for step in range(1,3):
                    if self.check_if_empty(row - step, col, board):
                        valid_moves.append( Move( position, (row - step, col), board ))
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

            else:
                if row > 0:
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
                    if row == 3:
                        if isinstance(board[row][col+1], Pawn) and self.opposite_color( row, col + 1, board):
                            valid_moves.append( Move( position, (row - 1, col + 1), board, True ) )
                        elif isinstance(board[row][col-1], Pawn) and self.opposite_color( row, col - 1, board):
                            valid_moves.append( Move( position, (row - 1, col - 1), board, True ) )


        elif self.color == "black" and not(white_turn):
                # First move for the pawn
                if not(self.have_moved):
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

                else:
                    if row < 7:
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
                    if row == 4:
                        if isinstance(board[row][col+1], Pawn) and self.opposite_color( row, col + 1, board):
                            valid_moves.append( Move( position, (row + 1, col + 1), board, True ) )
                        elif isinstance(board[row][col-1], Pawn) and self.opposite_color( row, col - 1, board):
                            valid_moves.append( Move( position, (row + 1, col - 1), board, True ) )
class Rook(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "R"
        pass
    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col =  position[1]
        if ( self.color == "white" and white_turn ) or ( self.color == "black" and not(white_turn) ):
            # Rook moves down
            for step in range(1,7):
                if row + step == 8:
                    break
                elif self.check_if_empty( row + step, col, board):
                    valid_moves.append( Move( position, ( row + step, col), board ) )
                elif self.opposite_color( row + step, col, board):
                    valid_moves.append( Move( position, ( row + step, col), board ) )
                    break
                else:
                    break
            # Rook moves up
            for step in range(1,7):
                if row - step == -1:
                    break
                elif self.check_if_empty( row - step, col, board):
                    valid_moves.append( Move( position, ( row - step, col), board ) )
                elif self.opposite_color( row - step, col, board):
                    valid_moves.append( Move( position, ( row - step, col), board ) )
                    break
                else:
                     break
            # Rook moves right
            for step in range(1,7):
                if col + step == 8:
                    break           
                elif self.check_if_empty( row, col + step, board):
                    valid_moves.append( Move( position, ( row, col+ step), board ) )
                elif self.opposite_color( row, col + step, board):
                    valid_moves.append( Move( position, ( row, col + step), board ) )
                    break
                else:
                    break
            # Rook moves left
            for step in range(1,7):
                if col - step == -1:
                    break           
                elif self.check_if_empty( row, col - step, board):
                    valid_moves.append( Move( position, ( row, col - step), board ) )
                elif self.opposite_color( row, col - step, board):
                    valid_moves.append( Move( position, ( row, col - step), board ) )
                    break
                else:
                    break

        
class Knight(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "K"
    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        if ( self.color == "white" and white_turn ) or ( self.color == "black" and not(white_turn) ):
            # Knight move 2 down and 1 left or right
            if row + 2 < 8:
                if col + 1 != 8:
                    if self.check_if_empty( row + 2, col + 1, board):
                        valid_moves.append( Move( position, ( row + 2, col + 1), board) )
                    elif self.opposite_color( row + 2, col + 1, board):
                        valid_moves.append( Move( position, ( row + 2, col + 1), board) )
                if col - 1 != -1:
                    if self.check_if_empty( row + 2, col - 1, board):
                        valid_moves.append( Move( position, ( row + 2, col - 1), board) )
                    elif self.opposite_color( row + 2, col - 1, board):
                        valid_moves.append( Move( position, ( row + 2, col - 1), board) )    

            # Knight move 2 up and 1 left or right
            if row - 2 > 0:
                if col + 1 != 8:
                    if self.check_if_empty( row - 2, col + 1, board):
                        valid_moves.append( Move( position, ( row - 2, col + 1), board) )
                    elif self.opposite_color( row - 2, col + 1, board):
                        valid_moves.append( Move( position, ( row - 2, col + 1), board) )
                if col - 1 != -1:
                    if self.check_if_empty( row - 2, col - 1, board):
                        valid_moves.append( Move( position, ( row - 2, col - 1), board) )
                    elif self.opposite_color( row - 2, col - 1, board):
                        valid_moves.append( Move( position, ( row - 2, col - 1), board) ) 

            # Knight move 2 left and 1 up or down
            if col - 2 > 0:
                if row + 1 != 8:
                    if self.check_if_empty( row + 1, col - 2, board):
                        valid_moves.append( Move( position, ( row + 1, col - 2), board) )
                    elif self.opposite_color( row + 1, col - 2, board):
                        valid_moves.append( Move( position, ( row + 1, col - 2), board) )
                if row - 1 != -1:
                    if self.check_if_empty( row - 1, col - 2, board):
                        valid_moves.append( Move( position, ( row - 1, col - 2), board) )
                    elif self.opposite_color( row - 1, col - 2, board):
                        valid_moves.append( Move( position, ( row - 1, col - 2), board) )  

            # Knight move 2 left and 1 up or down
            if col + 2 < 8:
                if row + 1 != 8:
                    if self.check_if_empty( row + 1, col + 2, board):
                        valid_moves.append( Move( position, ( row + 1, col + 2), board) )
                    elif self.opposite_color( row + 1, col + 2, board):
                        valid_moves.append( Move( position, ( row + 1, col + 2), board) )
                if row - 1 != -1:
                    if self.check_if_empty( row - 1, col + 2, board):
                        valid_moves.append( Move( position, ( row - 1, col + 2), board) )
                    elif self.opposite_color( row - 1, col + 2, board):
                        valid_moves.append( Move( position, ( row - 1, col + 2), board) ) 



class Bishop(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "B"
    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        if ( self.color == "white" and white_turn ) or ( self.color == "black" and not(white_turn) ):
            # Bishop moves up and right
            for step in range(1,7):
                if col + step == 8 or row + step == 8:
                    break           
                elif self.check_if_empty( row + step , col + step, board):
                    valid_moves.append( Move( position, ( row + step, col + step), board ) )
                elif self.opposite_color( row + step, col + step, board):
                    valid_moves.append( Move( position, ( row + step, col + step), board ) )
                    break 
                else:
                    break
            # Bishop moves down and right
            for step in range(1,7):
                if col + step == 8 or row - step == -1:
                    break           
                elif self.check_if_empty( row - step , col + step, board):
                    valid_moves.append( Move( position, ( row - step, col + step), board ) )
                elif self.opposite_color( row - step, col + step, board):
                    valid_moves.append( Move( position, ( row - step, col + step), board ) )
                    break 
                else:
                    break
            # Bishop moves up and left
            for step in range(1,7):
                if col - step == -1 or row + step == 8:
                    break           
                elif self.check_if_empty( row + step , col - step, board):
                    valid_moves.append( Move( position, ( row + step, col - step), board ) )
                elif self.opposite_color( row + step, col - step, board):
                    valid_moves.append( Move( position, ( row + step, col - step), board ) )
                    break 
                else:
                    break
            #Bishop moves down and left
            for step in range(1,7):
                if col - step == -1 or row - step == -1:
                    break           
                elif self.check_if_empty( row - step , col - step, board):
                    valid_moves.append( Move( position, ( row - step, col - step), board ) )
                elif self.opposite_color( row - step, col - step, board):
                    valid_moves.append( Move( position, ( row - step, col - step), board ) )
                    break 
                else:
                    break

class Queen(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "Q"
    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        if ( self.color == "white" and white_turn ) or ( self.color == "black" and not(white_turn) ):
            # Queen moves down
            for step in range(1,7):
                if row + step == 8:
                    break
                elif self.check_if_empty( row + step, col, board):
                    valid_moves.append( Move( position, ( row + step, col), board ) )
                elif self.opposite_color( row + step, col, board):
                    valid_moves.append( Move( position, ( row + step, col), board ) )
                    break
                else:
                    break
            # Queen moves up
            for step in range(1,7):
                if row - step == -1:
                    break
                elif self.check_if_empty( row - step, col, board):
                    valid_moves.append( Move( position, ( row - step, col), board ) )
                elif self.opposite_color( row - step, col, board):
                    valid_moves.append( Move( position, ( row - step, col), board ) )
                    break
                else:
                     break
            # Queen moves right
            for step in range(1,7):
                if col + step == 8:
                    break           
                elif self.check_if_empty( row, col + step, board):
                    valid_moves.append( Move( position, ( row, col+ step), board ) )
                elif self.opposite_color( row, col + step, board):
                    valid_moves.append( Move( position, ( row, col + step), board ) )
                    break
                else:
                    break
            # Queen moves left
            for step in range(1,7):
                if col - step == -1:
                    break           
                elif self.check_if_empty( row, col - step, board):
                    valid_moves.append( Move( position, ( row, col - step), board ) )
                elif self.opposite_color( row, col - step, board):
                    valid_moves.append( Move( position, ( row, col - step), board ) )
                    break
                else:
                    break
            # Queen moves down and right 
            for step in range(1,7):
                if col + step == 8 or row + step == 8:
                    break           
                elif self.check_if_empty( row + step , col + step, board):
                    valid_moves.append( Move( position, ( row + step, col + step), board ) )
                elif self.opposite_color( row + step, col + step, board):
                    valid_moves.append( Move( position, ( row + step, col + step), board ) )
                    break 
                else:
                    break
            # Queen moves up and right
            for step in range(1,7):
                if col + step == 8 or row - step == -1:
                    break           
                elif self.check_if_empty( row - step , col + step, board):
                    valid_moves.append( Move( position, ( row - step, col + step), board ) )
                elif self.opposite_color( row - step, col + step, board):
                    valid_moves.append( Move( position, ( row - step, col + step), board ) )
                    break 
                else:
                    break
            # Queen moves down and left 
            for step in range(1,7):
                if col - step == -1 or row + step == 8:
                    break           
                elif self.check_if_empty( row + step , col - step, board):
                    valid_moves.append( Move( position, ( row + step, col - step), board ) )
                elif self.opposite_color( row + step, col - step, board):
                    valid_moves.append( Move( position, ( row + step, col - step), board ) )
                    break 
                else:
                    break
            # Queen moves up and left
            for step in range(1,7):
                if col - step == -1 or row - step == -1:
                    break           
                elif self.check_if_empty( row - step , col - step, board):
                    valid_moves.append( Move( position, ( row - step, col - step), board ) )
                elif self.opposite_color( row - step, col - step, board):
                    valid_moves.append( Move( position, ( row - step, col - step), board ) )
                    break 
                else:
                    break


class King(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "K"
    # position is a tuple, board is a instance of Board, valid_moves is a list with moves and white_turn is a bool
    def get_moves(self, position, board, valid_moves, white_turn):
        row = position[0]
        col = position[1]
        if ( self.color == "white" and white_turn ) or ( self.color == "black" and not(white_turn) ):
            # King moves down
            if row + 1 != 8:
                if self.check_if_empty( row + 1, col, board):
                 valid_moves.append( Move( position, ( row + 1, col), board ) )
                elif self.opposite_color( row + 1, col, board):
                  valid_moves.append( Move( position, ( row + 1, col), board ) ) 

            # King moves down
            if row - 1 != -1:
                if self.check_if_empty( row - 1, col, board):
                 valid_moves.append( Move( position, ( row - 1, col), board ) )
                elif self.opposite_color( row - 1, col, board):
                  valid_moves.append( Move( position, ( row - 1, col), board ) )  

            # King moves right
            if col + 1 != 8:
                if self.check_if_empty( row, col + 1, board):
                 valid_moves.append( Move( position, ( row, col + 1), board ) )
                elif self.opposite_color( row, col + 1, board):
                  valid_moves.append( Move( position, ( row, col + 1), board ) ) 

            # King moves right
            if col - 1 != 8:
                if self.check_if_empty( row, col - 1, board):
                 valid_moves.append( Move( position, ( row, col - 1), board ) )
                elif self.opposite_color( row, col - 1, board):
                  valid_moves.append( Move( position, ( row, col - 1), board ) )

            # King moves down and right 
            if col + 1 != 8 and row + 1 != 8:
                if self.check_if_empty( row + 1 , col + 1, board):
                    valid_moves.append( Move( position, ( row + 1, col + 1), board ) )
                elif self.opposite_color( row + 1, col + 1, board):
                    valid_moves.append( Move( position, ( row + 1, col + 1), board ) )

            # King moves down and left 
            if col - 1 != -1 and row + 1 != 8:
                if self.check_if_empty( row + 1 , col - 1, board):
                    valid_moves.append( Move( position, ( row + 1, col - 1), board ) )
                elif self.opposite_color( row + 1, col - 1, board):
                    valid_moves.append( Move( position, ( row + 1, col - 1), board ) )

            # King moves up and left 
            if col - 1 != -1 and row - 1 != -1:
                if self.check_if_empty( row - 1 , col - 1, board):
                    valid_moves.append( Move( position, ( row - 1, col - 1), board ) )
                elif self.opposite_color( row - 1, col - 1, board):
                    valid_moves.append( Move( position, ( row - 1, col - 1), board ) )

            # King moves up and right 
            if col + 1 != 8 and row - 1 != -1:
                if self.check_if_empty( row - 1 , col + 1, board):
                    valid_moves.append( Move( position, ( row - 1, col + 1), board ) )
                elif self.opposite_color( row - 1, col + 1, board):
                    valid_moves.append( Move( position, ( row - 1, col + 1), board ) )

class Empty(Piece):
    def __init__(self, color, image):
        Piece.__init__(self, color, image)
        self.piece = "E"

    def get_moves(self, position, board, valid_moves, white_turn):
        pass
    
