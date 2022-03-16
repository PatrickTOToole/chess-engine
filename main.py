from chess_engine import *

gam = GameBoard()
print(gam)
move_count = 1
move_record = {}
res = False
while True:
    move_record[move_count] = []
    while(not res):
        move = input("move (white): ")
        m = move.split("-")
        pieceRef = gam.getPieceAt(str(m[0]))
        if pieceRef == None:
            continue
        target = gam.getSpaceAt(m[1])
        res = pieceRef.move(Team.WHITE, target)
    move_record[move_count].append(move)
    res = False
    while(not res):
        move = input("move (black): ")
        m = move.split("-")
        pieceRef = gam.getPieceAt(str(m[0]))
        if pieceRef == None:
            continue
        target = gam.getSpaceAt(m[1])
        res = pieceRef.move(Team.BLACK, target)
    move_record[move_count].append(move)
    res = False

    print(gam)
    move_count += 1