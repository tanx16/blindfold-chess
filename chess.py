import string

class Game:
    def __init__(self, board):
        #self.board is instance of Chessboard
        self.board = board
        self.turn = None
class Chessboard:
    def __init__(self):
        #creates matrix that represents board current state
        rows = [None, None, None, None, None, None, None, None]
        self.pieces = []
        for i in range(8):
            self.pieces.append(rows)
    def __str__(self):
        #prints board
        for i in range(8):
            for j in range(8):
                if self.getPiece(i, j):
                    print(self.getPiece(i, j), end=' ')
                else:
                    print('*', end=' ')
            print()
    def getPiece(self, col, row):
        #returns piece in location with row and col, returns None if no piece
        return self.pieces[col][row]
    def getLocation(self, piece):
        assert getPiece(piece.col, piece.row) == piece, "piece missing/not in right position: %r" % piece
        return piece.row, piece.col
    def move(self, piece, new_col, new_row):
        if legalMove(self, piece, new_col, new_row):
            setPosition(piece, new_col, new_row)
    def setPosition(self, piece, new_col, new_row):
        assert getPiece(piece.col, piece.row) == piece
        self.pieces[piece.col][piece.row] = None
        piece.row = new_row
        piece.col = new_col
        self.pieces[new_col][new_row] = piece
        assert not self.inCheck(), "A king is in check."
    def inCheck(self, newposition): #Checks if the new position (a matrix of pieces) has a king under check.
        return False #TODO
class Chesspiece:
    canPromote = False
    checked = False
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
    def legalMove(self, board, new_col, new_row):
        #inside the board, no piece in destination that is your piece
        return new_col < 8 and new_col >= 0 and new_row < 8 and new_row >= 0 and board.pieces[new_col][new_row].color != self.color
        #Change so that it works when there is no piece on the new location.
class Queen(Chesspiece):
    def legalMove(self, board, new_col, new_row):
        if #something something something
            return False
        return Chesspiece.legalMove(board, new_col, new_row)
class King(Chesspiece):

class Pawn(Chesspiece):
    def legalMove(self, board, new_col, new_row):
        destination = board.pieces[new_col][new_row]
        if not Chesspiece.legalMove(board, new_col, new_row):
            return False
        if self.color == "white":
            if new_row == self.row + 1 and new_col == self.col and not destination:
                return True
            else:
                if not destination:
                    return False
                elif new_row == self.row + 1 and abs(new_col-self.col)==1 and destination.color != self.color:
                    return True
        else:
            if new_row == self.row - 1 and new_col == self.col and not destination:
                return True
            else:
                if not destination:
                    return False
                elif new_row == self.row - 1 and abs(new_col-self.col)==1 and destination.color != self.color:
                    return True        
class Knight(Chesspiece):
    def legalMove(self, board, new_col, new_row):
        if not Chesspiece.legalMove(board, new_col, new_row):
            return False
        if abs(new_row - self.row) == 2 and abs(new_col - self.col) == 1:
            return True
        elif abs(new_row - self.row) == 1 and abs(new_col - self.col) == 2:
            return True
class Bishop(Chesspiece):

class Rook(Chesspiece):
