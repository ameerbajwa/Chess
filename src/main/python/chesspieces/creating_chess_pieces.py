
# CREATE A CLASS TITLED CHESS PIECE WHERE IT HAS THE SAME __init__ and __repr__ functions for each chess piece
#  THEN EACH CHESS PIECE SHOULD EXTEND THIS CLASS

class King():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_K')

class Queen():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_Q')

class Bishop():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_B')

class Knight():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_Kn')

class Rook():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_R')

class Pawn():
    def __init__(self, player, chess_piece, current_position):
        self.player = player
        self.chess_piece = chess_piece
        self.current_position = current_position

    def __repr__(self):
        return (self.player[0] + '_p')




