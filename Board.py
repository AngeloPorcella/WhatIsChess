import pieces

rows = int(8)
cols = int(8)
pieceList = {}
moveLog = () # TODO make this track pieces and their moves set up as a 2-tuple of piece, end location
board = [[0 for i in range(cols)] for j in range(rows)]


def printBoard():
    for row in board:
        print()
        for square in row:
            print(squareBehavior(square), end=" ")


# black pieces have a value below 0, white pieces have a positive value
def squareBehavior(square) -> str:
    if square == 0:
        return "+"
    elif square == 1:
        return "P"
    elif square == 2:
        return "N"  # N is for knight
    elif square == 3:
        return "B"
    elif square == 4:
        return "R"
    elif square == 5:
        return "Q"
    elif square == 6:
        return "K"
    elif square == -1:
        return "p"
    elif square == -2:
        return "n"
    elif square == -3:
        return "b"
    elif square == -4:
        return "r"
    elif square == -5:
        return "q"
    elif square == -6:
        return "k"


# Initialize all pieces in a standard setup
def updateBoard():
    for i in range(rows):
        for j in range(cols):
            board[i][j] = 0
    for key, value in pieceList.items():
        pos = key.getPos()
        row = pos[0]
        column = pos[1]
        board[row][column] = key.type
    printBoard()


def getKey(val):
    for key, value in pieceList.items():
        if val == value:
            return key

def checkTarget(piece):
    # this shit is fucked. Please look through
    for key in pieceList:
        for move in key.moveList:
            for value in pieceList.values():
                currPos = key.getPos()
                y = move[0] - currPos[0]
                x = move[1] - currPos[1]
                newPos = (y, x)
                if newPos == value:
                    print("Dis shit gotta sightline x ray stype")
                else:
                    print("nobody lookin")


    # TODO Check every possible square hit by every piece after a move is played
    # TODO this is to ensure pins arent missed
# TODO Verify pieces can't move through other pieces
# TODO Make a method for capturing pieces - can't capture own pieces
# TODO Make a method that checks sightlines (for checks and such)
# TODO Make sure moved pieces are tracked (en passant and castling)
# TODO Make turns a thing
# TODO Eventually make a GUI
def movePiece():
    whatPiece = input("Select a piece: ")
    inputList = whatPiece.split()
    column = inputList[0]
    row = inputList[1]
    currPos = decodeInput((column, row))
    piece = getKey(currPos)
    if piece is None:
        print("No piece here")
        return

    whereTo = input("To: ")
    inputList = whereTo.split()
    column = inputList[0]
    row = inputList[1]
    move = decodeInput((column, row))
    y = move[0] - currPos[0]
    x = move[1] - currPos[1]
    posChange = (y, x)

    if posChange in piece.getMoveList():
        standingPiece = getKey(move)
        if standingPiece is None or standingPiece.color != piece.color:
            print(piece.name + " has moved to " + whereTo + ".")
            if standingPiece is not None and standingPiece.color != piece.color:
                del pieceList[standingPiece]
            pieceList[piece] = move
            piece.currentPos = move
            updateBoard()
        else:
            print("not a legal move")
            if piece.name == "Pawn" or piece.name == "King":
                piece.pieceMoved()
    else:

        print("not a legal move")


def decodeInput(moveTuple):
    startRow = int(moveTuple[1])
    row = 8 - startRow
    column = 0
    if moveTuple[0] == 'a':
        column = 0
    elif moveTuple[0] == 'b':
        column = 1
    elif moveTuple[0] == 'c':
        column = 2
    elif moveTuple[0] == 'd':
        column = 3
    elif moveTuple[0] == 'e':
        column = 4
    elif moveTuple[0] == 'f':
        column = 5
    elif moveTuple[0] == 'g':
        column = 6
    elif moveTuple[0] == 'h':
        column = 7
    return row, column


