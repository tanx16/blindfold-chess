from game import *
class Chesspiece:
    canPromote = False
    checked = False
    def __init__(self, col, row, color):
        self.row = row
        self.col = col
        self.color = color
        self.moved = False
    def __str__(self):
        return self.name # + " (" + self.color + ")"
    def legalMove(self, board, new_col, new_row):
        #inside the board, no piece in destination that is your piece, is your piece
        if new_col < 8 and new_col >= 0 and new_row < 8 and new_row >= 0 and self.color == board.turn and not board.kingInCheck(board.kingPos):
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
    def legalCastle(self, board, side):
        if side == "k":
            if self.color == "white":
                rook_piece = board.pieces[0][7]
                if self.moved or rook_piece.moved:
                    return False
                for i in board.pieces[0][5:7]:
                    if i:
                        return False
                for j in range(5, 7):
                    if kingInCheck(0, j):
                        return False
                return True
            else:
                rook_piece = board.pieces[7][7]
                if self.moved or rook_piece.moved:
                    return False
                for i in board.pieces[7][5:7]:
                    if i:
                        return False
                for j in range(5, 7):
                    if kingInCheck(7, j):
                        return False
                return True
        if side == "q":
            if self.color == "white":
                rook_piece = board.pieces[0][0]
                if self.moved or rook_piece.moved:
                    return False
                for i in board.pieces[0][1:4]:
                    if i:
                        return False
                for j in range(1, 4):
                    if kingInCheck(7, j):
                        return False
                return True
            else:
                rook_piece = board.pieces[7][0]
                if self.moved or rook_piece.moved:
                    return False
                for i in board.pieces[7][1:4]:
                    if i:
                        return False
                for j in range(1, 4):
                    if kingInCheck(0, j):
                        return False
                return True
class Pawn(Chesspiece):
    name = "p"
    def legalMove(self, board, new_col, new_row):
        destination = board.pieces[new_row][new_col]
        if not Chesspiece.legalMove(self, board, new_col, new_row):
            return False
        if self.color == "white":
            direction = 1
        else:
            direction = -1
        if new_col == self.col and not destination:
            if new_row == self.row + direction:
                return True
            elif new_row == self.row + 2*direction and not self.moved:
                board.doubleMoved = 2
                return True
            else:
                return False
        elif new_row == self.row + direction and abs(new_col - self.col) == 1:
            if destination:
                return True
            elif isinstance(board.pieces[self.row][new_col], Pawn) and board.doubleMoved > 0:
                board.takePiece(new_col, new_row - direction) #Captures the doubleMoved pawn
                return True
            else:
                return False
        else:
            return False
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
