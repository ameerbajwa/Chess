key = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}


def creating_list_of_available_moves(chess_piece, chess_piece_position, chessboard, player):
    old_loc_y = int(chess_piece_position[0])-1
    old_loc_x = key[chess_piece_position[1]]-1

    dict_of_chess_moves = {'Pawn': pawn_moves,
                           'King': king_moves,
                           'Queen': queen_moves,
                           'Bishop': bishop_moves,
                           'Knight': knight_moves,
                           'Rook': rook_moves
                           }

    try:
        list_of_moves = dict_of_chess_moves[chess_piece](old_loc_y, old_loc_x, chessboard, player)
        return list_of_moves
    except KeyError:
        print('Did not select an appropriate chess piece. Please play your turn again.')
        turn = 'failure'


def pawn_moves(old_loc_y, old_loc_x, chessboard, player):

def king_moves(old_loc_y, old_loc_x, chessboard, player):

def queen_moves(old_loc_y, old_loc_x, chessboard, player):

def bishop_moves(old_loc_y, old_loc_x, chessboard, player):

def knight_moves(old_loc_y, old_loc_x, chessboard, player):

def rook_moves(old_loc_y, old_loc_x, chessboard, player):


def move_chess_piece(chess_piece, chess_piece_position, move_to, chessboard, player):
    
    old_loc_y = int(chess_piece_position[0])-1
    old_loc_x = key[chess_piece_position[1]]-1
    new_loc_y = int(move_to[0])-1
    new_loc_x = key[move_to[1]]-1

    dict_of_chess_moves = {'Pawn': move_pawn,
                           'King': move_king,
                           'Queen': move_queen,
                           'Bishop': move_bishop,
                           'Knight': move_knight,
                           'Rook': move_rook
                           }

    try:
        chessboard, turn = dict_of_chess_moves[chess_piece](old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player)
    except KeyError:
        print('Did not select an appropriate chess piece. Please play your turn again.')
        turn = 'failure'

    game_status = 'Continue'
    return chessboard, game_status, turn


def jump_over_chess_piece_condition(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x, move):

    if move == 'diagonally':
        if abs(new_loc_y-old_loc_y) >= 2:
            for i in range(1,abs(new_loc_y-old_loc_y)):
                if new_loc_y < old_loc_y and new_loc_x < old_loc_x:
                    if chessboard.iloc[new_loc_y+i, new_loc_x+i] != '*':
                        return True
                elif new_loc_y < old_loc_y and new_loc_x > old_loc_x:
                    if chessboard.iloc[new_loc_y+i, new_loc_x-i] != '*':
                        return True
                elif new_loc_y > old_loc_y and new_loc_x < old_loc_x:
                    if chessboard.iloc[new_loc_y-i, new_loc_x+i] != '*':
                        return True
                elif new_loc_y > old_loc_y and new_loc_x > old_loc_x:
                    if chessboard.iloc[new_loc_y-i, new_loc_x-i] != '*':
                        return True
            else:
                return False
        else:
            return False

    if move == 'up_and_down':
        if abs(new_loc_y-old_loc_y) >= 2:
            for i in range(1, abs(new_loc_y-old_loc_y)):
                if new_loc_y < old_loc_y:
                    if chessboard.iloc[new_loc_y+i, new_loc_x] != '*':
                        return True
                elif new_loc_y > old_loc_y:
                    if chessboard.iloc[new_loc_y-i, new_loc_x] != '*':
                        return True
            else:
                return False
        else:
            return False

    if move == 'sideways':
        if abs(new_loc_x-old_loc_x) >= 2:
            for i in range(1, abs(new_loc_x-old_loc_x)):
                if new_loc_x < old_loc_x:
                    if chessboard.iloc[new_loc_y, new_loc_x+i] != '*':
                        return True
                elif new_loc_x > old_loc_x:
                    if chessboard.iloc[new_loc_y, new_loc_x-i] != '*':
                        return True
            else:
                return False
        else:
            return False


def move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x):

    chessboard.iloc[new_loc_y, new_loc_x] = chessboard.iloc[old_loc_y, old_loc_x]
    chessboard.iloc[new_loc_y, new_loc_x].current_position[0] = new_loc_y
    chessboard.iloc[new_loc_y, new_loc_x].current_position[1] = new_loc_x
    chessboard.iloc[old_loc_y, old_loc_x] = '*'

    return chessboard


