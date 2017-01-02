import string

class Game:
    def __init__(self, board):
        #self.board is instance of Chessboard
        self.over = False
        self.board = board
        wpawn1 = Pawn(0, 1, "white", "p")
        wpawn2 = Pawn(1, 1, "white", "p")
        wpawn3 = Pawn(2, 1, "white", "p")
        wpawn4 = Pawn(3, 1, "white", "p")
        wpawn5 = Pawn(4, 1, "white", "p")
        wpawn6 = Pawn(5, 1, "white", "p")
        wpawn7 = Pawn(6, 1, "white", "p")
        wpawn8 = Pawn(7, 1, "white", "p")
        wrook1 = Rook(0, 0, "white", "r")
        wknight1 = Knight(1, 0, "white", "n")
        wbishop1 = Bishop(2, 0, "white", "b")
        wqueen = Queen(3, 0, "white", "q")
        wking = King(4, 0, "white", "K")
        wbishop2 = Bishop(5, 0, "white", "b")
        wknight2 = Knight(6, 0, "white", "n")
        wrook2 = Rook(7, 0, "white", "r")

        bpawn1 = Pawn(0, 6, "black", "p")
        bpawn2 = Pawn(1, 6, "black", "p")
        bpawn3 = Pawn(2, 6, "black", "p")
        bpawn4 = Pawn(3, 6, "black", "p")
        bpawn5 = Pawn(4, 6, "black", "p")
        bpawn6 = Pawn(5, 6, "black", "p")
        bpawn7 = Pawn(6, 6, "black", "p")
        bpawn8 = Pawn(7, 6, "black", "p")
        brook1 = Rook(0, 7, "black", "r")
        bknight1 = Knight(1, 7, "black", "n")
        bbishop1 = Bishop(2, 7, "black", "b")
        bqueen = Queen(3, 7, "black", "q")
        bking = King(4, 7, "black", "k")
        bbishop2 = Bishop(5, 7, "black", "b")
        bknight2 = Knight(6, 7, "black", "n")
        brook2 = Rook(7, 7, "black", "r")

        self.board.pieces[0] = [wrook1, wknight1, wbishop1, wqueen, wking, wbishop2, wknight2, wrook2]
        self.board.pieces[1] = [wpawn1, wpawn2, wpawn3, wpawn4, wpawn5, wpawn6, wpawn7, wpawn8]
        self.board.pieces[6] = [bpawn1, bpawn2, bpawn3, bpawn4, bpawn5, bpawn6, bpawn7, bpawn8]
        self.board.pieces[7] = [brook1, bknight1, bbishop1, bqueen, bking, bbishop2, bknight2, brook2]

class Chessboard:
    def __init__(self):
        #creates matrix that represents board current state
        self.turn = "white"
        rows = [None, None, None, None, None, None, None, None]
        self.pieces = []
        for i in range(8):
            self.pieces.append(rows)
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
        assert piece.color == self.turn
        self.pieces[piece.row][piece.col] = None
        piece.row = new_row
        piece.col = new_col
        self.pieces[new_row][new_col] = piece
        if self.turn == "white":
            self.turn = "black"
        else:
            self.turn = "white"
        #assert not self.isInCheck(), "A king is in check." #Change from assert statement later
    def move(self, piece, new_col, new_row):
        if piece.legalMove(self, new_col, new_row, piece.color):
            self.setPosition(piece, new_col, new_row)
        else:
            print("Please enter a valid move.")

    #def isInCheck(self, newposition): #Checks if the new position (a matrix of pieces) has a king under check.

class Chesspiece:
    canPromote = False
    checked = False
    def __init__(self, col, row, color, name):
        self.row = row
        self.col = col
        self.color = color
        self.name = name
    def __str__(self):
        return self.name
    def legalMove(self, board, new_col, new_row):
        #inside the board, no piece in destination that is your piece
        if new_col < 8 and new_col >= 0 and new_row < 8 and new_row >= 0:
            return board.pieces[new_row][new_col] == None or board.pieces[new_row][new_col].color != self.color
class Queen(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        if Chesspiece.legalMove(board, new_col, new_row, color):
           return Rook.legalMove(self, board, new_col, new_row, color) or Bishop.legalMove(self, board, new_col, new_row, color)
        else:
           return False
class King(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        if abs(self.col - new_col) <= 1 and abs(self.row - new_row) <= 1:
            if not (self.col == new_col and self.row == new_row):
                return Chesspiece.legalMove(self, board, new_col, new_row)
            return False
        return False
class Pawn(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        destination = board.pieces[new_row][new_col]
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            return False
        if self.color == "white":
            if new_row == self.row + 1 and new_col == self.col and not destination:
                return True
            else:
                if new_row == self.row + 1 and abs(new_col-self.col)==1:
                    if not destination:
                        return False
                    else:
                        return destination.color != self.color
        else:
            if new_row == self.row - 1 and new_col == self.col and not destination:
                return True
            else:
                if new_row == self.row - 1 and abs(new_col-self.col)==1:
                    if not destination:
                        return False
                    else:
                        return destination.color != self.color
class Knight(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        if abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1:
            return Chesspiece.legalMove(self, board, new_col, new_row)
        elif abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2:
            return Chesspiece.legalMove(self, board, new_col, new_row)
        else:
            return False
class Bishop(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        destination = board.pieces[new_col][new_row]
        print(destination)
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            print("original error")
            return False
        if not abs(self.row - new_row) == abs(self.col - new_col):
            print("not straight line")
            return False
        index1 = (new_col - self.col) // abs(new_col - self.col)
        index2 = (new_row - self.row) // abs(new_row - self.row)
        for _ in range(abs(new_col - self.col)):
            if board.pieces[self.row + index2][self.col + index1]:
                return False
        if destination:
            if destination.color == self.color:
                return False
        return True

class Rook(Chesspiece):
    def legalMove(self, board, new_col, new_row, color):
        destination = board.pieces[new_col][new_row]
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            return False
        if not (self.col == new_col or self.row == new_row):
            return False
        for i, j in zip(range(1, self.col - new.col), range(1, self.row - new.row)):
            if board.pieces[self.col + i][self.row + j]:
                return False
        if destination:
            if destination.color == self.color:
                return False
        return True
