import string
from pieces import *

class Game:
    def __init__(self, board):
        #self.board is instance of Chessboard
        self.over = False
        self.board = board

        wpawn1 = Pawn(0, 1, "white")
        wpawn2 = Pawn(1, 1, "white")
        wpawn3 = Pawn(2, 1, "white")
        wpawn4 = Pawn(3, 1, "white")
        wpawn5 = Pawn(4, 1, "white")
        wpawn6 = Pawn(5, 1, "white")
        wpawn7 = Pawn(6, 1, "white")
        wpawn8 = Pawn(7, 1, "white")
        wrook1 = Rook(0, 0, "white")
        wknight1 = Knight(1, 0, "white")
        wbishop1 = Bishop(2, 0, "white")
        wqueen = Queen(3, 0, "white")
        wking = King(4, 0, "white")
        wbishop2 = Bishop(5, 0, "white")
        wknight2 = Knight(6, 0, "white")
        wrook2 = Rook(7, 0, "white")

        bpawn1 = Pawn(0, 6, "black")
        bpawn2 = Pawn(1, 6, "black")
        bpawn3 = Pawn(2, 6, "black")
        bpawn4 = Pawn(3, 6, "black")
        bpawn5 = Pawn(4, 6, "black")
        bpawn6 = Pawn(5, 6, "black")
        bpawn7 = Pawn(6, 6, "black")
        bpawn8 = Pawn(7, 6, "black")
        brook1 = Rook(0, 7, "black")
        bknight1 = Knight(1, 7, "black")
        bbishop1 = Bishop(2, 7, "black")
        bqueen = Queen(3, 7, "black")
        bking = King(4, 7, "black")
        bbishop2 = Bishop(5, 7, "black")
        bknight2 = Knight(6, 7, "black")
        brook2 = Rook(7, 7, "black")

        self.board.pieces[0] = [wrook1, wknight1, wbishop1, wqueen, wking, wbishop2, wknight2, wrook2]
        self.board.pieces[1] = [wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8]
        self.board.pieces[6] = [bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8]
        self.board.pieces[7] = [brook1, bknight1, bbishop1, bqueen, bking, bbishop2, bknight2, brook2]

class Chessboard:
    def __init__(self):
        #creates matrix that represents board current state
        self.turn = "white"
        self.pieces = []
        for i in range(8):
            self.pieces.append([None, None, None, None, None, None, None, None])
    def display(self):
        #prints board, starting with (0, 7) in the top left and ending with (7, 0) in the bottom right.
        for j in range(7, -1 ,-1):
            for i in range(8):
                if self.getPiece(i, j):
                    print(self.getPiece(i, j), end=' ')
                else:
                    print('*', end=' ')
            print()
    def getPiece(self, col, row):
        #returns piece in location with row and col, returns None if no piece
        return self.pieces[row][col]
    def getLocation(self, piece):
        assert getPiece(piece.col, piece.row) == piece, "piece missing/not in right position: %r" % piece
        return piece.row, piece.col
    def setPosition(self, piece, new_col, new_row):
        self.pieces[piece.row][piece.col] = None
        piece.row = new_row
        piece.col = new_col
        self.pieces[new_row][new_col] = piece
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        #assert not self.isInCheck(), "A king is in check." #Change from assert statement later
    def addPiece(self, piece, new_col, new_row):
        self.pieces[new_col][new_row] = piece
    def move(self, piece, new_col, new_row):
        if piece.legalMove(self, new_col, new_row):
            self.setPosition(piece, new_col, new_row)
        else:
            print("Please enter a valid move.")

    #def isInCheck(self, newposition): #Checks if the new position (a matrix of pieces) has a king under check.
