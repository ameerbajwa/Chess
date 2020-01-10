import pandas as pd
from src.main.python.chesspieces import creating_chess_pieces

def initialize_chessboard():
    chessboard = [[''] * 8 for i in range(0,8)]

    columns = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    indices = [i for i in range(1,9)]
    chessboard_table = pd.DataFrame(data=chessboard, columns=columns, index=indices)

    return (chessboard_table)

def initialize_chess_pieces(chessboard):

    white_king = creating_chess_pieces.King('White', [7, 3])
    chessboard.loc[8, 'D'] = white_king
    white_queen = creating_chess_pieces.Queen('White', [7, 4])
    chessboard.loc[8, 'E'] = white_queen

    white_bishop_1 = creating_chess_pieces.Bishop('White', [7, 2])
    chessboard.loc[8, 'C'] = white_bishop_1
    white_bishop_2 = creating_chess_pieces.Bishop('White', [7, 5])
    chessboard.loc[8, 'F'] = white_bishop_2

    white_knight_1 = creating_chess_pieces.Knight('White', [7, 1])
    chessboard.loc[8, 'B'] = white_knight_1
    white_knight_2 = creating_chess_pieces.Knight('White', [7, 6])
    chessboard.loc[8, 'G'] = white_knight_2

    white_rook_1 = creating_chess_pieces.Rook('White', [7, 0])
    chessboard.loc[8, 'A'] = white_rook_1
    white_rook_2 = creating_chess_pieces.Rook('White', [7, 7])
    chessboard.loc[8, 'H'] = white_rook_2

    white_pawns = []
    black_pawns = []

    for i in range(0,8):
        white_pawns.append(creating_chess_pieces.Pawn('White', [6,i]))
        chessboard.iloc[6,i] = white_pawns[i]
        black_pawns.append(creating_chess_pieces.Pawn('Black', [1,i]))
        chessboard.iloc[1,i] = black_pawns[i]

    black_king = creating_chess_pieces.King('Black', [0, 4])
    chessboard.loc[1, 'E'] = black_king
    black_queen = creating_chess_pieces.Queen('Black', [0, 3])
    chessboard.loc[1, 'D'] = black_queen

    black_bishop_1 = creating_chess_pieces.Bishop('Black', [0, 2])
    chessboard.loc[1, 'C'] = black_bishop_1
    black_bishop_2 = creating_chess_pieces.Bishop('Black', [0, 5])
    chessboard.loc[1, 'F'] = black_bishop_2

    black_knight_1 = creating_chess_pieces.Knight('Black', [0, 1])
    chessboard.loc[1, 'B'] = black_knight_1
    black_knight_2 = creating_chess_pieces.Knight('Black', [0, 6])
    chessboard.loc[1, 'G'] = black_knight_2

    black_rook_1 = creating_chess_pieces.Rook('Black', [0, 0])
    chessboard.loc[1, 'A'] = black_rook_1
    black_rook_2 = creating_chess_pieces.Rook('White', [0, 7])
    chessboard.loc[1, 'H'] = black_rook_2

    return (chessboard)