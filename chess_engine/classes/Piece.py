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
    def creates_passant(self, target):
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
    def move(self, target):
        if self.is_pinned:
            return False
        if self.can_move(target):
            if self.creates_passant(target):
                inc = 0
                if self.team == Team.BLACK:
                    inc = -1
                else:
                    inc = 1
                self.gameboard.board[self.curr.col][int(self.curr.row) + inc].isPassant = True
                self.gameboard.board[self.curr.col][int(self.curr.row) + inc].passant_piece = self
                if self.gameboard.passant != None:
                    self.gameboard.passant.resetPassant()
                self.gameboard.passant = self.gameboard.board[self.curr.col][int(self.curr.row) + inc]
            if self.is_passant(target):
                target.onPassant(self)

            self.curr.setPiece(None)
            self.removeAttacking(self.curr)
            target.setPiece(self)
            self.setAttacking(target)
            self.has_moved = True
            self.gameboard.updateUI()
            return True
        else:
            return False
    
