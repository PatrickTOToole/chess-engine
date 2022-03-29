from chess_engine.classes import Piece
from chess_engine.util import Team



class King(Piece):
    def can_move(self, target):
        col_diff = abs(ord(self.curr.col) - ord(target.col))
        row_diff = abs(self.curr.row - target.row)
        if col_diff + row_diff == 1 or col_diff == row_diff == 1:
            # TODO
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
        return self.team_str + "K"
    def __repr__(self):
        return "K"
        