# simple play loop for testing
def playLoop():
    updateBoard()
    print()
    choice = input("would you like to play? y/n ->")
    if choice == "y":
        while choice != "n":
            movePiece()


# setup for pieces on the board
wPawn1 = pieces.Pawn(1, (6, 0))
pieceList[wPawn1] = wPawn1.getPos()
wPawn2 = pieces.Pawn(1, (6, 1))
pieceList[wPawn2] = wPawn2.getPos()
wPawn3 = pieces.Pawn(1, (6, 2))
pieceList[wPawn3] = wPawn3.getPos()
wPawn4 = pieces.Pawn(1, (6, 3))
pieceList[wPawn4] = wPawn4.getPos()
wPawn5 = pieces.Pawn(1, (6, 4))
pieceList[wPawn5] = wPawn5.getPos()
wPawn6 = pieces.Pawn(1, (6, 5))
pieceList[wPawn6] = wPawn6.getPos()
wPawn7 = pieces.Pawn(1, (6, 6))
pieceList[wPawn7] = wPawn7.getPos()
wPawn8 = pieces.Pawn(1, (6, 7))
pieceList[wPawn8] = wPawn8.getPos()

bPawn1 = pieces.Pawn(-1, (1, 0))
pieceList[bPawn1] = bPawn1.getPos()
bPawn2 = pieces.Pawn(-1, (1, 1))
pieceList[bPawn2] = bPawn2.getPos()
bPawn3 = pieces.Pawn(-1, (1, 2))
pieceList[bPawn3] = bPawn3.getPos()
bPawn4 = pieces.Pawn(-1, (1, 3))
pieceList[bPawn4] = bPawn4.getPos()
bPawn5 = pieces.Pawn(-1, (1, 4))
pieceList[bPawn5] = bPawn5.getPos()
bPawn6 = pieces.Pawn(-1, (1, 5))
pieceList[bPawn6] = bPawn6.getPos()
bPawn7 = pieces.Pawn(-1, (1, 6))
pieceList[bPawn7] = bPawn7.getPos()
bPawn8 = pieces.Pawn(-1, (1, 7))
pieceList[bPawn8] = bPawn8.getPos()

bRook1 = pieces.Rook(-1, (0, 0))
pieceList[bRook1] = bRook1.getPos()
bRook2 = pieces.Rook(-1, (0, 7))
pieceList[bRook2] = bRook2.getPos()

wRook1 = pieces.Rook(1, (7, 0))
pieceList[wRook1] = wRook1.getPos()
wRook2 = pieces.Rook(1, (7, 7))
pieceList[wRook2] = wRook2.getPos()

bKnight1 = pieces.Knight(-1, (0, 1))
pieceList[bKnight1] = bKnight1.getPos()
bKnight2 = pieces.Knight(-1, (0, 6))
pieceList[bKnight2] = bKnight2.getPos()

wKnight1 = pieces.Knight(1, (7, 1))
pieceList[wKnight1] = wKnight1.getPos()
wKnight2 = pieces.Knight(1, (7, 6))
pieceList[wKnight2] = wKnight2.getPos()

bBishop1 = pieces.Bishop(-1, (0, 2))
pieceList[bBishop1] = bBishop1.getPos()
bBishop2 = pieces.Bishop(-1, (0, 5))
pieceList[bBishop2] = bBishop2.getPos()

wBishop1 = pieces.Bishop(1, (7, 2))
pieceList[wBishop1] = wBishop1.getPos()
wBishop2 = pieces.Bishop(1, (7, 5))
pieceList[wBishop2] = wBishop2.getPos()

bQueen = pieces.Queen(-1, (0, 3))
pieceList[bQueen] = bQueen.getPos()
wQueen = pieces.Queen(1, (7, 3))
pieceList[wQueen] = wQueen.getPos()

bKing = pieces.King(-1, (0, 4))
pieceList[bKing] = bKing.getPos()
wKing = pieces.King(1, (7, 4))
pieceList[wKing] = wKing.getPos()

playLoop()
