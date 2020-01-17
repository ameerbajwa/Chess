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
        if (chessboard.iloc[chess_piece_location[0]-1, chess_piece_location[1]-1].chess_piece == 'Pawn'):
            # and (chessboard.iloc[chess_piece_location[0]-1, chess_piece_location[1]-1].current_position[0] == chess_piece_location[0]-1) and (chessboard.iloc[chess_piece_location[0]-1, chess_piece_location[1]-1].current_position[1] == chess_piece_location[1]-1):
            print('Selected a Pawn')
            chessboard = move_pawn(chess_piece_location, move_to_location, chessboard, player)
        else:
            print('Chess piece selected is not a pawn')

    game_status = 'Continue'
    return chessboard, game_status


def move_pawn(chess_piece_location, move_to_location, chessboard, player):

    new_loc_y = move_to_location[0]-1
    new_loc_x = move_to_location[1]-1
    old_loc_y = chess_piece_location[0]-1
    old_loc_x = chess_piece_location[1]-1

    blank_spot_condition = (chessboard.iloc[new_loc_y, new_loc_x] == '.')
    move_1_spot = (old_loc_y-new_loc_y)**2 == 1 and (old_loc_x-new_loc_x)**2 == 0
    move_2_spot = (old_loc_y-new_loc_y)**2 == 4 and (old_loc_x-new_loc_x)**2 == 0
    attack = (old_loc_y-new_loc_y)**2 == 1 and (old_loc_x-new_loc_x)**2 == 1

    if (player == 'White' and old_loc_y-new_loc_y == 1 and old_loc_x-new_loc_x == 0) or (player == 'Black' and new_loc_y-old_loc_y == 1 and old_loc_x-new_loc_x == 0):
        chessboard.iloc[move_to_location[0]-1, move_to_location[1]-1] = chessboard.iloc[chess_piece_location[0]-1,chess_piece_location[1]-1]
        chessboard.iloc[move_to_location[0]-1, move_to_location[1]-1].current_position[0] = move_to_location[0]-1
        chessboard.iloc[move_to_location[0]-1, move_to_location[1]-1].current_position[1] = move_to_location[1]-1
        chessboard.iloc[chess_piece_location[0]-1, chess_piece_location[1]-1] = '.'

    return chessboard

