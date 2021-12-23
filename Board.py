from Piece import Piece, Rook, Knight, Bishop, Queen, King, Pawn, Empty
import pygame as p

class Board():

    def __init__(self, SQ_SIZE, DIMENSION):
        self.black_check = False
        self.white_check = False
        self.white_to_move = True
        self.moveLog = []
        self.colors = [p.Color("white"),p.Color("dark gray")]
        self.SQ_SIZE = SQ_SIZE
        self.DIMENSION = DIMENSION
        self.highligt_color = (255,255,84)
        self.highlight_sq = ()
        self.PIECE_IMAGES = {}
        self.move_log = []
        self.valid_moves = []
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


    def load_images(self):
        pieces = ["bR","bN","bB","bQ","bK","bB","bN","bR","bP","wR","wN","wB","wQ","wK","wB","wN","wR","wP","transparent"]
        for piece in pieces:
            self.PIECE_IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"),(self.SQ_SIZE, self.SQ_SIZE))

    def make_move(self, move):
        if not(isinstance(move.pieceMoved, Empty)):
            self.board[move.startRow][move.startCol] = Empty("", self.PIECE_IMAGES["transparent"])
            self.board[move.endRow][move.endCol] = move.pieceMoved
            self.moveLog.append(move)
            if isinstance(move.pieceMoved, Pawn):
                move.pieceMoved.have_moved = True
                if move.endRow == 0 or move.endRow == 7:
                    ## promotion of pawn is handled here, right now it automaticlly promotes to queen
                    self.board[move.endRow][move.endCol] = Queen(f"{move.pieceMoved.color}", self.PIECE_IMAGES[f"{move.pieceMoved.color[0]}Q"])
            self.white_to_move = not self.white_to_move # swap player turn



    def highlight(self, sq_selected):
        self.highlight_sq = sq_selected


    def get_valid_moves(self):
        pass

    def get_all_moves(self):
        self.valid_moves = []
        for row in range(self.DIMENSION):
            for column in range(self.DIMENSION):
                self.board[row][column].get_moves((row, column), self.board, self.valid_moves, self.white_to_move)
                
    def check_if_check(self):
        pass


