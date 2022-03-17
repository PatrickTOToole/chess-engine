from chess_engine.classes import Piece
from chess_engine.util import Team



class Rook(Piece):
    def can_move(self, target):
        return super().can_move(target)

    def __str__(self):
        return self.team_str + "R"
    def __repr__(self):
        return "R"