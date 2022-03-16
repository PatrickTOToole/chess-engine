from chess_engine.util import Team
from chess_engine.classes import Pawn


class Space:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.piece = None
        self.isPassant = False
        self.isAttacked = False
        self.passant_piece = None
    
    def setPiece(self, piece):
        if piece != None and piece.team == Team.BLACK and type(piece) == Pawn:
            if self.row == 1:
                options = {}
                input("Select N (knight), R (rook), B (bishop), Q (queen)")
                
                raise Exception("PROMOTION UNIMPLEMENTED")
        if piece != None and piece.team == Team.WHITE and type(piece) == Pawn:
            if self.row == 8:
                options = {}
                input("Select N (knight), R (rook), B (bishop), Q (queen)")
                
                raise Exception("PROMOTION UNIMPLEMENTED")
        self.piece = piece
        if piece != None:
            piece.curr = self
    def resetPassant(self):
        self.isPassant = False
        self.passant_piece = None
    def __str__(self):
        return f"{self.col}{self.row}: {self.piece}"
    def __repr__(self):
        return f"{self.col}{self.row}: {self.piece}"

