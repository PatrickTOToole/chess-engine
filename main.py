from chess_engine import *
import tkinter as tk

window = tk.Tk()
board_frame = tk.Frame()
gameboard = GameBoard(board_frame)
board_frame.pack()

def doMove(move_count, move_record, team):
    res = False
    while(not res):
        if team == Team.BLACK:
            team_str = "black"
        else:
            team_str = "white"
        move = input(f"move ({team_str}): ")
        m = move.split("-")
        pieceRef = gameboard.getPieceAt(str(m[0]))
        if pieceRef == None or pieceRef.team != team:
            continue
        target = gameboard.getSpaceAt(m[1])
        res = pieceRef.move(target)
    move_record[move_count].append(move)
    if gameboard.passant != None and gameboard.passant.passant_piece != None:
        if gameboard.passant.passant_piece.team != team:
            gameboard.passant.resetPassant()
            gameboard.passant = None
    print(gameboard)
    if team == Team.BLACK:
        move_count += 1
    return move_count, move_record

def task(move_count, move_record):
    move_record[move_count] = []
    doMove(move_count, move_record, Team.WHITE)
    doMove(move_count, move_record, Team.BLACK)
    window.after(0, task, move_count, move_record)

move_record = {}
window.after(0, task, 0, move_record)
window.mainloop()