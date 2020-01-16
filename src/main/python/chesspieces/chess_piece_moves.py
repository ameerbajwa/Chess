from src.main.python.chesspieces import creating_chess_pieces
import pandas as pd

key = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H':8}


def move_chess_piece(chess_piece, chess_piece_position, move_to, chessboard, player):

    chess_piece_location = []
    move_to_location = []
    
    chess_piece_location.append(int(chess_piece_position[0]))
    chess_piece_location.append(key[chess_piece_position[1]])
    
    move_to_location.append(int(move_to[0]))
    move_to_location.append(key[move_to[1]])

    if chess_piece == 'Pawn':
        move_pawn(chess_piece_location, move_to_location, chessboard, player)

    game_status = 'Continue'
    return game_status


def move_pawn(chess_piece_location, move_to_location, chessboard, player):
    
    if (chess_piece_location == creating_chess_pieces.Pawn.current_position):
        print('Selected Pawn')

        if player == 'White':
            if (move_to_location[0] == 5) and (chessboard.loc[6, move_to_location[1]] == ''):
                chessboard.loc[move_to_location[0], move_to_location[1]] = chessboard.loc[move_to_location[0]-2, move_to_location[1]]
                chessboard.loc[move_to_location[0]-2, move_to_location[1]] = ''
            else:
                chessboard.loc[move_to_location[0], move_to_location[1]] = chessboard.loc[move_to_location[0]-1, move_to_location[1]]
                chessboard.loc[move_to_location[0]-1, move_to_location[1]] = ''
    
        if player == 'Black':
            if (move_to_location[0] == 4) and (chessboard.loc[3, move_to_location[1]] == ''):
                chessboard.loc[move_to_location[0], move_to_location[1]] = chessboard.loc[move_to_location[0]+2, move_to_location[1]]
                chessboard.loc[move_to_location[0]+2, move_to_location[1]] = ''
            else:
                chessboard.loc[move_to_location[0], move_to_location[1]] = chessboard.loc[move_to_location[0]+1, move_to_location[1]]
                chessboard.loc[move_to_location[0]+1, move_to_location[1]] = ''

