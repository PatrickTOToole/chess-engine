from chess_engine.classes import Space
from chess_engine.classes import Pawn
from chess_engine.classes import Queen
from chess_engine.classes import King
from chess_engine.classes import Rook
from chess_engine.classes import Bishop
from chess_engine.classes import Knight
from chess_engine.util.Team import Team

import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk

def toChr(num):
    return chr(96 + num)

class objWrapper:
    def __init__(self, obj, col, row, move):
        self.obj = obj
        self.col = col
        self.row = row
        self.mov = move
    def callback(self, event):
        self.mov.move.append(f"{toChr(self.col)}{self.row}")
        print(self.mov.move)

class GameBoard:
    def __init__(self, frame, move, root):
        self.elts = {}
        self.board = {}
        self.frame = frame
        self.passant = None
        self.move = move
        self.root = root
        for i in range(1,9):
            tk_arr = {}
            new_arr = {}
            for j in range(1,9):
                rank = self.toStdIdx(i) % 2
                file = j % 2
                color = (rank + file) % 2
                new_arr[j] = Space(self.toChr(i), j, color, self)
                bg_curr = "brown"
                if color:
                    bg_curr = "tan"
                #test = ImageTk.PhotoImage(image1)
                #label = tk.Label(image=test)
                #label = tk.Label(master=frame, text="", bg=bg_curr, width = 5, height=2)
                label = tk.Label(master=frame, bg=bg_curr)#, width = 5, height=2)
                wlabel = objWrapper(label, i, j, self.move)
                wlabel.obj.callback = wlabel.callback
                wlabel.obj.bind("<Button-1>", wlabel.obj.callback)
                wlabel.obj.grid(row = 8-(self.toStdIdx(j)) , column = self.toStdIdx(i))
                tk_arr[j] = wlabel
            self.elts[self.toChr(i)] = tk_arr
            self.board[self.toChr(i)] = new_arr
            
        for i in range(1,9):
            self.addPiece(Pawn(Team.WHITE, self.board[self.toChr(i)][2], self), i, 2)
            self.addPiece(Pawn(Team.BLACK, self.board[self.toChr(i)][7], self), i, 7)
        
        self.addPiece(Rook(Team.WHITE, self.board["a"][1], self), 1, 1)
        self.addPiece(Rook(Team.BLACK, self.board["a"][8], self), 1, 8)

        self.addPiece(Knight(Team.WHITE, self.board["b"][1], self), 2, 1)
        self.addPiece(Knight(Team.BLACK, self.board["b"][8], self), 2, 8)

        self.addPiece(Bishop(Team.WHITE, self.board["c"][1], self), 3, 1)
        self.addPiece(Bishop(Team.BLACK, self.board["c"][8], self), 3, 8)

        self.addPiece(King(Team.WHITE, self.board["d"][1], self), 4, 1)
        self.addPiece(King(Team.BLACK, self.board["d"][8], self), 4, 8)

        self.addPiece(Queen(Team.WHITE, self.board["e"][1], self), 5, 1)
        self.addPiece(Queen(Team.BLACK, self.board["e"][8], self), 5, 8)

        self.addPiece(Bishop(Team.WHITE, self.board["f"][1], self), 6, 1)
        self.addPiece(Bishop(Team.BLACK, self.board["f"][8], self), 6, 8)

        self.addPiece(Knight(Team.WHITE, self.board["g"][1], self), 7, 1)
        self.addPiece(Knight(Team.BLACK, self.board["g"][8], self), 7, 8)

        self.addPiece(Rook(Team.WHITE, self.board["h"][1], self), 8, 1)
        self.addPiece(Rook(Team.BLACK, self.board["h"][8], self), 8, 8)
    
    def toChr(self, num):
        return chr(96 + num)
    def toStdIdx(self,num):
        return num - 1
    def addPiece(self, pc, i, j):
        self.board[self.toChr(i)][j].piece = pc
        self.elts[self.toChr(i)][j].obj.config(text = str(pc))
        test = PhotoImage(file = f"./assets/{str(pc)}.png")
        self.elts[self.toChr(i)][j].obj.config(image = test)
        self.elts[self.toChr(i)][j].obj.image = test



    def updateUI(self):
        for i in range(1,9):
            for j in range(1,9):
                pz = str(self.board[self.toChr(i)][j].piece)
                if pz == "None":
                    pz = ""
                    self.elts[self.toChr(i)][j].obj.config(image = None)
                self.elts[self.toChr(i)][j].obj.config(text = pz)
                if pz != "":
                    test = PhotoImage(file = f"./assets/{str(pz)}.png")
                    self.elts[self.toChr(i)][j].obj.config(image = test)
                    self.elts[self.toChr(i)][j].obj.image = test


    def getPieceAt(self, notation: str):
        if len(notation) == 2:
            col = notation[0]
            row = int(notation[1])
            return self.board[col][row].piece
        else:
            return None
    def getSpaceAt(self, notation: str):
        if len(notation) == 2:
            col = notation[0]
            row = int(notation[1])
            return self.board[col][row]
        else:
            return None
    def __str__(self):
        out = ""
        for i in self.board:
            out += str(self.board[i]) + "\n"
        return out
        