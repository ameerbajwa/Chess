from src.main.python.chesspieces import creating_chess_pieces
import pandas as pd

key = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H':8}


def move_chess_piece(chess_piece, chess_piece_position, move_to, chessboard, player):
    
    old_loc_y = int(chess_piece_position[0])-1
    old_loc_x = key[chess_piece_position[1]]-1
    new_loc_y = int(move_to[0])-1
    new_loc_x = key[move_to[1]]-1

    dict_of_chess_moves = {'Pawn': move_pawn(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player),
                           'King': move_king(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player),
                           'Queen': move_queen(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player),
                           'Bishop': move_bishop(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player),
                           'Knight': move_knight(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player),
                           'Rook': move_rook(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player)}

    chessboard, turn = dict_of_chess_moves[chess_piece]

    game_status = 'Continue'
    return chessboard, game_status, turn


def move_pawn(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if (chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Pawn'):
        print('Selected a Pawn')

        blank_spot_condition = (chessboard.iloc[new_loc_y, new_loc_x] == '.')
        move_1_spot = (old_loc_y - new_loc_y) ** 2 == 1 and (old_loc_x - new_loc_x) ** 2 == 0
        move_2_spot = (old_loc_y - new_loc_y) ** 2 == 4 and (old_loc_x - new_loc_x) ** 2 == 0
        attack_white = old_loc_y - new_loc_y == 1 and (old_loc_x - new_loc_x) ** 2 == 1
        attack_black = new_loc_y - old_loc_y == 1 and (old_loc_x - new_loc_x) ** 2 == 1

        if (player == 'White' and ((move_1_spot and blank_spot_condition) or (
                move_2_spot and blank_spot_condition and old_loc_y == 6)) or (
                    attack_white and chessboard.iloc[new_loc_y, new_loc_x].player == 'Black')) or (
                player == 'Black' and ((move_1_spot and blank_spot_condition) or (
                move_2_spot and blank_spot_condition and old_loc_y == 1)) or (
                        attack_black and chessboard.iloc[new_loc_y, new_loc_x].player == 'White')):
            chessboard.iloc[new_loc_y, new_loc_x] = chessboard.iloc[old_loc_y, old_loc_x]
            chessboard.iloc[new_loc_y, new_loc_x].current_position[0] = new_loc_y
            chessboard.iloc[new_loc_y, new_loc_x].current_position[1] = new_loc_x
            chessboard.iloc[old_loc_y, old_loc_x] = '.'

            turn = 'success'
        else:
            turn = 'failure'
            print('Invalid command. Retry turn.')

        return chessboard, turn
    else:
        print('Chess piece selected is not a pawn')
        turn = 'failure'
        return chessboard, turn


def move_king(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if (chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'King'):
        print('Selected King')

        blank_spot_condition = chessboard.iloc[new_loc_y, new_loc_x] == '.'
        move_1_spot_any_direction = ((new_loc_y - old_loc_y) ** 2 <= 1 or (new_loc_x - old_loc_x) ** 2 <= 1) and (
                    new_loc_y - old_loc_x) ** 2 + (new_loc_x - old_loc_x) ** 2 > 0

        if (player == 'White' and move_1_spot_any_direction and (
                blank_spot_condition or chessboard.iloc[new_loc_y, new_loc_x].player == 'Black')) or (
                player == 'Black' and move_1_spot_any_direction and (
                blank_spot_condition or chessboard.iloc[new_loc_y, new_loc_x].player == 'White')):
            chessboard.iloc[new_loc_y, new_loc_x] = chessboard.iloc[old_loc_y, old_loc_x]
            chessboard.iloc[new_loc_y, new_loc_x].current_position[0] = new_loc_y
            chessboard.iloc[new_loc_y, new_loc_x].current_position[1] = new_loc_x
            chessboard.iloc[old_loc_y, old_loc_x] = '.'

            turn = 'success'
        else:
            turn = 'failure'
            print('Invalid command. Retry turn.')

        return chessboard, turn
    else:
        turn = 'failure'
        print('Chess piece selected is not a king')
        return chessboard, turn


def move_queen(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):
    return chessboard


def move_bishop(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):
    return chessboard


def move_knight(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if (chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Knight'):
        print('Selected a Knight')

        blank_spot_condition = chessboard.iloc[new_loc_y, new_loc_x] == '.'
        L_move = (new_loc_y - old_loc_y) ** 2 + (new_loc_x - old_loc_x) ** 2 == 5

        if (player == 'White' and L_move and (
                blank_spot_condition or chessboard.iloc[new_loc_y, new_loc_x].player == 'Black')) or (
                player == 'Black' and L_move and (
                blank_spot_condition or chessboard.iloc[new_loc_y, new_loc_x].player == 'White')):
            chessboard.iloc[new_loc_y, new_loc_x] = chessboard.iloc[old_loc_y, old_loc_x]
            chessboard.iloc[new_loc_y, new_loc_x].current_position[0] = new_loc_y
            chessboard.iloc[new_loc_y, new_loc_x].current_position[1] = new_loc_x
            chessboard.iloc[old_loc_y, old_loc_x] = '.'

            turn = 'success'
        else:
            turn = 'failure'
            print('Invalid command. Retry turn.')

        return chessboard, turn
    else:
        turn = 'failure'
        print('Chess piece selected is not a Knight')
        return chessboard, turn


def move_rook(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):
    return chessboard



