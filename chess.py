import string
class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 0
class Chessboard:
    def __init__(self, setup):
        self.pieces = setup
    def __str__(self):
        for i in range(1, 9):
            for j in string.ascii_lowercase[:8]:
                if self.getPiece(i, j):
                    print(self.getPiece(i, j))
                else:
                    print('x')
    def getPiece(self, row, col):
        for p in self.pieces:
            return p if p.col == col and p.row == row
        return None
    def move(self, piece, newloc):
        if legalMove(self, piece, newloc):
            setPosition(piece, newloc)
class Chesspiece:
    canPromote = False
    def __init__(self, loc):
        self.col = loc[0]
        self.row = loc[1]
    def legalMove(self, board, newloc):
        return newloc[0] <= 'h' and newloc[1] <= 8:

class Queen(Chesspiece):
    
class King(Chesspiece):

class Pawn(Chesspiece):

class Knight(Chesspiece):

class Bishop(Chesspiece):

class Rook(Chesspiece):
