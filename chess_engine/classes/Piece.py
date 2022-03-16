from abc import ABC, abstractmethod
from chess_engine.util.Team import Team

class Piece(ABC):
    def __init__(self, team, curr, gameboard):
        self.team = team
        if team == Team.BLACK:
            self.team_str = "b"
        else:
            self.team_str = "w"

        self.curr = curr
        self.is_pinned = False
        self.has_moved = False
        self.gameboard = gameboard
    
    @abstractmethod
    def can_move(self, target):
        pass
    @abstractmethod
    def is_passant(self, target):
        pass
    @abstractmethod
    def setAttacking(self, target):
        pass
    @abstractmethod
    def removeAttacking(self, target):
        pass
    def move(self, team, target):
        if self.can_move(target):
            if not self.is_passant(target):
                self.curr.setPiece(None)
            else:
                self.curr.isPassant = True
                self.curr.passant_piece = self
            self.removeAttacking(self.curr)
            target.setPiece(self)
            self.setAttacking(target)
            self.has_moved = True
            return True
        else:
            return False
    
