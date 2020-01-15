import pandas as pd

def move_chess_piece(chess_piece, move_to, chessboard, player):

    if chess_piece == 'Pawn':
        move_pawn(move_to, chessboard, player)

    game_status = 'Contine'
    return game_status

def move_pawn(move_to, chessboard, player):
    if player == 'White':
        if (move_to[0] == 5) and (chessboard.loc[6, move_to[1]] == ''):
            chessboard.loc[move_to[0], move_to[1]] = chessboard[move_to[0]-2, move_to[1]]
            chessboard[move_to[0]-2, move_to[1]] = ''
        else:
            chessboard.loc[move_to[0], move_to[1]] = chessboard[move_to[0]-1, move_to[1]]
            chessboard[move_to[0]-1, move_to[1]] = ''

    if player == 'Black':
        if (move_to[0] == 4) and (chessboard.loc[3, move_to[1]] == ''):
            chessboard.loc[move_to[0], move_to[1]] = chessboard[move_to[0]+2, move_to[1]]
            chessboard[move_to[0]+2, move_to[1]] = ''
        else:
            chessboard.loc[move_to[0], move_to[1]] = chessboard[move_to[0]+1, move_to[1]]
            chessboard[move_to[0]+1, move_to[1]] = ''

