from chess-engine/util import Team
from chess-engine/classes import Piece


class Space:
    def __init__(self, col, row):
        self.col = col
        self.row = row
        self.piece = None
        self.isPassant = False
    
    def setPiece(self, piece :Piece):
        self.piece = piece
        
