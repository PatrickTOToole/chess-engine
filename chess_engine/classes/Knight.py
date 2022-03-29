from chess_engine.classes import Piece
from chess_engine.util import Team



class Knight(Piece):
    def can_move(self, target):
        col_diff = abs(ord(self.curr.col) - ord(target.col))
        row_diff = abs(self.curr.row - target.row)
        if row_diff + col_diff == 3 and row_diff != 0 and col_diff != 0:
            if target.piece == None:
                return True, False
            if target.piece.team != self.team:
                return True, True
            else:
                return False, False
        return False, False
    def creates_passant(self, target):
        return super().creates_passant(target)
    def is_passant(self, target):
        return super().is_passant(target)
    def removeAttacking(self, target):
        return super().removeAttacking(target)
    def setAttacking(self, target):
        return super().setAttacking(target)
    def __str__(self):
        return self.team_str + "N"
    def __repr__(self):
        return "N"
        