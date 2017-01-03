import string

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

class Chesspiece:
    canPromote = False
    checked = False
    def __init__(self, col, row, color):
        self.row = row
        self.col = col
        self.color = color
    def __str__(self):
        return self.name
    def legalMove(self, board, new_col, new_row):
        #inside the board, no piece in destination that is your piece, is your piece
        print(new_col, new_row)
        if new_col < 8 and new_col >= 0 and new_row < 8 and new_row >= 0 and self.color == board.turn:
            return board.pieces[new_row][new_col] == None or board.pieces[new_row][new_col].color != self.color
class Queen(Chesspiece):
    name = "q"
    def legalMove(self, board, new_col, new_row):
        if Chesspiece.legalMove(self, board, new_col, new_row):
           return Rook.legalMove(self, board, new_col, new_row) or Bishop.legalMove(self, board, new_col, new_row)
        else:
           return False
class King(Chesspiece):
    name = "k"
    def legalMove(self, board, new_col, new_row):
        if abs(self.col - new_col) <= 1 and abs(self.row - new_row) <= 1:
            if not (self.col == new_col and self.row == new_row):
                return Chesspiece.legalMove(self, board, new_col, new_row)
            return False
        return False
class Pawn(Chesspiece):
    name = "p"
    def legalMove(self, board, new_col, new_row):
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
    name = "n"
    def legalMove(self, board, new_col, new_row):
        if abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1:
            return Chesspiece.legalMove(self, board, new_col, new_row)
        elif abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2:
            return Chesspiece.legalMove(self, board, new_col, new_row)
        else:
            return False
class Bishop(Chesspiece):
    name = "b"
    def legalMove(self, board, new_col, new_row):
        destination = board.pieces[new_row][new_col]
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            return False
        if not abs(self.row - new_row) == abs(self.col - new_col):
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
    name = "r"
    def legalMove(self, board, new_col, new_row):
        destination = board.pieces[new_row][new_col]
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            return False
        if not (self.col == new_col or self.row == new_row):
            return False
        for i, j in zip(range(1, self.col - new_col), range(1, self.row - new_row)):
            if board.pieces[self.row + i][self.col + j]:
                return False
        if destination:
            print(destination)
            if destination.color == self.color:
                return False
        return True
