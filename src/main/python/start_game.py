from src.main.python.chessboard import creating_chessboard
from src.main.python.chesspieces import chess_piece_moves

print ('WELCOME TO AMEER\'S CHESS GAME\n')

chessboard = creating_chessboard.initialize_chessboard()
chessboard_with_pieces = creating_chessboard.initialize_chess_pieces(chessboard)
print (chessboard)

# print ('Pawn to 6A')
#
# chessboard.loc[6,'A'] = chessboard.loc[7,'A']
# chessboard.loc[7,'A'] = ''
# print (chessboard)

# player_1 = input('Who will be player_1? (ENTER "White" or "Black") ')
# if (player_1 == 'White'):
#     player_2 = 'Black'
# else:
#     player_2 = 'White'

game_finished = False

while (game_finished != True):
    counter = 1

    if (counter % 2) == 1:
        player = 'White'
    else:
        player = 'Black'

    chess_piece = input('Which piece to move? ')
    move_to = input('To? ')
    game_status = chess_piece_moves.move_chess_piece(chess_piece, move_to, chessboard, player, counter)
    counter += 1

