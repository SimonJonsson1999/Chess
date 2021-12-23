import pygame as p
from Piece import Piece
from Board import Board
from Move import Move
WIDTH = HEIGHT = 480
DIMENSION = 8 #8 by 8 board
SQ_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
def main():
    screen = p.display.set_mode((WIDTH, HEIGHT)) #create the screen
    clock = p.time.Clock() #create a clock

    board = Board(SQ_SIZE, DIMENSION)

    screen.fill(p.Color("Black"))
    player_clicks = []
    sq_selected = ()
    moveMade = False
    run = True
    while run:
            for event in p.event.get():
                if event.type == p.QUIT:
                    run = False
                elif event.type == p.MOUSEBUTTONDOWN:
                    location = p.mouse.get_pos() #(x,y) location of mouse
                    col = location[0]//SQ_SIZE
                    row = location[1]//SQ_SIZE
                    if sq_selected == (row, col): # check if user click the same square twice
                        sq_selected = () # deselct the squares
                        player_clicks = [] # clear playerClicks
                    else:
                        sq_selected = (row, col)
                        player_clicks.append(sq_selected) # append for both and second clicks
                    if len(player_clicks) == 2: # after second clicks
                        move = Move(player_clicks[0],player_clicks[1],board.board)
                        board.get_all_moves()
                        #board.get_valid_moves()

                        for valid_move in board.valid_moves:
                            if valid_move == move:
                                board.make_move(move)
                                moveMade = True
                                break
                        if moveMade:
                            board.get_all_moves()
                            moveMade = False
                            sq_selected = () # reset user clicks
                            player_clicks = []
                        else:
                            player_clicks = [sq_selected]

            clock.tick(MAX_FPS)
            if sq_selected:
                board.highlight(sq_selected)
            board.draw(screen)
            p.display.flip()
if __name__ == "__main__":
    main()