def move_pawn(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Pawn':
        print('Selected a Pawn')

        blank_spot_condition = (chessboard.iloc[new_loc_y, new_loc_x] == '*')
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

            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
        else:
            turn = 'failure'
            print('Invalid command. Pawns can only move 1 spot forward or diagonally one spot forward if attacking an opposing chess piece. Retry turn.')
    else:
        print('Chess piece selected is not a pawn')
        turn = 'failure'

    return chessboard, turn


def move_king(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'King':
        print('Selected King')

        move_1_spot_any_direction = ((new_loc_y - old_loc_y) ** 2 <= 1 or (new_loc_x - old_loc_x) ** 2 <= 1) and ((
                    new_loc_y - old_loc_x) ** 2 + (new_loc_x - old_loc_x) ** 2 > 0)

        if move_1_spot_any_direction is False:
            turn = 'failure'
            print('Invalid command. King can only move 1 spot in any direction. Retry turn.')
        elif chessboard.iloc[new_loc_y, new_loc_x] != '*':
            if chessboard.iloc[new_loc_y, new_loc_x].player == player:
                turn = 'failure'
                print('Invalid command. Cannot take the place of your own chess piece. Retry turn.')
            else:
                chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
                turn = 'success'
        else:
            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
    else:
        turn = 'failure'
        print('Chess piece selected is not a king')

    return chessboard, turn


def move_queen(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Queen':
        print('Selected a Queen')

        move_up_and_down = (old_loc_y - new_loc_y)**2 > 0 and (old_loc_x - new_loc_x) ** 2 == 0
        move_sideways = (old_loc_y - new_loc_y)**2 == 0 and (old_loc_x - new_loc_x) ** 2 > 0
        move_diagonally = (old_loc_y-new_loc_y)**2 == (old_loc_x-new_loc_x)**2

        if move_up_and_down is True:
            queen_move = 'up_and_down'
        elif move_sideways is True:
            queen_move = 'sideways'
        elif move_diagonally is True:
            queen_move = 'diagonally'

        if (move_up_and_down is False) and (move_diagonally is False) and (move_sideways is False):
            turn = 'failure'
            print('Invalid command. Retry turn.')
        elif jump_over_chess_piece_condition(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x, queen_move) is True:
            turn = 'failure'
            print('Invalid command. Queen cannot jump over chess pieces. Retry turn.')
        elif chessboard.iloc[new_loc_y, new_loc_x] != '*':
            if chessboard.iloc[new_loc_y, new_loc_x].player == player:
                turn = 'failure'
                print('Invalid command. Cannot take the place of your own chess piece. Retry turn.')
            else:
                chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
                turn = 'success'
        else:
            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
    else:
        turn = 'failure'
        print('Chess piece selected is not a Rook')

    return chessboard, turn


def move_bishop(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Bishop':
        print('Selected a Bishop')

        move_diagonally = (old_loc_y-new_loc_y)**2 == (old_loc_x-new_loc_x)**2

        if move_diagonally is False:
            turn = 'failure'
            print('Invalid command. Bishops can only move diagonally. Retry turn.')
        elif jump_over_chess_piece_condition(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x, 'diagonally') is True:
            turn = 'failure'
            print('Invalid command. Bishops cannot jump over chess pieces. Retry turn.')
        elif chessboard.iloc[new_loc_y, new_loc_x] != '*':
            if chessboard.iloc[new_loc_y, new_loc_x].player == player:
                turn = 'failure'
                print('Invalid command. Cannot take place of your own chess piece. Retry turn.')
            else:
                chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
                turn = 'success'
        else:
            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
    else:
        turn = 'failure'
        print('Chess piece selected is not a Bishop')

    return chessboard, turn


def move_knight(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Knight':
        print('Selected a Knight')

        L_move = (new_loc_y - old_loc_y) ** 2 + (new_loc_x - old_loc_x) ** 2 == 5

        if L_move is False:
            turn = 'failure'
            print('Invalid command. Knights can only move in an L direction. Retry turn.')
        elif chessboard.iloc[new_loc_y, new_loc_x] != '*':
            if chessboard.iloc[new_loc_y, new_loc_x].player == player:
                turn = 'failure'
                print('Invalid command. Cannot take the place of your own chess piece. Retry turn.')
            else:
                chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
                turn = 'success'
        else:
            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
    else:
        turn = 'failure'
        print('Chess piece selected is not a Knight')

    return chessboard, turn


def move_rook(old_loc_y, old_loc_x, new_loc_y, new_loc_x, chessboard, player):

    if chessboard.iloc[old_loc_y, old_loc_x].chess_piece == 'Rook':
        print('Selected a Rook')

        move_up_and_down = (old_loc_y - new_loc_y)**2 > 0 and (old_loc_x - new_loc_x) ** 2 == 0
        move_sideways = (old_loc_y - new_loc_y)**2 == 0 and (old_loc_x - new_loc_x) ** 2 > 0

        if move_up_and_down is True:
            rook_move = 'up_and_down'
        elif move_sideways is True:
            rook_move = 'sideways'

        if move_up_and_down is False and move_sideways is False:
            turn = 'failure'
            print('Invalid command. Rooks can only move up and down or sideways. Retry turn.')
        elif jump_over_chess_piece_condition(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x, rook_move) is True:
            turn = 'failure'
            print('Invalid command. Rooks cannot jump over chess pieces. Retry turn.')
        elif chessboard.iloc[new_loc_y, new_loc_x] != '*':
            if chessboard.iloc[new_loc_y, new_loc_x].player == player:
                turn = 'failure'
                print('Invalid command. Cannot take the place of your own chess piece. Retry turn.')
            else:
                chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
                turn = 'success'
        else:
            chessboard = move(chessboard, old_loc_y, old_loc_x, new_loc_y, new_loc_x)
            turn = 'success'
    else:
        turn = 'failure'
        print('Chess piece selected is not a Rook')

    return chessboard, turn


