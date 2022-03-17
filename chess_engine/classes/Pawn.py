from chess_engine.classes import Piece
from chess_engine.util import Team



class Pawn(Piece):

    def can_move(self, target):
        inc = 0
        if self.team == Team.BLACK:
            inc = -1
        else:
            inc = 1

        # Check if it is a valid au Passant
        if self.is_passant(target):
            return True

        # Check if it is a valid standard attack move
        if target.piece != None and target.piece.team != self.team and not self.is_pinned:
            if target.row == self.curr.row + inc and abs(ord(target.col) - ord(self.curr.col)) == 1:
                if 0 < target.row <= 8 and 97 <= ord(self.curr.col) + ord(target.col) - ord(self.curr.col) < 105:
                    return True


        # Check if it is a valid 2 step move
        if self.creates_passant(target):
            return True
        
        # Check if it is a valid 1 step move
        if target.col == self.curr.col and target.row == self.curr.row + inc and target.piece == None:
            if 0 < self.curr.row + 1*inc <= 8:
                return True
        return False

    def setAttacking(self, target):
        inc = 0
        if self.team == Team.BLACK:
            inc = -1
        else:
            inc = 1
        if not self.is_pinned:
            if 0 < target.row + inc <= 8:
                if ord(target.col) != 97:
                    self.gameboard.board[chr(ord(target.col)-1)][target.row + inc].isAttacked = True
                if ord(target.col) != 104:
                    self.gameboard.board[chr(ord(target.col)+1)][target.row + inc].isAttacked = True
                
    def removeAttacking(self, target):
        inc = 0
        if self.team == Team.BLACK:
            inc = -1
        else:
            inc = 1
        if 0 < target.row + inc <= 8:
            if ord(target.col) != 97:
                self.gameboard.board[chr(ord(target.col)-1)][target.row + inc].isAttacked = False
            if ord(target.col) != 104:
                self.gameboard.board[chr(ord(target.col)+1)][target.row + inc].isAttacked = False


    def creates_passant(self, target):
        inc = 0
        if self.team == Team.BLACK:
            inc = -1
        else:
            inc = 1
        if not self.has_moved and target.col == self.curr.col and target.row == self.curr.row + 2*inc:
            if 0 < self.curr.row + 2*inc <= 8:
                return True
        return False
    def is_passant(self, target):
        inc = 0
        if self.team == Team.BLACK:
            inc = -1
        else:
            inc = 1
        if target.isPassant and target.passant_piece.team != self.team and not self.is_pinned:
            if target.row == self.curr.row + inc and abs(ord(target.col) - ord(self.curr.col)) == 1:
                return True
        return False
    def __str__(self):
        return self.team_str + "P"
    def __repr__(self):
        return "P"
        