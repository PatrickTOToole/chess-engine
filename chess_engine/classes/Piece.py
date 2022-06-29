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
        return False, False
    def cast_line(self, target):
        dir = [0,0]
        if target.col == self.curr.col and target.row != self.curr.row:
            dir = [1, target.row - self.curr.row]
        elif target.row == self.curr.row:
            dir = [-1, ord(target.col)- ord(self.curr.col)]
        curr_check = [ord(self.curr.col), self.curr.row]
        if dir[0] == 0: return None, False
        dir_num = 0
        if dir[1] > 0:
            dir_num = 1
        else:
            dir_num = -1
        if dir[0] == 1:
            while curr_check[1] != target.row - dir_num:
                curr_check[1] = curr_check[1] + dir_num
                curr_space = self.gameboard.board[chr(curr_check[0])][curr_check[1]]
                curr_piece = curr_space.piece
                if curr_piece != None:
                    return curr_space, False

        else:
            while curr_check[0] != ord(target.col) - dir_num:
                curr_check[0] = curr_check[0] + dir_num
                curr_space = self.gameboard.board[chr(curr_check[0])][curr_check[1]]
                curr_piece = curr_space.piece
                if curr_piece != None:
                    return curr_space, False


        spaces = []
        return None, True
    def cast_diagonal(self, target):
        dir = [0,0]
        dir[0] = ord(target.col) - ord(self.curr.col)
        dir[1] = target.row - self.curr.row
        if abs(dir[0]) != abs(dir[1]):
            return 0, False
        if dir[0] == 0:
            return 0, False
        else:
            if abs(dir[0]) == 1:
                return 0, True
            dir[0] = int(dir[0] / abs(dir[0]))
            dir[1] = int(dir[1] / abs(dir[1]))
            curr_check = [ord(self.curr.col), self.curr.row]
            while curr_check[0] != ord(target.col) -1  and curr_check[1] != target.row -1:
                curr_check[0] += dir[0]
                curr_check[1] += dir[1]
                curr_space = self.gameboard.board[chr(curr_check[0])][curr_check[1]]
                curr_piece = curr_space.piece
                if curr_piece != None:
                    return curr_space, False

            print(dir)
            return 0, True

        
    @abstractmethod
    def creates_passant(self, target):
        return False
    @abstractmethod
    def is_passant(self, target):
        return False
    @abstractmethod
    def setAttacking(self, target):
        pass
    @abstractmethod
    def removeAttacking(self, target):
        pass
    def move(self, target):
        if self.is_pinned:
            return False
        canMove, cap = self.can_move(target)
        if canMove:
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
            return True, cap
        else:
            return False, False
    