from chess_engine.classes import Piece
from chess_engine.util import Team



class Queen(Piece):
    def can_move(self, target):
        return super().can_move(target)
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
