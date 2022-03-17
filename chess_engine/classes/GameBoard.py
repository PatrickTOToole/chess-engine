from chess_engine.classes import Space
from chess_engine.classes import Pawn
from chess_engine.util.Team import Team
import tkinter as tk

class GameBoard:
    def __init__(self, frame):
        self.elts = {}

        for i in range(8):
            new_arr = {}
            for j in range(1,9):
                rank = i % 2
                file = j % 2
                color = (rank + file) % 2
                bg_curr = "brown"
                if color:
                    bg_curr = "tan"
                label = tk.Label(master=frame, text="hello", bg=bg_curr, width = 5, height=2)
                label.grid(row = 8-(j - 1) , column = i)
                new_arr[j] = label
            self.elts[chr(97 + i)] = new_arr
        # for i in range(8):
        #     elts.append([])
        #     for j in range(1,9):
        #         rank = i % 2
        #         file = j % 2
        #         color = (rank + file) % 2
        #         bg_curr = "brown"
        #         if color:
        #             bg_curr = "tan"
        #         label = tk.Label(master=frame, text="hello", bg=bg_curr, width = 5, height=2)
        #         label.grid(row = i, column = (j - 1))
        #         elts[i].append(label)
        # elts[2][2].config(text = "goodb")
        # self.elts = elts
        self.frame = frame
        self.board = {}
        for i in range(8):
            new_arr = {}
            for j in range(1,9):
                rank = i % 2
                file = j % 2
                color = (rank + file) % 2
                new_arr[j] = Space(chr(97 + i), j, color)
            self.board[chr(97 + i)] = new_arr
        for i in range(8):
            self.board[chr(97 + i)][2].piece = Pawn(Team.WHITE, self.board[chr(97 + i)][2], self)
            self.board[chr(97 + i)][7].piece = Pawn(Team.BLACK, self.board[chr(97 + i)][7], self)
            self.elts[chr(97 + i)][2].config(text = "wP")
            self.elts[chr(97 + i)][7].config(text = "bP")
    
    def updateUI(self):
        for i in range(8):
            for j in range(1,9):
                self.elts[chr(97 + i)][j].config(text = str(self.board[chr(97 + i)][j].piece))


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