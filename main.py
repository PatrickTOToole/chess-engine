from glob import glob
from operator import is_
from chess_engine import *
import tkinter as tk
import sys

window = tk.Tk()
board_frame = tk.Frame()
class moveWrapper:
    def __init__(self):
        self.move = []
mov = moveWrapper()
gameboard = GameBoard(board_frame, mov)
board_frame.pack()
is_white = True
logfile = open("log", "w+")
move_record = {1:[]}
move_count = 1

def doMove(team, moveNot):
    res = False
    cap = False
    global move_count
    global move_record
    # while(not res):
        # if team == Team.BLACK:
        #     team_str = "black"
        # else:
        #     team_str = "white"
        #move = input(f"move ({team_str}): ")

    m = moveNot.split("-")
    pieceRef = gameboard.getPieceAt(str(m[0]))
    if pieceRef == None or pieceRef.team != team:
        return move_count, move_record, False
    target = gameboard.getSpaceAt(m[1])
    res, cap = pieceRef.move(target)
    if cap:
        mid = "x"
    else:
        mid = "-"
    print(move_record[move_count], team == Team.BLACK)

    move_record[move_count].append(m[0] + mid + m[1])
    if gameboard.passant != None and gameboard.passant.passant_piece != None:
        if gameboard.passant.passant_piece.team != team:
            gameboard.passant.resetPassant()
            gameboard.passant = None
    if team == Team.BLACK:
        logfile.write(f"{move_count}: {move_record[move_count][0]} {move_record[move_count][1]}\n")
        move_count += 1


    return move_count, move_record, True

def task():
    global mov
    global is_white
    global move_count
    global move_record
    if len(mov.move) < 2:
        window.after(1, task)
    else:
        p1 = mov.move[0]
        p2 = mov.move[1]
        mov.move = []
        moveNot = f"{p1}-{p2}"
        if is_white:
            move_count, move_record, res = doMove(Team.WHITE, moveNot)
            is_white = False
        else:
            move_count, move_record, res = doMove(Team.BLACK, moveNot)
            move_record[move_count] = []
            is_white = True

        window.after(0, task)

    
window.after(0, task)
window.mainloop()
