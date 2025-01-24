from Piece import Piece, Rook, Knight, Bishop, Queen, King, Pawn, Empty
import pygame as p

class Board():

    def __init__(self, SQ_SIZE, DIMENSION):
        self.black_check = False
        self.white_check = False
        self.white_to_move = True
        self.movelog = []
        self.colors = [p.Color("white"),p.Color("dark gray")]
        self.SQ_SIZE = SQ_SIZE
        self.DIMENSION = DIMENSION
        self.highligt_color = (255,255,84)
        self.move_highligt_color = (100,100,50)
        self.highlight_sq = ()
        self.highlight_moves = []
        self.PIECE_IMAGES = {}
        self.load_images()
        self.no_capture_or_pawn_move_count = 0
        self.board = [
                    [Rook("black", self.PIECE_IMAGES["bR"]), Knight("black", self.PIECE_IMAGES["bN"]), Bishop("black", self.PIECE_IMAGES["bB"]), Queen("black", self.PIECE_IMAGES["bQ"]), King("black",self.PIECE_IMAGES["bK"]), Bishop("black", self.PIECE_IMAGES["bB"]), Knight("black", self.PIECE_IMAGES["bN"]), Rook("black", self.PIECE_IMAGES["bR"])],
                    [Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"]), Pawn("black", self.PIECE_IMAGES["bP"])],
                    [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
                    [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
                    [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
                    [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
                    [Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"]), Pawn("white", self.PIECE_IMAGES["wP"])],
                    [Rook("white", self.PIECE_IMAGES["wR"]), Knight("white", self.PIECE_IMAGES["wN"]), Bishop("white", self.PIECE_IMAGES["wB"]), Queen("white", self.PIECE_IMAGES["wQ"]), King("white", self.PIECE_IMAGES["wK"]), Bishop("white", self.PIECE_IMAGES["wB"]), Knight("white", self.PIECE_IMAGES["wN"]), Rook("white", self.PIECE_IMAGES["wR"])],
                    ]
    def draw(self,screen):
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                color = self.colors[ (row + column) % 2 ]
                if self.highlight_sq == (row, column) and not(isinstance(self.board[row][column], Empty)):
                    p.draw.rect(screen, self.highligt_color, p.Rect(column*self.SQ_SIZE, row*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                    self.highlight_sq = ()

                else:
                    p.draw.rect(screen, color, p.Rect(column*self.SQ_SIZE, row*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))
                piece = self.board[row][column]
                if piece:
                    screen.blit(piece.image, p.Rect(column*self.SQ_SIZE, row*self.SQ_SIZE, self.SQ_SIZE, self.SQ_SIZE))



    def draw_moves(self,screen):
        for square in self.highlight_moves:
            p.draw.circle(screen, self.move_highligt_color, (square[1]*self.SQ_SIZE + self.SQ_SIZE/2, square[0]*self.SQ_SIZE + self.SQ_SIZE/2), self.SQ_SIZE/2, 3)

        self.highlight_moves = []

    def load_images(self):
        pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bP","wR","wN","wB","wQ","wK","wB","wN","wR","wP","transparent"]
        for piece in pieces:
            self.PIECE_IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(self.SQ_SIZE, self.SQ_SIZE))

    def make_move(self, move):
        self.board[move.startRow][move.startCol] = Empty("", self.PIECE_IMAGES["transparent"])
        self.board[move.endRow][move.endCol] = move.pieceMoved
        if move.castle:
            if move.endCol == 6: 
                rook_start_col = 7
                rook_end_col = 5
            elif move.endCol == 2:  
                rook_start_col = 0
                rook_end_col = 3
            
        if isinstance(move.pieceMoved, Pawn) or move.pieceCaptured:
            self.no_capture_or_pawn_move_count = 0  
        else:
            self.no_capture_or_pawn_move_count += 1

           
            rook = self.board[move.startRow][rook_start_col]
            self.board[move.startRow][rook_start_col] = Empty("", self.PIECE_IMAGES["transparent"])
            self.board[move.startRow][rook_end_col] = rook
            rook.have_moved += 1

        
        if move.apassant:
            if move.pieceMoved.color == "white":
                self.board[move.endRow + 1][move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])
            elif move.pieceMoved.color == "black":
                self.board[move.endRow - 1][move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])

        self.movelog.append(move)

       
        if isinstance(move.pieceMoved, Pawn):
            move.pieceMoved.have_moved += 1
            if move.endRow == 0 or move.endRow == 7:
                self.board[move.endRow][move.endCol] = Queen(f"{move.pieceMoved.color}", self.PIECE_IMAGES[f"{move.pieceMoved.color[0]}Q"])

        self.white_to_move = not self.white_to_move


    def highlight(self, sq_selected):
        self.highlight_sq = sq_selected

    def highlight_move(self, sq_selected):
        moves = self.get_all_moves()
        valid_moves = self.get_valid_moves(moves)
        for move in valid_moves:
            if move.startRow == sq_selected[0] and move.startCol == sq_selected[1]:
                self.highlight_moves.append((move.endRow, move.endCol))

         

    def get_valid_moves(self, moves):
        valid_moves = []
        for move in moves:
            make_move = True
            if move.apassant:
                last_move = self.movelog[-1]
                if move.pieceMoved.color == "white":
                    if last_move.endRow == move.endRow + 1 and last_move.endCol == move.endCol:
                        make_move = True
                    else:
                        make_move = False
                elif move.pieceMoved.color == "black":
                    if last_move.endRow == move.endRow - 1 and last_move.endCol == move.endCol:
                        make_move = True
                    else:
                        make_move = False
            
            if isinstance(move.pieceMoved, King) and move.pieceMoved.color == "white":
                if move.endCol == 6: 
                    if not self.is_square_under_attack(move.startRow, 4) and not self.is_square_under_attack(move.startRow, 5):
                        make_move = True
                    else:
                        make_move = False
            
                elif move.endCol == 2:
                    if not self.is_square_under_attack(move.startRow, 4) and not self.is_square_under_attack(move.startRow, 3):
                        make_move = True
                    else:
                        make_move = False

        
            if isinstance(move.pieceMoved, King) and move.pieceMoved.color == "black" and not move.pieceMoved.have_moved:
                if move.endCol == 6: 
                    if not self.is_square_under_attack(move.startRow, 4) and not self.is_square_under_attack(move.startRow, 5):
                        make_move = True
                    else:
                        make_move = False
            
                elif move.endCol == 2:
                    if not self.is_square_under_attack(move.startRow, 4) and not self.is_square_under_attack(move.startRow, 3):
                        make_move = True
                    else:
                        make_move = False

            if make_move:
                self.make_move(move)
                second_moves = self.get_all_moves()
                king_captured = False
                for second_move in second_moves:
                    if isinstance( second_move.pieceCaptured, King):
                        if (self.white_to_move and second_move.pieceCaptured.color == "black") or (not self.white_to_move and second_move.pieceCaptured.color == "white"):
                            king_captured = True
                            
                if not king_captured:
                    valid_moves.append(move)
                self.undo_move()
            
        return valid_moves

    def get_all_moves(self):
        moves = []
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                self.board[row][column].get_moves((row, column), self.board, moves, self.white_to_move)
        return moves

    def __copy__(self, other):
        if isinstance(other, Board):
            other.board = self.board
            self.black_check = False
            self.white_check = False
            other.white_to_move = self.white_to_move
            other.moveLog = self.moveLog
            other.SQ_SIZE = self.SQ_SIZE
            other.DIMENSION = self.DIMENSION
            other.valid_moves = self.valid_moves
            return True
        else:
            return False

    def undo_move(self):
        if self.movelog:
            last_move = self.movelog.pop()
            if isinstance ( last_move.pieceMoved, Pawn):
                last_move.pieceMoved.have_moved -= 1

            if last_move.apassant:
                if last_move.pieceMoved.color == "white":
                    self.board[last_move.endRow + 1][last_move.endCol] = last_move.pieceCaptured
                    self.board[last_move.endRow][last_move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])
                elif last_move.pieceMoved.color == "black":
                    self.board[last_move.endRow - 1][last_move.endCol] = last_move.pieceCaptured
                    self.board[last_move.endRow ][last_move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])

            elif last_move.castle:
                if last_move.endCol == 6:  # Kingside castling
                    rook_start_col = 7
                    rook_end_col = 5
                elif last_move.endCol == 2:  # Queenside castling
                    rook_start_col = 0
                    rook_end_col = 3
            
                rook = self.board[last_move.startRow][rook_end_col]
                self.board[last_move.startRow][rook_start_col] = rook
                self.board[last_move.startRow][rook_end_col] = Empty("", self.PIECE_IMAGES["transparent"])
                self.board[last_move.endRow][last_move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])
                rook.have_moved = False
            else:
                self.board[last_move.endRow][last_move.endCol] = last_move.pieceCaptured
                  
            self.board[last_move.startRow][last_move.startCol] = last_move.pieceMoved
            self.white_to_move = not(self.white_to_move)

    def is_square_under_attack(self, row, col):
        # Check if the square is under attack by any opponent piece
        
        opponent_color = "black" if self.white_to_move else "white"
        for r in range(self.DIMENSION):
            for c in range(self.DIMENSION):
                piece = self.board[r][c]
                if piece.color == opponent_color:
                    moves = []
                    piece.get_moves((r, c), self.board, moves, self.white_to_move)
                    for move in moves:
                        if move.endRow == row and move.endCol == col:
                            return True
        return False
    
    def get_all_pieces(self):
        """
        Returns a list of all active pieces on the board along with their positions.
        Each entry in the list is a tuple (piece, (row, col)).
        """
        all_pieces = []
        for row in range(self.DIMENSION):
            for col in range(self.DIMENSION):
                piece = self.board[row][col]
                if not isinstance(piece, Empty):  # Skip empty squares
                    all_pieces.append((piece, (row, col)))
        return all_pieces
    
    def get_board(self):
        return self.board


