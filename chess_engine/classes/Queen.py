from chess_engine.classes import Piece
from chess_engine.util import Team



class Queen(Piece):
    def can_move(self, target):
        line_space, can_line = self.cast_line(target)
        diag_space, can_diag = self.cast_diagonal(target)

        # Checks Bishop Move
        if can_diag and abs(ord(self.curr.col) - ord(target.col)) - abs(self.curr.row - target.row) == 0:
            if target.piece == None:
                return True, False
            if target.piece.team != self.team:
                return True, True
            else:
                return False, False
        # Checks Rook Move
        elif not can_line:
            return False, False
        elif abs(ord(self.curr.col) - ord(target.col)) != 0 and abs(self.curr.row - target.row) == 0:
            if target.piece == None:
                return True, False
            if target.piece.team != self.team:
                return True, True
            else:
                return False, False
        elif abs(ord(self.curr.col) - ord(target.col)) == 0 and abs(self.curr.row - target.row) != 0:
            if target.piece == None:
                return True, False
            if target.piece.team != self.team:
                return True, True
            else:
                return False, False
        else:
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
        return self.team_str + "Q"
    def __repr__(self):
        return "Q"
