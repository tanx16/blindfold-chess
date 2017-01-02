from chess import *

new_chessboard = Chessboard()
new_game = Game(new_chessboard)
column_names = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7}
def start():
    print("Hi! Welcome to Blind Chess, a challenging game where neither side can see the chessboard!\n")
    answer = input("Would you like to play? Y/N\n")
    if answer.lower() == "y":
        begin()
    elif answer.lower() == "n":
        print("Okay, Bye!")
    else:
        print("Please enter either y or n.")
        start()
def begin():
    print("Here are the instructions.")
    print("To input a coordinate, enter the first letter of the piece, and then the column and number you want and where the piece comes from. Ex. Pb2b3 to move pawn to b3 from b2.\n")
    print("Since knight and king both start with k, use n for knight. Have fun!")
    while not new_game.over:
        answer = input("%s's turn. Please input a coordinate.\n" % new_game.board.turn)
        orig_row = int(answer[2]) - 1
        new_row = int(answer[4]) - 1
        name = answer[0]
        if orig_row > 7 or orig_row < 0 or new_row > 7 or new_row < 0:
            print("Please enter a valid row.")
            continue
        try:
            orig_col = column_names[answer[1]]
            new_col = column_names[answer[3]]
            piece = new_game.board.getPiece(orig_row, orig_col)
            if piece.name != name.lower():
                print("There is no such piece there.")
                continue
            new_game.board.move(piece, new_col, new_row)
        except KeyError:
            print("Please enter a valid column")
start()
