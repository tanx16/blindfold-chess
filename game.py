import string
from pieces import *
import sys

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
        """
        self.board.addPiece(Pawn(4, 6, "white"), 4, 6)
        self.board.addPiece(Pawn(4, 1, "black"), 4, 1)
        """
class Chessboard:
    def __init__(self):
        #creates matrix that represents board current state
        self.turn = "white"
        self.pieces = []
        self.doubleMoved = 0 #Used for en passant
        self.kingPos = (4, 0)
        self.otherKingPos = (4, 7)
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
        #Needs error checking for locs off the board
        return self.pieces[row][col]
    def getLocation(self, piece):
        assert getPiece(piece.col, piece.row) == piece, "piece missing/not in right position: %r" % piece
        return piece.row, piece.col
    def setPosition(self, piece, new_col, new_row):
        self.pieces[piece.row][piece.col] = None
        piece.row = new_row
        piece.col = new_col
        self.addPiece(piece, new_col, new_row)
        if self.doubleMoved > 0:
            self.doubleMoved -= 1
        #assert not self.isInCheck(), "A king is in check." #Change from assert statement later
    def addPiece(self, piece, col, row):
        if self.pieces[row][col]:
            self.takePiece(col, row) #So we can keep track of taken pieces
        self.pieces[row][col] = piece
    def takePiece(self, col, row):
        #Possibly keep track of taken pieces here
        self.pieces[row][col] = None
    def promote(self, piece): #Add error handling later
        pieces = {"b": Bishop(piece.col, piece.row, piece.color), "n": Knight(piece.col, piece.row, piece.color), "r": Rook(piece.col, piece.row, piece.color), "q": Queen(piece.col, piece.row, piece.color)}
        new_piece = input("Promote pawn to? \n").lower()
        if new_piece.lower() in pieces:
            self.addPiece(pieces[new_piece], piece.col, piece.row)
        else:
            print("Invalid piece.")
            self.promote(piece)
    def move(self, piece, new_col, new_row):
        if piece.legalMove(self, new_col, new_row):
            self.setPosition(piece, new_col, new_row)
            piece.moved = True
            if piece.name == "p" and (new_row == 7 or new_row == 0):
                self.promote(piece)
            if piece.name == "k":
                self.kingPos = (new_col, new_row)
            self.kingPos, self.otherKingPos = self.otherKingPos, self.kingPos
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"
        else:
            print("Please enter a valid move.")
    def white_side_castle(self, side):
        king_piece = self.pieces[0][4]
        if king_piece.legalCastle(self, side):
            if side == "k":
                rook_piece = self.pieces[0][7]
                self.setPosition(king_piece, 6, 0)
                self.setPosition(rook_piece, 5, 0)
            else:
                rook_piece = self.pieces[0][0]
                self.setPosition(king_piece, 2, 0)
                self.setPosition(rook_piece, 3, 0)
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"
        else:
            print("Cannot castle.")
    def black_side_castle(self, side):
        king_piece = self.pieces[7][4]
        if king_piece.legalCastle(self, side):
            if side == "k":
                rook_piece = self.pieces[7][7]
                self.setPosition(king_piece, 6, 7)
                self.setPosition(rook_piece, 5, 7)
            else:
                rook_piece = self.pieces[7][0]
                self.setPosition(king_piece, 2, 7)
                self.setPosition(rook_piece, 3, 7)
            if self.turn == "white":
                self.turn = "black"
            else:
                self.turn = "white"
        else:
            print("Cannot castle.")

    def kingInCheck(self, col, row): #Checks if the king would be in check at (row, col)
        """
        This works by generating lists of places to look for the checking piece.
        """
        if self.color == "white":
            direction = 1
        else:
            direction = -1
        pawnList = [(col+1, row+direction), (col-1, row+direction)]
        #Any way to describe all possible combinations of +-1 and +-2?
        knightList = [(col+1, row+2), (col+1, row-2), (col-1, row+2), (col-1, row-2), (col+2, row+1), (col+2, row-1), (col-2, row+1), (col-2, row-1)]
        rookList = []
        #Generates 4 positions where there is a piece that could be a rook
        for i in range(row+1, 8):
            if self.getPiece(col, i):
                rooklist.append((col, i))
                break #is this right?
        for j in range(-1, row-1):
            if self.getPiece(col, j):
                rooklist.append((col, j))
                break #ditto
        for k in range(-1, col-1):    
            if self.getPiece(k, row):
                rooklist.append((k, row))
                break
        for l in range(col+1, 8):    
            if self.getPiece(k, row):
                rooklist.append((k, row))
                break
        bishopList = []
        for m in range(0, 4):
           if self.getPiece(col+m, row+m): 
                return False
        return False
