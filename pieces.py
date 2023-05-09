class Piece:
    def __init__(self, color, currentPos):
        if color > 0:
            self.color = "white"
        elif color < 0:
            self.color = "black"
        self.currentPos = currentPos
        self.alive = True
        self.moveList = ()


    def getMoveList(self):
        return self.moveList


    def getPos(self):
        return self.currentPos


    def isAlive(self):
        return self.alive


    def getColor(self):
        return self.color

class Pawn(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "Pawn"
        self.moved = False
        self.val = 1
        if self.color == "white":
            self.type = 1
        else:
            self.type = -1
            # MAKE SURE TO CHANGE MOVED TO TRUE ONCE THIS HAS BEEN DONE
        if self.color == "black":
            self.moveList = ((1, 0), (2, 0), (1, 1), (1, -1))  # move forward 2, attack right, attack left
        else:
            self.moveList = ((-1, 0), (-2, 0), (-1, 1), (-1, -1))  # move forward 2, attack right, attack left


    def pieceMoved(self):
        self.moved = True
        if self.color == "black":
            self.moveList = ((1, 0), (1, 1), (1, -1))  # move forward, attack right, attack left
        else:
            self.moveList = ((-1, 0), (-1, 1), (-1, -1))  # move forward, attack right, attack left




class Knight(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "Knight"
        self.val = 3
        if self.color == "white":
            self.type = 2
        else:
            self.type = -2
        self.moveList = (
            (2, 1), (2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2), (-2, 1), (-2, -1)
        )


class Bishop(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "Bishop"
        self.val = 3
        if self.color == "white":
            self.type = 3
        else:
            self.type = -3
        self.moveList = (
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)
        )


class Rook(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "Rook"
        self.moved = False
        self.val = 4
        if self.color == "white":
            self.type = 4
        else:
            self.type = -4
        self.moveList = (
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0)
        )


class Queen(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "Queen"
        self.val = 8
        if self.color == "white":
            self.type = 5
        else:
            self.type = -5
        self.moveList = (
            (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
            (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0),
            (0, -1), (0, -2), (0, -3), (0, -4), (0, -5), (0, -6), (0, -7),
            (-1, 0), (-2, 0), (-3, 0), (-4, 0), (-5, 0), (-6, 0), (-7, 0),
            (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7),
            (-1, -1), (-2, -2), (-3, -3), (-4, -4), (-5, -5), (-6, -6), (-7, -7),
            (1, -1), (2, -2), (3, -3), (4, -4), (5, -5), (6, -6), (7, -7),
            (-1, 1), (-2, 2), (-3, 3), (-4, 4), (-5, 5), (-6, 6), (-7, 7)
        )


class King(Piece):
    def __init__(self, color, currentPos):
        super().__init__(color, currentPos)
        self.name = "King"
        if self.color == "white":
            self.type = 6
        else:
            self.type = -6
        self.moved = False
        self.checked = False
        self.canCastle = True
        if self.moved:
            self.moveList = (
                (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)
            )
        else:
            if self.canCastle:
                self.moveList = (
                    (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1), (0, 2), (0, -2)
                )
            else:
                self.moveList = (
                    (0, 1), (1, 0), (0, -1), (-1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)
                )
