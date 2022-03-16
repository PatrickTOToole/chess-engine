from chess_engine.classes import Space
from chess_engine.classes import Pawn
from chess_engine.util.Team import Team

class GameBoard:
    def __init__(self):
        self.board = {}
        for i in range(8):
            new_arr = {}
            for j in range(1,9):
                new_arr[j] = Space(chr(97 + i), j)
            self.board[chr(97 + i)] = new_arr
        for i in range(8):
            self.board[chr(97 + i)][2].piece = Pawn(Team.WHITE, self.board[chr(97 + i)][2], self)
            self.board[chr(97 + i)][7].piece = Pawn(Team.BLACK, self.board[chr(97 + i)][7], self)

    def getPieceAt(self, notation: str):
        if len(notation) == 2:
            col = notation[0]
            row = int(notation[1])
            return self.board[col][row].piece
        else:
            raise Exception("Invalid Notation - Expected: [a-h][1-8]")
    def getSpaceAt(self, notation: str):
        if len(notation) == 2:
            col = notation[0]
            row = int(notation[1])
            return self.board[col][row]
        else:
            raise Exception("Invalid Notation - Expected: [a-h][1-8]")
    def __str__(self):
        out = ""
        for i in self.board:
            out += str(self.board[i]) + "\n"
        return out