from chess_engine.util import Team
from chess_engine.classes import Pawn
from chess_engine.classes import Knight
from chess_engine.classes import Queen
from chess_engine.classes import Rook
from chess_engine.classes import Bishop


class Space:
    def __init__(self, col, row, color, gameboard):
        self.col = col
        self.row = row
        self.piece = None
        self.isPassant = False
        self.passant_piece = None
        self.color = color
        self.gameboard = gameboard

    def setPiece(self, piece):
        # if piece != None and piece.team == Team.BLACK and type(piece) == Pawn:
        #     if self.row == 1:
        #         options = {}
        #         sel = input("Select N (knight), R (rook), B (bishop), Q (queen)")
                
        #         raise Exception("PROMOTION UNIMPLEMENTED")
        # if piece != None and piece.team == Team.WHITE and type(piece) == Pawn:
        #     if self.row == 8:
        if piece != None and type(piece) == Pawn:
            if piece.team == Team.BLACK:
                row = 1
            else:
                row = 8
            if self.row == row:
                options = {
                    "N": Knight(piece.team, self, self.gameboard),
                    "R": Rook(piece.team, self, self.gameboard),
                    "B": Bishop(piece.team, self, self.gameboard),
                    "Q": Queen(piece.team, self, self.gameboard),
                    }
                sel = input("Select N (knight), R (rook), B (bishop), Q (queen)")
                piece = options[sel]
                
        self.piece = piece
        if piece != None:
            piece.curr = self
    def onPromote(self, piece):
        if piece != None and piece.team == Team.WHITE and type(piece) == Pawn:
            if piece.team == Team.BLACK:
                row = 1
            else:
                row = 8
            if self.row == row:
                options = {}
                sel = input("Select N (knight), R (rook), B (bishop), Q (queen)")
                
                raise Exception("PROMOTION UNIMPLEMENTED")

    def onPassant(self, attacker):
        inc = 0
        if attacker.team == Team.BLACK:
            inc = -1
        else:
            inc = 1
        self.gameboard.board[self.col][int(self.row) - inc].piece = None
        self.passant_piece = None
        self.isPassant = False
        self.gameboard.updateUI()
    def resetPassant(self):
        self.isPassant = False
        self.passant_piece = None
    def __str__(self):
        if self.piece:
            return f"{self.col}: {self.isPassant}"
        else:
            return f"{self.col}: {self.isPassant}"

    def __repr__(self):
        if self.piece:
            return f"{self.col}: {self.isPassant}"
        else:
            return f"{self.col}: {self.isPassant}"
