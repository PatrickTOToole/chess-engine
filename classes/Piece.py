from abc import ABC, abstractmethod
from chess-engine/classes import Space
from chess-engine/util import Team

class Piece(ABC):
    def __init__(self, Team team):
        self.team = team;
        self.is_pinned = False;
    
    @abstractmethod
    def can_move(self, curr :Space, target :Space):
        pass
    def move(self, Space curr, Space target):
        if self.can_move(curr, target):
            curr.setPiece(None)
            target.setPiece(self)
            return True
        else:
            return False
    
