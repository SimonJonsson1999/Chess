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
        # self.board = [
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Pawn("black", self.PIECE_IMAGES["bP"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Pawn("white", self.PIECE_IMAGES["wP"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])],
        #     [Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"]), Empty("", self.PIECE_IMAGES["transparent"])]
        # ]

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

        # Check if it's an en passant move
        if move.apassant:
            if move.pieceMoved.color == "white":
                # Remove the captured black pawn for en passant
                self.board[move.endRow + 1][move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])
            elif move.pieceMoved.color == "black":
                # Remove the captured white pawn for en passant
                self.board[move.endRow - 1][move.endCol] = Empty("", self.PIECE_IMAGES["transparent"])

        self.movelog.append(move)

        # Handle pawn promotion if needed
        if isinstance(move.pieceMoved, Pawn):
            move.pieceMoved.have_moved += 1
            if move.endRow == 0 or move.endRow == 7:
                # Automatically promote pawn to queen for simplicity
                self.board[move.endRow][move.endCol] = Queen(f"{move.pieceMoved.color}", self.PIECE_IMAGES[f"{move.pieceMoved.color[0]}Q"])

        # Switch the player's turn
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
            else:
                self.board[last_move.endRow][last_move.endCol] = last_move.pieceCaptured
                  
            self.board[last_move.startRow][last_move.startCol] = last_move.pieceMoved
            self.white_to_move = not(self.white_to_move)


