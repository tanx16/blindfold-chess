from pieces import *
from game import *
import sys

new_chessboard = Chessboard()
new_game = Game(new_chessboard)
column_names = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
def start():
    print("Hi! Welcome to Blind Chess, a challenging game where neither side can see the chessboard!\n")
    answer = input("Would you like to play? Y/N\n")
    if answer.lower() == "y":
        print("Here are the instructions.")
        print("To input a coordinate, enter the first letter of the piece, and then the column and number you want and where the piece comes from. Ex. Pb2b3 to move pawn to b3 from b2.\n")
        print("To castle, type qcastle or kcastle for the appropriate side.")
        print("Since knight and king both start with k, use n for knight. Have fun!")
        begin()
    elif answer.lower() == "n":
        sys.exit("Okay, Bye!")
    else:
        print("Please enter either y or n.")
        start()
def begin():
    while not new_game.over:
        new_game.board.display()
        answer = input("%s's turn. Please input a coordinate.\n" % new_game.board.turn)
        if answer == "quit()":
            sys.exit("Okay, Bye!")
        if answer[:3] == "get":
            col = column_names[answer[4]]
            row = int(answer[5]) - 1
            piece = new_chessboard.getPiece(col, row)
            print(piece, piece.color if piece else piece)
        if answer == "qcastle" or answer == "kcastle":
            if new_game.board.turn == "white":
                new_game.board.white_side_castle(answer[0])
                continue
            else:
                new_game.board.black_side_castle(answer[0])
                continue
        try:
            orig_row = int(answer[2]) - 1
            new_row = int(answer[4]) - 1
            name = answer[0]
        except (ValueError, IndexError):
            print("Please enter a valid command.")
            begin()
        if orig_row > 7 or orig_row < 0 or new_row > 7 or new_row < 0:
            print("Please enter a valid row.")
            continue
        try:
            orig_col = column_names[answer[1]]
            new_col = column_names[answer[3]]
            piece = new_game.board.getPiece(orig_col, orig_row)
            if piece.name != name.lower():
                print("There is no such piece there.")
                continue
            new_game.board.move(piece, new_col, new_row)
        except (KeyError, AttributeError):
            print("Please enter a valid command.")
start()
