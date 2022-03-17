from chess_engine import *
import tkinter as tk

window = tk.Tk()
board_frame = tk.Frame()
gam = GameBoard(board_frame)
board_frame.pack()





def task(move_count, move_record):
    print(gam)
    res = False
    move_record[move_count] = []
    while(not res):
        move = input("move (white): ")
        m = move.split("-")
        pieceRef = gam.getPieceAt(str(m[0]))
        if pieceRef == None:
            continue
        target = gam.getSpaceAt(m[1])
        res = pieceRef.move(target)
    move_record[move_count].append(move)
    res = False
    while(not res):
        move = input("move (black): ")
        m = move.split("-")
        pieceRef = gam.getPieceAt(str(m[0]))
        if pieceRef == None:
            continue
        target = gam.getSpaceAt(m[1])
        res = pieceRef.move(target)
    move_record[move_count].append(move)
    res = False
    print(gam)
    move_count += 1
    window.after(0, task, move_count, move_record)

move_record = {}
window.after(0, task, 0, move_record)
window.mainloop()